"""
Generate per-company HTML + tailored resume PDF for each target company.
"""
import os, shutil
from pathlib import Path
from project_paths import PROJECT_ROOT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable
from reportlab.lib.enums import TA_CENTER

BASE = str(PROJECT_ROOT)
GENERIC_PDF = f"{BASE}/Naveen_Reddy_Alka_Resume.pdf"

BLUE = colors.HexColor("#1a3a5c")
LIGHT_GRAY = colors.HexColor("#555555")

name_style   = ParagraphStyle("Name",    fontSize=22, fontName="Helvetica-Bold",  textColor=BLUE,         spaceAfter=10, leading=28, alignment=TA_CENTER)
contact_style= ParagraphStyle("Contact", fontSize=9,  fontName="Helvetica",       textColor=LIGHT_GRAY,   spaceAfter=6,  alignment=TA_CENTER)
section_style= ParagraphStyle("Section", fontSize=11, fontName="Helvetica-Bold",  textColor=BLUE,         spaceBefore=10,spaceAfter=3)
job_style    = ParagraphStyle("Job",     fontSize=9.5,fontName="Helvetica-Bold",  textColor=colors.black, spaceBefore=7, spaceAfter=1)
body_style   = ParagraphStyle("Body",    fontSize=9,  fontName="Helvetica",       textColor=colors.black, spaceAfter=2,  leading=13)
bullet_style = ParagraphStyle("Bullet",  fontSize=9,  fontName="Helvetica",       textColor=colors.black, spaceAfter=3,  leading=13, leftIndent=12, firstLineIndent=-12)

def hr():   return HRFlowable(width="100%", thickness=0.75, color=BLUE, spaceAfter=4, spaceBefore=2)
def sec(t): return [Paragraph(t.upper(), section_style), hr()]
def bul(t): return Paragraph(f"• {t}", bullet_style)
def job(t): return Paragraph(f"<b>{t}</b>", job_style)

CONTACT = "San Francisco Bay Area &nbsp;|&nbsp; 314-498-5314 &nbsp;|&nbsp; naveenreddy.alka@gmail.com &nbsp;|&nbsp; linkedin.com/in/naveenreddyalka"

SKILLS = [
    ("Languages",           "Java (SCJP 98%), Scala, Kotlin, TypeScript, JavaScript, Python, Perl"),
    ("Frameworks",          "Spring Boot, Spring WebFlux, Project Reactor, Hibernate, Finagle, Node.js, GraphQL, Jersey"),
    ("Messaging",           "Apache Kafka, RabbitMQ, ActiveMQ"),
    ("Databases",           "Cassandra, Redis, CouchBase, Elasticsearch, MySQL, PostgreSQL, Oracle, MongoDB"),
    ("Cloud & Infra",       "AWS, GCP, Azure, Kubernetes, Docker, Nginx, HAProxy, Tomcat"),
    ("Observability",       "Datadog, New Relic, Splunk, Sentry, Graphite/StatsD"),
    ("CI/CD",               "GitLab CI/CD, Jenkins, GitHub Actions, Maven, Gradle, Git"),
    ("Practices",           "Microservices, Event-Driven Architecture, Event Sourcing, TDD, PCI DSS, Agile/Scrum"),
]

