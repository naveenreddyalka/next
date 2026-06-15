---
name: job-apply-linkedin
description: Apply to jobs via LinkedIn Easy Apply using Cursor browser automation and saved candidate defaults. Use when user asks to Easy Apply on LinkedIn, apply from linkedin.com/jobs, or batch LinkedIn applications.
---

# Job Apply — LinkedIn Easy Apply

## Prerequisites

- Cursor IDE Browser MCP enabled
- User logged into LinkedIn **in Cursor's browser tab** (agent cannot use external Chrome session)
- Defaults from [../job-apply-browser/DEFAULT_ANSWERS.md](../job-apply-browser/DEFAULT_ANSWERS.md)

## Quick start inputs

Collect from user:
- LinkedIn job URL (or company + role to search)
- Resume: LinkedIn profile **or** tailored PDF path (`{company}/Naveen_Reddy_Alka_{Co}_Resume.pdf`)
- Submit policy: auto-submit vs pause for review before final click

## Session setup (first time per Cursor session)

1. `browser_navigate` ? `https://www.linkedin.com/jobs/`
2. **Stop — user logs in manually** (password, 2FA, CAPTCHA)
3. User says: "Logged in — continue"
4. `browser_lock` ? proceed with applications ? `browser_unlock` when done

Never ask user to paste LinkedIn password in chat.

## Easy Apply workflow

1. Navigate to job posting URL
2. `browser_snapshot` — confirm "Easy Apply" button visible
3. Click **Easy Apply**
4. Step through modal pages:
   - Contact info (usually pre-filled — verify email/phone)
   - Resume (select PDF upload or LinkedIn profile per user preference)
   - Screening questions ? map to DEFAULT_ANSWERS.md
   - EEO/diversity (optional on LinkedIn — fill if required)
5. **Review page:** pause if user requested review; else Submit
6. Confirm "Application sent" or equivalent success state
7. Record: company, role, URL, date, resume used

## If not Easy Apply

Some listings show **Apply on company website** — switch to [`job-apply-browser`](../job-apply-browser/SKILL.md) skill for ATS/Greenhouse flows.

## Screening question mapping

| Common question | Default |
|-----------------|---------|
| Work authorization in US | Yes |
| Require sponsorship now/future | Yes |
| Willing to relocate | Confirm with user if asked |
| Years of experience | Derive from resume (Staff SWE, ~18+ years) |
| Salary expectations | **Ask user** before submitting if required |

Full mapping: `DEFAULT_ANSWERS.md`

## Browser MCP rules

- Snapshot before every interaction
- Short waits (1-3s) + re-snapshot instead of long blind waits
- On CAPTCHA / verification loop: stop, ask user to complete manually
- Max 4 retries on same failing action — then report blocker

## Tracking

After each successful apply:
- Note in conversation for user
- Optionally add row to company's applications in `files/scripts/build_company_pages_data.py` + run `refresh_company_pages.sh`
- For Databricks roles on LinkedIn: also update `databricks/application_tracker.md`

## Safety

- Do not claim success without "Application sent" or equivalent
- Do not auto-submit if screening questions are ambiguous
- Use tailored PDF when applying to priority target companies (see CONTEXT.md company list)
