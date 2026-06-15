---
name: prepare-company-resume
description: Generate or update tailored PDF resumes per target company using ReportLab scripts and resume source markdown. Use when user asks to build, regenerate, or tailor a company resume, update resume bullets, or create Naveen_Reddy_Alka_{Company}_Resume.pdf.
---

# Prepare Company Resume

## When to use

- Regenerate generic resume PDF
- Create or update a company-tailored resume
- After editing bullets in `resume_updates.md` or `resume_creditkarma_bullets.md`

## Source files (read before editing)

| File | Content |
|------|---------|
| `resume_updates.md` | All sections in paste-ready markdown |
| `resume_creditkarma_bullets.md` | Detailed CK bullets from promo docs |
| `CONTEXT.md` | Work history, title rules, number conventions |
| `files/evl/` | Employment verification letters (ground truth for dates/numbers) |

## Hard rules

- Email: `naveenreddy.alka@gmail.com` — never `@intuit.com`
- Title at CK: **Staff Software Engineer** (Feb 2022 – Present)
- Phone: 314-498-5314
- Do not invent metrics; use defensible numbers from EVLs (see CONTEXT.md § Key Decisions)

## Regenerate commands

From project root (`~/Home/next`):

```bash
cd files/scripts

# Generic master resume ? ~/Home/next/Naveen_Reddy_Alka_Resume.pdf
python3 build_resume.py

# 11 original companies (anthropic, confluent, databricks, google, netflix, nvidia, openai, servicenow, snowflake, stripe, uber)
python3 gen_company.py

# xAI + SpaceX only
python3 gen_xai_spacex.py
```

Requires: `pip install reportlab` (use `.venv` if present).

Output per company:
- `{company}/Naveen_Reddy_Alka_{CompanySlug}_Resume.pdf`
- Also copies generic PDF to each company folder

## Tailoring guidance

Each company entry in `gen_company.py` / `gen_xai_spacex.py` has:
- `profile` — opening summary paragraph
- `tags` — skills emphasis
- Optional bullet reordering for company fit

When tailoring for a new role:
1. Read the job description and company `company_extra_data.py` focus areas
2. Edit the company block in the generator script OR `resume_updates.md` if doing manual paste
3. Regenerate PDF
4. Verify output opens correctly

## Company page HTML

Company pages link to the tailored PDF automatically. After regenerating resumes, no HTML rebuild needed unless job metadata changed.

## Do not

- Paste full resume text into application forms unless user explicitly approves
- Change employment dates without EVL confirmation
- Add NICMAR degree or "Personal Details" / "References" sections (removed by design)