# ── Job content blocks ──────────────────────────────────────────────────────
CK_BULLETS = [
    "Designed and built the Portal Provider framework — core abstraction for dynamic portal configuration powering <b>90%+ of Credit Karma portals clients</b>; foundation of the federated portals SDK adopted org-wide.",
    "Led end-to-end delivery of Dashboard × Portals SDK federation — designed Bridge API for phased A/B rollout, achieved <b>100% production ramp</b>, enabled RecSys V2 integration, unblocked HELOC/Home Refi verticals; recognized with 5+ public kudos by VP and two Directors.",
    "Architected Portals Local Eligibility (GA Feb 2025) — moved eligibility into client-side SDK delivering <b>45% faster rendering</b> and eliminating redundant upstream network calls.",
    "Led Data Contracts from inception through production (Oct 2025) — cross-language codegen (TypeScript, GraphQL, Scala), Thrift IDL, automated publish pipeline reducing release time <b>from days to minutes</b>; named org-wide adoption lead by Director.",
    "Resolved critical Talon/Polly production incidents: memory leaks, pm2 socket exhaustion, MGS startup latency spikes; built reusable load testing infrastructure now used across all Polly teams.",
    "Own and evolve Finagle-based web framework (EOL Twitter stack) serving all Credit Karma product teams — SLAs, scalability, incremental modernization in Scala and TypeScript.",
]
MMT_BULLETS = [
    "Sole architect of MakeMyTrip's payments platform revamp — multi-datacenter, multi-tenant system integrating <b>80+ payment gateways and aggregators</b> (saved cards over HSM, wallets, discounting, fraud management).",
    "Achieved <b>50% reduction in payment response time</b>, <b>60% reduction in maintenance cost</b>, and <b>2%+ improvement in payment success rate</b> over billions of dollars of monthly transactions — driving <b>millions in incremental revenue</b>.",
    "Built and led team of 5 engineers; owned full delivery: architecture reviews with CTO, A/B testing, staged rollout, disaster recovery, full CI/CD via Jenkins + Cucumber + Selenium.",
    "Stack: Java · Spring · Hibernate · MySQL · CouchBase · RabbitMQ · Kafka · Cassandra · Tomcat.",
]
MYNTRA_BULLETS = [
    "Led Secure Checkout team owning Payments, Address, and Cart — <b>100% uptime</b> at <b>500M+ active carts</b> and <b>150,000+ daily payment transactions</b> on India's largest fashion platform.",
    "Built Payment Plan Service (PPS) from scratch — unified all payment instruments (CC, DC, Gift Cards, Wallets, CashBack) with dynamic gateway auto-switching algorithm.",
    "Engineered 50x traffic scaling for End of Season Sale — Cassandra NoSQL primary store + first-of-its-kind application-level distributed sharding over MySQL for 500M+ objects.",
    "Stack: Java · Spring · Hibernate · MySQL · Cassandra · Jersey · Nginx · ZooKeeper · ActiveMQ · Elasticsearch · HAProxy.",
]
WAVE_BULLETS = [
    "Founding member of Wavecrest engineering team — promoted <b>3 times in 4 years</b> (SE → SSE → Lead Engineer → Dev Lead).",
    "Led 8-engineer team building cashier and eWallet products — prepaid cards, payroll cards, digital wallets, mobile payments processing <b>200,000+ card issuances per day</b> with PCI compliance.",
    "Delivered financial systems for PartyGaming-Bwin, Reliance, GTECH, TrillionPay, O2; accountable for architecture, code quality, mentorship.",
    "Stack: Java · Spring · Hibernate · MySQL · ActiveMQ · SOAP · REST · Redis · Docker · Jenkins.",
]
TURO = [
    "Resolved critical network, infra, and design-level bottlenecks — optimized API-to-database patterns reducing latency by up to <b>30%</b> and improving overall throughput.",
    "Led modernization of high-traffic legacy services, improving reliability and reducing incident rate across the backend.",
]
PEARSON = [
    "Architected cross-cutting platform services (logging, security, metrics, monitoring) using Spring WebFlux + Project Reactor — adopted by <b>all engineering teams</b>, standardizing observability org-wide.",
    "Delivered Kafka event pipelines, CouchBase data layer, and Kubernetes + AWS shared infra enabling Pearson's reactive architecture roadmap.",
]
NORDSTROM = [
    "Ordering and Allocation team — led decommission of legacy monolithic ordering systems into Kubernetes-native microservices using Spring Boot + REST/SOAP across AWS and GCP.",
    "Drove performance optimization and security hardening; worked with MySQL/Postgres, Docker/Linux, Git.",
]
WENOVA = [
    "Designed and built Customer Data Hub (CDH) — central microservice exposing REST + GraphQL APIs to 10+ internal systems including Salesforce, with Kafka event-driven propagation.",
    "Delivered Java/Spring/Hibernate services on AWS with PostgreSQL/NoSQL; XML/XSLT/SOAP data transformation pipelines.",
]
VERSE = [
    "Designed Books search platform — full-text search, fuzzy matching, autocomplete, vernacular support serving millions of queries via Elasticsearch + Node.js.",
    "Stack: Java · Spring · Hibernate · Elasticsearch · Node.js · Kafka · Redis · Docker.",
]
IVY = [
    "Built scalable components for Store, Affiliates, and Loyalty Systems on a high-traffic gaming affiliate platform.",
    "Stack: Java · Spring · Struts2 · Perl · MySQL · Ajax · Jenkins · Tomcat.",
]
CTS = [
    "Core engineer on American Express small business apply site — led Apply-Strategy project: complete data management system upgrade, data migration, DOJO migration from MooTools.",
    "Stack: Java · J2EE · Struts · XSLT · XSD · Dojo · EJB · RMI · Tomcat.",
]

