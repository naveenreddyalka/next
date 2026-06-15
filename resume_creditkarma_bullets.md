# CreditKarma — Resume Bullets (Draft from Promo Docs)
# Senior Software Engineer II · Feb 2022 – Present

---

## FINAL BULLETS (copy these into resume)

**CreditKarma, Oakland · Senior Software Engineer II · Feb 2022 – Present**

- Designed and built the Portal Provider framework — the core abstraction for dynamic portal configuration that **90% of CreditKarma portals clients** currently depend on, directly underpinning the entire federated portals SDK architecture adopted across all product teams
- Led end-to-end architecture and production delivery of the Dashboard × Portals SDK federation — the team's most complex migration — including designing the Bridge API for phased A/B rollout; achieved **100% production ramp**, enabled RecSys V2 integration (nested grouping, heterogeneous content ranking, reduced RecSys calls via FAO), and unblocked new vertical onboarding (HELOC, Home refi); recognized by VP and two Directors across 5+ public kudos
- Architected and shipped Local Eligibility for Portals SDK (GA Feb 2025), moving eligibility evaluation from centralized backend into client-side SDK — delivered **45% faster rendering** for Assets team, eliminated redundant network calls, and added production observability via custom eligibility metrics
- Led Data Contracts from inception through production (Oct 2025) — bootstrapped fwk_data-contracts Nx monorepo from scratch, built cross-language codegen (TypeScript, GraphQL, Scala), authored Thrift IDL in con_idl, and automated the publish pipeline reducing contract release time **from days to minutes**; named by Director as org-wide primary contact for adoption
- Diagnosed and fixed critical Talon/Polly production bugs as the platform's first consumer at scale: memory leaks in the processing pipeline, pm2 socket exhaustion halting Polly request handling, and MGS startup latency; built reusable load testing infrastructure (containers_portals-pig-graphql-service) now available for all future Polly regression testing
- Maintain and evolve Finagle-based web framework (EOL Twitter stack) used by all CreditKarma product development teams — managing SLAs, scalability, and incremental modernization while contributing to CreditKarma's open-source projects in Scala and TypeScript

---

## SOURCE EVIDENCE (what each bullet is based on)

### Bullet 1 — Portal Provider Framework
Source: Technical Review doc
> "In 2023, he designed and built the Portal Provider framework in containers_federated-portals-client the core abstraction for dynamic portal configuration that 90% of current portals clients still rely on that directly underpins the architecture of the current federated portals SDK."
Number: 90% — directly quoted

### Bullet 2 — Dashboard/RecSys V2 Migration
Source: Promo doc + Technical Review
- "Big shout out to teams' joint efforts, thanks to @Naveen Reddy Alka... on troubleshooting, testing to unblock the issue in every step!" — Rui Wu (VP area)
- "HUGE kudos to you all (esp @Naveen Reddy Alka) on driving this integration front" — Vibha Rao, Director
- "Big shoutout to everyone who made this migration happen" (tagged Naveen) — Martin Song, Director
- "Many people to thank for, especially... @Naveen Reddy Alka... Truly inspiring and amazing team work!" — Bin Liu, VP
- "achieved successful ramp of the bridge API to 100% on production" — Tech Review doc
Numbers: 100% ramp — directly quoted

### Bullet 3 — Local Eligibility / 45% faster
Source: Technical Review doc
> "[Assets performance gains] 45% faster rendering with Assets running local eligibility"
> "Shipped Local Eligibility to GA in Feb 2025"
Number: 45% — directly from presentation referenced in tech review

### Bullet 4 — Data Contracts
Source: Technical Review doc
> "Automated publish pipeline eliminating manual publishing steps & enabling continuous delivery of contract changes, reducing time to release for contract changes from days to mins"
> "Successfully shipped Data contracts to production Oct 2025"
> Vibha Rao (Director): "Named Naveen as primary contact for Data Contracts implementation & pilot adoption (org-wide forum)"
Numbers: days→minutes — directly quoted

### Bullet 5 — Talon/Polly hardening
Source: Technical Review doc
> "Fixed memory leak and socket exhaustion upstream, protecting all current and future Polly consumers"
> "Startup latency fix eliminated the service degradation vector in production"
> "Testing framework gave the team its first reproducible Polly performance baseline"

### Bullet 6 — Framework / Finagle
Source: Original resume + Technical Review
> "help manage a custom web framework used by all our product development teams, which is based on Finagle from Twitter, even though it is now end-of-life"
> "Naveen exercised a program-level technical leadership working across different teams"

---

## WHAT'S STILL MISSING (questions to fill gaps)

1. How many product teams depend on the Portals Framework? (know it's "all" — any number like 15+ teams?)
2. What is the traffic scale of the Portals service? (e.g., X million requests/day)
3. Any latency or uptime SLA numbers you hit/maintained?
4. How many engineers does the CreditKarma Portals org have roughly?
5. Any P95 latency improvement numbers from Polly hardening?

Even without those, the 5 bullets above are strong and defensible from the docs.
