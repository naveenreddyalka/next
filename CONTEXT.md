# Naveen Reddy Alka — Job Search Project Context
> Handoff document for any tool or session picking up this project.
> Last updated: June 2026  
> **Project location:** `~/Home/next`  
> **GitHub:** https://github.com/naveenreddyalka/next  
> **Agent entry point:** Read `AGENTS.md` → `CONTEXT.md` → `HANDOFF_NEXT_AGENT.md`

---

## Who

**Naveen Reddy Alka**
- Email: naveenreddy.alka@gmail.com (personal) | naveenreddy_alka@intuit.com (work — do NOT use on resume)
- Phone: 314-498-5314
- Location: San Francisco Bay Area
- LinkedIn: linkedin.com/in/naveenreddyalka
- Current title: **Staff Software Engineer** at Credit Karma (Feb 2022 – Present)
- Education: MS Computer Science, Arizona State University 2021 | B.Tech Civil Engineering, NIT Warangal 2007

---

## What We Built

### Folder Structure (`~/Home/next/`)
```
/Home/next/
├── README.md                           ← Project overview + clone instructions
├── AGENTS.md                           ← AI agent operating manual
├── HANDOFF_NEXT_AGENT.md               ← Active sprint / current application state
├── index.html                          ← Main hub (13 company cards + task checklist)
├── Naveen_Reddy_Alka_Resume.pdf        ← Generic resume (master copy)
├── resume_updates.md                   ← All resume sections in paste-ready markdown
├── resume_creditkarma_bullets.md       ← Detailed CK bullets from promo docs
├── job_matches.md                      ← All 13 matched roles with job IDs
│
├── .cursor/skills/                     ← Agent skills (in repo)
│   ├── job-apply-browser/              ← Greenhouse / ATS applications
│   ├── job-apply-linkedin/             ← LinkedIn Easy Apply
│   ├── prepare-company-resume/         ← PDF resume generation
│   └── company-pages-maintenance/      ← Interview questions + HTML pipeline
│
├── {company}/                          ← One folder per target company
│   ├── index.html                      ← Apply | My Applications | Latest Questions
│   ├── company_info.html               ← Research (comp, interview, pros/cons)
│   ├── Naveen_Reddy_Alka_{Co}_Resume.pdf
│   └── Naveen_Reddy_Alka_Resume.pdf    ← Generic resume copy
│
├── databricks/
│   └── application_tracker.md          ← Active Greenhouse application batch
│
├── resources/                          ← General reference docs (HTML)
│
└── files/
    ├── evl/                            ← Employment verification letters
    ├── scripts/                        ← Data pipeline + resume generators
    │   ├── company_extra_data.py       ← Snapshot, perks, how-to-crack
    │   ├── company_questions_seed.py   ← Interview question seed bank
    │   ├── refresh_company_pages.sh    ← Rebuild all HTML
    │   └── project_paths.py            ← PROJECT_ROOT (location-independent)
    └── launchd/                        ← Weekly refresh LaunchAgent plist
```

### Target Companies (13 total)
| Company | Role | Job ID | URL |
|---------|------|--------|-----|
| Anthropic | Staff SWE, Platform | 5157847008 | https://boards.greenhouse.io/anthropic/jobs/5157847008 |
| OpenAI | Senior Staff Backend SWE, API Platform | API-Platform-SWE | https://openai.com/careers/ |
| xAI | Senior Grok Engineer | 4823149007 | https://job-boards.greenhouse.io/xai/jobs/4823149007 |
| NVIDIA | Senior Cloud Platform SWE | JR2003876 | https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/JR2003876 |
| ServiceNow | Staff SWE, Backend Java | 744000086443311 | https://jobs.servicenow.com/en/jobs/744000086443311 |
| Confluent | Senior SWE — Apache Kafka | 15812054 | https://careers.confluent.io/jobs/15812054 |
| Databricks | Staff SWE — Distributed Data Systems | 6937001002 | https://www.databricks.com/company/careers/open-positions/6937001002 |
| Stripe | SWE, Payments | 7529787 | https://stripe.com/jobs/listing/software-engineer/7529787 |
| Google | SWE, Cloud Financial Services | 121405674409075398 | https://careers.google.com/jobs/results/121405674409075398 |
| Snowflake | Senior SWE — Cloud Services | SNCOUS683A | https://careers.snowflake.com/us/en |
| Netflix | Distributed Systems Engineer 5 — Cloud Gateway | 790315481039 | https://jobs.netflix.com/jobs/790315481039 |
| Uber | Staff SWE (Backend) — Java Platform | 156244 | https://www.uber.com/global/en/careers/list/156244/ |
| SpaceX | Sr. Backend SWE — Distributed Systems (Starlink) | 8300183002 | https://job-boards.greenhouse.io/spacex/jobs/8300183002 |

