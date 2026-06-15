# Handoff For Next Agent (Job Applications)

Last updated: 2026-06-15

## Start here

1. Read [`AGENTS.md`](AGENTS.md) — operating rules and skill index
2. Read [`CONTEXT.md`](CONTEXT.md) — candidate profile and project history
3. Load the skill for your task from [`.cursor/skills/`](.cursor/skills/)

**Project root:** `~/Home/next` (was `~/next` — migrated 2026-06-15)  
**GitHub:** https://github.com/naveenreddyalka/next

---

## Company Page Maintenance (automatic)

- **Source data (agents edit directly):** `files/scripts/company_extra_data.py`, `build_company_pages_data.py`
- **Latest interview questions:** `company_questions_seed.py` + `company_questions_inbox.json` → merged by `update_latest_questions.py`
- **Auto-rebuild:** LaunchAgent `com.naveen.next.refresh-company-pages` — every **Sunday 9:00 AM** + RunAtLoad
- **Pipeline:** `files/scripts/refresh_company_pages.sh`
- **Re-install schedule after move:** `files/scripts/install_refresh_schedule.sh`
- **Log:** `.refresh_company_pages.log`
- **Skill:** `.cursor/skills/company-pages-maintenance/SKILL.md`
- **UI:** Each `{company}/index.html` has tabs: Apply | My Applications | Latest Questions

---

## Goal

Continue and finish Databricks job applications in `databricks/` with these rules:
- Use the Databricks tailored PDF resume only: `databricks/Naveen_Reddy_Alka_Databricks_Resume.pdf`
- Do not paste resume text manually unless explicitly approved by user
- Update `databricks/application_tracker.md` after every major step
- **Skill:** `.cursor/skills/job-apply-browser/SKILL.md`

---

## Source Of Truth

- Tracker: `databricks/application_tracker.md`
- Candidate defaults: `.cursor/skills/job-apply-browser/DEFAULT_ANSWERS.md`
- LinkedIn applies: `.cursor/skills/job-apply-linkedin/SKILL.md`

---

## Current Status

Already submitted:
- `6937001002` (submitted earlier)
- `5646855002` (submitted)
- `7823561002` (submitted)
- `5408888002` (submitted)

In progress:
- `5646866002` Staff Software Engineer - Database Engine Internals
  - URL: `https://job-boards.greenhouse.io/embed/job_app?for=databricks&token=5646866002`
  - PDF is attached (Remove file button visible)
  - Greenhouse is requiring a fresh Security code
  - Last code `0Wyowmxv` was rejected

Pending:
- `7994801002` Staff Software Engineer - IAM
- `7274908002` Senior Staff Software Engineer - Security Infrastructure

---

## Known Constraints / Pitfalls

1. PDF attach may require user manual action (native file picker).
2. Security code expires quickly — ask user, fill, submit immediately.
3. Greenhouse dropdowns show `invalid` until explicitly reselected.
4. Education fields required on some Databricks roles.

---

## Resume + Form Defaults

See `.cursor/skills/job-apply-browser/DEFAULT_ANSWERS.md` for full mapping.

Key values:
- Work authorization: **Yes** | Sponsorship: **Yes**
- Email: naveenreddy.alka@gmail.com
- Education: ASU, Master's, Computer Science, 2019–2021

---

## Immediate Next Action

1. Resume from role `5646866002`
2. Enter fresh Security code from user
3. Submit and confirm success page
4. Update tracker row + submission log
5. Move to `7994801002`, then `7274908002`
6. Pause only when user action needed (PDF attach or security code)

---

## LinkedIn Easy Apply (not started)

When user requests LinkedIn applications:
1. User logs into LinkedIn in Cursor browser tab manually
2. Follow `.cursor/skills/job-apply-linkedin/SKILL.md`
3. Prefer tailored PDF per company from `{company}/Naveen_Reddy_Alka_{Co}_Resume.pdf`

---

## Communication Pattern For User

- Keep updates concise and frequent.
- When blocked, ask for one exact input (e.g., "please send security code").
- After each submit, report: job ID, submitted status, confirmation URL, tracker updated.
