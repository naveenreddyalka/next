import os
from pathlib import Path
from project_paths import PROJECT_ROOT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable
from reportlab.lib.enums import TA_CENTER

BASE = str(PROJECT_ROOT)
BLUE = colors.HexColor("#1a3a5c")
LIGHT_GRAY = colors.HexColor("#555555")

name_style   = ParagraphStyle("Name",    fontSize=22, fontName="Helvetica-Bold", textColor=BLUE, spaceAfter=10, leading=28, alignment=TA_CENTER)
contact_style= ParagraphStyle("Contact", fontSize=9,  fontName="Helvetica",      textColor=LIGHT_GRAY, spaceAfter=6, alignment=TA_CENTER)
section_style= ParagraphStyle("Section", fontSize=11, fontName="Helvetica-Bold", textColor=BLUE, spaceBefore=10, spaceAfter=3)
job_style    = ParagraphStyle("Job",     fontSize=9.5,fontName="Helvetica-Bold", textColor=colors.black, spaceBefore=7, spaceAfter=1)
body_style   = ParagraphStyle("Body",    fontSize=9,  fontName="Helvetica",      textColor=colors.black, spaceAfter=2, leading=13)
bullet_style = ParagraphStyle("Bullet",  fontSize=9,  fontName="Helvetica",      textColor=colors.black, spaceAfter=3, leading=13, leftIndent=12, firstLineIndent=-12)

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

CK = [
    "Designed and built the Portal Provider framework — core abstraction for dynamic portal configuration powering <b>90%+ of Credit Karma portals clients</b>; foundation of federated portals SDK adopted org-wide.",
    "Led end-to-end delivery of Dashboard × Portals SDK federation — designed Bridge API for phased A/B rollout, achieved <b>100% production ramp</b>, enabled RecSys V2, unblocked HELOC/Home Refi verticals; 5+ public kudos by VP and two Directors.",
    "Architected Portals Local Eligibility (GA Feb 2025) — moved eligibility into client-side SDK delivering <b>45% faster rendering</b> and eliminating redundant upstream network calls.",
    "Led Data Contracts from inception through production (Oct 2025) — cross-language codegen (TypeScript, GraphQL, Scala), Thrift IDL, automated publish pipeline reducing release time <b>from days to minutes</b>; named org-wide adoption lead.",
    "Resolved critical Talon/Polly production incidents: memory leaks, pm2 socket exhaustion, MGS startup latency spikes; built reusable load testing infrastructure across all Polly teams.",
    "Own and evolve Finagle-based web framework (EOL Twitter stack) serving all Credit Karma product teams — SLAs, scalability, incremental modernization in Scala and TypeScript.",
]
MMT = [
    "Sole architect of MakeMyTrip's payments platform revamp — multi-datacenter, multi-tenant system integrating <b>80+ payment gateways</b> (HSM, wallets, discounting, fraud management).",
    "Achieved <b>50% reduction in payment response time</b>, <b>60% reduction in maintenance cost</b>, <b>2%+ improvement in payment success rate</b> over billions of dollars of monthly transactions — driving <b>millions in incremental revenue</b>.",
    "Built and led team of 5; owned full delivery including CTO-level architecture reviews, A/B testing, staged rollout, DR, and CI/CD via Jenkins + Cucumber + Selenium.",
    "Stack: Java · Spring · Hibernate · MySQL · CouchBase · RabbitMQ · Kafka · Cassandra · Tomcat.",
]
MYNTRA = [
    "Led Secure Checkout team — <b>100% uptime</b> at <b>500M+ active carts</b> and <b>150,000+ daily payment transactions</b> on India's largest fashion platform.",
    "Built Payment Plan Service (PPS) from scratch — unified all payment instruments with dynamic gateway auto-switching algorithm.",
    "Engineered 50x traffic scaling for End of Season Sale — Cassandra NoSQL primary + algorithmic distributed sharding over MySQL for 500M+ objects.",
    "Stack: Java · Spring · Hibernate · MySQL · Cassandra · Jersey · Nginx · ZooKeeper · ActiveMQ · Elasticsearch · HAProxy.",
]
WAVE = [
    "Founding member — promoted <b>3 times in 4 years</b> (SE → SSE → Lead Eng → Dev Lead).",
    "Led 8-engineer team: cashier and eWallet products processing <b>200,000+ card issuances per day</b> with PCI compliance.",
    "Delivered financial systems for PartyGaming-Bwin, Reliance, GTECH, TrillionPay, O2.",
    "Stack: Java · Spring · Hibernate · MySQL · ActiveMQ · SOAP · REST · Redis · Docker · Jenkins.",
]
TURO   = ["Resolved critical network, infra, and design bottlenecks — optimized API-to-database patterns reducing latency by up to <b>30%</b>.",
           "Led modernization of high-traffic legacy services, improving reliability across the backend."]
