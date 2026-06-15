# next — Naveen Reddy Alka Job Search Hub

Personal job search project: company research pages, tailored resumes, application tracking, interview prep, and agent workflows for browser-based applying.

**Canonical location:** `~/Home/next`  
**GitHub:** https://github.com/naveenreddyalka/next

---

## Quick start (human)

```bash
# Clone (after move)
git clone https://github.com/naveenreddyalka/next.git ~/Home/next
cd ~/Home/next

# Open hub in browser
open index.html

# Optional: Python venv for resume generation
python3 -m venv .venv && source .venv/bin/activate
pip install reportlab
```

---

## Quick start (AI agent)

**Read in this order before doing anything:**

1. [`AGENTS.md`](AGENTS.md) — rules, skills index, workflows
2. [`CONTEXT.md`](CONTEXT.md) — candidate profile, resume history, company list
3. [`HANDOFF_NEXT_AGENT.md`](HANDOFF_NEXT_AGENT.md) — active tasks and current application state

Then load the skill matching the task from [`.cursor/skills/`](.cursor/skills/).

---

## Project layout

```
next/
??? index.html                    # Hub — 13 company cards
??? CONTEXT.md                    # Full candidate + project context
??? HANDOFF_NEXT_AGENT.md         # Active handoff / current sprint
??? AGENTS.md                     # Agent operating manual
??? job_matches.md                # Target roles + job IDs
??? resume_updates.md             # Paste-ready resume sections
??? Naveen_Reddy_Alka_Resume.pdf  # Generic master resume
?
??? {company}/                    # anthropic, databricks, stripe, ...
?   ??? index.html                # Apply | My Applications | Latest Questions
?   ??? company_info.html         # Research: comp, interview, pros/cons
?   ??? Naveen_Reddy_Alka_{Co}_Resume.pdf
?
??? databricks/
?   ??? application_tracker.md    # Active Greenhouse batch tracker
?
??? resources/                    # comp, interview prep, H1B guides (HTML)
??? files/
?   ??? evl/                      # Employment verification letters (source)
?   ??? scripts/                  # Data pipeline + resume generators
?   ??? launchd/                  # Weekly auto-refresh plist (generated on install)
?
??? .cursor/skills/               # Agent skills (committed to repo)
    ??? job-apply-browser/        # Greenhouse / company ATS forms
    ??? job-apply-linkedin/       # LinkedIn Easy Apply
    ??? prepare-company-resume/   # Tailored PDF resume generation
    ??? company-pages-maintenance/ # Interview questions + HTML rebuild
```

---

## Company pages pipeline

Source data (agents edit):

| File | Purpose |
|------|---------|
| `files/scripts/company_extra_data.py` | Snapshot, perks, how-to-crack prep |
| `files/scripts/build_company_pages_data.py` | Base company rows + applications |
| `files/scripts/company_questions_seed.py` | Interview question seed bank |
| `files/scripts/company_questions_inbox.json` | Drop-in new questions (prepended on refresh) |

Regenerate HTML:

```bash
~/Home/next/files/scripts/refresh_company_pages.sh
```

**Auto-refresh:** LaunchAgent `com.naveen.next.refresh-company-pages` — Sundays 9 AM + on load.  
Re-install after moving project:

```bash
~/Home/next/files/scripts/install_refresh_schedule.sh
```

---

## Target companies (13)

Anthropic, OpenAI, xAI, NVIDIA, ServiceNow, Confluent, Databricks, Stripe, Google, Snowflake, Netflix, Uber, SpaceX.

See `job_matches.md` and `CONTEXT.md` for job IDs and URLs.

---

## Active work (as of 2026-06-09)

- **Databricks batch:** 4 submitted, 1 in progress (`5646866002` — needs fresh Greenhouse security code), 2 pending. See `databricks/application_tracker.md`.
- **Company pages:** Latest Questions tab live; weekly refresh merges new interview reports.
- **LinkedIn Easy Apply:** Not started — use `job-apply-linkedin` skill when ready.

---

## Contact defaults

- Email: naveenreddy.alka@gmail.com (never use @intuit.com on applications)
- Phone: 314-498-5314
- LinkedIn: linkedin.com/in/naveenreddyalka
- Work authorization: Yes | Sponsorship needed: Yes

Full form defaults: `.cursor/skills/job-apply-browser/DEFAULT_ANSWERS.md`
