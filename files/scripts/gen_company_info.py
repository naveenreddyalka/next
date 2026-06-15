#!/usr/bin/env python3
"""Patch or generate company_info.html with pros/cons, snapshot, prep guide, and applications."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from company_sections import render_info_page_sections
from project_paths import PROJECT_ROOT

BASE = PROJECT_ROOT
DATA = Path(__file__).with_name("company_pages_data.json")

EXTRA_CSS = """
  .two-col{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:1rem}
  @media(max-width:700px){.two-col{grid-template-columns:1fr}}
  .pros-box{background:#EAF3DE;border-radius:10px;padding:1rem 1.25rem}
  .cons-box{background:#FCE8E8;border-radius:10px;padding:1rem 1.25rem}
  .pros-box h3,.cons-box h3{font-size:.9rem;margin:0 0 .5rem}
  .pros-box h3{color:#27500A}.cons-box h3{color:#7a0009}
  .pros-box li,.cons-box li{font-size:.85rem;line-height:1.55;margin-bottom:4px}
  .app-table{width:100%;border-collapse:collapse;font-size:.85rem;margin:.75rem 0 1rem;background:#fff;border-radius:10px;overflow:hidden;border:1px solid #e5e4e0}
  .app-table th{text-align:left;padding:.65rem 1rem;background:#f5f4f0;font-weight:500;font-size:.78rem;color:#555}
  .app-table td{padding:.65rem 1rem;border-bottom:1px solid #f0efe9;vertical-align:top}
  .status-badge{display:inline-block;padding:2px 9px;border-radius:12px;font-size:.72rem;font-weight:600}
  .status-submitted{background:#EAF3DE;color:#27500A}
  .status-progress{background:#FAEEDA;color:#633806}
  .status-pending{background:#f0efe9;color:#555}
  .status-none{background:#f5f4f0;color:#888}
  .apps-summary{font-size:.82rem;color:#666;margin-bottom:.5rem}
  .q-item{border:1px solid #e5e4e0;border-radius:10px;padding:12px 14px;margin-bottom:10px;background:#fff}
  .q-head{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-bottom:6px}
  .q-type{display:inline-block;padding:2px 8px;border-radius:10px;font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.04em}
  .type-coding{background:#E8F0FE;color:#1A56CE}
  .type-design{background:#FCE8E8;color:#7a0009}
  .type-behavioral{background:#EAF3DE;color:#27500A}
  .type-other{background:#f5f4f0;color:#555}
  .q-meta{font-size:.72rem;color:#888}
  .q-text{font-size:.85rem;line-height:1.6;color:#333}
"""

HERO_COLORS = {
    "anthropic": "#0F6E56",
    "openai": "#10a37f",
    "nvidia": "#534AB7",
    "servicenow": "#62D84E",
    "confluent": "#172B4D",
    "databricks": "#FF3621",
    "stripe": "#635BFF",
    "google": "#4285F4",
    "snowflake": "#29B5E8",
    "netflix": "#E50914",
    "uber": "#1a1a18",
    "xai": "#000000",
    "spacex": "#005288",
}

INFO_BOX_CLASS = {
    "anthropic": ("#E1F5EE", "#085041"),
    "openai": ("#d4f1e9", "#0a6b52"),
    "nvidia": ("#EEEDFE", "#3C3489"),
    "servicenow": ("#E8F5E9", "#2E7D32"),
    "confluent": ("#E6EBF5", "#172B4D"),
    "databricks": ("#FFE8E5", "#8C1A0E"),
    "stripe": ("#EEEDFE", "#3C3489"),
    "google": ("#E8F0FE", "#1A56CE"),
    "snowflake": ("#d6f0fa", "#0e6b91"),
    "netflix": ("#fce8e8", "#7a0009"),
    "uber": ("#f0f0ee", "#333"),
    "xai": ("#f0f0f0", "#111"),
    "spacex": ("#e8f4fa", "#005288"),
}


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def status_class(status):
    s = status.lower()
    if s == "submitted":
        return "status-submitted"
    if s == "in progress":
        return "status-progress"
    if s == "pending":
        return "status-pending"
    return "status-none"


def render_apps_table(apps):
    if not apps:
        return '<p style="font-size:.85rem;color:#888">No applications tracked yet.</p>'
    rows = ""
    for a in apps:
        rows += (
            f"<tr><td>{esc(a['role'])}</td><td><code>{esc(a['id'])}</code></td>"
            f"<td><span class=\"status-badge {status_class(a['status'])}\">{esc(a['status'])}</span></td>"
            f"<td>{esc(a['date'])}</td>"
            f"<td><a href=\"{a['url']}\" target=\"_blank\" class=\"apply-btn\" style=\"margin-top:0\">View</a></td></tr>"
        )
    submitted = sum(1 for a in apps if a["status"] == "Submitted")
    return (
        f'<p class="apps-summary">{submitted} submitted &middot; {len(apps)} total tracked</p>'
        f'<div style="overflow-x:auto"><table class="app-table">'
        f"<thead><tr><th>Role</th><th>Job ID</th><th>Status</th><th>Date</th><th>Link</th></tr></thead>"
        f"<tbody>{rows}</tbody></table></div>"
    )


def render_pros_cons(co):
    pros = "".join(f"<li>{esc(p)}</li>" for p in co["pros"])
    cons = "".join(f"<li>{esc(c)}</li>" for c in co["cons"])
    return f"""
  <h2>Pros and cons - decision guide</h2>
  <div class="two-col">
    <div class="pros-box"><h3>Pros</h3><ul>{pros}</ul></div>
    <div class="cons-box"><h3>Cons</h3><ul>{cons}</ul></div>
  </div>"""


def render_applications_section(apps):
    return f"""
  <h2>My applications</h2>
  {render_apps_table(apps)}
  <p style="font-size:.82rem;color:#888;margin-top:.5rem">Also track status on the <a href="index.html">job apply page</a>.</p>"""


def ensure_css(html):
    if ".app-table" in html and ".pros-box" in html:
        return html
    if EXTRA_CSS.strip() in html:
        return html
    return html.replace("</style>", EXTRA_CSS + "\n</style>", 1)


def insert_or_replace_info_sections(html, co):
    block = render_info_page_sections(co)
    if not block.strip():
        return html
    if 'id="company-snapshot"' in html:
        return re.sub(
            r'<h2 id="company-snapshot">.*?(?=<h2>Pros and cons|<h2>Interview format)',
            block.strip() + "\n\n  ",
            html,
            count=1,
            flags=re.DOTALL,
        )
    # Insert after "Why you're a match" info-box
    m = re.search(
        r'(<h2>Why you.*?match</h2>\s*<div class="info-box">.*?</div>\s*)',
        html,
        flags=re.DOTALL,
    )
    if m:
        return html[: m.end()] + block + "\n\n  " + html[m.end() :]
    # Fallback: before Open roles
    if "<h2>Open roles" in html:
        return html.replace("<h2>Open roles", block + "\n\n  <h2>Open roles", 1)
    return html.replace("</main>", block + "\n</main>", 1)


def patch_existing(html, co, apps):
    html = ensure_css(html)
    html = insert_or_replace_info_sections(html, co)

    pros_block = render_pros_cons(co)
    if "Pros and cons" not in html:
        marker = "<h2>Interview format"
        if marker in html:
            html = html.replace(marker, pros_block + "\n\n  " + marker, 1)
        else:
            html = html.replace("</main>", pros_block + "\n</main>", 1)
    else:
        html = re.sub(
            r"<h2>Pros and cons.*?</div>\s*(?:<h2>Benefits.*?</ul>)?",
            pros_block.strip(),
            html,
            count=1,
            flags=re.DOTALL,
        )

    apps_block = render_applications_section(apps)
    if re.search(r"<h2>Application status</h2>", html):
        html = re.sub(
            r"<h2>Application status</h2>.*?(?=<a href=|<h2>|</main>)",
            apps_block.strip() + "\n  ",
            html,
            count=1,
            flags=re.DOTALL,
        )
    elif "My applications" not in html:
        html = html.replace("</main>", apps_block + "\n</main>", 1)
    else:
        html = re.sub(
            r"<h2>My applications</h2>.*?(?=<a href=|<h2>|</main>)",
            apps_block.strip() + "\n  ",
            html,
            count=1,
            flags=re.DOTALL,
        )

    if 'href="index.html">? Job Page</a>' not in html:
        html = html.replace(
            '<a href="../index.html">? Home</a>',
            '<a href="../index.html">? Home</a><a href="index.html">? Job Page</a>',
            1,
        )
    return html


def generate_new(slug, co, apps):
    hero = HERO_COLORS.get(slug, co["color"])
    bg, fg = INFO_BOX_CLASS.get(slug, ("#f0f4ff", "#333"))
    comp_cards = "".join(
        f'<div class="comp-card"><div class="num">{n}</div><div class="lbl">{l}</div></div>'
        for n, l in co["comp"]
    )
    meta = "".join(f"<span>{esc(m)}</span>" for m in co["meta"])
    interview = "".join(f"<li>{esc(i)}</li>" for i in co["interview"])
    tag_color = hero if slug != "uber" else "#333"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(co['name'])} - Naveen's Job Tracker</title>
<style>
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f5f4f0;color:#1a1a18;line-height:1.6}}
  .hero{{background:{hero};color:#fff;padding:2rem 2.5rem}}
  .hero h1{{font-size:1.8rem;font-weight:500;margin-bottom:.25rem}}
  .hero p{{font-size:.9rem;opacity:.8}}
  .hero-meta{{display:flex;gap:1rem;margin-top:1rem;flex-wrap:wrap}}
  .hero-meta span{{font-size:.82rem;background:rgba(255,255,255,.15);padding:4px 12px;border-radius:20px}}
  main{{max-width:860px;margin:0 auto;padding:2rem 1.5rem}}
  h2{{font-size:1.1rem;font-weight:500;margin:2rem 0 .75rem;padding-bottom:.4rem;border-bottom:1px solid #e5e4e0}}
  .comp-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:1.5rem}}
  .comp-card{{background:#fff;border:1px solid #e5e4e0;border-radius:10px;padding:.85rem;text-align:center}}
  .comp-card .num{{font-size:1.25rem;font-weight:500;color:{hero}}}
  .comp-card .lbl{{font-size:.72rem;color:#888;margin-top:2px}}
  .highlight-box{{background:#fff8ed;border-left:3px solid #EF9F27;padding:.75rem 1rem;border-radius:0 8px 8px 0;font-size:.85rem;color:#633806;margin-bottom:1rem}}
  .info-box{{background:{bg};border-radius:10px;padding:1rem 1.25rem;margin-bottom:1rem;font-size:.85rem;color:{fg}}}
  .prep-list{{list-style:none;padding:0}}
  .prep-list li{{padding:.5rem 0;border-bottom:1px solid #f0efe9;font-size:.9rem;display:flex;gap:.5rem}}
  .prep-list li::before{{content:"\\2192";color:{hero};flex-shrink:0}}
  .apply-btn{{display:inline-block;margin-top:.75rem;font-size:.82rem;padding:6px 16px;border-radius:8px;border:1px solid {hero};color:{hero};text-decoration:none;background:#fff}}
  .topnav{{background:#1a3a5c;padding:10px 24px;font-size:13px}}
  .topnav a{{color:#aac4e0;text-decoration:none;margin-right:16px}}
  .topnav a:hover{{color:white}}
{EXTRA_CSS}
</style>
</head>
<body>
<nav class="topnav"><a href="../index.html">&larr; Home</a><a href="index.html">&larr; Job Page</a></nav>
<div class="hero">
  <h1>{esc(co['name'])}</h1>
  <p>{esc(co['tier'])} &middot; {esc(co['focus'])} &middot; {esc(co['location'])}</p>
  <div class="hero-meta">{meta}</div>
</div>
<main>
  <h2>Compensation - {esc(co['tier'])}</h2>
  <div class="comp-grid">{comp_cards}</div>
  <p style="font-size:.82rem;color:#888">{esc(co['comp_note'])}</p>
  <div class="highlight-box">{esc(co['highlight'])}</div>
  <div class="info-box"><strong>Why you are a strong match:</strong> {esc(co['fit'])}</div>
  <p style="font-size:.82rem;color:#666;margin-top:.5rem"><strong>H1B / Visa:</strong> {esc(co['h1b'])}</p>
{render_info_page_sections(co)}
{render_pros_cons(co)}
  <h2>Interview format at {esc(co['name'])}</h2>
  <ul class="prep-list">{interview}</ul>
{render_applications_section(apps)}
</main>
</body>
</html>"""


def main():
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    for slug, co in payload["companies"].items():
        apps = payload.get("applications", {}).get(slug) or co.get("target_apps") or []
        path = BASE / slug / "company_info.html"
        if path.exists():
            html = patch_existing(path.read_text(encoding="utf-8"), co, apps)
        else:
            html = generate_new(slug, co, apps)
        path.write_text(html, encoding="utf-8")
        print(f"ok {slug}/company_info.html")


if __name__ == "__main__":
    main()