PEARSON= ["Built cross-cutting platform services (logging, security, metrics, monitoring) using Spring WebFlux + Project Reactor — adopted by all engineering teams.",
           "Delivered Kafka event pipelines, CouchBase data layer, Kubernetes + AWS shared infra enabling Pearson's reactive architecture roadmap."]
NORDSTROM=["Ordering/Allocation team — led decommission of legacy monolithic ordering systems into Kubernetes-native microservices on AWS/GCP with GitLab CI/CD.",
            "Drove performance optimization and security hardening (Java/Spring/Hibernate, MySQL/Postgres, Docker/Linux)."]
WENOVA  = ["Designed Customer Data Hub (CDH) — central microservice exposing REST + GraphQL APIs to 10+ internal systems with Kafka event-driven propagation.",
            "Delivered Java/Spring/Hibernate services on AWS; XML/XSLT/SOAP data transformation pipelines."]
VERSE   = ["Built Books search platform — full-text search, fuzzy matching, autocomplete, vernacular support via Elasticsearch + Node.js serving millions of queries.",
            "Stack: Java · Spring · Elasticsearch · Node.js · Kafka · Redis · Docker."]
IVY     = ["Built scalable Affiliates and Loyalty System components on a high-traffic gaming platform.",
            "Stack: Java · Spring · Struts2 · Perl · MySQL · Ajax · Jenkins."]
CTS     = ["Core engineer on Amex small business apply site — led Apply-Strategy project: data management upgrade, migration, DOJO framework migration.",
            "Stack: Java · J2EE · Struts · XSLT · XSD · Dojo · EJB · RMI."]

STD_JOBS = [
    ("Credit Karma, Oakland  ·  Staff Software Engineer  ·  Feb 2022 – Present", CK),
    ("Turo, San Francisco  ·  Senior Software Engineer  ·  Jan 2021 – Feb 2022", TURO),
    ("Pearson Inc, San Francisco  ·  Senior Software Engineer  ·  Jan 2020 – Jan 2021", PEARSON),
    ("Nordstrom, Seattle  ·  Senior Engineer  ·  Mar 2019 – Oct 2019", NORDSTROM),
    ("Wenova Inc, St. Louis  ·  Software Engineer  ·  Mar 2018 – Mar 2019", WENOVA),
    ("MakeMyTrip, Bangalore  ·  Sr. Principal Software Engineer — Payments Architect  ·  Sep 2016 – Jan 2018", MMT),
    ("VERSE – DailyHunt, Bangalore  ·  Principal Software Engineer  ·  Apr 2016 – Sep 2016", VERSE),
    ("Myntra – Flipkart, Bangalore  ·  Technical Lead, Secure Checkout  ·  Dec 2013 – Mar 2016", MYNTRA),
    ("Wavecrest Payment Services  ·  Dev Lead  ·  Nov 2009 – Dec 2013", WAVE),
    ("IvyComptech, Hyderabad  ·  Software Engineer  ·  Jan 2009 – Nov 2009", IVY),
    ("Cognizant, Hyderabad  ·  Program Analyst  ·  Nov 2007 – Jan 2009", CTS),
]

def build_pdf(path, profile, jobs):
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
    for title, bullets in jobs:
        s.append(job(title))
        for bl in bullets:
            s.append(bul(bl))
    s += sec("Education")
    s.append(Paragraph("<b>Arizona State University</b> — MS Computer Science, 2021", body_style))
    s.append(Paragraph("<b>National Institute of Technology, Warangal</b> — B.Tech Civil Engineering, 2007", body_style))
    doc.build(s)

