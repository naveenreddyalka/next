# Agent Operating Manual — `next` Job Search Project

This file tells any AI agent how to pick up and continue work on this repo without losing context.

---

## First actions (every session)

1. Read [`CONTEXT.md`](CONTEXT.md) — who Naveen is, resume rules, company list, work history.
2. Read [`HANDOFF_NEXT_AGENT.md`](HANDOFF_NEXT_AGENT.md) — **current sprint** (what's in progress right now).
3. Identify task type and **read the matching skill** in [`.cursor/skills/`](.cursor/skills/) before acting.

**Project root:** resolve via `files/scripts/project_paths.py` ? `PROJECT_ROOT`.  
Do **not** hardcode `~/next` — canonical path is **`~/Home/next`**.

---

## Skills index

| Skill | When to use |
|-------|-------------|
| [`job-apply-browser`](.cursor/skills/job-apply-browser/SKILL.md) | Greenhouse, Lever, Workday, company career sites (Databricks batch) |
| [`job-apply-linkedin`](.cursor/skills/job-apply-linkedin/SKILL.md) | LinkedIn Easy Apply modal flows |
| [`prepare-company-resume`](.cursor/skills/prepare-company-resume/SKILL.md) | Regenerate or tailor company PDF resumes |
| [`company-pages-maintenance`](.cursor/skills/company-pages-maintenance/SKILL.md) | Interview questions, company HTML, weekly refresh |

Shared defaults for all application forms:  
[`.cursor/skills/job-apply-browser/DEFAULT_ANSWERS.md`](.cursor/skills/job-apply-browser/DEFAULT_ANSWERS.md)

---

## Hard rules (never break)

### Resume & identity
- **Email on applications:** `naveenreddy.alka@gmail.com` only — never `@intuit.com`.
- **Title:** Staff Software Engineer at Credit Karma (not Senior SWE II).
- **Do not paste full resume text** into forms unless user explicitly approves.
- **Databricks applications:** PDF attach only — `databricks/Naveen_Reddy_Alka_Databricks_Resume.pdf`.

### Application integrity
- Never fabricate answers; use `DEFAULT_ANSWERS.md` or ask user.
- Never claim "submitted" without confirmation page URL or visible success state.
- Update trackers after every major step:
  - Databricks ? `databricks/application_tracker.md`
  - Other companies ? update `files/scripts/build_company_pages_data.py` applications + run refresh

### User does not run scripts manually
- Agent edits source data and runs `files/scripts/refresh_company_pages.sh` when HTML needs updating.
- User only intervenes for: login, 2FA, CAPTCHA, security codes, manual PDF attach if automation blocked.

---

## Browser automation (Cursor IDE Browser MCP)

Used for job applications. Workflow:

1. `browser_tabs` list ? check existing tabs
2. `browser_navigate` to job URL
3. **User logs in manually** for LinkedIn (never ask for password in chat)
4. `browser_lock` ? interact ? `browser_unlock`
5. `browser_snapshot` before every click/fill
6. Stop and ask user on CAPTCHA, 2FA, or security code

See `job-apply-browser` and `job-apply-linkedin` skills for step-by-step flows.

---

## Company pages architecture

| Page | Purpose |
|------|---------|
| `{company}/index.html` | Apply tab, My Applications tab, Latest Questions tab |
| `{company}/company_info.html` | Full research (comp, pros/cons, interview format) — separate page by design |

**Do not** merge company_info content into index tabs — user preference.

### Data flow

```
company_extra_data.py          ??
company_questions_seed.py      ???? update_latest_questions.py
company_questions_inbox.json   ??         ?
build_company_pages_data.py ?????????????
         ?
         ???? gen_company_index.py  ? {company}/index.html
         ???? gen_company_info.py  ? {company}/company_info.html
```

Run: `files/scripts/refresh_company_pages.sh`

---

## Databricks batch (active)

Tracker: [`databricks/application_tracker.md`](databricks/application_tracker.md)

| Job ID | Status |
|--------|--------|
| 6937001002, 5646855002, 7823561002, 5408888002 | Submitted |
| 5646866002 | In progress — PDF attached, needs fresh security code |
| 7994801002, 7274908002 | Pending |

Direct Greenhouse embed URL pattern:
`https://job-boards.greenhouse.io/embed/job_app?for=databricks&token={JOB_ID}`

---

## Resume generation

```bash
cd ~/Home/next/files/scripts
python3 build_resume.py           # generic PDF at project root
python3 gen_company.py            # 11 original company folders + PDFs
python3 gen_xai_spacex.py         # xAI + SpaceX
```

Source bullets: `resume_updates.md`, `resume_creditkarma_bullets.md`, `files/evl/`.

---

## Git workflow

- Repo: `github.com/naveenreddyalka/next`
- Commit after meaningful changes (data, trackers, skills, handoff updates).
- Do not commit: `.venv/`, `.cursor-personal/`, `.refresh_company_pages.log`

---

## Communication pattern with user

- Concise status updates during application batches.
- When blocked, ask for **one exact input** (e.g. "send the Greenhouse security code").
- After each submit report: job ID, status, confirmation URL, tracker updated.

---

## Open backlog

- Finish Databricks batch (5646866002 ? 7994801002 ? 7274908002)
- LinkedIn Easy Apply for target companies
- Continue enriching Latest Questions via public sources + inbox
- Get referrals at Stripe, Anthropic, Confluent
- LeetCode prep: 2 medium/day (arrays, graphs, DP)

See `CONTEXT.md` § Open Items for full list.
