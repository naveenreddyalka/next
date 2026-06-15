from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.enums import TA_CENTER
from pathlib import Path
from project_paths import PROJECT_ROOT

OUTPUT = str(PROJECT_ROOT / "Naveen_Reddy_Alka_Resume.pdf")

doc = SimpleDocTemplate(
    OUTPUT, pagesize=letter,
    leftMargin=0.65*inch, rightMargin=0.65*inch,
    topMargin=0.55*inch, bottomMargin=0.55*inch,
)

BLUE = colors.HexColor("#1a3a5c")
LIGHT_GRAY = colors.HexColor("#555555")

name_style = ParagraphStyle("Name", fontSize=22, fontName="Helvetica-Bold",
    textColor=BLUE, spaceAfter=10, leading=28, alignment=TA_CENTER)
contact_style = ParagraphStyle("Contact", fontSize=9, fontName="Helvetica",
    textColor=LIGHT_GRAY, spaceAfter=6, alignment=TA_CENTER)
section_style = ParagraphStyle("Section", fontSize=11, fontName="Helvetica-Bold",
    textColor=BLUE, spaceBefore=10, spaceAfter=3)
job_title_style = ParagraphStyle("JobTitle", fontSize=9.5, fontName="Helvetica-Bold",
    textColor=colors.black, spaceBefore=7, spaceAfter=1)
body_style = ParagraphStyle("Body", fontSize=9, fontName="Helvetica",
    textColor=colors.black, spaceAfter=2, leading=13)
bullet_style = ParagraphStyle("Bullet", fontSize=9, fontName="Helvetica",
    textColor=colors.black, spaceAfter=3, leading=13,
    leftIndent=12, firstLineIndent=-12)

def hr():
    return HRFlowable(width="100%", thickness=0.75, color=BLUE, spaceAfter=4, spaceBefore=2)

def section(title):
    return [Paragraph(title.upper(), section_style), hr()]

def b(text):
    return Paragraph(f"• {text}", bullet_style)

def job(title):
    return Paragraph(f"<b>{title}</b>", job_title_style)

story = []

# Header
story.append(Paragraph("NAVEEN REDDY ALKA", name_style))
story.append(Paragraph(
    "San Francisco Bay Area &nbsp;|&nbsp; 314-498-5314 &nbsp;|&nbsp; naveenreddy.alka@gmail.com &nbsp;|&nbsp; linkedin.com/in/naveenreddyalka",
    contact_style))

# Profile
story += section("Profile")
story.append(Paragraph(
    "Senior Software Engineer with 17+ years of progressive expertise in platform infrastructure, distributed systems, "
    "and large-scale backend engineering across FinTech, Payments, and eCommerce. At Credit Karma, architected the "
    "Portal Provider framework now powering 90%+ of all portals clients, and led the organization's most complex "
    "platform migrations end-to-end. Previously designed MakeMyTrip's payments platform from scratch — a "
    "multi-datacenter, multi-tenant system integrating 80+ payment gateways — cutting response times by 50%, "
    "maintenance costs by 60%, and generating millions in incremental revenue. Recognized for founding-level "
    "contributions at two companies and three promotions at Wavecrest within four years. Core stack: Java · Scala · "
    "TypeScript · Kafka · Cassandra · Kubernetes · Spring Boot · AWS/GCP/Azure. MS Computer Science, Arizona State "
    "University 2021.",
    body_style))

# Skills
story += section("Skills")
for label, val in [
    ("Languages", "Java (SCJP 98%), Scala, Kotlin, TypeScript, JavaScript, Python, Perl"),
    ("Frameworks", "Spring Boot, Spring WebFlux, Project Reactor, Hibernate, Finagle, Node.js, GraphQL, Jersey, Struts2"),
    ("Messaging & Streaming", "Apache Kafka, RabbitMQ, ActiveMQ"),
    ("Databases", "Cassandra, Redis, CouchBase, Elasticsearch, MySQL, PostgreSQL, Oracle, MongoDB"),
    ("Cloud & Infra", "AWS, GCP, Azure, Kubernetes, Docker, Nginx, HAProxy, Tomcat"),
    ("Observability", "Datadog, New Relic, Splunk, Sentry, Graphite/StatsD"),
    ("CI/CD & Build", "GitLab CI/CD, Jenkins, GitHub Actions, Maven, Gradle, Git, SVN"),
    ("Practices", "Microservices, Event-Driven Architecture, Event Sourcing, TDD, PCI DSS, Agile/Scrum, System Design"),
]:
    story.append(Paragraph(f"<b>{label}:</b>  {val}", body_style))

# Experience
story += section("Experience")

