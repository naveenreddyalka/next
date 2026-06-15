#!/usr/bin/env python3
"""Generate company index.html: job apply page + applications tab. Research lives in company_info.html."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from company_sections import render_why_section_index, render_latest_questions
from project_paths import PROJECT_ROOT

BASE = PROJECT_ROOT
DATA = Path(__file__).with_name("company_pages_data.json")


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


def render_apps(apps):
    if not apps:
        return '<p class="muted">No applications tracked yet.</p>'
    rows = ""
    for a in apps:
        rows += (
            f"<tr><td>{esc(a['role'])}</td>"
            f"<td><code>{esc(a['id'])}</code></td>"
            f"<td><span class=\"status-badge {status_class(a['status'])}\">{esc(a['status'])}</span></td>"
            f"<td>{esc(a['date'])}</td>"
            f"<td><a href=\"{a['url']}\" target=\"_blank\" class=\"link-sm\">View</a></td></tr>"
        )
    submitted = sum(1 for a in apps if a["status"] == "Submitted")
    return (
        f'<p class="apps-summary">{submitted} submitted &middot; {len(apps)} total tracked</p>'
        f'<div class="table-wrap"><table class="app-table">'
        f"<thead><tr><th>Role</th><th>Job ID</th><th>Status</th><th>Date</th><th>Link</th></tr></thead>"
        f"<tbody>{rows}</tbody></table></div>"
    )


def render_page(slug, co, apps):
    color = co["color"]
    has_research = (BASE / slug / "company_info.html").exists()
    research_nav = (
        '<a href="company_info.html">Company Research</a>'
        if has_research
        else ""
    )
    jobs_html = ""
    for j in co["jobs"]:
        jobs_html += (
            f'<div class="job-row"><div class="job-title">{esc(j["title"])}</div>'
            f'<div class="job-id">Job ID: {esc(j["id"])}</div>'
            f'<div class="job-fit">{esc(j["fit"])}</div>'
            f'<a class="apply-btn" href="{j["url"]}" target="_blank">Apply Now</a></div>'
        )
    tags_html = " ".join(f'<span class="tag">{esc(t)}</span>' for t in co["tags"])
    tracker_note = (
        '<p class="muted" style="margin-top:12px;">See also: '
        '<a href="application_tracker.md" class="link-sm">application_tracker.md</a></p>'
        if slug == "databricks"
        else ""
    )
    research_card = ""
    if has_research:
        research_card = f"""
    <div class="card research-card">
      <h2>Company Research</h2>
      <p>Compensation, interview process, pros/cons, benefits, and open roles are on the dedicated research page.</p>
      <a class="research-btn" href="company_info.html">Open {esc(co['name'])} Research Page</a>
    </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Naveen Reddy Alka - {esc(co['name'])}</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f5f7fa; color: #1a1a2e; }}
  .topnav {{ background: #1a3a5c; padding: 10px 24px; font-size: 13px; }}
  .topnav a {{ color: #aac4e0; text-decoration: none; margin-right: 16px; }}
  .topnav a:hover {{ color: white; }}
  header {{ background: {color}; color: white; padding: 32px 40px; }}
  header h1 {{ font-size: 28px; font-weight: 700; }}
  header p {{ margin-top: 6px; opacity: 0.85; font-size: 14px; }}
  .tabs {{ display: flex; gap: 0; background: white; border-bottom: 2px solid #e8eaf0; padding: 0 24px; max-width: 900px; margin: 0 auto; }}
  .tab-btn {{ background: none; border: none; padding: 14px 20px; font-size: 13px; font-weight: 600; color: #666; cursor: pointer; border-bottom: 3px solid transparent; margin-bottom: -2px; }}
  .tab-btn:hover {{ color: {color}; }}
  .tab-btn.active {{ color: {color}; border-bottom-color: {color}; }}
  .container {{ max-width: 900px; margin: 32px auto 48px; padding: 0 24px; }}
  .tab-panel {{ display: none; }}
  .tab-panel.active {{ display: block; }}
  .card {{ background: white; border-radius: 12px; padding: 28px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(0,0,0,.07); }}
  .card h2 {{ font-size: 16px; font-weight: 700; color: {color}; margin-bottom: 16px; text-transform: uppercase; letter-spacing: .06em; border-bottom: 2px solid {color}; padding-bottom: 8px; }}
  .job-row {{ border: 1px solid #e8eaf0; border-radius: 8px; padding: 18px; margin-bottom: 14px; }}
  .job-title {{ font-size: 15px; font-weight: 600; }}
  .job-id {{ font-size: 12px; color: #888; margin-top: 3px; }}
  .job-fit {{ font-size: 13px; color: #444; margin-top: 10px; line-height: 1.6; }}
  .apply-btn {{ display: inline-block; margin-top: 12px; padding: 8px 18px; background: {color}; color: white; border-radius: 6px; text-decoration: none; font-size: 13px; font-weight: 600; }}
  .research-btn {{ display: inline-block; margin-top: 12px; padding: 10px 20px; background: #1a3a5c; color: white; border-radius: 6px; text-decoration: none; font-size: 13px; font-weight: 600; }}
  .resume-link {{ display: inline-block; margin: 4px 8px 4px 0; padding: 8px 18px; background: #1a3a5c; color: white; border-radius: 6px; text-decoration: none; font-size: 13px; font-weight: 600; }}
  .pitch {{ font-size: 14px; line-height: 1.7; color: #333; }}
  .tag {{ display: inline-block; padding: 3px 10px; background: #f0f2f7; border-radius: 20px; font-size: 12px; color: #555; margin: 3px 3px 3px 0; }}
  .research-card p {{ font-size: 13px; color: #555; line-height: 1.6; }}
  .app-table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  .app-table th {{ text-align: left; padding: 10px 12px; background: #f8f9fc; border-bottom: 2px solid #e8eaf0; font-size: 11px; text-transform: uppercase; color: #666; }}
  .app-table td {{ padding: 10px 12px; border-bottom: 1px solid #f0f2f7; vertical-align: top; }}
  .table-wrap {{ overflow-x: auto; }}
  .status-badge {{ display: inline-block; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: 600; }}
  .status-submitted {{ background: #eaf3de; color: #27500a; }}
  .status-progress {{ background: #fff3cd; color: #856404; }}
  .status-pending {{ background: #e8eaf0; color: #555; }}
  .status-none {{ background: #f0f2f7; color: #888; }}
  .apps-summary {{ font-size: 13px; color: #666; margin-bottom: 12px; }}
  .muted {{ font-size: 13px; color: #888; }}
  .link-sm {{ font-size: 12px; color: {color}; text-decoration: none; font-weight: 600; }}
  .link-sm:hover {{ text-decoration: underline; }}
  .detail-list {{ padding-left: 18px; margin: 10px 0 16px; }}
  .detail-list li {{ font-size: 13px; line-height: 1.65; color: #444; margin-bottom: 6px; }}
  .growth-note {{ font-size: 13px; color: #633806; background: #fff8ed; padding: 10px 14px; border-radius: 6px; margin: 8px 0 14px; line-height: 1.55; }}
  .prep-label {{ font-size: 13px; color: #333; margin: 14px 0 6px; }}
  .card h3 {{ font-size: 13px; font-weight: 700; color: {color}; margin: 18px 0 8px; text-transform: uppercase; letter-spacing: .04em; }}
  .q-item {{ border: 1px solid #e8eaf0; border-radius: 8px; padding: 14px 16px; margin-bottom: 10px; }}
  .q-head {{ display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin-bottom: 8px; }}
  .q-type {{ display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: .04em; }}
  .type-coding {{ background: #e8f0fe; color: #1a56ce; }}
  .type-design {{ background: #fce8e8; color: #7a0009; }}
  .type-behavioral {{ background: #eaf3de; color: #27500a; }}
  .type-other {{ background: #f0f2f7; color: #555; }}
  .q-meta {{ font-size: 11px; color: #888; }}
  .q-text {{ font-size: 13px; line-height: 1.6; color: #333; }}
</style>
</head>
<body>
<nav class="topnav">
  <a href="../index.html">&larr; Home</a>
  {research_nav}
</nav>
<header>
  <h1>Naveen Reddy Alka &rarr; {esc(co['name'])}</h1>
  <p>naveenreddy.alka@gmail.com &nbsp;&middot;&nbsp; 314-498-5314 &nbsp;&middot;&nbsp; linkedin.com/in/naveenreddyalka &nbsp;&middot;&nbsp; San Francisco Bay Area</p>
</header>
<div class="tabs">
  <button class="tab-btn active" onclick="showTab('apply', this)">Apply</button>
  <button class="tab-btn" onclick="showTab('applications', this)">My Applications</button>
  <button class="tab-btn" onclick="showTab('questions', this)">Latest Questions</button>
</div>
<div class="container">
  <div id="tab-apply" class="tab-panel active">
    {research_card}
    <div class="card"><h2>Target Roles at {esc(co['name'])}</h2>{jobs_html}</div>
    <div class="card"><h2>Why {esc(co['name'])}</h2>{render_why_section_index(co)}</div>
    <div class="card"><h2>Resume</h2>
      <p style="font-size:13px;color:#555;margin-bottom:12px;">Tailored resume for {esc(co['name'])}.</p>
      <a class="resume-link" href="Naveen_Reddy_Alka_{co['resume_slug']}_Resume.pdf">Tailored Resume</a>
      <a class="resume-link" href="../Naveen_Reddy_Alka_Resume.pdf" style="background:#555;">Generic Resume</a>
    </div>
    <div class="card"><h2>Key Skills Match</h2>{tags_html}</div>
  </div>
  <div id="tab-applications" class="tab-panel">
    <div class="card">
      <h2>Applications - {esc(co['name'])}</h2>
      {render_apps(apps)}
      {tracker_note}
    </div>
  </div>
  <div id="tab-questions" class="tab-panel">
    <div class="card">
      <h2>Latest Questions - {esc(co['name'])}</h2>
      <p class="muted" style="margin-bottom:14px;">Recent coding, system design, and behavioral questions from Blind, LeetCode, Glassdoor, Reddit, and interview reports. Newest first; refreshed weekly.</p>
      {render_latest_questions(co, compact=True)}
    </div>
  </div>
</div>
<script>
function showTab(id, btn) {{
  document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('tab-' + id).classList.add('active');
  btn.classList.add('active');
}}
</script>
</body>
</html>"""


def main():
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    for slug, co in payload["companies"].items():
        apps = payload.get("applications", {}).get(slug) or co.get("target_apps") or []
        out = BASE / slug / "index.html"
        out.write_text(render_page(slug, co, apps), encoding="utf-8")
        print(f"ok {slug}/index.html")


if __name__ == "__main__":
    main()
