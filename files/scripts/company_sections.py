#!/usr/bin/env python3
"""Shared HTML renderers for company snapshot and interview prep sections."""


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render_snapshot_block(co, compact=False):
    extra = co.get("snapshot") or {}
    if not extra:
        return ""
    perks = extra.get("perks") or co.get("benefits") or []
    perks_html = "".join(f"<li>{esc(p)}</li>" for p in perks)
    tag = "h3" if compact else "h3"
    cls = "detail-list" if compact else "prep-list"
    growth = extra.get("growth_note", "")
    growth_html = f'<p class="growth-note">{esc(growth)}</p>' if growth else ""
    return f"""
    <{tag}>Company snapshot</{tag}>
    <ul class="{cls}">
      <li><strong>Company type:</strong> {esc(extra.get('company_type', 'N/A'))}</li>
      <li><strong>Salary range (Bay Area):</strong> {esc(extra.get('salary_range', 'See comp grid'))}</li>
    </ul>
    {growth_html}
    <{tag}>Benefits and perks</{tag}>
    <ul class="{cls}">{perks_html}</ul>"""


def render_how_to_crack_block(co, compact=False):
    htc = co.get("how_to_crack") or {}
    if not htc:
        return ""
    plan = htc.get("prep_plan") or []
    plan_html = "".join(f"<li>{esc(p)}</li>" for p in plan)
    tag = "h3" if compact else "h2"
    id_attr = '' if compact else ' id="how-to-crack"'
    list_cls = "detail-list" if compact else "prep-list"
    return f"""
    <{tag}{id_attr}>How to crack {esc(co['name'])}</{tag}>
    <ul class="{list_cls}">
      <li><strong>Interview style:</strong> {esc(htc.get('style', ''))}</li>
      <li><strong>Rounds:</strong> {esc(htc.get('rounds', ''))}</li>
      <li><strong>Coding:</strong> {esc(htc.get('coding', ''))}</li>
    </ul>
    <p class="prep-label"><strong>4-week prep plan:</strong></p>
    <ul class="{list_cls}">{plan_html}</ul>"""


def render_why_section_index(co):
    """Full Why card content for index.html."""
    return f"""
      <p class="pitch">{esc(co['profile'])}</p>
      {render_snapshot_block(co, compact=True)}
      {render_how_to_crack_block(co, compact=True)}
      <p class="muted" style="margin-top:12px;"><a href="company_info.html" class="link-sm">Full company research page</a></p>"""


def render_latest_questions(co, compact=False):
    items = co.get("latest_questions") or []
    if not items:
        return '<p class="muted">No reported questions yet. List refreshes weekly from Blind, LeetCode, Glassdoor, and Reddit.</p>'
    rows = ""
    for item in items:
        qtype = item.get("type", "Other")
        cls = {
            "Coding": "type-coding",
            "System Design": "type-design",
            "Behavioral": "type-behavioral",
        }.get(qtype, "type-other")
        link = ""
        if item.get("url"):
            link = f' <a href="{esc(item["url"])}" target="_blank" class="link-sm">source</a>'
        meta = f'{esc(item.get("source", ""))} | {esc(item.get("reported", item.get("added", "")))}'
        rows += (
            f'<div class="q-item"><div class="q-head">'
            f'<span class="q-type {cls}">{esc(qtype)}</span>'
            f'<span class="q-meta">{meta}</span></div>'
            f'<div class="q-text">{esc(item["question"])}{link}</div></div>'
        )
    updated = ""
    if not compact:
        updated = '<p class="muted" style="margin-bottom:12px;">Newest reports first. Updated weekly via scheduled refresh.</p>'
    return updated + rows


def render_info_page_sections(co):
    """Sections for company_info.html after Why you're a match."""
    snap = co.get("snapshot") or {}
    if not snap:
        return ""
    return f"""
  <h2 id="company-snapshot">Company snapshot and benefits</h2>
  <ul class="prep-list">
    <li><strong>Company type:</strong> {esc(snap.get('company_type', ''))}</li>
    <li><strong>Salary range (Bay Area):</strong> {esc(snap.get('salary_range', ''))}</li>
    <li><strong>Growth / equity outlook:</strong> {esc(snap.get('growth_note', ''))}</li>
  </ul>
  <h3 style="font-size:.95rem;margin:1rem 0 .5rem">Benefits and perks</h3>
  <ul class="prep-list">{"".join(f"<li>{esc(p)}</li>" for p in (snap.get('perks') or co.get('benefits') or []))}</ul>
{render_how_to_crack_block(co, compact=False)}
  <h2 id="latest-questions">Latest interview questions</h2>
  {render_latest_questions(co)}"""