def build_pdf(path, profile, job_order):
    doc = SimpleDocTemplate(path, pagesize=letter,
        leftMargin=0.65*inch, rightMargin=0.65*inch,
        topMargin=0.55*inch, bottomMargin=0.55*inch)
    s = []
    s.append(Paragraph("NAVEEN REDDY ALKA", name_style))
    s.append(Paragraph(CONTACT, contact_style))
    s += sec("Profile")
    s.append(Paragraph(profile, body_style))
    s += sec("Skills")
    for lbl, val in SKILLS:
        s.append(Paragraph(f"<b>{lbl}:</b>  {val}", body_style))
    s += sec("Experience")
    for title, bullets in job_order:
        s.append(job(title))
        for bl in bullets:
            s.append(bul(bl))
    s += sec("Education")
    s.append(Paragraph("<b>Arizona State University</b> — MS Computer Science, 2021", body_style))
    s.append(Paragraph("<b>National Institute of Technology, Warangal</b> — B.Tech Civil Engineering, 2007", body_style))
    doc.build(s)

# ── Standard job order ──────────────────────────────────────────────────────
STD_JOBS = [
    ("Credit Karma, Oakland  ·  Staff Software Engineer  ·  Feb 2022 – Present", CK_BULLETS),
    ("Turo, San Francisco  ·  Senior Software Engineer  ·  Jan 2021 – Feb 2022", TURO),
    ("Pearson Inc, San Francisco  ·  Senior Software Engineer  ·  Jan 2020 – Jan 2021", PEARSON),
    ("Nordstrom, Seattle  ·  Senior Engineer  ·  Mar 2019 – Oct 2019", NORDSTROM),
    ("Wenova Inc, St. Louis  ·  Software Engineer  ·  Mar 2018 – Mar 2019", WENOVA),
    ("MakeMyTrip, Bangalore  ·  Sr. Principal Software Engineer — Payments Architect  ·  Sep 2016 – Jan 2018", MMT_BULLETS),
    ("VERSE – DailyHunt, Bangalore  ·  Principal Software Engineer  ·  Apr 2016 – Sep 2016", VERSE),
    ("Myntra – Flipkart, Bangalore  ·  Technical Lead, Secure Checkout  ·  Dec 2013 – Mar 2016", MYNTRA_BULLETS),
    ("Wavecrest Payment Services  ·  Dev Lead  ·  Nov 2009 – Dec 2013", WAVE_BULLETS),
    ("IvyComptech, Hyderabad  ·  Software Engineer  ·  Jan 2009 – Nov 2009", IVY),
    ("Cognizant, Hyderabad  ·  Program Analyst  ·  Nov 2007 – Jan 2009", CTS),
]