# Credit Karma
story.append(job("Credit Karma, Oakland  ·  Staff Software Engineer  ·  Feb 2022 – Present"))
for t in [
    "Designed and built the Portal Provider framework — the core abstraction for dynamic portal configuration that <b>90%+ of Credit Karma portals clients</b> depend on; directly underpins the federated portals SDK architecture adopted org-wide.",
    "Led end-to-end architecture and delivery of the Dashboard × Portals SDK federation — the team's most complex migration — designing the Bridge API for phased A/B rollout; achieved <b>100% production ramp</b>, enabled RecSys V2 integration, and unblocked new vertical onboarding (HELOC, Home Refi); recognized with 5+ public kudos by VP and two Directors.",
    "Architected Portals Local Eligibility (GA Feb 2025) — moved eligibility evaluation from centralized backend into client-side SDK, delivering <b>45% faster rendering</b> and eliminating redundant upstream network calls across the Assets team.",
    "Led Data Contracts from inception through production (Oct 2025) — built cross-language codegen pipeline (TypeScript, GraphQL, Scala), authored Thrift IDL, and automated publish pipeline reducing contract release time <b>from days to minutes</b>; named by Director as org-wide adoption lead.",
    "Diagnosed and resolved critical Talon/Polly production incidents at scale: memory leaks, pm2 socket exhaustion halting request handling, MGS startup latency spikes; built reusable load testing infra now used across all Polly teams.",
    "Own and evolve the Finagle-based web framework (EOL Twitter stack) serving all Credit Karma product teams — managing SLAs, scalability, and incremental modernization in Scala and TypeScript.",
]:
    story.append(b(t))

# Turo
story.append(job("Turo, San Francisco  ·  Senior Software Engineer  ·  Jan 2021 – Feb 2022"))
for t in [
    "Identified and resolved critical network, infrastructure, and design-level bottlenecks on the core platform backend — optimizing API-to-database communication patterns, reducing latency by up to <b>30%</b> and significantly improving system throughput.",
    "Led modernization of high-traffic legacy services, improving reliability, reducing incident rate, and raising overall platform performance across the backend.",
]:
    story.append(b(t))

# Pearson
story.append(job("Pearson Inc, San Francisco  ·  Senior Software Engineer  ·  Jan 2020 – Jan 2021"))
for t in [
    "Architected and delivered cross-cutting platform services — logging, security, metrics, and monitoring — using reactive programming (Spring WebFlux, Project Reactor) adopted by <b>all engineering teams</b>, eliminating duplicated boilerplate and standardizing observability across the organization.",
    "Delivered Kafka-based event pipelines, CouchBase data layer, and Kubernetes + AWS shared infrastructure enabling Pearson's reactive architecture roadmap — reducing per-team infrastructure setup time by weeks.",
]:
    story.append(b(t))

# Nordstrom
story.append(job("Nordstrom, Seattle  ·  Senior Engineer  ·  Mar 2019 – Oct 2019  ·  $150,000"))
for t in [
    "Part of the Ordering and Allocation team leading decommission of legacy monolithic ordering systems into cloud-native microservices using Spring Boot + REST/SOAP, deployed on Kubernetes across AWS and GCP with GitLab CI/CD.",
    "Drove performance optimization, security hardening, and distributed systems best practices across the team; worked with MySQL, Postgres, Docker/Linux, and full-stack distributed architecture.",
]:
    story.append(b(t))

# Wenova
story.append(job("Wenova Inc, St. Louis  ·  Software Engineer  ·  Mar 2018 – Mar 2019"))
for t in [
    "Designed and built the Customer Data Hub (CDH) — a central microservice acting as the system of record for all customer data, exposing REST and GraphQL APIs to 10+ internal systems including Salesforce, with Kafka event-driven propagation ensuring real-time consistency.",
    "Developed and integrated software systems on AWS using Java/Spring/Hibernate, XML/XSLT/SOAP/JSON, PostgreSQL, and NoSQL databases; delivered complex data transformation pipelines and REST web services in Agile environment.",
]:
    story.append(b(t))

# MakeMyTrip
story.append(job("MakeMyTrip, Bangalore  ·  Sr. Principal Software Engineer — Payments Architect  ·  Sep 2016 – Jan 2018"))
for t in [
    "Sole architect of MakeMyTrip's payments platform revamp — designed and delivered a ground-up, multi-datacenter, multi-tenant system integrating <b>80+ payment gateways and aggregators</b> supporting every payment instrument in India (saved cards over HSM, wallets, discounting, fraud management, admin cockpit).",
    "Achieved <b>50% reduction in average payment response time</b>, <b>60% reduction in maintenance cost</b>, and a <b>2%+ improvement in payment success rate</b> over billions of dollars of monthly transactions — driving <b>millions in incremental revenue</b>.",
    "Built and led a team of 5 engineers; owned full delivery lifecycle including architecture walkthroughs with CTO and Chief Architect, POC development, A/B testing, staged production rollout, disaster recovery, and complete CI/CD automation via Jenkins + Cucumber + Selenium.",
    "Stack: Java · Spring · Hibernate · MySQL · CouchBase · RabbitMQ · Kafka · Cassandra · Tomcat · Jenkins.",
]:
    story.append(b(t))