COMPANIES = {
    "xai": {
        "name": "xAI",
        "color": "#000000",
        "profile": "Staff Software Engineer with 17+ years in platform infrastructure and high-scale distributed systems. At Credit Karma, architected the Portal Provider framework powering 90%+ of portals clients and leads the most complex cross-team platform migrations. Deep Scala, TypeScript, Java, Kafka, Kubernetes expertise. Thrives in small, high-impact teams moving fast — exactly the xAI model. MS CS, ASU 2021.",
        "jobs": [
            {"title": "Senior Grok Engineer", "id": "4823149007",
             "url": "https://job-boards.greenhouse.io/xai/jobs/4823149007",
             "fit": "Small team, high ownership, Scala/TypeScript/Java platform engineering. Credit Karma Finagle framework ownership and cross-org platform migrations directly match xAI's engineering model."},
            {"title": "Software Engineer — Grok Voice", "id": "4720475007",
             "url": "https://job-boards.greenhouse.io/xai/jobs/4720475007",
             "fit": "Backend systems engineering at scale. Distributed backend, event-driven architecture, low-latency API design."},
        ],
        "tags": ["Java","Scala","TypeScript","Kafka","Kubernetes","Platform Engineering","Distributed Systems","Node.js","Finagle","AWS/GCP"],
        "interview": """<h3>Interview Process</h3>
<p>xAI moves fast — typically 2–3 rounds total:</p>
<ul>
  <li><b>Technical Screen (1hr)</b> — Coding + system design. Expect distributed systems, API design, scalability questions.</li>
  <li><b>Onsite / Virtual Loop (2–3 hrs)</b> — Deep system design, coding, and a culture/mission fit conversation. No fluff — they want to see you build things fast.</li>
</ul>
<p style="margin-top:10px;"><b>Key prep:</b> Be ready to discuss real systems you've built end-to-end. xAI values ownership and speed — lead with your MakeMyTrip payments platform revamp and Credit Karma platform framework.</p>""",
        "comp": "$250k–$400k+ base + significant equity (pre-IPO xAI). Palo Alto / SF.",
    },
    "spacex": {
        "name": "SpaceX",
        "color": "#005288",
        "profile": "Staff Software Engineer with 17+ years building distributed backend systems at scale — payment platforms, platform frameworks, and multi-datacenter infrastructure. At Credit Karma, owns platform framework serving all engineering teams. Previously architected systems handling billions of transactions and 500M+ objects. Strong Java/Python/Kafka/Kubernetes background with hands-on experience in high-reliability, high-throughput production systems. MS CS, ASU 2021.",
        "jobs": [
            {"title": "Sr. Software Engineer — Backend / Distributed Systems (Starlink)", "id": "8300183002",
             "url": "https://job-boards.greenhouse.io/spacex/jobs/8300183002",
             "fit": "Distributed systems, high-reliability backend, Kafka/Cassandra at scale, multi-datacenter architecture — all directly applicable to Starlink's ground software infrastructure."},
        ],
        "tags": ["Java","Python","Kafka","Cassandra","Kubernetes","Distributed Systems","High Availability","Microservices","AWS","Event-Driven"],
        "interview": """<h3>Interview Process</h3>
<p>SpaceX is rigorous and moves deliberately:</p>
<ul>
  <li><b>Recruiter Screen (30 min)</b> — Background, motivation, availability.</li>
  <li><b>Technical Phone Screen (1hr)</b> — Data structures, algorithms, system design basics.</li>
  <li><b>Onsite Loop (4–5 hrs)</b> — Multiple rounds: coding (LeetCode medium/hard), system design (distributed systems heavy), and a hiring manager conversation on ownership and mission alignment.</li>
</ul>
<p style="margin-top:10px;"><b>Key prep:</b> SpaceX values mission commitment and engineering depth. Lead with your multi-datacenter architecture experience (MakeMyTrip) and high-availability system ownership. Expect deep distributed systems design questions.</p>""",
        "comp": "$180k–$260k base + stock. Hawthorne CA / Redmond WA / remote.",
    },
}

NAV = '<style>.topnav{background:#1a3a5c;padding:10px 24px;font-size:13px;} .topnav a{color:#aac4e0;text-decoration:none;margin-right:16px;} .topnav a:hover{color:white;}</style>'

