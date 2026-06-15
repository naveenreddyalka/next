# Interview question seed bank - merged into company_latest_questions.json on each refresh.
# New entries are prepended (newest first). Sources: Blind, LeetCode Discuss, Glassdoor, Reddit, Exponent, interviewing.io

def q(qtype, question, source, reported, url=""):
    return {"type": qtype, "question": question, "source": source, "reported": reported, "url": url}


QUESTIONS = {
    "anthropic": [
        q("Coding", "Implement an in-memory database with SET/GET/DELETE, then add TTL, filtered scans, and file compression levels", "Medium / Exponent", "2025-09", "https://medium.com/@anqi.silvia/my-2025-anthropic-software-engineer-interview-experience-9fc15cd81a99"),
        q("Coding", "Build a multi-threaded web crawler with deduplication and rate limiting", "interviewing.io", "2025-12", "https://interviewing.io/anthropic-interview-questions"),
        q("Coding", "Implement LRU cache with serialization and evolving constraints", "Exponent", "2025-10", "https://www.tryexponent.com/guides/anthropic-software-engineer-interview/questions"),
        q("System Design", "Design a batch inferencing API over GPU clusters (scheduling, cold start, model caching)", "Exponent", "2025-08", "https://www.tryexponent.com/experiences/anthropic-staff-software-engineer-interview-9bfb57"),
        q("System Design", "Design distributed search for 1B documents at 1M QPS with sharding and LLM inference scaling", "Medium", "2025-09", "https://medium.com/@anqi.silvia/my-2025-anthropic-software-engineer-interview-experience-9fc15cd81a99"),
        q("System Design", "Design inference batching on a single GPU maximizing utilization under synchronous user waits", "Exponent", "2026-03", "https://www.tryexponent.com/guides/anthropic-software-engineer-interview/questions"),
        q("Behavioral", "Tell me about a safety-first technical decision you made on a project", "Medium", "2025-09", "https://medium.com/@anqi.silvia/my-2025-anthropic-software-engineer-interview-experience-9fc15cd81a99"),
        q("Behavioral", "Describe a technical misjudgment that delayed a project - what did you learn?", "Medium", "2025-09", "https://medium.com/@anqi.silvia/my-2025-anthropic-software-engineer-interview-experience-9fc15cd81a99"),
    ],
    "openai": [
        q("Coding", "Implement a time-based key-value store with get/set and expiry", "IGotAnOffer", "2025-11", "https://igotanoffer.com/en/advice/openai-coding-interview"),
        q("Coding", "Build a multithreaded web crawler with URL deduplication and failure handling", "IGotAnOffer", "2025-11", "https://igotanoffer.com/en/advice/openai-coding-interview"),
        q("Coding", "Implement Unix cd command with symlink resolution and cycle detection", "IGotAnOffer", "2025-11", "https://igotanoffer.com/en/advice/openai-coding-interview"),
        q("System Design", "Design ChatGPT-scale chat service - press on 100x/1000x load growth", "Exponent", "2025-10", "https://www.tryexponent.com/guides/openai-software-engineer-interview"),
        q("System Design", "Design model-serving platform with request batching, queuing, and GPU utilization", "interviewing.io", "2025-12", "https://interviewing.io/openai-interview-questions"),
        q("Behavioral", "Technical project deep dive - what did YOU own vs the team?", "Exponent", "2025-08", "https://www.tryexponent.com/experiences/openai-senior-software-engineer-interview-60a1ae"),
    ],
    "xai": [
        q("Coding", "Rate-limited API design with sliding window per user", "General / Blind pattern", "2025-12", ""),
        q("System Design", "Design a low-latency inference API serving Grok at scale", "General prep", "2025-12", ""),
        q("Behavioral", "Why xAI / Grok - ownership and speed under ambiguity", "General prep", "2025-12", ""),
    ],
    "nvidia": [
        q("Coding", "LRU Cache - O(1) get/put", "LeetCode / jointaro", "2025-06", "https://www.jointaro.com/interviews/companies/nvidia/"),
        q("Coding", "Graph/tree medium problems with memory or concurrency follow-ups", "Leetcode Wizard", "2025-08", "https://leetcodewizard.io/blog/mastering-the-nvidia-software-engineer-interview-questions-process-and-expert-tips-for-preparation"),
        q("System Design", "Design large-scale GPU inference scheduling and model serving pipeline", "IGotAnOffer", "2025-05", "https://igotanoffer.com/en/advice/nvidia-software-engineer-interview"),
        q("Behavioral", "Explain CUDA memory coalescing and how it affects kernel performance", "huru.ai", "2025-10", "https://huru.ai/nvidia-interview-questions-mastering-cuda-inference-systems/"),
    ],
    "servicenow": [
        q("Coding", "Trapping Rain Water - two-pointer / sliding window pattern", "TechPrep", "2026-01", "https://www.techprep.app/blog/servicenow-interview-process"),
        q("Coding", "Implement LRU cache and explain trade-offs", "cvcraft.roynex", "2026-04", "https://cvcraft.roynex.com/companies/servicenow"),
        q("Coding", "Topological sort - when would you use it in a workflow product?", "cvcraft.roynex", "2026-04", "https://cvcraft.roynex.com/companies/servicenow"),
        q("System Design", "Design ServiceNow incident-management workflow engine for millions of workflows across 8K tenants", "Tech Interview Dot Org", "2026-01", "https://www.techinterview.org/companies/servicenow/"),
        q("System Design", "Design permissions model for CMDB with 100M configuration items and role hierarchies", "Tech Interview Dot Org", "2026-01", "https://www.techinterview.org/companies/servicenow/"),
        q("System Design", "Shard a relational schema for 5,000 enterprise tenants with data isolation", "cvcraft.roynex", "2026-04", "https://cvcraft.roynex.com/companies/servicenow"),
        q("Behavioral", "Tell me about staying Hungry & Humble while shipping under pressure", "cvcraft.roynex", "2026-04", "https://cvcraft.roynex.com/companies/servicenow"),
    ],
    "confluent": [
        q("Coding", "Word and phrase search across a list of documents", "LeetCode Discuss / CodingKaro", "2024-12", "https://leetcode.com/discuss/post/6155819/confluent-onsite-round-by-anonymous_user-sho3/"),
        q("Coding", "Validate Sudoku board and extend to Sudoku solver", "Glassdoor / LeetCode Discuss", "2024-12", "https://www.glassdoor.com/Interview/Confluent-Software-Engineer-Interview-Questions-EI_IE1048428.0,9_KO10,27.htm"),
        q("Coding", "Implement LRU cache with TTL expiration", "Glassdoor / jointaro", "2025-11", "https://www.jointaro.com/interviews/companies/confluent/work-experiences/software-engineer-bengaluru-november-7-2025-4-09fb2dd5/"),
        q("Coding", "LFU cache with thread-safety follow-up", "LeetCode Discuss", "2024-12", "https://leetcode.com/discuss/post/6155819/confluent-onsite-round-by-anonymous_user-sho3/"),
        q("System Design", "Design URL shortener with streaming analytics hook", "LeetCode Discuss", "2024-12", "https://leetcode.com/discuss/post/6155819/confluent-onsite-round-by-anonymous_user-sho3/"),
        q("System Design", "Design multi-tenant Kafka cluster with isolation and rebalancing", "Handoff prep", "2025-10", ""),
        q("Behavioral", "Deep Kafka domain: compaction, ISR, partition rebalancing under failure", "Handoff prep", "2025-10", ""),
    ],
    "databricks": [
        q("Coding", "Concurrency round: implement thread-safe logger or concurrent writers (signature round)", "jobsbyculture / interviewing.io", "2026-01", "https://jobsbyculture.com/blog/databricks-interview-prep-2026"),
        q("Coding", "Variable-sized tic-tac-toe game implementation", "interviewing.io", "2025-12", "https://interviewing.io/databricks-interview-questions"),
        q("Coding", "IP address to CIDR range matching", "interviewing.io", "2025-12", "https://interviewing.io/databricks-interview-questions"),
        q("Coding", "Largest rectangle in histogram applied to 2D workspace grid", "JobMentis", "2026-01", "https://www.jobmentis.com/en/interviews/databricks/swe"),
        q("System Design", "Design real-time streaming pipeline / data lakehouse ingestion at scale", "jobsbyculture", "2026-01", "https://jobsbyculture.com/blog/databricks-interview-prep-2026"),
        q("System Design", "Design production RAG architecture (GenAI round increasingly common)", "jobsbyculture", "2026-01", "https://jobsbyculture.com/blog/databricks-interview-prep-2026"),
        q("System Design", "Design cheapest-book search service across distributors", "interviewing.io", "2025-12", "https://interviewing.io/databricks-interview-questions"),
        q("Behavioral", "STAR stories: conflict resolution, ownership, cross-functional feedback", "YouTube / candidate reports", "2025-11", "https://www.youtube.com/watch?v=Fdd0PjsieWk"),
    ],
    "stripe": [
        q("Coding", "Design a rate limiter - N requests per user per minute (sliding window)", "Leetcode Wizard", "2025-10", "https://leetcodewizard.io/blog/mastering-the-stripe-software-engineer-interview-questions-process-and-expert-tips-for-preparation"),
        q("Coding", "Bug bash: find race conditions and off-by-one bugs in ~200 lines of payment code", "techinterview.org", "2026-01", "https://www.techinterview.org/post/3233460268/stripe-interview-guide-2026-process-bug-bash-round-and-payment-systems/"),
        q("Coding", "Integration round: build feature using Stripe API docs + GitHub repo", "Exponent", "2025-12", "https://www.tryexponent.com/guides/stripe-software-engineer-interview"),
        q("System Design", "Design Stripe payment processing with idempotency keys and exactly-once semantics", "techinterview.org", "2026-01", "https://www.techinterview.org/post/3233460268/stripe-interview-guide-2026-process-bug-bash-round-and-payment-systems/"),
        q("System Design", "Design distributed rate limiter for Stripe API (multi-region)", "techinterview.org", "2026-01", "https://www.techinterview.org/post/3233460268/stripe-interview-guide-2026-process-bug-bash-round-and-payment-systems/"),
        q("Behavioral", "Ownership example - incident you drove and cross-team disagreement", "Exponent", "2025-12", "https://www.tryexponent.com/guides/stripe-software-engineer-interview"),
    ],
    "google": [
        q("Coding", "LRU cache O(1) - common Google follow-up chain", "Onsites.fyi", "2025-10", "https://www.onsites.fyi/blog/article/google-L5-software-engineer-interview-questions"),
        q("Coding", "Median of data stream (two heaps)", "Onsites.fyi / Medium", "2025-10", "https://www.onsites.fyi/blog/article/google-L5-software-engineer-interview-questions"),
        q("Coding", "Graph: shortest paths, topological sort, strongly connected components", "Medium L5 reports", "2025-09", "https://medium.com/@rohitverma_87831/my-interview-experience-at-google-afc1080df175"),
        q("System Design", "Design Google-scale autocomplete with prefix frequency ranking", "Onsites.fyi", "2025-10", "https://www.onsites.fyi/blog/article/google-L5-software-engineer-interview-questions"),
        q("Behavioral", "Googleyness: mentor junior engineers, lead without authority, controversial decision", "gitGood.dev", "2025-11", "https://gitgood.dev/prep/google-l5-swe"),
    ],
    "snowflake": [
        q("Coding", "Tree medium with pruning + greedy max-heap follow-up", "Glassdoor", "2025-06", "https://www.glassdoor.com/Interview/Snowflake-Software-Engineer-Interview-Questions-EI_IE928471.0,9_KO10,27.htm"),
        q("Coding", "Check whether any character has been duplicated in a string", "Exponent", "2026-01", "https://www.tryexponent.com/guides/snowflake-software-engineer-interview"),
        q("System Design", "Design quota management service with concurrent users, reclamation, and lock contention", "DEV Community", "2025-11", "https://dev.to/net_programhelp_e160eef28/snowflake-backend-sde-phone-interview-experience-code-isnt-tricky-but-engineering-thinking-is-351g"),
        q("System Design", "Design multi-tenant data warehouse isolating business units without workload interference", "System Design Handbook", "2025-10", "https://www.systemdesignhandbook.com/guides/snowflake-system-design-interview/"),
        q("System Design", "Design real-time data ingestion pipeline at Snowflake scale", "Refer.me", "2025-09", "https://www.refer.me/interview/technical-interview-for-snowflake-software-engineer-technical-interview-at-snowflake"),
        q("Behavioral", "Explain engineering trade-offs linking technical design to business metrics", "DEV Community", "2025-11", "https://dev.to/net_programhelp_e160eef28/snowflake-backend-sde-phone-interview-experience-code-isnt-tricky-but-engineering-thinking-is-351g"),
    ],
    "netflix": [
        q("Coding", "LC 901 Online Stock Span variant - sliding window / monotonic stack", "programhelp.net", "2025-11", "https://programhelp.net/en/vo/netflix-software-engineer-interview-guide-top-questions-tips/"),
        q("Coding", "OOD: design a class from one-liner spec - clarify requirements first", "Blind", "2025-08", "https://www.teamblind.com/post/netflix-interview-prep-2025-oi6mk43k"),
        q("System Design", "Design log/video playback pipeline at Netflix scale (multi-region, fault tolerance)", "programhelp.net", "2025-11", "https://programhelp.net/en/vo/netflix-software-engineer-interview-guide-top-questions-tips/"),
        q("System Design", "Open Connect CDN - multi-region failover and traffic routing", "Prepfully", "2025-10", "https://prepfully.com/interview-guides/netflix-software-engineer"),
        q("Behavioral", "Culture memo alignment - freedom and responsibility, high performance bar", "Blind", "2025-08", "https://www.teamblind.com/post/netflix-l4-full-stack-engineer-interview-prep-0cdqwyl4"),
    ],
    "uber": [
        q("Coding", "Optimal Binary Search Tree variation (DP on trees)", "interviewexperiences.in", "2025-11", "https://interviewexperiences.in/experience/uber/interview-experience-sde2-uber-nov-2025"),
        q("Coding", "Minimax game - two players pick only corner values each turn", "interviewexperiences.in", "2025-11", "https://interviewexperiences.in/experience/uber/interview-experience-sde2-uber-nov-2025"),
        q("Coding", "Implement Linux filesystem commands: mkdir, cd, ls, pwd (N-ary tree)", "interviewexperiences.in", "2025-11", "https://interviewexperiences.in/experience/uber/interview-experience-sde2-uber-nov-2025"),
        q("System Design", "Design real-time driver dispatch - match riders to nearest driver in 1-2 seconds", "Tech Interview Dot Org", "2026-01", "https://www.techinterview.org/post/3233460273/uber-interview-guide-2026-dispatch-systems-geospatial-algorithms-and-marketplace-engineering/"),
        q("System Design", "Design Splitwise - minimize transactions, handle concurrent expense entries", "interviewexperiences.in", "2025-11", "https://interviewexperiences.in/experience/uber/interview-experience-sde2-uber-nov-2025"),
        q("System Design", "Design real-time stock price notification system", "devbrainiac", "2025-10", "https://devbrainiac.com/blogs/83/uber-sde-2-interview-experience/"),
        q("Behavioral", "Deep dive on production failure you owned and cross-team disagreement", "devbrainiac", "2025-10", "https://devbrainiac.com/blogs/83/uber-sde-2-interview-experience/"),
    ],
    "spacex": [
        q("Coding", "Hybrid algorithm + design: multi-location inventory management with transfers at scale", "interviewing.io", "2025-10", "https://interviewing.io/spacex-interview-questions"),
        q("Coding", "Real-time scheduler for concurrent spacecraft telemetry streams", "cleverprep", "2025-11", "https://www.cleverprep.com/companies/spacex/software-engineer"),
        q("System Design", "Design telemetry data pipeline for a rocket launch (compression, failure handling)", "System Design Handbook", "2025-10", "https://www.systemdesignhandbook.com/guides/spacex-system-design-interview/"),
        q("System Design", "Design fault-tolerant rocket guidance handling sensor failures (TMR, watchdog timers)", "engineerknow / Tech Interview Dot Org", "2025-12", "https://www.engineerknow.com/2026/04/30-popular-spacex-engineering-technical.html"),
        q("Behavioral", "Mission commitment and long hours expectations - honest HM conversation", "Handoff prep", "2025-10", ""),
    ],
}
