# Resume Updates — Ready to Paste into Google Doc
# Naveen Reddy Alka · June 2026
# Copy each section below into the corresponding section of your Google Doc

---

## ✅ SECTION 0: HEADER CONTACT LINE

Use this exact contact line in the resume header:

San Francisco Bay Area · 314-498-5314 · naveenreddy.alka@gmail.com · linkedin.com/in/naveenreddyalka

---

## ✅ SECTION 1: PROFILE (replace the existing paragraph)

Senior Software Engineer with 17+ years building platform infrastructure and distributed backend systems across FinTech, Payments, and eCommerce at scale. At Credit Karma, designed and own the core Portal Provider framework relied on by 90% of portals clients, and lead the team's most complex platform migrations end-to-end. Previously architected MakeMyTrip's payment platform from scratch: multi-datacenter, event-driven, cutting response times 50%, maintenance costs 60%, and driving millions in incremental revenue. Core stack: Java · Scala · TypeScript · Kafka · Cassandra · Kubernetes · Spring Boot · AWS/GCP/Azure. MS Computer Science, Arizona State University 2021.

---

## ✅ SECTION 2: SKILLS (replace the existing Skills section entirely)

**Languages**
Java (SCJP 98%), Scala, Kotlin, TypeScript, JavaScript, Python

**Frameworks & Libraries**
Spring Boot, Spring WebFlux, Project Reactor, Hibernate, Finagle, Node.js, GraphQL

**Messaging & Streaming**
Apache Kafka, RabbitMQ, ActiveMQ

**Databases & Storage**
Cassandra, Redis, CouchBase, Elasticsearch, MySQL, PostgreSQL, Oracle

**Cloud & Infrastructure**
AWS, GCP, Azure, Kubernetes, Docker, Nginx, HAProxy

**Observability & Monitoring**
Datadog, New Relic, Splunk, Sentry, Graphite/StatsD

**CI/CD & Build**
GitLab CI/CD, Jenkins, GitHub Actions, Maven, Gradle, Git

**Practices**
Microservices, Event-Driven Architecture, Event Sourcing, TDD, Agile/Scrum, System Design

---

## ✅ SECTION 3: CREDITKARMA — WORK EXPERIENCE
## (Replace the existing CreditKarma prose with these bullets)

**Credit Karma, Oakland · Senior Software Engineer II · Feb 2022 – Present**

- Designed and built the Portal Provider framework — the core abstraction for dynamic portal configuration that **90% of Credit Karma portals clients** currently depend on, directly underpinning the entire federated portals SDK architecture adopted across all product teams
- Led end-to-end architecture and production delivery of the Dashboard × Portals SDK federation — the team's most complex migration — including designing the Bridge API for phased A/B rollout; achieved **100% production ramp**, enabled RecSys V2 integration (nested grouping, heterogeneous ranking, FAO reducing RecSys calls), and unblocked new vertical onboarding (HELOC, Home Refi); recognized across 5+ public kudos by VP and two Directors
- Architected and shipped Portals Local Eligibility (GA Feb 2025), moving eligibility evaluation from centralized backend into client-side SDK — delivered **45% faster rendering** for Assets team, eliminated redundant network calls, and built production observability via custom eligibility metrics instrumentation
- Led Data Contracts from inception through production (Oct 2025) — bootstrapped fwk_data-contracts Nx monorepo from scratch, built cross-language codegen (TypeScript, GraphQL, Scala), authored Thrift IDL, and automated the publish pipeline reducing contract release time **from days to minutes**; named by Director as org-wide primary contact for adoption
- Diagnosed and fixed critical Talon/Polly production bugs as the platform's first consumer at scale: memory leaks in processing pipeline, pm2 socket exhaustion halting request handling, and MGS startup latency degradation; built reusable load testing infrastructure now available for all future Polly regression testing
- Maintain and evolve Finagle-based web framework (EOL Twitter stack) serving all Credit Karma product teams — managing SLAs, scalability, and incremental modernization in Scala and TypeScript while contributing to Credit Karma open-source projects

---

## ✅ SECTION 4: REMAINING JOBS — REWRITTEN AS BULLETS
## (Replace each job's prose block with the bullets below)

---

### Turo, San Francisco · Senior Software Engineer · Jan 2021 – Feb 2022

- Optimized API-to-database communication patterns on core platform backend, resolving network, infrastructure, and design-level bottlenecks to improve system throughput and response times
- Maintained and modernized legacy platform services, improving reliability and performance across the backend

---