for slug, co in COMPANIES.items():
    folder = f"{BASE}/{slug}"
    os.makedirs(folder, exist_ok=True)

    # Tailored PDF
    pdf_name = f"Naveen_Reddy_Alka_{slug.capitalize()}_Resume.pdf"
    build_pdf(f"{folder}/{pdf_name}", co["profile"], STD_JOBS)
    import shutil
    shutil.copy(f"{BASE}/Naveen_Reddy_Alka_Resume.pdf", f"{folder}/Naveen_Reddy_Alka_Resume.pdf")

    # Jobs HTML
    jobs_html = ""
    for j in co["jobs"]:
        jobs_html += f"""
    <div class="job-row">
      <div class="job-title">{j['title']}</div>
      <div class="job-id">Job ID: {j['id']}</div>
      <div class="job-fit">{j['fit']}</div>
      <a class="apply-btn" href="{j['url']}" target="_blank">Apply Now ↗</a>
    </div>"""

    tags = " ".join(f'<span class="tag">{t}</span>' for t in co["tags"])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Naveen Reddy Alka — {co['name']}</title>
{NAV}
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f5f7fa; color: #1a1a2e; }}
  header {{ background: {co['color']}; color: white; padding: 32px 40px; }}
  header h1 {{ font-size: 28px; font-weight: 700; }}
  header p {{ margin-top: 6px; opacity: 0.85; font-size: 14px; }}
  .container {{ max-width: 900px; margin: 32px auto; padding: 0 24px; }}
  .card {{ background: white; border-radius: 12px; padding: 28px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(0,0,0,.07); }}
  .card h2 {{ font-size: 14px; font-weight: 700; color: {co['color']}; margin-bottom: 16px; text-transform: uppercase; letter-spacing: .06em; border-bottom: 2px solid {co['color']}; padding-bottom: 8px; }}
  .job-row {{ border: 1px solid #e8eaf0; border-radius: 8px; padding: 18px; margin-bottom: 14px; }}
  .job-title {{ font-size: 15px; font-weight: 600; }}
  .job-id {{ font-size: 12px; color: #888; margin-top: 3px; }}
  .job-fit {{ font-size: 13px; color: #444; margin-top: 10px; line-height: 1.6; }}
  .apply-btn {{ display: inline-block; margin-top: 12px; padding: 8px 18px; background: {co['color']}; color: white; border-radius: 6px; text-decoration: none; font-size: 13px; font-weight: 600; }}
  .resume-link {{ display: inline-block; margin: 4px 8px 4px 0; padding: 8px 18px; background: #1a3a5c; color: white; border-radius: 6px; text-decoration: none; font-size: 13px; font-weight: 600; }}
  .pitch {{ font-size: 14px; line-height: 1.7; color: #333; }}
  .tag {{ display: inline-block; padding: 3px 10px; background: #f0f2f7; border-radius: 20px; font-size: 12px; color: #555; margin: 3px 3px 3px 0; }}
  .card h3 {{ font-size: 13px; font-weight: 700; margin: 16px 0 8px; color: #1a1a2e; }}
  .card ul {{ padding-left: 18px; }}
  .card li {{ font-size: 13px; line-height: 1.7; color: #444; margin-bottom: 4px; }}
  .card p {{ font-size: 13px; line-height: 1.7; color: #444; margin-bottom: 6px; }}
  .comp {{ font-size: 14px; font-weight: 600; color: #1a3a5c; margin-top: 10px; }}
</style>
</head>
<body>
<nav class="topnav"><a href="../index.html">← Home</a><a href="index.html">This Company</a></nav>
<header>
  <h1>Naveen Reddy Alka → {co['name']}</h1>
  <p>naveenreddy.alka@gmail.com &nbsp;·&nbsp; 314-498-5314 &nbsp;·&nbsp; linkedin.com/in/naveenreddyalka &nbsp;·&nbsp; San Francisco Bay Area</p>
</header>
<div class="container">

  <div class="card">
    <h2>Target Roles at {co['name']}</h2>
    {jobs_html}
  </div>

  <div class="card">
    <h2>Why {co['name']}</h2>
    <p class="pitch">{co['profile']}</p>
  </div>

  <div class="card">
    <h2>Interview Process &amp; Compensation</h2>
    {co['interview']}
    <div class="comp">💰 {co['comp']}</div>
  </div>

  <div class="card">
    <h2>Resume</h2>
    <a class="resume-link" href="{pdf_name}">📄 Tailored Resume</a>
    <a class="resume-link" href="Naveen_Reddy_Alka_Resume.pdf" style="background:#555;">📄 Generic Resume</a>
  </div>

  <div class="card">
    <h2>Key Skills Match</h2>
    {tags}
  </div>

</div>
</body>
</html>"""

    with open(f"{folder}/index.html", "w") as f:
        f.write(html)

    print(f"✓ {slug}")

print("Done")
