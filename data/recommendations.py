# Targeted Learning Recommendations for each skill based on gap severity

SKILL_RECOMMENDATIONS = {
    "Python": {
        "gap": "Improve Python fundamentals, control structures, object-oriented concepts, exception handling, data structures, and advanced functional programming (lambda, map, filter, generators).",
        "expert": "Maintain Python proficiency by exploring asynchronous programming, performance optimization, and custom library development."
    },
    "SQL": {
        "gap": "Practice complex SQL queries including JOINs, subqueries, HAVING clause, CTEs (Common Table Expressions), window functions, indexing, and query optimization.",
        "expert": "Master advanced database administration, query plan optimization, sharding, and partitioning."
    },
    "Excel": {
        "gap": "Master advanced Excel functions like VLOOKUP, INDEX-MATCH, SUMIFS, Pivot Tables, conditional formatting, and data visualization charts.",
        "expert": "Explore Excel VBA macros and Power Query integration for automated reporting."
    },
    "Power BI": {
        "gap": "Learn DAX measures, Power Query data transformation, data modeling (star schema), relationship building, and interactive dashboard publishing.",
        "expert": "Focus on enterprise workspace management, row-level security (RLS), and incremental data refresh."
    },
    "Statistics": {
        "gap": "Strengthen statistical concepts including probability distributions, hypothesis testing (t-test, ANOVA), p-values, regression analysis, and confidence intervals.",
        "expert": "Study advanced Bayesian inference, multivariate statistical modeling, and experimental design (A/B testing)."
    },
    "Tableau": {
        "gap": "Practice building calculated fields, Level of Detail (LOD) expressions, parameters, dynamic filters, dashboard actions, and visual storytelling.",
        "expert": "Optimize workbook performance, server deployment, and custom Tableau extensions."
    },
    "DSA using Python": {
        "gap": "Practice linear data structures (stacks, queues, linked lists), tree traversals, graph algorithms (BFS, DFS, Dijkstra), dynamic programming, and time/space complexity analysis.",
        "expert": "Solve hard algorithmic challenges on LeetCode/HackerRank and master advanced graph & string matching algorithms."
    },
    "OOPs using Python": {
        "gap": "Understand core Object-Oriented principles: Encapsulation, Inheritance, Polymorphism, Abstraction, magic methods (__init__, __str__), and class/static methods.",
        "expert": "Apply SOLID principles and design patterns (Factory, Singleton, Observer, Decorator) in software architecture."
    },
    "Flask": {
        "gap": "Learn Flask routing, request handling, Jinja2 templating, SQLAlchemy ORM integration, blueprint modularization, and basic authentication.",
        "expert": "Build microservice architecture, implement OAuth2, and deploy Flask apps with Gunicorn and Docker."
    },
    "Django": {
        "gap": "Master Django MVT architecture, models & migrations, Django ORM querysets, forms, class-based views, admin panel customization, and middleware.",
        "expert": "Implement Django Channels for WebSockets, caching strategies (Redis), and celery async task queues."
    },
    "REST API": {
        "gap": "Learn RESTful principles, HTTP methods (GET, POST, PUT, DELETE, PATCH), status codes, JSON payload design, authentication (JWT/OAuth), and API documentation (Swagger/OpenAPI).",
        "expert": "Focus on API rate limiting, API gateways, versioning strategies, and GraphQL comparison."
    },
    "HTML": {
        "gap": "Study HTML5 semantic tags (<nav>, <article>, <section>), forms & inputs validation, accessibility (ARIA attributes), and SEO meta tags.",
        "expert": "Master Web Components, Shadow DOM, and web accessibility standards (WCAG 2.1 AAA)."
    },
    "CSS": {
        "gap": "Master CSS Box Model, Flexbox layout, CSS Grid, media queries for responsive design, specificity rules, CSS custom properties, and animations.",
        "expert": "Explore CSS architecture (BEM, CSS Modules, Tailwind), SASS preprocessors, and complex keyframe animations."
    },
    "JavaScript": {
        "gap": "Deepen JavaScript knowledge: ES6+ syntax (destructuring, spread, arrow functions), Promises, async/await, DOM manipulation, closures, and event loop mechanics.",
        "expert": "Master JavaScript engine internals (V8), memory management, Web Workers, and TypeScript."
    },
    "React.js": {
        "gap": "Learn React component lifecycle, Hooks (useState, useEffect, useContext, useMemo), props management, state management, and React Router.",
        "expert": "Focus on Next.js server-side rendering (SSR), Redux Toolkit, performance optimization (React.memo), and custom hooks."
    },
    "C++": {
        "gap": "Focus on C++ pointers, memory management (new/delete, smart pointers), OOP concepts, Standard Template Library (vector, map, set), and template programming.",
        "expert": "Study modern C++ (C++17/20), move semantics, multi-threading, and low-level memory layout."
    },
    "C": {
        "gap": "Learn C language pointers, manual memory allocation (malloc/calloc/free), structure alignment, header files, and defensive coding against buffer overflows.",
        "expert": "Study embedded systems programming, kernel module development, and low-level assembly integration."
    },
    "Java": {
        "gap": "Master Java OOP concepts, Collections Framework, Exception handling, Generics, Stream API, JVM memory management, and multi-threading basics.",
        "expert": "Master Spring Boot framework, microservices design, reactive programming (Project Reactor), and JVM tuning."
    },
    "Machine Learning": {
        "gap": "Study supervised and unsupervised learning algorithms (Linear/Logistic Regression, Decision Trees, Random Forest, SVM, K-Means), evaluation metrics (Precision, Recall, F1), and cross-validation.",
        "expert": "Explore ensemble methods (XGBoost, LightGBM), hyperparameter tuning, MLOps, and model deployment pipelines."
    },
    "Deep Learning": {
        "gap": "Understand Artificial Neural Networks (ANN), activation functions (ReLU, Sigmoid, Softmax), backpropagation, Convolutional Neural Networks (CNN) for computer vision, and Recurrent Neural Networks (RNN/LSTM).",
        "expert": "Master Transformer architectures, LLMs, PyTorch/TensorFlow frameworks, GANs, and model quantization."
    },
    "Linear Algebra": {
        "gap": "Review matrix operations, determinants, vector spaces, eigenvalues, eigenvectors, matrix transposition, and Singular Value Decomposition (SVD).",
        "expert": "Apply advanced linear algebra to dimensionality reduction (PCA), neural network weight transformations, and optimization algorithms."
    },
    "Big Data": {
        "gap": "Learn Apache Hadoop architecture (HDFS, MapReduce), Apache Spark DataFrames & RDDs, real-time streaming with Kafka, and NoSQL databases.",
        "expert": "Architect distributed data lakes, optimize Spark job memory usage, and manage cloud data warehouses (Snowflake, Databricks)."
    },
    "Computer Network": {
        "gap": "Study OSI and TCP/IP model layers, IP addressing & subnetting, DNS, ARP, HTTP/HTTPS, TCP vs UDP handshakes, and network troubleshooting tools (ping, traceroute).",
        "expert": "Master BGP routing protocols, SDN (Software-Defined Networking), network traffic analysis, and packet inspection."
    },
    "OS": {
        "gap": "Learn Operating System core concepts: Process vs Thread management, CPU scheduling, Memory management (paging, virtual memory), Deadlocks, and File systems.",
        "expert": "Study OS kernel architecture, device drivers, IPC mechanisms, and virtualization hypervisors."
    },
    "Cyber Security Fundamentals": {
        "gap": "Understand the CIA Triad (Confidentiality, Integrity, Availability), authentication mechanisms (MFA), malware types (ransomware, trojans), firewalls, and defense-in-depth strategies.",
        "expert": "Master Security Operations Center (SOC) workflows, SIEM platform management (Splunk), and incident response frameworks."
    },
    "Ethical Hacking": {
        "gap": "Learn penetration testing methodologies: Reconnaissance (Nmap), vulnerability identification, web security (OWASP Top 10), Wireshark packet analysis, and Metasploit basics.",
        "expert": "Obtain industry certifications (OSCP, CEH), perform red team operations, and master custom exploit payload development."
    },
    "Vulnerability Assessment": {
        "gap": "Learn CVSS scoring metrics, vulnerability scanning using Nessus/OpenVAS, prioritizing CVE remediations, and generating security compliance reports.",
        "expert": "Build automated vulnerability management pipelines integrated into DevSecOps CI/CD."
    },
    "Cryptography": {
        "gap": "Understand Symmetric vs Asymmetric encryption (AES, RSA), cryptographic hashing (SHA-256), Digital Signatures, PKI (Public Key Infrastructure), and Diffie-Hellman key exchange.",
        "expert": "Explore post-quantum cryptography, elliptic curve cryptography (ECC), and zero-knowledge proofs (ZKP)."
    },
    "Database Management": {
        "gap": "Study relational database normalization (1NF, 2NF, 3NF), ACID transactions, primary/foreign key constraints, and SQL injection prevention techniques.",
        "expert": "Master distributed database transactions, replication strategies, and DB security hardening."
    },
    "Figma": {
        "gap": "Master Figma Auto Layout, components & variants, frame constraints, style libraries, interactive prototyping, and Smart Animate.",
        "expert": "Build comprehensive scalable enterprise design systems and design-to-code handoff workflows."
    },
    "Wireframing": {
        "gap": "Practice low-fidelity sketching, visual hierarchy, layout grid systems, structural component placement, and rapid iterative wireframing.",
        "expert": "Conduct usability testing on low-fi wireframes to validate information architecture early."
    },
    "Prototyping": {
        "gap": "Create interactive high-fidelity screen flows, micro-interactions, overlay transitions, component state triggers, and conduct user testing sessions.",
        "expert": "Build advanced dynamic prototypes with variables, expressions, and conditional logic in tools like ProtoPie or Figma."
    },
    "Typography": {
        "gap": "Study font classifications (Serif, Sans-Serif), hierarchy (h1-h6, body), line height (leading), character spacing (kerning/tracking), and WCAG readability contrast.",
        "expert": "Develop custom typographic systems and fluid typography scales for responsive design systems."
    },
    "Color Theory": {
        "gap": "Learn color relationships (Complementary, Analogous), HSL color model, WCAG 2.1 color contrast standards (4.5:1 ratio), and the 60-30-10 color distribution rule.",
        "expert": "Design accessible multi-theme color systems (Light/Dark mode) with semantic design tokens."
    },
    "Cloud Security": {
        "gap": "Understand cloud IAM roles & policies, Principle of Least Privilege, zero-trust architecture, encryption at rest and in transit, and Web Application Firewalls (WAF).",
        "expert": "Implement Cloud Security Posture Management (CSPM), automated compliance auditing, and threat detection."
    },
    "AWS": {
        "gap": "Master core AWS services: EC2 virtual servers, S3 object storage, RDS databases, VPC networking, IAM security, and Lambda serverless functions.",
        "expert": "Prepare for AWS Solutions Architect Professional certification and master multi-region fault-tolerant cloud architectures."
    },
    "DevOps": {
        "gap": "Learn CI/CD automation pipelines (Jenkins/GitHub Actions), containerization with Docker, infrastructure as code with Terraform, and basic bash scripting.",
        "expert": "Master Kubernetes cluster management, Helm charts, GitOps (ArgoCD), and continuous monitoring (Prometheus & Grafana)."
    },
    "Networking": {
        "gap": "Understand cloud networking: VPC subnets, route tables, internet gateways, NAT gateways, security groups, Network ACLs, and Load Balancers.",
        "expert": "Design complex hybrid cloud networking with AWS Direct Connect, Transit Gateway, and mesh networking."
    },
    "Linux": {
        "gap": "Master Linux command line navigation, file permissions (chmod/chown), text searching (grep/find), process management (top/ps), and cron task scheduling.",
        "expert": "Master Linux system administration, shell scripting, systemd service creation, and kernel performance tuning."
    }
}