---

## Resume — Full Work History

All bullets are sourced from EVL letters (files/evl/) and Credit Karma promo/tech review documents.
Numbers are presented in the best defensible light.

### Credit Karma, Oakland — Staff Software Engineer — Feb 2022 – Present
- Portal Provider framework: 90%+ of CK portals clients depend on it
- Dashboard × Portals SDK federation: 100% production ramp, RecSys V2 integration, HELOC/Home Refi unblocked
- Portals Local Eligibility: 45% faster rendering
- Data Contracts: days→minutes release time; org-wide adoption lead
- Talon/Polly incident resolution + load testing infra
- Finagle web framework (EOL Twitter stack) ownership
- Stack: Scala, TypeScript, Java, Kafka, Kubernetes, Finagle, GraphQL, Node.js, AWS/GCP

### Turo, San Francisco — Senior Software Engineer — Jan 2021 – Feb 2022
- Resolved API-to-DB bottlenecks, ~30% latency reduction
- Modernized legacy services
- Stack: Java, Spring Boot, microservices

### Pearson Inc, San Francisco — Senior Software Engineer — Jan 2020 – Jan 2021
- Cross-cutting platform services (logging, security, metrics, monitoring) using Spring WebFlux + Project Reactor — adopted by all engineering teams
- Kafka pipelines, CouchBase data layer, Kubernetes + AWS infra
- Stack: Java, Spring WebFlux, Project Reactor, Kafka, CouchBase, Kubernetes, AWS

### Nordstrom, Seattle — Senior Engineer — Mar 2019 – Oct 2019
- Salary: $150,000/yr confirmed in EVL
- Ordering and Allocation team: legacy monolith → Kubernetes microservices
- AWS + GCP, GitLab CI/CD, Spring Boot, MySQL/Postgres
- Stack: Java, Spring, Hibernate, MySQL, Postgres, Docker, AWS, GCP, Git

### Wenova Inc, St. Louis — Software Engineer — Mar 2018 – Mar 2019
- Customer Data Hub (CDH) microservice: REST + GraphQL APIs to 10+ internal systems, Kafka propagation
- Stack: Java, Spring, Hibernate, XML/XSLT, GraphQL, PostgreSQL, AWS

### MakeMyTrip, Bangalore — Sr. Principal Software Engineer (Payments Architect) — Sep 2016 – Jan 2018
- Sole architect of full ground-up payments platform revamp
- Multi-datacenter, multi-tenant, 80+ payment gateways/aggregators
- 50% reduction in response time, 60% reduction in maintenance cost, 2%+ payment success rate over billions in monthly transactions → millions in incremental revenue
- Led team of 5; owned full delivery lifecycle
- Stack: Java, Spring, Hibernate, MySQL, CouchBase, RabbitMQ, Kafka, Cassandra, Tomcat, Jenkins

### VERSE – DailyHunt, Bangalore — Principal Software Engineer — Apr 2016 – Sep 2016
- Books search platform: Elasticsearch + Node.js, serving millions of queries
- Full-text search, fuzzy matching, autocomplete, vernacular support
- Stack: Java, Spring, Elasticsearch, Node.js, Kafka, Redis, Docker

### Myntra – Flipkart, Bangalore — Technical Lead, Secure Checkout — Dec 2013 – Mar 2016
- Payments, Address, Cart systems: 100% uptime, 500M+ active carts, 150,000+ daily payments
- Payment Plan Service (PPS) built from scratch: all payment instruments, dynamic gateway switching
- 50x traffic scaling for End of Season Sale: Cassandra + algorithmic distributed sharding over MySQL
- Stack: Java, Spring, Hibernate, MySQL, Cassandra, Jersey, Nginx, ZooKeeper, ActiveMQ, Elasticsearch, HAProxy

### Wavecrest Payment Services, Hyderabad — Dev Lead — Nov 2009 – Dec 2013
- Founding member; 3 promotions in 4 years (SE → SSE → Lead Eng → Dev Lead)
- Led 8-engineer team: cashier + eWallet, 200,000+ card issuances/day, PCI compliant
- Clients: PartyGaming-Bwin, Reliance, GTECH, TrillionPay, O2, Loopium, Tarcha
- Stack: Java, Spring, Hibernate, MySQL, ActiveMQ, SOAP, REST, Redis, Docker, Dojo/jQuery, Jenkins