# VERSE
story.append(job("VERSE – DailyHunt, Bangalore  ·  Principal Software Engineer  ·  Apr 2016 – Sep 2016"))
for t in [
    "Designed and built a dynamic Books search platform serving millions of search queries — full-text search, fuzzy matching, autocomplete, and vernacular language support — using Elasticsearch + Node.js at scale.",
    "Stack: Java · Spring · Hibernate · Elasticsearch · Node.js · Kafka · Redis · Docker.",
]:
    story.append(b(t))

# Myntra
story.append(job("Myntra – Flipkart, Bangalore  ·  Technical Lead, Secure Checkout  ·  Dec 2013 – Mar 2016"))
for t in [
    "Led the Secure Checkout team owning Payments, Address, and Cart systems on India's largest fashion eCommerce platform — maintained <b>100% uptime</b> at <b>500M+ active carts</b> and <b>150,000+ daily payment transactions</b> during peak sale events.",
    "Designed and built Payment Plan Service (PPS) from scratch — unified ownership of all multi-instrument payment transactions (CC, DC, Gift Cards, Wallets, CashBack) with an auto-switching algorithm dynamically selecting the optimal gateway per transaction.",
    "Engineered 50x traffic scaling for End of Season Sale — built Cassandra-based NoSQL primary store and a first-of-its-kind application-level distributed sharding solution over MySQL to manage 500M+ cart objects on a relational database.",
    "Stack: Java · Spring · Hibernate · MySQL · Cassandra · Jersey · Nginx · ZooKeeper · ActiveMQ · Elasticsearch · HAProxy · Jenkins · Tomcat.",
]:
    story.append(b(t))

# Wavecrest
story.append(job("Wavecrest Payment Services, Hyderabad  ·  Dev Lead (SE → SSE → Lead Eng → Dev Lead)  ·  Nov 2009 – Dec 2013"))
for t in [
    "Founding member of the Wavecrest engineering team — promoted <b>three times in four years</b> (Software Engineer → Senior → Lead Engineer → Dev Lead) based on exceptional performance and technical leadership.",
    "Led a team of 8 engineers building cashier and eWallet products: prepaid gift cards, payroll cards, tax refund cards, open/closed loop solutions, digital wallets, and mobile payments — processing <b>200,000+ new card issuances per day</b> with full PCI compliance.",
    "Delivered enterprise financial systems for PartyGaming-Bwin, Reliance, GTECH, TrillionPay, O2, Loopium, and Tarcha; accountable for architecture, code quality, performance reviews, and mentorship of the full team.",
    "Stack: Java · Spring · Hibernate · MySQL · RMI/EJB · ActiveMQ · SOAP · REST · Redis · Docker · Dojo/jQuery · Jenkins.",
]:
    story.append(b(t))

# IvyComptech
story.append(job("IvyComptech, Hyderabad  ·  Software Engineer  ·  Jan 2009 – Nov 2009"))
for t in [
    "Built new scalable components for Store, Affiliates, and Loyalty Systems — delivered features and performance improvements across a high-traffic gaming affiliate platform.",
    "Stack: Java · Spring · Struts2 · Perl · MySQL · Ajax · Jenkins · Tomcat.",
]:
    story.append(b(t))

# Cognizant
story.append(job("Cognizant, Hyderabad  ·  Program Analyst  ·  Nov 2007 – Jan 2009"))
for t in [
    "Core engineer on the American Express small business credit card apply site — led the Apply-Strategy project delivering a complete upgrade to the data management system, including data migration, Struts front-end controllers, and DOJO JavaScript framework migration from MooTools.",
    "Stack: Java · J2EE · Struts · XSLT · XSD · Dojo · EJB · RMI · Tomcat.",
]:
    story.append(b(t))

# Education
story += section("Education")
story.append(Paragraph("<b>Arizona State University</b> — MS Computer Science, 2021", body_style))
story.append(Paragraph("<b>National Institute of Technology, Warangal</b> — B.Tech Civil Engineering, 2007", body_style))

doc.build(story)
print("PDF created:", OUTPUT)