YOUTUBE_LEARNING_LINKS = {
    "Data Analyst": {
        "Python": "https://youtu.be/m67-bOpOoPU?si=TrC5ps6H6prwTHa_",
        "SQL": "https://youtu.be/-6KHvE78Fv0?si=uqP0vgVVqJugMHt3",
        "Excel": "https://youtu.be/ZmBjibf8dyQ?si=HgrgMueuLgydW6CM",
        "Power BI": "https://youtu.be/GUzNVy4Elyo?si=NkNp9Qd8rIpe2ZRn",
        "Statistics": "https://youtu.be/_DrtU0LTOtU?si=t2zSkl-mjH828T5i",
        "Tableau": "https://youtu.be/K3pXnbniUcM?si=Y-Nj-jzOFimtp_ju"
    },
    "Python Developer": {
        "Python": "https://youtu.be/m67-bOpOoPU?si=TrC5ps6H6prwTHa_",
        "DSA using Python": "https://youtu.be/cKeKp17afZw?si=9pXdWW-40w13RfLb",
        "OOPs using Python": "https://youtu.be/Ej_02ICOIgs?si=Op3khY8gL5IBczqK",
        "OOP using Python": "https://youtu.be/Ej_02ICOIgs?si=Op3khY8gL5IBczqK",
        "SQL": "https://youtu.be/-6KHvE78Fv0?si=uqP0vgVVqJugMHt3",
        "Flask": "https://youtu.be/mvRPa9-5Zsc?si=GlsflChsLSGsVuvH",
        "Django": "https://youtu.be/gyAtd6Z2QmQ?si=5uwKpHdU_PFGzGp1",
        "REST API": "https://youtu.be/41bRmKMb464?si=m_dE8vQpl39w8jmc"
    },
    "Full Stack Developer": {
        "HTML": "https://youtu.be/8oONqsEKf6k?si=OuikFihHfpiN0Ry7",
        "CSS": "https://youtu.be/lgKbG9pKmx8?si=eq7HHCBcipEyBrUT",
        "JavaScript": "https://youtu.be/ynvnxx7rWQ4?si=wKhqNp_9d7vvBIBM",
        "React.js": "https://youtu.be/8pWdE6ozjf8?si=u79dK7Z_KPt0p536",
        "React JS": "https://youtu.be/8pWdE6ozjf8?si=u79dK7Z_KPt0p536",
        "Python": "https://youtu.be/m67-bOpOoPU?si=TrC5ps6H6prwTHa_",
        "SQL": "https://youtu.be/-6KHvE78Fv0?si=uqP0vgVVqJugMHt3",
        "REST API": "https://youtu.be/41bRmKMb464?si=m_dE8vQpl39w8jmc",
        "Django": "https://youtu.be/gyAtd6Z2QmQ?si=5uwKpHdU_PFGzGp1"
    },
    "FS Developer": {
        "HTML": "https://youtu.be/8oONqsEKf6k?si=OuikFihHfpiN0Ry7",
        "CSS": "https://youtu.be/lgKbG9pKmx8?si=eq7HHCBcipEyBrUT",
        "JavaScript": "https://youtu.be/ynvnxx7rWQ4?si=wKhqNp_9d7vvBIBM",
        "React.js": "https://youtu.be/8pWdE6ozjf8?si=u79dK7Z_KPt0p536",
        "React JS": "https://youtu.be/8pWdE6ozjf8?si=u79dK7Z_KPt0p536",
        "Python": "https://youtu.be/m67-bOpOoPU?si=TrC5ps6H6prwTHa_",
        "SQL": "https://youtu.be/-6KHvE78Fv0?si=uqP0vgVVqJugMHt3",
        "REST API": "https://youtu.be/41bRmKMb464?si=m_dE8vQpl39w8jmc",
        "Django": "https://youtu.be/gyAtd6Z2QmQ?si=5uwKpHdU_PFGzGp1"
    },
    "AI/ML Engineer": {
        "Python": "https://youtu.be/m67-bOpOoPU?si=TrC5ps6H6prwTHa_",
        "C++": "https://youtu.be/VnaKu8_H3jU?si=XMNukiFLuu8_z5gm",
        "C": "https://youtu.be/fmSnLiAv-zc?si=r7PtYpQdWItHWJce",
        "Java": "https://youtu.be/IT2durkDCXM?si=jNnysQdG2mOkmsT6",
        "Machine Learning": "https://youtu.be/aiCIWGSCCKo?si=GQJo6tU5HJH09Kxv",
        "Deep Learning": "https://youtu.be/8t_AJicjR-w?si=7-4H3Zm9-79PMC2a",
        "Statistics": "https://youtu.be/_DrtU0LTOtU?si=t2zSkl-mjH828T5i",
        "Linear Algebra": "https://youtu.be/LzLswBOf_vM?si=1FwWCYULZoYtg4h5",
        "Big Data": "https://youtu.be/TVNVQP7L9IE?si=nDcz8Jh_fWz4mu2p"
    },
    "AI & ML Engineer": {
        "Python": "https://youtu.be/m67-bOpOoPU?si=TrC5ps6H6prwTHa_",
        "C++": "https://youtu.be/VnaKu8_H3jU?si=XMNukiFLuu8_z5gm",
        "C": "https://youtu.be/fmSnLiAv-zc?si=r7PtYpQdWItHWJce",
        "Java": "https://youtu.be/IT2durkDCXM?si=jNnysQdG2mOkmsT6",
        "Machine Learning": "https://youtu.be/aiCIWGSCCKo?si=GQJo6tU5HJH09Kxv",
        "Deep Learning": "https://youtu.be/8t_AJicjR-w?si=7-4H3Zm9-79PMC2a",
        "Statistics": "https://youtu.be/_DrtU0LTOtU?si=t2zSkl-mjH828T5i",
        "Linear Algebra": "https://youtu.be/LzLswBOf_vM?si=1FwWCYULZoYtg4h5",
        "Big Data": "https://youtu.be/TVNVQP7L9IE?si=nDcz8Jh_fWz4mu2p"
    },
    "Cyber Security Analyst": {
        "Computer Network": "https://youtu.be/yiIpBNBl4bc?si=EhiNcaIjs-FW6XE7",
        "Computer Networks": "https://youtu.be/yiIpBNBl4bc?si=EhiNcaIjs-FW6XE7",
        "OS": "https://youtu.be/S-qPQiD0vqU?si=KlsqEseXoJpHgcCp",
        "Ethical Hacking": "https://youtu.be/vh3WW3d0yxg?si=YbOJi55SHIfiE6YZ",
        "Vulnerability Assessment": "https://youtu.be/iLdsCnpMnTg?si=G12c5Tzhbiwu39_n",
        "Cryptography": "https://youtu.be/j_8PLI_wCVU?si=8y5H3gHeTvReuCNL",
        "Database Management": "https://youtu.be/mDFXzRBpJTI?si=TB57G0QHSg2U8Kc3",
        "C": "https://youtu.be/fmSnLiAv-zc?si=r7PtYpQdWItHWJce",
        "C++": "https://youtu.be/VnaKu8_H3jU?si=XMNukiFLuu8_z5gm",
        "Python": "https://youtu.be/m67-bOpOoPU?si=TrC5ps6H6prwTHa_",
        "Java": "https://youtu.be/IT2durkDCXM?si=jNnysQdG2mOkmsT6"
    },
    "Cybersecurity Analyst": {
        "Computer Network": "https://youtu.be/yiIpBNBl4bc?si=EhiNcaIjs-FW6XE7",
        "Computer Networks": "https://youtu.be/yiIpBNBl4bc?si=EhiNcaIjs-FW6XE7",
        "OS": "https://youtu.be/S-qPQiD0vqU?si=KlsqEseXoJpHgcCp",
        "Ethical Hacking": "https://youtu.be/vh3WW3d0yxg?si=YbOJi55SHIfiE6YZ",
        "Vulnerability Assessment": "https://youtu.be/iLdsCnpMnTg?si=G12c5Tzhbiwu39_n",
        "Cryptography": "https://youtu.be/j_8PLI_wCVU?si=8y5H3gHeTvReuCNL",
        "Database Management": "https://youtu.be/mDFXzRBpJTI?si=TB57G0QHSg2U8Kc3",
        "C": "https://youtu.be/fmSnLiAv-zc?si=r7PtYpQdWItHWJce",
        "C++": "https://youtu.be/VnaKu8_H3jU?si=XMNukiFLuu8_z5gm",
        "Python": "https://youtu.be/m67-bOpOoPU?si=TrC5ps6H6prwTHa_",
        "Java": "https://youtu.be/IT2durkDCXM?si=jNnysQdG2mOkmsT6"
    },
    "UI/UX Designer": {
        "Figma": "https://youtu.be/NPhm4ObcWhE?si=OW1Bb-QdxI5lssRX",
        "Wireframing": "https://youtu.be/_vLXDrNUdJ0?si=K26gIm6lXmRfCljX",
        "Prototyping": "https://youtu.be/LlDOKy0DMWQ?si=tDSbdKO8-krO514G",
        "Color Theory": "https://youtu.be/xHI5z0XbeMY?si=L5ABHZ1QVIXXVb4j"
    },
    "Cloud Computing": {
        "Cloud Security": "https://www.youtube.com/live/Ijkvx1u0w6o?si=F6yMsyVTewMBtx7u",
        "AWS": "https://youtu.be/eZeNIakuqbc?si=4Tx0knd9oE3elYEH",
        "DevOps": "https://youtu.be/aXJ2tJT8xpY?si=jPqNeVrxanUFUC6W",
        "Networking": "https://youtu.be/kdYPGbEm4uA?si=RYfqhJia8DgFulsc",
        "Linux": "https://youtu.be/WmuE-MHRGbQ?si=FE_s3Xdvpt7vVPAC"
    }
}

def get_recommendation(skill_name, student_level, industry_level):
    gap = industry_level - student_level
    info = SKILL_RECOMMENDATIONS.get(skill_name, {
        "gap": "Focus on fundamental concepts and practical hands-on exercises for " + skill_name + ".",
        "expert": "Continue practicing advanced topics and building real-world projects in " + skill_name + "."
    })
    
    if gap <= 0:
        return f"Met Industry Standard! {info['expert']}"
    else:
        return f"Level Gap: {gap} level(s). {info['gap']}"

def get_youtube_link(role_name, skill_name):
    role_links = YOUTUBE_LEARNING_LINKS.get(role_name, {})
    return role_links.get(skill_name, None)