### Pearson Inc, San Francisco · Senior Software Engineer · Jan 2020 – Jan 2021

- Built cross-cutting platform services (logging, security, metrics, monitoring) using reactive programming (Spring WebFlux, Project Reactor) adopted by all engineering teams, reducing per-service boilerplate and standardizing observability across Pearson's engineering organization
- Delivered shared infrastructure on Kubernetes + AWS; Kafka-based event pipelines; CouchBase data layer — enabling Pearson's reactive architecture roadmap at scale

---

### Nordstrom, Seattle · Senior Software Engineer · Mar 2019 – Nov 2019

- Led modernization of legacy monolithic ordering system into Kubernetes-native microservices using Spring Boot/Data REST APIs with GitLab CI/CD, reducing operational complexity and deployment cycle time
- Architected distributed data store using AWS Aurora + Cassandra on EC2, publishing event changelog to Kafka for downstream consumer decoupling

---

### Wenova, St. Louis · Software Engineer · Mar 2018 – Mar 2019

- Designed and built Customer Data Hub (CDH) microservice — the system of record for customer data providing APIs to all internal systems including Salesforce, with Kafka event-driven propagation for real-time customer updates
- Implemented performance improvements and resolved critical design issues across Java/Spring/Hibernate stack

---

### MakeMyTrip, Bangalore · Sr. Principal Software Engineer (Architect, Payments) · Sep 2016 – Jan 2018

- Architected complete ground-up revamp of MakeMyTrip's payment platform — multi-datacenter, handling traffic from multiple active DCs simultaneously
- Reduced payment response times by **50%**, increased payment success rates driving **millions in incremental revenue**, and cut maintenance costs by **60%**
- Designed event-driven retry logic using RabbitMQ for high-performance, fault-tolerant payment processing
- Stack: Spring Boot · JPA-Hibernate · MySQL · CouchBase · RabbitMQ · AWS + dedicated infrastructure

---

### VERSE – DailyHunt, Bangalore · Principal Software Engineer · Apr 2016 – Sep 2016

- Built Elasticsearch-based search platform for Books — full-text search, fuzzy matching, autocomplete, and vernacular support at scale
- Developed Node.js service layer powering the search backend

---

### Myntra – Flipkart, Bangalore · Technical Lead · Jan 2014 – Apr 2016

- Led Payments, Cart, and Address services for Myntra — maintaining **100% uptime** at **500 million carts** and **100,000+ payments per day**
- Built in-house distributed database using application-level sharding over MySQL + Cassandra to handle payment transaction volume at scale

---

### Wavecrest, Hyderabad · Dev Lead · Nov 2009 – Dec 2013

- Led team of 8 engineers building cashier and eWallet products — prepaid gift cards, payroll cards, tax refund cards, open/closed loop solutions — issuing **100,000+ new cards per day** with PCI compliance
- Delivered financial systems for PartyGaming-Bwin, Reliance, GTECH, TrillionPay across digital wallets and mobile payments

---

### IvyComptech, Hyderabad · Software Engineer · Jan 2009 – Nov 2009

- Built Party Affiliates and Loyalty systems; added merchandise reward system and player-category loyalty tiers (Java · J2EE · Spring · Struts2)

---

### Cognizant, Hyderabad · Program Analyst · Nov 2007 – Jan 2009

- Implemented Apply Strategy for American Express's online application site — data migration, validation framework, and DOJO front-end integration (Java · J2EE · Struts · XSLT)

---

## ✅ SECTION 5: EDUCATION (keep as-is, just format cleanly)

**Arizona State University** — MS Computer Science, 2021
**National Institute of Technology, Warangal** — B.Tech Civil Engineering, 2007

(Remove the NICMAR Construction Management degree — not relevant for tech roles)

---

## ❌ REMOVE ENTIRELY
- "Personal Details and Interests" section (birthdate + hobbies — not used in US resumes, age can invite discrimination)
- "Reference" section (not needed — recruiters don't call references at resume stage)

---

## 📋 QUESTIONS TO FILL REMAINING GAPS (optional — if you have the numbers)
1. How many product teams use the Portals Framework? (know it's "all" — any number like 15+ teams?)
2. What is the traffic scale of the Portals service? (millions of requests/day?)
3. Any P95 latency improvement from Polly hardening?
4. Turo: any % improvement in API latency or DB query time?
5. Pearson: how many engineering teams adopted the cross-cutting services you built?

Even without these, all bullets above are strong and every number is sourced directly from your promo/tech review docs.