# ── Company definitions ─────────────────────────────────────────────────────
COMPANIES = {
    "stripe": {
        "name": "Stripe",
        "color": "#635bff",
        "jobs": [
            {"title": "Software Engineer, Payments", "id": "7529787",
             "url": "https://stripe.com/jobs/listing/software-engineer/7529787",
             "fit": "Payments domain depth across MakeMyTrip (80+ gateways, billions in txns), Myntra (150k+ daily payments), and Wavecrest (200k+ card issuances/day) — 10+ years in PCI-compliant payment systems."}
        ],
        "profile": "Payments-specialist Senior Software Engineer with 17+ years — 10+ of which spent exclusively in payment systems. Architected MakeMyTrip's payment platform from scratch (80+ gateways, multi-datacenter, 50% faster response, 60% lower cost), led Myntra's 150,000+ daily payment transaction stack, and built Wavecrest's PCI-compliant card issuance platform processing 200,000+ cards per day. Deep Java/Spring/Kafka/Cassandra stack. MS CS, ASU 2021.",
        "job_order": [
            ("MakeMyTrip, Bangalore  ·  Sr. Principal Software Engineer — Payments Architect  ·  Sep 2016 – Jan 2018", MMT_BULLETS),
            ("Myntra – Flipkart, Bangalore  ·  Technical Lead, Secure Checkout  ·  Dec 2013 – Mar 2016", MYNTRA_BULLETS),
            ("Wavecrest Payment Services  ·  Dev Lead  ·  Nov 2009 – Dec 2013", WAVE_BULLETS),
            ("Credit Karma, Oakland  ·  Staff Software Engineer  ·  Feb 2022 – Present", CK_BULLETS),
            ("Turo, San Francisco  ·  Senior Software Engineer  ·  Jan 2021 – Feb 2022", TURO),
            ("Pearson Inc, San Francisco  ·  Senior Software Engineer  ·  Jan 2020 – Jan 2021", PEARSON),
            ("Nordstrom, Seattle  ·  Senior Engineer  ·  Mar 2019 – Oct 2019", NORDSTROM),
            ("Wenova Inc, St. Louis  ·  Software Engineer  ·  Mar 2018 – Mar 2019", WENOVA),
            ("VERSE – DailyHunt, Bangalore  ·  Principal Software Engineer  ·  Apr 2016 – Sep 2016", VERSE),
            ("IvyComptech, Hyderabad  ·  Software Engineer  ·  Jan 2009 – Nov 2009", IVY),
            ("Cognizant, Hyderabad  ·  Program Analyst  ·  Nov 2007 – Jan 2009", CTS),
        ],
    },
    "confluent": {
        "name": "Confluent",
        "color": "#0092e0",
        "jobs": [
            {"title": "Senior Software Engineer — Apache Kafka", "id": "15812054",
             "url": "https://careers.confluent.io/jobs/15812054",
             "fit": "Kafka used across MakeMyTrip (payment event streaming), Pearson (cross-team event pipelines), Wenova (CDH real-time propagation), Verse, and Credit Karma. Deep understanding of event-driven, distributed systems design."}
        ],
        "profile": "Senior Software Engineer with 17+ years and deep Apache Kafka expertise — used Kafka as the backbone of event-driven architectures at MakeMyTrip (payment streaming), Pearson (org-wide event pipelines), Wenova (real-time customer data propagation), and VERSE. Specializes in distributed systems, messaging infrastructure, and large-scale backend engineering. Java/Scala/Kafka/Cassandra/Kubernetes. MS CS, ASU 2021.",
        "job_order": STD_JOBS,
    },
    "databricks": {
        "name": "Databricks",
        "color": "#ff3621",
        "jobs": [
            {"title": "Staff Software Engineer — Distributed Data Systems", "id": "6937001002",
             "url": "https://www.databricks.com/company/careers/open-positions/6937001002",
             "fit": "Extensive distributed data systems: Cassandra clusters, CouchBase, Elasticsearch at scale, application-level sharding over MySQL (500M objects), multi-datacenter data architectures."}
        ],
        "profile": "Senior/Staff Software Engineer with 17+ years specializing in distributed data systems and large-scale backend infrastructure. Designed multi-datacenter data architectures at MakeMyTrip, built application-level distributed sharding over MySQL to manage 500M+ objects at Myntra, and led platform-wide data contracts and schema systems at Credit Karma. Deep Cassandra, Elasticsearch, CouchBase, Kafka, and Kubernetes expertise. Java/Scala/TypeScript. MS CS, ASU 2021.",
        "job_order": STD_JOBS,
    },
    "anthropic": {
        "name": "Anthropic",
        "color": "#c85f31",
        "jobs": [
            {"title": "Staff Software Engineer, Platform", "id": "5157847008",
             "url": "https://boards.greenhouse.io/anthropic/jobs/5157847008",
             "fit": "Platform framework ownership (Portal Provider powering 90%+ of CK clients), TypeScript/Scala/Node.js expertise, data contracts and schema systems, distributed systems at scale."}
        ],
        "profile": "Staff-level Software Engineer with 17+ years building platform infrastructure and distributed backend systems. At Credit Karma, designed and own the Portal Provider framework relied on by 90%+ of portals clients, led the org's most complex platform migrations, and built the Data Contracts system enabling cross-language schema governance. Deep Scala, TypeScript, Java, Kafka, Kubernetes, and cloud infrastructure expertise. MS CS, ASU 2021.",
        "job_order": STD_JOBS,
    },
    "openai": {
        "name": "OpenAI",
        "color": "#10a37f",
        "jobs": [
            {"title": "Senior Staff Backend Software Engineer, API Platform", "id": "API-Platform-SWE",
             "url": "https://openai.com/careers/",
             "fit": "API platform engineering at Credit Karma (Finagle web framework, federated SDK), distributed systems, TypeScript/Scala/Java, event-driven architecture, platform framework ownership."}
        ],
        "profile": "Senior Staff Software Engineer with 17+ years in platform infrastructure and API systems. At Credit Karma, owns the Finagle-based web framework serving all product teams and architected the federated Portal Provider framework relied on by 90%+ of clients. Deep expertise in distributed backend systems, event-driven architecture, and cross-language platform design. Java · Scala · TypeScript · Kafka · Kubernetes · AWS/GCP. MS CS, ASU 2021.",
        "job_order": STD_JOBS,
    },
    "nvidia": {
        "name": "NVIDIA",
        "color": "#76b900",
        "jobs": [
            {"title": "Senior Cloud Platform Software Engineer", "id": "JR2003876",
             "url": "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/JR2003876",
             "fit": "Cloud platform engineering: Kubernetes, Docker, AWS/GCP/Azure, distributed microservices, platform framework design, observability at scale (Datadog, Splunk, Sentry)."}
        ],
        "profile": "Senior Software Engineer with 17+ years in cloud platform and distributed infrastructure. Built and operated large-scale platforms on Kubernetes/Docker across AWS, GCP, and Azure — from Credit Karma's platform framework serving millions of users to MakeMyTrip's multi-datacenter payment infrastructure. Deep Java/Spring/Kafka/Cassandra stack with strong Kubernetes, observability, and CI/CD expertise. MS CS, ASU 2021.",
        "job_order": STD_JOBS,
    },
    "servicenow": {
        "name": "ServiceNow",
        "color": "#62d84e",
        "jobs": [
            {"title": "Staff Software Engineer, Backend Java", "id": "744000086443311",
             "url": "https://jobs.servicenow.com/en/jobs/744000086443311",
             "fit": "17+ years Java/Spring/Hibernate enterprise backend — designed large-scale platforms, REST/GraphQL API systems, event-driven microservices. Deep enterprise Java ecosystem expertise."}
        ],
        "profile": "Staff Java Backend Software Engineer with 17+ years designing and delivering enterprise-grade distributed systems. Expert in Java/Spring Boot/Hibernate, REST/GraphQL API design, Kafka, Cassandra, and Kubernetes. Built platform-scale systems at Credit Karma, MakeMyTrip, Myntra, and Wavecrest — from payment platforms processing billions of dollars to portal frameworks powering 90%+ of client traffic. MS CS, ASU 2021.",
        "job_order": STD_JOBS,
    },
    "google": {
        "name": "Google",
        "color": "#4285f4",
        "jobs": [
            {"title": "Software Engineer, Cloud Financial Services", "id": "121405674409075398",
             "url": "https://careers.google.com/jobs/results/121405674409075398",
             "fit": "FinTech + cloud at scale: MakeMyTrip payments architecture, Credit Karma platform infrastructure, GCP experience, distributed systems design, Kafka/Cassandra/Kubernetes at massive scale."}
        ],
        "profile": "Senior Software Engineer with 17+ years at the intersection of cloud infrastructure and financial systems. Architected multi-datacenter payment platforms at MakeMyTrip processing billions in monthly transactions, led platform migrations at Credit Karma serving millions of users, and built PCI-compliant financial systems at Wavecrest and Myntra. Deep GCP, AWS, Kubernetes, Kafka, Cassandra, Java, and Scala expertise. MS CS, ASU 2021.",
        "job_order": [
            ("MakeMyTrip, Bangalore  ·  Sr. Principal Software Engineer — Payments Architect  ·  Sep 2016 – Jan 2018", MMT_BULLETS),
            ("Myntra – Flipkart, Bangalore  ·  Technical Lead, Secure Checkout  ·  Dec 2013 – Mar 2016", MYNTRA_BULLETS),
            ("Credit Karma, Oakland  ·  Staff Software Engineer  ·  Feb 2022 – Present", CK_BULLETS),
            ("Wavecrest Payment Services  ·  Dev Lead  ·  Nov 2009 – Dec 2013", WAVE_BULLETS),
            ("Turo, San Francisco  ·  Senior Software Engineer  ·  Jan 2021 – Feb 2022", TURO),
            ("Pearson Inc, San Francisco  ·  Senior Software Engineer  ·  Jan 2020 – Jan 2021", PEARSON),
            ("Nordstrom, Seattle  ·  Senior Engineer  ·  Mar 2019 – Oct 2019", NORDSTROM),
            ("Wenova Inc, St. Louis  ·  Software Engineer  ·  Mar 2018 – Mar 2019", WENOVA),
            ("VERSE – DailyHunt, Bangalore  ·  Principal Software Engineer  ·  Apr 2016 – Sep 2016", VERSE),
            ("IvyComptech, Hyderabad  ·  Software Engineer  ·  Jan 2009 – Nov 2009", IVY),
            ("Cognizant, Hyderabad  ·  Program Analyst  ·  Nov 2007 – Jan 2009", CTS),
        ],
    },
    "snowflake": {
        "name": "Snowflake",
        "color": "#29b5e8",
        "jobs": [
            {"title": "Senior Software Engineer — Cloud Services", "id": "SNCOUS683A",
             "url": "https://careers.snowflake.com/us/en",
             "fit": "Cloud services, distributed data infrastructure, Cassandra/CouchBase/Elasticsearch at scale, multi-datacenter systems, Kubernetes/Docker, Java/Scala."}
        ],
        "profile": "Senior Software Engineer with 17+ years in cloud services and distributed data infrastructure. Deep experience designing and operating large-scale distributed data systems: Cassandra, CouchBase, Elasticsearch, Redis across multi-datacenter deployments. Built cloud-native platforms on Kubernetes/Docker/AWS/GCP at Credit Karma, MakeMyTrip, Pearson, and Nordstrom. Java/Scala/TypeScript. MS CS, ASU 2021.",
        "job_order": STD_JOBS,
    },
    "netflix": {
        "name": "Netflix",
        "color": "#e50914",
        "jobs": [
            {"title": "Distributed Systems Engineer 5 — Cloud Gateway", "id": "790315481039",
             "url": "https://jobs.netflix.com/jobs/790315481039",
             "fit": "Distributed systems, platform/gateway frameworks, Finagle (Twitter stack) web framework ownership at Credit Karma, high-throughput API systems, Kafka/Cassandra/Kubernetes at scale."}
        ],
        "profile": "Senior/Staff Distributed Systems Engineer with 17+ years. Owns the Finagle-based web framework (Twitter stack) at Credit Karma serving all product teams — directly analogous to Netflix's gateway/platform engineering. Designed multi-datacenter payment infrastructure at MakeMyTrip, engineered 50x traffic scaling at Myntra, and built PCI-compliant high-throughput card systems at Wavecrest. Java · Scala · Kafka · Cassandra · Kubernetes. MS CS, ASU 2021.",
        "job_order": STD_JOBS,
    },
    "uber": {
        "name": "Uber",
        "color": "#000000",
        "jobs": [
            {"title": "Staff Software Engineer (Backend) — Java Platform", "id": "156244",
             "url": "https://www.uber.com/global/en/careers/list/156244/",
             "fit": "Java platform backend at scale: Finagle/Spring platform ownership, 17+ years Java/Spring/Hibernate, Kafka/Cassandra distributed systems, multi-datacenter architectures, team leadership."}
        ],
        "profile": "Staff Backend Software Engineer with 17+ years of deep Java platform expertise. At Credit Karma, owns the Finagle-based platform framework serving all engineering teams and leads the most complex cross-team platform migrations. Previously built multi-datacenter payment platforms (MakeMyTrip), scaled checkout systems to 500M+ carts (Myntra), and led Java platform teams at Wavecrest. Java · Spring Boot · Scala · Kafka · Cassandra · Kubernetes. MS CS, ASU 2021.",
        "job_order": STD_JOBS,
    },
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Naveen Reddy Alka — {name}</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f5f7fa; color: #1a1a2e; }}
  header {{ background: {color}; color: white; padding: 32px 40px; }}
  header h1 {{ font-size: 28px; font-weight: 700; }}
  header p {{ margin-top: 6px; opacity: 0.85; font-size: 14px; }}
  .container {{ max-width: 900px; margin: 32px auto; padding: 0 24px; }}
  .card {{ background: white; border-radius: 12px; padding: 28px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(0,0,0,.07); }}
  .card h2 {{ font-size: 16px; font-weight: 700; color: {color}; margin-bottom: 16px; text-transform: uppercase; letter-spacing: .06em; border-bottom: 2px solid {color}; padding-bottom: 8px; }}
  .job-row {{ border: 1px solid #e8eaf0; border-radius: 8px; padding: 18px; margin-bottom: 14px; }}
  .job-row:last-child {{ margin-bottom: 0; }}
  .job-title {{ font-size: 15px; font-weight: 600; color: #1a1a2e; }}
  .job-id {{ font-size: 12px; color: #888; margin-top: 3px; }}
  .job-fit {{ font-size: 13px; color: #444; margin-top: 10px; line-height: 1.6; }}
  .apply-btn {{ display: inline-block; margin-top: 12px; padding: 8px 18px; background: {color}; color: white; border-radius: 6px; text-decoration: none; font-size: 13px; font-weight: 600; }}
  .apply-btn:hover {{ opacity: .88; }}
  .resume-link {{ display: inline-block; margin-top: 4px; padding: 8px 18px; background: #1a3a5c; color: white; border-radius: 6px; text-decoration: none; font-size: 13px; font-weight: 600; }}
  .pitch {{ font-size: 14px; line-height: 1.7; color: #333; }}
  .tag {{ display: inline-block; padding: 3px 10px; background: #f0f2f7; border-radius: 20px; font-size: 12px; color: #555; margin: 3px 3px 3px 0; }}
</style>
</head>
<body>
<header>
  <h1>Naveen Reddy Alka → {name}</h1>
  <p>naveenreddy.alka@gmail.com &nbsp;·&nbsp; 314-498-5314 &nbsp;·&nbsp; linkedin.com/in/naveenreddyalka &nbsp;·&nbsp; San Francisco Bay Area</p>
</header>
<div class="container">

  <div class="card">
    <h2>Target Roles at {name}</h2>
    {jobs_html}
  </div>

  <div class="card">
    <h2>Why {name}</h2>
    <p class="pitch">{profile}</p>
  </div>

  <div class="card">
    <h2>Resume</h2>
    <p style="font-size:13px;color:#555;margin-bottom:12px;">Tailored resume emphasizing most relevant experience for {name}.</p>
    <a class="resume-link" href="Naveen_Reddy_Alka_{slug}_Resume.pdf">📄 Download Tailored Resume</a>
    &nbsp;
    <a class="resume-link" href="../Naveen_Reddy_Alka_Resume.pdf" style="background:#555;">📄 Generic Resume</a>
  </div>

  <div class="card">
    <h2>Key Skills Match</h2>
    {tags}
  </div>

</div>
</body>
</html>"""

SKILL_TAGS = {
    "stripe":     ["Java","Spring Boot","Kafka","Cassandra","MySQL","PCI DSS","Payments","REST","Event-Driven","Microservices","AWS","Redis"],
    "confluent":  ["Apache Kafka","Java","Scala","Event-Driven Architecture","Distributed Systems","Spring Boot","Cassandra","Kubernetes","Microservices"],
    "databricks": ["Distributed Systems","Cassandra","Elasticsearch","MySQL","Kafka","Java","Scala","Kubernetes","AWS","GCP","CouchBase"],
    "anthropic":  ["Scala","TypeScript","Java","Kafka","Kubernetes","Platform Engineering","Node.js","GraphQL","Finagle","Distributed Systems"],
    "openai":     ["Java","Scala","TypeScript","Node.js","GraphQL","Platform Engineering","Kafka","Kubernetes","Distributed Systems","AWS/GCP"],
    "nvidia":     ["Kubernetes","Docker","AWS","GCP","Azure","Java","Spring Boot","Kafka","Distributed Systems","Observability","Microservices"],
    "servicenow": ["Java","Spring Boot","Hibernate","REST","GraphQL","Kafka","Cassandra","MySQL","Microservices","Enterprise Architecture"],
    "google":     ["Java","Scala","Kafka","Cassandra","GCP","AWS","Payments","Distributed Systems","Kubernetes","FinTech"],
    "snowflake":  ["Java","Scala","Cassandra","CouchBase","Elasticsearch","Kubernetes","AWS","GCP","Distributed Data Systems"],
    "netflix":    ["Scala","Java","Finagle","Kafka","Cassandra","Kubernetes","Distributed Systems","Platform Engineering","High Availability"],
    "uber":       ["Java","Spring Boot","Kafka","Cassandra","Kubernetes","Platform Engineering","Finagle","Distributed Systems","Microservices"],
}

for slug, co in COMPANIES.items():
    folder = f"{BASE}/{slug}"
    os.makedirs(folder, exist_ok=True)

    # Build tailored PDF
    pdf_name = f"Naveen_Reddy_Alka_{slug.capitalize()}_Resume.pdf"
    pdf_path = f"{folder}/{pdf_name}"
    build_pdf(pdf_path, co["profile"], co["job_order"])

    # Build HTML
    jobs_html = ""
    for j in co["jobs"]:
        jobs_html += f"""
    <div class="job-row">
      <div class="job-title">{j['title']}</div>
      <div class="job-id">Job ID: {j['id']}</div>
      <div class="job-fit">{j['fit']}</div>
      <a class="apply-btn" href="{j['url']}" target="_blank">Apply Now ↗</a>
    </div>"""

    tags = " ".join(f'<span class="tag">{t}</span>' for t in SKILL_TAGS.get(slug, []))
    html = HTML_TEMPLATE.format(
        name=co["name"], color=co["color"],
        jobs_html=jobs_html, profile=co["profile"],
        slug=slug.capitalize(), tags=tags,
    )
    with open(f"{folder}/index.html", "w") as f:
        f.write(html)

    print(f"✓ {slug}: index.html + {pdf_name}")

print("\nAll done!")