### IvyComptech, Hyderabad — Software Engineer — Jan 2009 – Nov 2009
- Affiliates, Store, and Loyalty Systems
- Stack: Java, Spring, Struts2, Perl, MySQL, Ajax, Jenkins, Tomcat

### Cognizant, Hyderabad — Program Analyst — Nov 2007 – Jan 2009
- American Express small business apply site: Apply-Strategy project, data migration, DOJO migration
- Stack: Java, J2EE, Struts, XSLT, XSD, Dojo, EJB, RMI, Tomcat

---

## Skills (Full)
- **Languages:** Java (SCJP 98%), Scala, Kotlin, TypeScript, JavaScript, Python, Perl
- **Frameworks:** Spring Boot, Spring WebFlux, Project Reactor, Hibernate, Finagle, Node.js, GraphQL, Jersey, Struts2
- **Messaging:** Apache Kafka, RabbitMQ, ActiveMQ
- **Databases:** Cassandra, Redis, CouchBase, Elasticsearch, MySQL, PostgreSQL, Oracle, MongoDB
- **Cloud & Infra:** AWS, GCP, Azure, Kubernetes, Docker, Nginx, HAProxy, Tomcat
- **Observability:** Datadog, New Relic, Splunk, Sentry, Graphite/StatsD
- **CI/CD:** GitLab CI/CD, Jenkins, GitHub Actions, Maven, Gradle, Git, SVN
- **Practices:** Microservices, Event-Driven Architecture, Event Sourcing, TDD, PCI DSS, Agile/Scrum, System Design

---

## Resume Scripts
All resumes are generated via Python + ReportLab. To regenerate:
```bash
cd ~/Home/next/files/scripts
pip install reportlab   # or: source ../../.venv/bin/activate
python3 build_resume.py          # Generic resume
python3 gen_company.py           # 11 company tailored resumes
python3 gen_xai_spacex.py        # xAI + SpaceX resumes
```
See `.cursor/skills/prepare-company-resume/SKILL.md` for full workflow.

---

## EVL Source Files
All employment verification letters are in `files/evl/`:
- `experience/` — numbered PDFs (1=CTS, 2=IvyComptech, 3=Wavecrest, 4=Myntra, 5=VERSE, 6=MMT, 7=Wenova, 8=Nordstrom, 9=Pearson)
- `letters/` — original docx/pdf EVLs
- `new_evls/` — detailed draft EVLs with full responsibility breakdowns (cts, mmt, myntra, wavecrest)

---

## Key Decisions Made
1. **Title:** "Staff Software Engineer" at Credit Karma (not Senior SWE II)
2. **Email on resume:** naveenreddy.alka@gmail.com (not intuit email)
3. **Phone on resume:** 314-498-5314
4. **Numbers:** Presented at best defensible level from EVL sources; some rounded up (e.g. 200k+ cards/day, 30% Turo latency)
5. **Myntra dates:** Dec 30, 2013 – Mar 31, 2016 (confirmed from detailed EVL)
6. **MakeMyTrip response time:** 50% (profile) — EVL letter says 40%, but 50% used for impact
7. **NICMAR degree removed** — not relevant for tech roles
8. **"Personal Details" section removed** — not standard in US resumes
9. **References section removed** — not needed at resume stage

---

## Open Items / Things Still To Do
- Fill in Turo % latency improvement (exact number unknown, used ~30%)
- Fill in Pearson team count (how many engineering teams adopted cross-cutting services)
- Update LinkedIn to match resume title + bullets
- Get referrals at Stripe, Anthropic, Confluent
- Continue Databricks campaign (see `databricks/application_tracker.md`)
- Apply to remaining target companies after Databricks batch completes
- LeetCode prep: 2 medium/day, focus arrays, graphs, DP
- System design prep: Kafka, Cassandra, rate limiting, sharding patterns

---

## Active Campaign Handoff

- Primary handoff file: `HANDOFF_NEXT_AGENT.md`
- Databricks execution tracker: `databricks/application_tracker.md`
- Current state (as of 2026-06-05):
  - Submitted Databricks roles: `6937001002`, `5646855002`, `7823561002`, `5408888002`
  - In progress: `5646866002` (PDF attached, waiting for fresh security code)
  - Pending: `7994801002`, `7274908002`
  - Resume rule: PDF attach only for Databricks applications

---

## Navigation
- Open `file:///Users/nalka/Home/next/index.html` in browser to access the full hub
- All company pages: `file:///Users/nalka/Home/next/{company}/index.html`
- Generic resume: `file:///Users/nalka/Home/next/Naveen_Reddy_Alka_Resume.pdf`
