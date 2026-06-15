---
name: job-apply-browser
description: Applies to job listings through browser forms using saved candidate defaults. Use for Greenhouse, Lever, Workday, Databricks embed URLs, and company career site ATS forms. For LinkedIn Easy Apply use job-apply-linkedin skill instead.
---

# Job Apply Browser (ATS / Company Sites)

## Related skills

- **LinkedIn Easy Apply:** [job-apply-linkedin](../job-apply-linkedin/SKILL.md)
- **Resume PDF:** [prepare-company-resume](../prepare-company-resume/SKILL.md)
- **Defaults:** [DEFAULT_ANSWERS.md](DEFAULT_ANSWERS.md)

## Quick start

Collect:
- Job URL (prefer direct ATS apply URL)
- Tailored resume PDF path
- Company name (for tracker update)

Then:
1. Open URL in Cursor browser MCP
2. Fill form using DEFAULT_ANSWERS.md
3. Attach resume PDF
4. Handle security code / CAPTCHA with user help
5. Submit → confirm success page
6. Update tracker

## Workflow

### 1) Reach the real apply form

- **Databricks:** use direct embed URL (more reliable than wrapper page):
  `https://job-boards.greenhouse.io/embed/job_app?for=databricks&token=<job_id>`
- **Greenhouse:** prefer embed/apply URL when available
- Fresh `browser_snapshot` after every navigation/click

### 2) Fill core fields

- First/last name, email, phone, location, LinkedIn
- Education (Greenhouse often requires): ASU, Master's, Computer Science, 2019–2021
- Re-check `invalid` states; explicitly select dropdown options and blur

### 3) Standard question blocks

From DEFAULT_ANSWERS.md:
- Work authorization: **Yes** | Sponsorship: **Yes**
- Prior employment at company: No
- Export/sanctions: None of the above + Not applicable
- EEO: Male, Not Hispanic/Latino, Asian, Not protected veteran, No disability

### 4) Resume upload

- Click Attach → upload PDF
- Confirm: filename visible OR "Remove file" button appears
- **Databricks rule:** PDF only — never paste resume text unless user approves
- If native picker blocked: user attaches manually, agent continues

### 5) Security code / anti-bot

- Greenhouse may email a code before final submit
- Ask user for code; fill and submit quickly (codes expire)
- CAPTCHA/2FA: user takes over briefly

### 6) Verify submission

Success = confirmation page (e.g. `Thank you for applying`, URL contains `/confirmation`)

Report: job ID, submitted yes/no, confirmation URL, blockers

## Databricks batch tracker

Active tracker: `databricks/application_tracker.md`  
Update after **every** major step.

Current state — see `HANDOFF_NEXT_AGENT.md` for latest job IDs and statuses.

## Browser MCP (Cursor)

```
browser_navigate → browser_lock → snapshot/interact → browser_unlock
```

Stop on login walls unless user is present to authenticate.

## Safety

- Never fabricate answers
- Ask before submit if question missing from defaults
- Never claim success without confirmation evidence
