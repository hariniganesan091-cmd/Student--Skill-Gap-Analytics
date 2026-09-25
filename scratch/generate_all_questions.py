import json
import pprint
import os

questions_data = {}

def add_skill_qs(role, skill, q1, q2, q3, q4, q5):
    if role not in questions_data:
        questions_data[role] = {}
    
    q1["difficulty"] = "Basic"
    q2["difficulty"] = "Beginner"
    q3["difficulty"] = "Intermediate"
    q4["difficulty"] = "Advanced"
    q5["difficulty"] = "Expert"
    
    for idx, q in enumerate([q1, q2, q3, q4, q5]):
        assert q["answer"] in q["options"], f"Error in {role} -> {skill} Q{idx+1}: answer '{q['answer']}' not in options: {q['options']}"

    questions_data[role][skill] = [q1, q2, q3, q4, q5]

# ==========================================
# 1. DATA ANALYST (6 Skills x 5 = 30 Qs)
# ==========================================

add_skill_qs(
    "Data Analyst", "Python",
    {
        "q": "Which Python library is primarily used for tabular data manipulation and DataFrame operations?",
        "options": ["NumPy", "Pandas", "SciPy", "Matplotlib"],
        "answer": "Pandas"
    },
    {
        "q": "Which Pandas method drops rows or columns with missing (NaN) values?",
        "options": ["df.dropna()", "df.fillna()", "df.remove_null()", "df.clean()"],
        "answer": "df.dropna()"
    },
    {
        "q": "How do you merge two DataFrames on a common key column in Pandas?",
        "options": ["pd.concat()", "pd.merge()", "pd.join_tables()", "pd.append()"],
        "answer": "pd.merge()"
    },
    {
        "q": "What does `df.groupby('Category')['Sales'].transform('mean')` return in Pandas?",
        "options": [
            "An aggregated summary DataFrame grouped by Category",
            "A Series with the original DataFrame index containing the Category mean for each row",
            "A modified DataFrame with rows filtered to above-average sales",
            "A dictionary of category mean values"
        ],
        "answer": "A Series with the original DataFrame index containing the Category mean for each row"
    },
    {
        "q": "When processing a 15GB CSV file on a memory-constrained 8GB RAM system, which approach optimizes Pandas memory consumption?",
        "options": [
            "Use chunksize parameter in pd.read_csv() combined with dtype downcasting",
            "Increase Python recursion limit with sys.setrecursionlimit()",
            "Read the entire file into a single string using open().read()",
            "Use df.apply() on raw unparsed text lines"
        ],
        "answer": "Use chunksize parameter in pd.read_csv() combined with dtype downcasting"
    }
)

add_skill_qs(
    "Data Analyst", "SQL",
    {
        "q": "Which SQL clause filters records BEFORE any grouping or aggregation takes place?",
        "options": ["HAVING", "WHERE", "ORDER BY", "GROUP FILTER"],
        "answer": "WHERE"
    },
    {
        "q": "Which JOIN returns all records from the left table and matched records from the right table?",
        "options": ["INNER JOIN", "RIGHT JOIN", "LEFT JOIN", "FULL OUTER JOIN"],
        "answer": "LEFT JOIN"
    },
    {
        "q": "Which SQL window function computes a cumulative moving average across ordered rows?",
        "options": [
            "AVG(amount) OVER (PARTITION BY category ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)",
            "SUM(amount) GROUP BY category ORDER BY date",
            "CUMULATIVE_AVG(amount) BY category",
            "ROW_NUMBER() OVER (ORDER BY date) * AVG(amount)"
        ],
        "answer": "AVG(amount) OVER (PARTITION BY category ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)"
    },
    {
        "q": "What is the key functional difference between RANK() and DENSE_RANK()?",
        "options": [
            "RANK() leaves gaps in sequence after ties, whereas DENSE_RANK() assigns consecutive ranks without gaps",
            "DENSE_RANK() leaves gaps in sequence after ties, whereas RANK() assigns consecutive ranks",
            "RANK() works only on integer columns while DENSE_RANK() works on string columns",
            "There is no difference in ranking output"
        ],
        "answer": "RANK() leaves gaps in sequence after ties, whereas DENSE_RANK() assigns consecutive ranks without gaps"
    },
    {
        "q": "When optimizing a slow analytical query featuring nested correlated subqueries on an unindexed 50M-row table, what query refactoring yields the greatest speedup?",
        "options": [
            "Convert correlated subqueries into CTEs/Window Functions and add composite B-Tree indexes on join and filter columns",
            "Replace INNER JOIN with CROSS JOIN and add OPTION (RECOMPILE)",
            "Wrap query in a CURSOR loop fetching 1 row at a time",
            "Cast all date filtering columns to VARCHAR format"
        ],
        "answer": "Convert correlated subqueries into CTEs/Window Functions and add composite B-Tree indexes on join and filter columns"
    }
)

add_skill_qs(
    "Data Analyst", "Excel",
    {
        "q": "Which Excel formula searches for a value in the leftmost column of a table and returns a value in the same row?",
        "options": ["HLOOKUP", "VLOOKUP", "CONCATENATE", "COUNTIF"],
        "answer": "VLOOKUP"
    },
    {
        "q": "What feature in Excel dynamically summarizes, groups, and cross-tabulates data without formula editing?",
        "options": ["Pivot Table", "Data Validation", "Goal Seek", "Solver"],
        "answer": "Pivot Table"
    },
    {
        "q": "Which formula combination provides a flexible dynamic lookup that doesn't require the lookup column to be leftmost?",
        "options": ["INDEX and MATCH", "VLOOKUP and HLOOKUP", "SUMIF and COUNTIF", "INDIRECT and OFFSET"],
        "answer": "INDEX and MATCH"
    },
    {
        "q": "Which dynamic array formula in modern Excel extracts unique items from a list filtered by specific criteria?",
        "options": [
            "=UNIQUE(FILTER(array, include_condition))",
            "=DISTINCT(SUMIFS(array, condition))",
            "=INDEX(MATCH(UNIQUE(array)))",
            "=VLOOKUP_MULTI(array, condition)"
        ],
        "answer": "=UNIQUE(FILTER(array, include_condition))"
    },
    {
        "q": "In financial modeling, why is wrapping volatile function INDIRECT() inside thousands of grid cells detrimental?",
        "options": [
            "INDIRECT is a volatile function forcing Excel to recalculate the entire formula tree on every grid edit",
            "INDIRECT cannot reference cells in other worksheets",
            "INDIRECT limits sheet calculations to 256 rows",
            "INDIRECT permanently overwrites cell raw values"
        ],
        "answer": "INDIRECT is a volatile function forcing Excel to recalculate the entire formula tree on every grid edit"
    }
)

add_skill_qs(
    "Data Analyst", "Power BI",
    {
        "q": "What expression language is used in Power BI for custom calculated columns, measures, and tables?",
        "options": ["M Code", "DAX", "SQL", "VBA"],
        "answer": "DAX"
    },
    {
        "q": "Which Power BI editor is utilized for data transformation, cleaning, and unpivoting prior to loading data?",
        "options": ["Power Query Editor", "Power View", "Power Pivot", "Power Service"],
        "answer": "Power Query Editor"
    },
    {
        "q": "In Power BI data modeling, what dimensional modeling schema is industry standard for report speed?",
        "options": ["Star Schema", "Snowflake Schema with 10 normalization levels", "Single monolithic flat table", "Circular relation schema"],
        "answer": "Star Schema"
    },
    {
        "q": "Which DAX function alters evaluation context by overriding existing visual filters or applying new conditions?",
        "options": ["CALCULATE()", "FILTER()", "SUMX()", "ALLSELECTED()"],
        "answer": "CALCULATE()"
    },
    {
        "q": "How should you troubleshoot a high latency Power BI report caused by high cardinality in Fact table columns?",
        "options": [
            "Remove unused high cardinality columns, split combined DateTime columns into Date and Time keys, and replace calculated columns with DAX measures",
            "Enable Bidirectional Cross-filtering across all dimensions",
            "Convert all DirectQuery tables to Import mode without aggregations",
            "Replace measures with M Query custom columns"
        ],
        "answer": "Remove unused high cardinality columns, split combined DateTime columns into Date and Time keys, and replace calculated columns with DAX measures"
    }
)

add_skill_qs(
    "Data Analyst", "Statistics",
    {
        "q": "What statistical measure represents the exact middle value of an ordered dataset?",
        "options": ["Mean", "Median", "Mode", "Variance"],
        "answer": "Median"
    },
    {
        "q": "Which statistical hypothesis test compares the means of two independent numerical samples?",
        "options": ["Two-sample t-test", "Chi-Square test", "ANOVA", "Pearson correlation"],
        "answer": "Two-sample t-test"
    },
    {
        "q": "What does a p-value less than alpha (p < 0.05) signify in a hypothesis test?",
        "options": [
            "Reject null hypothesis; statistical evidence indicates significant effect",
            "Accept null hypothesis; no significant difference",
            "Sample size was insufficient",
            "Type II error probability is 100%"
        ],
        "answer": "Reject null hypothesis; statistical evidence indicates significant effect"
    },
    {
        "q": "What theorem states that the sample mean distribution approaches a normal distribution as sample size grows?",
        "options": ["Central Limit Theorem", "Law of Large Numbers", "Bayes' Theorem", "Chebyshev's Inequality"],
        "answer": "Central Limit Theorem"
    },
    {
        "q": "In multiple linear regression, how do you handle severe Multicollinearity (VIF > 10) between independent predictors?",
        "options": [
            "Remove or combine highly collinear predictors or use Ridge/Lasso regularization",
            "Log transform the dependent variable only",
            "Switch to simple K-Means clustering",
            "Increase significance threshold alpha to 0.50"
        ],
        "answer": "Remove or combine highly collinear predictors or use Ridge/Lasso regularization"
    }
)

add_skill_qs(
    "Data Analyst", "Tableau",
    {
        "q": "What type of fields in Tableau hold discrete qualitative attributes like Region or Customer Name?",
        "options": ["Dimension", "Measure", "Parameter", "Set"],
        "answer": "Dimension"
    },
    {
        "q": "What color visual cue represents continuous fields in Tableau worksheet pills?",
        "options": ["Green", "Blue", "Red", "Yellow"],
        "answer": "Green"
    },
    {
        "q": "Which calculation type in Tableau evaluates at a specific level of detail independent of view dimensions?",
        "options": ["Level of Detail (LOD) Expression", "Table Calculation", "Quick Table Calculation", "Row-level expression"],
        "answer": "Level of Detail (LOD) Expression"
    },
    {
        "q": "What distinguishes {FIXED} LOD expressions from {INCLUDE} LOD expressions regarding view context?",
        "options": [
            "{FIXED} evaluates using only specified dimensions ignoring view dimensions, whereas {INCLUDE} adds specified dimensions to view dimensions",
            "{FIXED} respects view filters while {INCLUDE} ignores all filters",
            "{FIXED} only works on measures, {INCLUDE} only on dimensions",
            "Both function identically in filter pipeline"
        ],
        "answer": "{FIXED} evaluates using only specified dimensions ignoring view dimensions, whereas {INCLUDE} adds specified dimensions to view dimensions"
    },
    {
        "q": "When optimizing a enterprise Tableau dashboard linked to live multi-million row database tables, which strategy yields maximum rendering performance?",
        "options": [
            "Create aggregated extracts, replace Quick Filters with Action Filters, and index database join columns",
            "Add floating text boxes and nested table calculations",
            "Convert discrete dimensions into continuous green pills",
            "Disable extract refreshes and compute row-level logic on client side"
        ],
        "answer": "Create aggregated extracts, replace Quick Filters with Action Filters, and index database join columns"
    }
)

# ==========================================
# 2. PYTHON DEVELOPER (7 Skills x 5 = 35 Qs)
# ==========================================

add_skill_qs(
    "Python Developer", "Python",
    {
        "q": "Which Python keyword is used to return a generator from a function instead of a single value?",
        "options": ["return", "yield", "generate", "emit"],
        "answer": "yield"
    },
    {
        "q": "What is the output of `bool([])` in Python?",
        "options": ["True", "False", "None", "Error"],
        "answer": "False"
    },
    {
        "q": "Which standard library module handles asynchronous concurrent I/O loops using async and await syntax?",
        "options": ["threading", "multiprocessing", "asyncio", "concurrent.futures"],
        "answer": "asyncio"
    },
    {
        "q": "In Python, how does the Global Interpreter Lock (GIL) affect multithreaded CPU-bound execution?",
        "options": [
            "The GIL prevents multiple native OS threads from executing Python bytecodes in parallel on multiple CPU cores",
            "The GIL speeds up CPU-bound tasks by auto-vectorizing loops",
            "The GIL restricts file read operations to a single thread",
            "The GIL disables memory garbage collection during loop execution"
        ],
        "answer": "The GIL prevents multiple native OS threads from executing Python bytecodes in parallel on multiple CPU cores"
    },
    {
        "q": "How can you implement a memory-efficient custom object with locked attribute keys in Python to reduce per-instance dict overhead?",
        "options": [
            "Define `__slots__` inside the class definition specifying attribute names as a tuple",
            "Decorate the class with `@classmethod` and `@staticmethod`",
            "Inherit from `collections.defaultdict`",
            "Override the `__getattr__` and `__setattr__` magic methods to raise AttributeError"
        ],
        "answer": "Define `__slots__` inside the class definition specifying attribute names as a tuple"
    }
)

add_skill_qs(
    "Python Developer", "DSA using Python",
    {
        "q": "What is the average time complexity of searching an element in a balanced Binary Search Tree (BST)?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        "answer": "O(log n)"
    },
    {
        "q": "Which data structure operates on a Last-In, First-Out (LIFO) principle?",
        "options": ["Queue", "Stack", "Linked List", "Tree"],
        "answer": "Stack"
    },
    {
        "q": "Which algorithm finds the shortest path from a single source vertex to all other vertices in a weighted graph with non-negative edge weights?",
        "options": ["Dijkstra's Algorithm", "Breadth-First Search (BFS)", "Depth-First Search (DFS)", "Kruskal's Algorithm"],
        "answer": "Dijkstra's Algorithm"
    },
    {
        "q": "How does LRU (Least Recently Used) Cache achieve O(1) time complexity for both `get` and `put` operations in Python?",
        "options": [
            "By combining a Hash Map (dict) with a Doubly Linked List",
            "By using a Min-Heap combined with a Binary Search Tree",
            "By sorting an array after every insertion",
            "By using recursive Memoization with Python set"
        ],
        "answer": "By combining a Hash Map (dict) with a Doubly Linked List"
    },
    {
        "q": "When solving the 0/1 Knapsack Problem dynamically, why is top-down memoization preferred over naive recursion?",
        "options": [
            "It avoids redundant subproblem calculations by storing intermediate results, reducing time complexity from exponential O(2^n) to pseudo-polynomial O(n*W)",
            "It reduces spatial complexity to O(1) guaranteed",
            "It converts non-linear constraints into linear equations",
            "It eliminates greedy search failure modes"
        ],
        "answer": "It avoids redundant subproblem calculations by storing intermediate results, reducing time complexity from exponential O(2^n) to pseudo-polynomial O(n*W)"
    }
)

add_skill_qs(
    "Python Developer", "OOPs using Python",
    {
        "q": "Which Object-Oriented principle allows a child class to inherit attributes and methods from a parent class?",
        "options": ["Encapsulation", "Inheritance", "Polymorphism", "Abstraction"],
        "answer": "Inheritance"
    },
    {
        "q": "Which magic method in Python initializes newly created object instances?",
        "options": ["__new__", "__init__", "__str__", "__call__"],
        "answer": "__init__"
    },
    {
        "q": "What decorator creates a read-only getter attribute in a Python class?",
        "options": ["@staticmethod", "@classmethod", "@property", "@abstractmethod"],
        "answer": "@property"
    },
    {
        "q": "In Python multiple inheritance, how does the Method Resolution Order (MRO) resolve method calls using `super()`?",
        "options": [
            "It follows the C3 Linearization algorithm to determine a deterministic order of base classes",
            "It checks base classes in random order at runtime",
            "It always prioritizes the last defined parent class",
            "It raises an AmbiguityError whenever two parents define the same method"
        ],
        "answer": "It follows the C3 Linearization algorithm to determine a deterministic order of base classes"
    },
    {
        "q": "How does the SOLID 'Dependency Inversion Principle' apply to Python backend class architectures?",
        "options": [
            "High-level modules should not depend on low-level concrete classes; both should depend on abstractions (interfaces or Abstract Base Classes)",
            "Classes should be open for modification and closed for extension",
            "Objects should be initialized using singleton magic methods only",
            "Subclasses must throw errors if they modify inherited methods"
        ],
        "answer": "High-level modules should not depend on low-level concrete classes; both should depend on abstractions (interfaces or Abstract Base Classes)"
    }
)

add_skill_qs(
    "Python Developer", "SQL",
    {
        "q": "Which SQL statement adds new data rows to an existing table?",
        "options": ["INSERT INTO", "UPDATE", "ADD ROW", "APPEND"],
        "answer": "INSERT INTO"
    },
    {
        "q": "What is the purpose of an INDEX on a SQL database column?",
        "options": [
            "To speed up data retrieval queries at the cost of additional write overhead",
            "To encrypt column values for security",
            "To format text strings into uppercase",
            "To automatically delete duplicate rows"
        ],
        "answer": "To speed up data retrieval queries at the cost of additional write overhead"
    },
    {
        "q": "What SQL clause handles transactional atomic operations by persisting changes to disk?",
        "options": ["COMMIT", "ROLLBACK", "SAVEPOINT", "CHECKPOINT"],
        "answer": "COMMIT"
    },
    {
        "q": "In SQL database isolation levels, what concurrency anomaly does `SERIALIZABLE` isolation prevent that `REPEATABLE READ` allows?",
        "options": [
            "Phantom Reads",
            "Dirty Reads",
            "Non-Repeatable Reads",
            "Lost Updates"
        ],
        "answer": "Phantom Reads"
    },
    {
        "q": "When optimizing a transactional backend experiencing deadlock errors under high concurrent writes, what remediation is most effective?",
        "options": [
            "Access tables and rows in a consistent deterministic order across transactions and keep transactions short",
            "Set isolation level to READ UNCOMMITTED globally",
            "Disable database foreign key checks permanently",
            "Replace primary key B-Trees with Hash indexes on auto-increment columns"
        ],
        "answer": "Access tables and rows in a consistent deterministic order across transactions and keep transactions short"
    }
)

add_skill_qs(
    "Python Developer", "Flask",
    {
        "q": "Which decorator in Flask binds a view function to an HTTP URL path?",
        "options": ["@app.route()", "@app.bind()", "@app.path()", "@app.url()"],
        "answer": "@app.route()"
    },
    {
        "q": "How do you retrieve JSON payload data sent in a POST request within a Flask view function?",
        "options": ["request.get_json()", "request.form[]", "request.args.get()", "request.body"],
        "answer": "request.get_json()"
    },
    {
        "q": "What feature in Flask allows modular structuring of large applications into smaller logical components?",
        "options": ["Blueprints", "Modules", "Routes", "Templates"],
        "answer": "Blueprints"
    },
    {
        "q": "In Flask, what object proxy allows accessing thread-safe request context data without passing request parameters explicitly?",
        "options": [
            "LocalProxy object (`request`, `g`) tied to current thread/async task context",
            "Global static dictionary `flask.globals`",
            "Database ORM session wrapper",
            "WSGI application environment object"
        ],
        "answer": "LocalProxy object (`request`, `g`) tied to current thread/async task context"
    },
    {
        "q": "When deploying a production Flask app handling 10,000 concurrent requests, what web server deployment architecture is recommended?",
        "options": [
            "Gunicorn / uWSGI behind Nginx reverse proxy with gevent or async worker class",
            "Run built-in `app.run(debug=True, host='0.0.0.0')` development server",
            "Wrap Flask inside single-threaded CGI script executed by Apache",
            "Execute Flask view functions directly via cron jobs"
        ],
        "answer": "Gunicorn / uWSGI behind Nginx reverse proxy with gevent or async worker class"
    }
)

add_skill_qs(
    "Python Developer", "Django",
    {
        "q": "Which command creates database schema migration files based on changes detected in `models.py`?",
        "options": ["python manage.py makemigrations", "python manage.py migrate", "python manage.py syncdb", "python manage.py buildmodels"],
        "answer": "python manage.py makemigrations"
    },
    {
        "q": "Which pattern architecture does Django natively follow?",
        "options": ["MVT (Model-View-Template)", "MVC (Model-View-Controller)", "MVVM (Model-View-ViewModel)", "Flux Architecture"],
        "answer": "MVT (Model-View-Template)"
    },
    {
        "q": "How do you prevent the N+1 query problem when fetching related foreign key objects in Django ORM?",
        "options": [
            "Use `select_related()` for single foreign keys and `prefetch_related()` for many-to-many/many-to-one relations",
            "Loop over QuerySet manually using `values_list()`",
            "Set `db_index=True` on every model field",
            "Disable Django ORM caching"
        ],
        "answer": "Use `select_related()` for single foreign keys and `prefetch_related()` for many-to-many/many-to-one relations"
    },
    {
        "q": "How does Django's built-in CSRF middleware protect forms against Cross-Site Request Forgery?",
        "options": [
            "It injects a secret cryptographically signed token into user sessions and verifies matching token header in POST requests",
            "It blocks requests coming from external IP addresses",
            "It encrypts database passwords before session storage",
            "It limits request rate to 10 requests per minute"
        ],
        "answer": "It injects a secret cryptographically signed token into user sessions and verifies matching token header in POST requests"
    },
    {
        "q": "When scaling a multi-tenant Django application with asynchronous long-running background tasks, what infrastructure stack is best suited?",
        "options": [
            "Celery with Redis/RabbitMQ message broker combined with Django Channels for WebSocket push notifications",
            "Synchronous threads inside `views.py` using `threading.Thread`",
            "Database triggers executing raw SQL stored procedures",
            "Custom infinite while loops inside Django middleware"
        ],
        "answer": "Celery with Redis/RabbitMQ message broker combined with Django Channels for WebSocket push notifications"
    }
)

add_skill_qs(
    "Python Developer", "REST API",
    {
        "q": "Which HTTP method is idempotent and primarily used to update an existing resource completely?",
        "options": ["POST", "PUT", "GET", "DELETE"],
        "answer": "PUT"
    },
    {
        "q": "What HTTP response status code represents a successful resource creation ('Created')?",
        "options": ["200 OK", "201 Created", "400 Bad Request", "404 Not Found"],
        "answer": "201 Created"
    },
    {
        "q": "What token authentication standard stores cryptographically signed JSON payloads sent in HTTP Authorization headers?",
        "options": ["JWT (JSON Web Token)", "Basic Auth", "API Key in query string", "Cookies only"],
        "answer": "JWT (JSON Web Token)"
    },
    {
        "q": "What design strategy guarantees API backward compatibility when breaking endpoint schema changes are introduced?",
        "options": [
            "API Versioning via URL paths (e.g., /api/v1/resource vs /api/v2/resource) or custom Accept headers",
            "Modifying existing JSON keys directly in production",
            "Returning HTTP 500 error code on legacy requests",
            "Overwriting old endpoints with GraphQL schemas without notice"
        ],
        "answer": "API Versioning via URL paths (e.g., /api/v1/resource vs /api/v2/resource) or custom Accept headers"
    },
    {
        "q": "How do you defend a public microservices REST API against Denial of Service (DoS) and brute-force key attacks?",
        "options": [
            "Implement Rate Limiting using Token Bucket / Leaky Bucket algorithms via API Gateway (e.g., Kong/Nginx) combined with OAuth2 scope validation",
            "Disable HTTP caching headers on all endpoints",
            "Allow infinite CORS origins across all endpoints",
            "Enforce synchronous database locking on every GET request"
        ],
        "answer": "Implement Rate Limiting using Token Bucket / Leaky Bucket algorithms via API Gateway (e.g., Kong/Nginx) combined with OAuth2 scope validation"
    }
)

# ==========================================
# 3. FULL STACK DEVELOPER (8 Skills x 5 = 40 Qs)
# ==========================================

add_skill_qs(
    "Full Stack Developer", "HTML",
    {
        "q": "Which HTML5 semantic element is used to define navigation links?",
        "options": ["<nav>", "<header>", "<section>", "<aside>"],
        "answer": "<nav>"
    },
    {
        "q": "Which HTML attribute specifies alternative text for an image if it cannot be displayed?",
        "options": ["alt", "title", "src", "description"],
        "answer": "alt"
    },
    {
        "q": "What is the primary function of WAI-ARIA attributes (e.g., `role`, `aria-label`) in HTML5?",
        "options": [
            "To enhance accessibility for assistive technologies like screen readers",
            "To apply CSS styles dynamically without stylesheets",
            "To speed up HTML parsing in modern browser engines",
            "To validate form inputs on server side"
        ],
        "answer": "To enhance accessibility for assistive technologies like screen readers"
    },
    {
        "q": "What happens when `<script defer>` is placed in the HTML `<head>` section?",
        "options": [
            "The script downloads asynchronously in parallel with HTML parsing and executes after HTML DOM construction completes",
            "The script executes immediately, blocking DOM parsing",
            "The script only executes when triggered by inline onclick events",
            "The script is skipped entirely unless manually called"
        ],
        "answer": "The script downloads asynchronously in parallel with HTML parsing and executes after HTML DOM construction completes"
    },
    {
        "q": "How does Shadow DOM encapsulation protect Web Components in HTML modern applications?",
        "options": [
            "It isolates DOM subtree elements and CSS styles so outer document styles and scripts cannot leak in or affect internal component structure",
            "It hides HTML source code from browser developer tools",
            "It encrypts DOM nodes before sending to server",
            "It automatically converts HTML tags into canvas graphics"
        ],
        "answer": "It isolates DOM subtree elements and CSS styles so outer document styles and scripts cannot leak in or affect internal component structure"
    }
)

add_skill_qs(
    "Full Stack Developer", "CSS",
    {
        "q": "Which CSS property changes the text color of an HTML element?",
        "options": ["color", "text-color", "font-color", "background-color"],
        "answer": "color"
    },
    {
        "q": "Which CSS layout module provides one-dimensional alignment for rows or columns?",
        "options": ["Flexbox", "CSS Grid", "Float", "Table"],
        "answer": "Flexbox"
    },
    {
        "q": "How does CSS Specificity calculate precedence between selectors?",
        "options": [
            "Inline styles (1000) > IDs (100) > Classes/Attributes/Pseudo-classes (10) > Elements/Pseudo-elements (1)",
            "Elements (100) > Classes (10) > IDs (1)",
            "Order of definition in CSS file is the only rule",
            "Alphabetical order of class names"
        ],
        "answer": "Inline styles (1000) > IDs (100) > Classes/Attributes/Pseudo-classes (10) > Elements/Pseudo-elements (1)"
    },
    {
        "q": "What CSS rule creates responsive layouts based on device viewport dimensions or features?",
        "options": ["@media query", "@container query", "@import", "@supports"],
        "answer": "@media query"
    },
    {
        "q": "How do browser hardware acceleration and `will-change: transform` prevent layout thrashing during animations?",
        "options": [
            "They offload element rendering onto GPU composite layers, avoiding expensive Reflow (Layout) and Repaint cycles on the CPU main thread",
            "They disable CSS Box Model calculations permanently",
            "They force synchronous DOM recalculations before repaint",
            "They convert vector animations into animated GIF images"
        ],
        "answer": "They offload element rendering onto GPU composite layers, avoiding expensive Reflow (Layout) and Repaint cycles on the CPU main thread"
    }
)

add_skill_qs(
    "Full Stack Developer", "JavaScript",
    {
        "q": "Which keyword declares a block-scoped variable in JavaScript that cannot be re-declared in the same scope?",
        "options": ["let", "var", "global", "define"],
        "answer": "let"
    },
    {
        "q": "What is the result of `typeof null` in JavaScript?",
        "options": ["'object'", "'null'", "'undefined'", "'boolean'"],
        "answer": "'object'"
    },
    {
        "q": "What feature allows inner functions to access variables from their enclosing lexical scope even after parent function execution completes?",
        "options": ["Closure", "Hoisting", "Callback", "Prototype Chain"],
        "answer": "Closure"
    },
    {
        "q": "How does the JavaScript Event Loop coordinate execution between Microtasks and Macrotasks?",
        "options": [
            "The Microtask queue (Promises, queueMicrotask) is completely drained after every task before processing the next Macrotask (setTimeout, setInterval)",
            "Macrotasks are executed with higher priority than Microtasks",
            "Microtasks and Macrotasks run in parallel threads on multi-core CPUs",
            "The Event Loop randomly picks tasks from both queues"
        ],
        "answer": "The Microtask queue (Promises, queueMicrotask) is completely drained after every task before processing the next Macrotask (setTimeout, setInterval)"
    },
    {
        "q": "How can you prevent memory leaks caused by detached DOM nodes and uncleared event listeners in single-page JavaScript web apps?",
        "options": [
            "Remove event listeners explicitly on component unmount and use `WeakMap` or `WeakSet` for object references",
            "Set all variables to global `window` scope",
            "Use `eval()` inside interval timers",
            "Disable browser garbage collection using `console.clear()`"
        ],
        "answer": "Remove event listeners explicitly on component unmount and use `WeakMap` or `WeakSet` for object references"
    }
)

add_skill_qs(
    "Full Stack Developer", "React.js",
    {
        "q": "Which React Hook manages state inside functional components?",
        "options": ["useState", "useEffect", "useContext", "useRef"],
        "answer": "useState"
    },
    {
        "q": "What syntax extension allows writing HTML-like markup inside JavaScript React components?",
        "options": ["JSX", "TSX", "HTML5", "ECMAScript Template"],
        "answer": "JSX"
    },
    {
        "q": "Which Hook performs side effects (fetching data, subscribing to timers) in functional React components?",
        "options": ["useEffect", "useState", "useMemo", "useCallback"],
        "answer": "useEffect"
    },
    {
        "q": "Why is passing `key` props crucial when rendering dynamic arrays of components in React?",
        "options": [
            "It gives React a stable identity for items so Virtual DOM diffing can accurately reorder, insert, or remove nodes without re-rendering unchanged children",
            "It applies CSS styling to list items",
            "It encrypts list element state",
            "It binds event handlers to list items automatically"
        ],
        "answer": "It gives React a stable identity for items so Virtual DOM diffing can accurately reorder, insert, or remove nodes without re-rendering unchanged children"
    },
    {
        "q": "How do `useMemo` and `useCallback` prevent unnecessary component re-renders in large React render trees?",
        "options": [
            "useMemo memoizes calculated values, and useCallback memoizes function instances across re-renders when dependencies haven't changed",
            "useMemo modifies DOM elements directly skipping React Virtual DOM",
            "useCallback forces immediate synchronous component mounts",
            "Both hooks convert functional components into class components automatically"
        ],
        "answer": "useMemo memoizes calculated values, and useCallback memoizes function instances across re-renders when dependencies haven't changed"
    }
)

add_skill_qs(
    "Full Stack Developer", "Python",
    {
        "q": "Which keyword defines a function in Python?",
        "options": ["def", "function", "func", "define"],
        "answer": "def"
    },
    {
        "q": "What is the result of `len({'a': 1, 'b': 2})`?",
        "options": ["2", "4", "1", "Error"],
        "answer": "2"
    },
    {
        "q": "Which built-in Python function turns an iterable into pairs of `(index, element)`?",
        "options": ["enumerate()", "zip()", "map()", "filter()"],
        "answer": "enumerate()"
    },
    {
        "q": "What is the key difference between deep copy and shallow copy in Python's `copy` module?",
        "options": [
            "Shallow copy constructs a new object inserting references to child objects; deep copy recursively copies child objects",
            "Deep copy copies references only; shallow copy copies recursively",
            "Shallow copy converts objects to JSON strings",
            "Deep copy works only on primitive numeric data types"
        ],
        "answer": "Shallow copy constructs a new object inserting references to child objects; deep copy recursively copies child objects"
    },
    {
        "q": "How do context managers (`with` statement) implement resource allocation and cleanup using magic methods in Python?",
        "options": [
            "They execute `__enter__()` before block entry and guarantee `__exit__()` execution upon block exit even if exceptions are raised",
            "They run `__init__()` and `__del__()` asynchronously on a background thread",
            "They wrap functions in `try...except` blocks automatically",
            "They disable garbage collection while inside the context block"
        ],
        "answer": "They execute `__enter__()` before block entry and guarantee `__exit__()` execution upon block exit even if exceptions are raised"
    }
)

add_skill_qs(
    "Full Stack Developer", "SQL",
    {
        "q": "Which SQL statement is used to remove a table structure and all its data permanently from a database?",
        "options": ["DROP TABLE", "DELETE FROM", "TRUNCATE TABLE", "REMOVE TABLE"],
        "answer": "DROP TABLE"
    },
    {
        "q": "What does the `GROUP BY` clause do in a SQL query?",
        "options": [
            "Groups rows sharing identical column values into summary rows",
            "Sorts query output alphabetically",
            "Joins two foreign tables on a primary key",
            "Enforces unique constraints on columns"
        ],
        "answer": "Groups rows sharing identical column values into summary rows"
    },
    {
        "q": "What SQL constraint ensures that all values in a column are unique and non-null?",
        "options": ["PRIMARY KEY", "FOREIGN KEY", "CHECK", "DEFAULT"],
        "answer": "PRIMARY KEY"
    },
    {
        "q": "What is database Normalization (1NF, 2NF, 3NF) designed to achieve?",
        "options": [
            "Eliminate data redundancy and prevent update/insertion anomalies by organizing fields into logical normalized tables",
            "Increase query response time by duplicating data across tables",
            "Encrypt sensitive customer fields automatically",
            "Convert relational tables into NoSQL JSON documents"
        ],
        "answer": "Eliminate data redundancy and prevent update/insertion anomalies by organizing fields into logical normalized tables"
    },
    {
        "q": "How does SQL Query Optimizer use Index Scans vs Index Seeks when executing filtering queries?",
        "options": [
            "Index Seek navigates B-Tree nodes directly for specific keys (O(log N)), while Index Scan traverses the entire index leaf chain (O(N))",
            "Index Scan is always faster than Index Seek",
            "Index Seek is used only for text wildcard searches",
            "Index Scan requires full table locks on write operations"
        ],
        "answer": "Index Seek navigates B-Tree nodes directly for specific keys (O(log N)), while Index Scan traverses the entire index leaf chain (O(N))"
    }
)

add_skill_qs(
    "Full Stack Developer", "REST API",
    {
        "q": "Which HTTP header specifies the format of the data being sent in a request body (e.g. `application/json`)?",
        "options": ["Content-Type", "Accept", "Authorization", "User-Agent"],
        "answer": "Content-Type"
    },
    {
        "q": "What does HTTP status code 403 Forbidden indicate?",
        "options": [
            "The client is authenticated but lacks required permission to access the resource",
            "The requested resource was not found on the server",
            "The request payload format was invalid JSON",
            "The server encountered an unhandled exception"
        ],
        "answer": "The client is authenticated but lacks required permission to access the resource"
    },
    {
        "q": "What mechanism allows servers to specify which external origin domains can fetch resources via cross-site browser requests?",
        "options": ["CORS (Cross-Origin Resource Sharing)", "CSRF Token", "Content Security Policy (CSP)", "SSL Pinning"],
        "answer": "CORS (Cross-Origin Resource Sharing)"
    },
    {
        "q": "In REST API design, what is an 'Idempotent' method?",
        "options": [
            "A method where making multiple identical requests yields the exact same server state result as a single request (e.g., PUT, DELETE, GET)",
            "A method that can only be called once per IP address",
            "A method that returns encrypted responses",
            "A method that requires WebSocket connections"
        ],
        "answer": "A method where making multiple identical requests yields the exact same server state result as a single request (e.g., PUT, DELETE, GET)"
    },
    {
        "q": "How do API Gateways handle Authentication Offloading and Microservice Rate Limiting?",
        "options": [
            "They inspect incoming JWT tokens at the gateway boundary, reject invalid requests early, and rate-limit IP/Key buckets before proxying to backend services",
            "They pass all unvalidated traffic directly to microservices to evaluate auth",
            "They convert incoming REST HTTP calls into SQL queries directly",
            "They store user session states in browser cookies"
        ],
        "answer": "They inspect incoming JWT tokens at the gateway boundary, reject invalid requests early, and rate-limit IP/Key buckets before proxying to backend services"
    }
)

add_skill_qs(
    "Full Stack Developer", "Django",
    {
        "q": "Which Django file defines data models and database fields?",
        "options": ["models.py", "views.py", "urls.py", "admin.py"],
        "answer": "models.py"
    },
    {
        "q": "Which Django command applies pending migrations to update the database schema?",
        "options": ["python manage.py migrate", "python manage.py makemigrations", "python manage.py runserver", "python manage.py collectstatic"],
        "answer": "python manage.py migrate"
    },
    {
        "q": "What tool in Django handles user authentication, groups, permissions, and password hashing out of the box?",
        "options": ["django.contrib.auth", "django.contrib.admin", "django.contrib.sessions", "django.contrib.messages"],
        "answer": "django.contrib.auth"
    },
    {
        "q": "How do custom Django Middleware classes process requests and responses?",
        "options": [
            "They wrap request processing in a chain of callable methods (`process_request`, `process_response`) executed in order before and after view execution",
            "They replace models.py database definitions",
            "They compile HTML templates into JavaScript bytecode",
            "They run as external background processes on separate servers"
        ],
        "answer": "They wrap request processing in a chain of callable methods (`process_request`, `process_response`) executed in order before and after view execution"
    },
    {
        "q": "When deploying Django REST Framework (DRF) alongside React frontends, how should token refreshing be securely managed?",
        "options": [
            "Store short-lived access tokens in memory and long-lived refresh tokens in httpOnly, Secure, SameSite cookies",
            "Store refresh tokens in localStorage as plaintext strings",
            "Include database user passwords inside JWT headers",
            "Disable token expiration entirely"
        ],
        "answer": "Store short-lived access tokens in memory and long-lived refresh tokens in httpOnly, Secure, SameSite cookies"
    }
)

# ==========================================
# 4. AI/ML ENGINEER (9 Skills x 5 = 45 Qs)
# ==========================================

add_skill_qs(
    "AI/ML Engineer", "Python",
    {
        "q": "Which numerical library provides multi-dimensional array objects (ndarray) in Python?",
        "options": ["NumPy", "Pandas", "Scikit-Learn", "Matplotlib"],
        "answer": "NumPy"
    },
    {
        "q": "What is Vectorization in NumPy?",
        "options": [
            "Executing operations on entire arrays in optimized C code without explicit Python for-loops",
            "Converting images into vector graphics format",
            "Replacing floating-point numbers with integer vectors",
            "Sorting arrays using multithreaded queues"
        ],
        "answer": "Executing operations on entire arrays in optimized C code without explicit Python for-loops"
    },
    {
        "q": "What mechanism in NumPy allows array arithmetic operations between arrays of different shapes?",
        "options": ["Broadcasting", "Reshaping", "Slicing", "Concatenation"],
        "answer": "Broadcasting"
    },
    {
        "q": "How does Python handle memory management for large arrays using memory views (`memoryview`)?",
        "options": [
            "It allows slicing and buffer access without copying underlying memory bytes",
            "It compresses numeric arrays into zip archives in RAM",
            "It offloads memory onto hard drive swap partitions",
            "It converts Python integers to strings"
        ],
        "answer": "It allows slicing and buffer access without copying underlying memory bytes"
    },
    {
        "q": "In deep learning frameworks like PyTorch, how does automatic differentiation (`autograd`) track operations on Tensors?",
        "options": [
            "By dynamically constructing a Directed Acyclic Graph (DAG) of computations where leaves are input tensors and root is loss",
            "By compiling Python code into C++ headers before runtime",
            "By calculating numerical derivatives using finite difference approximation at every step",
            "By storing matrix values in disk-backed SQL tables"
        ],
        "answer": "By dynamically constructing a Directed Acyclic Graph (DAG) of computations where leaves are input tensors and root is loss"
    }
)

add_skill_qs(
    "AI/ML Engineer", "C++",
    {
        "q": "Which feature in C++ allows automatic memory cleanup when an object goes out of scope?",
        "options": ["Destructors", "Constructors", "Smart Pointers", "Garbage Collector"],
        "answer": "Destructors"
    },
    {
        "q": "Which C++ Standard Template Library (STL) container represents a dynamic array that automatically resizes?",
        "options": ["std::vector", "std::list", "std::array", "std::set"],
        "answer": "std::vector"
    },
    {
        "q": "Which modern C++ smart pointer enforces exclusive single ownership of a dynamically allocated resource?",
        "options": ["std::unique_ptr", "std::shared_ptr", "std::weak_ptr", "std::auto_ptr"],
        "answer": "std::unique_ptr"
    },
    {
        "q": "What feature introduced in C++11 enables moving resources from temporary objects without deep copying?",
        "options": [
            "Move Semantics and Rvalue References (`&&`)",
            "Virtual Function Overriding",
            "Template Specialization",
            "Friend Classes"
        ],
        "answer": "Move Semantics and Rvalue References (`&&`)"
    },
    {
        "q": "When optimizing tensor computation kernels in C++ for machine learning inference, what low-level technique maximizes SIMD hardware utilization?",
        "options": [
            "Using SIMD intrinsics (AVX-512 / NEON) combined with explicit memory alignment (`alignas`) and loop unrolling",
            "Replacing pointer arithmetic with recursive virtual method calls",
            "Allocating all matrices on heap using `malloc()` inside loops",
            "Wrapping C++ loops inside Python string execution calls"
        ],
        "answer": "Using SIMD intrinsics (AVX-512 / NEON) combined with explicit memory alignment (`alignas`) and loop unrolling"
    }
)

add_skill_qs(
    "AI/ML Engineer", "C",
    {
        "q": "Which standard library function dynamically allocates memory on the heap in C?",
        "options": ["malloc()", "alloc()", "new()", "create()"],
        "answer": "malloc()"
    },
    {
        "q": "What operator is used to dereference a pointer in C?",
        "options": ["*", "&", "->", "."],
        "answer": "*"
    },
    {
        "q": "How do you free dynamically allocated memory in C to prevent memory leaks?",
        "options": ["free(ptr)", "delete(ptr)", "dealloc(ptr)", "clear(ptr)"],
        "answer": "free(ptr)"
    },
    {
        "q": "What security vulnerability occurs when writing data past the allocated length of a buffer in C?",
        "options": [
            "Buffer Overflow",
            "Null Pointer Dereference",
            "Use-After-Free",
            "Format String Bug"
        ],
        "answer": "Buffer Overflow"
    },
    {
        "q": "In high-performance embedded AI runtimes, how does Cache Line Padding in C structures prevent 'False Sharing' on multi-core CPUs?",
        "options": [
            "By aligning thread-specific variables on separate cache line boundaries (e.g., 64 bytes) to avoid invalidating CPU L1/L2 caches",
            "By disabling CPU hardware caches entirely",
            "By storing all struct attributes as void pointers",
            "By converting C structs to packed bitfields"
        ],
        "answer": "By aligning thread-specific variables on separate cache line boundaries (e.g., 64 bytes) to avoid invalidating CPU L1/L2 caches"
    }
)

add_skill_qs(
    "AI/ML Engineer", "Java",
    {
        "q": "Which keyword is used to inherit a class in Java?",
        "options": ["extends", "implements", "inherits", "super"],
        "answer": "extends"
    },
    {
        "q": "Which memory area in JVM stores Java object instances?",
        "options": ["Heap Memory", "Stack Memory", "Metaspace", "Program Counter Register"],
        "answer": "Heap Memory"
    },
    {
        "q": "Which Java 8 feature allows functional style processing of sequences of elements?",
        "options": ["Stream API", "Reflection API", "Generics", "Serialization"],
        "answer": "Stream API"
    },
    {
        "q": "How does the Java Garbage Collector (GC) identify unreachable objects eligible for collection?",
        "options": [
            "By tracing object reference graphs starting from Garbage Collection (GC) Roots",
            "By keeping a reference counter on each object",
            "By checking if objects are older than 10 seconds",
            "By scanning disk storage logs"
        ],
        "answer": "By tracing object reference graphs starting from Garbage Collection (GC) Roots"
    },
    {
        "q": "In high-throughput enterprise ML model scoring services in Java, how do you mitigate Garbage Collection latency spikes (Stop-The-World pauses)?",
        "options": [
            "Use low-latency garbage collectors like ZGC / Shenandoah and reuse object pools for request tensors",
            "Increase thread stack size to 1GB",
            "Disable JVM Bytecode verification",
            "Call `System.gc()` inside every HTTP controller handle method"
        ],
        "answer": "Use low-latency garbage collectors like ZGC / Shenandoah and reuse object pools for request tensors"
    }
)

add_skill_qs(
    "AI/ML Engineer", "Machine Learning",
    {
        "q": "Which machine learning paradigm uses labeled training data to predict outcomes?",
        "options": ["Supervised Learning", "Unsupervised Learning", "Reinforcement Learning", "Self-Supervised Learning"],
        "answer": "Supervised Learning"
    },
    {
        "q": "What problem occurs when a model performs exceptionally well on training data but poorly on unseen test data?",
        "options": ["Overfitting", "Underfitting", "High Bias", "Data Leakage"],
        "answer": "Overfitting"
    },
    {
        "q": "Which metric evaluates classification model performance by harmonic mean of Precision and Recall?",
        "options": ["F1-Score", "Accuracy", "Mean Squared Error (MSE)", "R-Squared"],
        "answer": "F1-Score"
    },
    {
        "q": "How does Gradient Boosting (e.g., XGBoost) build ensemble decision trees?",
        "options": [
            "It builds decision trees sequentially, where each new tree fits on the residual errors (pseudo-residuals) of the previous models",
            "It builds independent trees in parallel and averages their predictions",
            "It randomly drops tree nodes during evaluation",
            "It calculates linear weights using matrix inversion"
        ],
        "answer": "It builds decision trees sequentially, where each new tree fits on the residual errors (pseudo-residuals) of the previous models"
    },
    {
        "q": "How do L1 (Lasso) and L2 (Ridge) Regularization prevent overfitting, and how do their penalty terms differ in feature selection?",
        "options": [
            "L1 adds absolute weight penalty forcing coefficients to zero (feature selection); L2 adds squared weight penalty shrinking weights towards zero",
            "L2 eliminates features completely while L1 keeps all features",
            "L1 increases model variance while L2 increases model bias",
            "Both penalties work only on decision tree leaf nodes"
        ],
        "answer": "L1 adds absolute weight penalty forcing coefficients to zero (feature selection); L2 adds squared weight penalty shrinking weights towards zero"
    }
)

add_skill_qs(
    "AI/ML Engineer", "Deep Learning",
    {
        "q": "What non-linear activation function computes `f(x) = max(0, x)` in neural networks?",
        "options": ["ReLU", "Sigmoid", "Tanh", "Softmax"],
        "answer": "ReLU"
    },
    {
        "q": "Which neural network architecture is tailored for grid-like spatial data like images?",
        "options": ["Convolutional Neural Network (CNN)", "Recurrent Neural Network (RNN)", "Multi-Layer Perceptron (MLP)", "Autoencoder"],
        "answer": "Convolutional Neural Network (CNN)"
    },
    {
        "q": "What algorithm computes loss gradients with respect to neural network weights using the chain rule?",
        "options": ["Backpropagation", "Forward Pass", "Gradient Ascent", "Convolution"],
        "answer": "Backpropagation"
    },
    {
        "q": "What mechanism in Transformer models (e.g., BERT, GPT) enables modeling relationships between words regardless of positional distance?",
        "options": [
            "Self-Attention Mechanism (Scaled Dot-Product Attention)",
            "Recurrent Gated Hidden Units",
            "Max Pooling Layers",
            "Batch Normalization"
        ],
        "answer": "Self-Attention Mechanism (Scaled Dot-Product Attention)"
    },
    {
        "q": "When training deep neural networks (100+ layers), how do Vanishing/Exploding Gradients occur and how do Residual Connections (ResNets) mitigate them?",
        "options": [
            "Gradients exponentially shrink/explode during backprop across deep layers; Residual skip connections create identity paths allowing gradients to flow directly",
            "Vanishing gradients happen when learning rate is too high; skip connections double learning rate",
            "Exploding gradients crash GPU memory; skip connections offload activations to CPU",
            "Skip connections replace matrix multiplications with addition"
        ],
        "answer": "Gradients exponentially shrink/explode during backprop across deep layers; Residual skip connections create identity paths allowing gradients to flow directly"
    }
)

add_skill_qs(
    "AI/ML Engineer", "Statistics",
    {
        "q": "What is the probability of an event given that another event has already occurred?",
        "options": ["Conditional Probability", "Joint Probability", "Marginal Probability", "Prior Probability"],
        "answer": "Conditional Probability"
    },
    {
        "q": "Which rule calculates posterior probability P(A|B) using prior probability P(A) and likelihood P(B|A)?",
        "options": ["Bayes' Theorem", "Central Limit Theorem", "Markov's Inequality", "Law of Total Probability"],
        "answer": "Bayes' Theorem"
    },
    {
        "q": "Which probability distribution models the number of events occurring in a fixed interval of time/space given a constant average rate?",
        "options": ["Poisson Distribution", "Binomial Distribution", "Normal Distribution", "Uniform Distribution"],
        "answer": "Poisson Distribution"
    },
    {
        "q": "What parameter estimation method finds parameter values that maximize the likelihood of observing the given sample data?",
        "options": [
            "Maximum Likelihood Estimation (MLE)",
            "Ordinary Least Squares (OLS)",
            "Gradient Descent",
            "Markov Chain Monte Carlo (MCMC)"
        ],
        "answer": "Maximum Likelihood Estimation (MLE)"
    },
    {
        "q": "When conducting A/B testing with multiple concurrent metrics, how does the Bonferroni Correction prevent inflation of Type I error (False Positive rate)?",
        "options": [
            "It adjusts the significance threshold alpha by dividing it by the total number of statistical hypothesis tests performed",
            "It increases sample size requirements by 10x",
            "It replaces t-tests with Chi-square goodness-of-fit tests",
            "It sets p-value cutoff to 0.50"
        ],
        "answer": "It adjusts the significance threshold alpha by dividing it by the total number of statistical hypothesis tests performed"
    }
)

add_skill_qs(
    "AI/ML Engineer", "Linear Algebra",
    {
        "q": "What is the result of multiplying an N x M matrix by an M x P matrix?",
        "options": ["N x P matrix", "M x M matrix", "N x N matrix", "P x N matrix"],
        "answer": "N x P matrix"
    },
    {
        "q": "What vector satisfies the equation `A * v = lambda * v` for a square matrix A?",
        "options": ["Eigenvector", "Unit vector", "Orthogonal vector", "Gradient vector"],
        "answer": "Eigenvector"
    },
    {
        "q": "What matrix factorization technique decomposes any M x N real matrix into `U * Sigma * V^T`?",
        "options": ["Singular Value Decomposition (SVD)", "LU Decomposition", "Cholesky Decomposition", "QR Decomposition"],
        "answer": "Singular Value Decomposition (SVD)"
    },
    {
        "q": "How does Principal Component Analysis (PCA) utilize Eigenvectors of the covariance matrix for dimensionality reduction?",
        "options": [
            "Eigenvectors specify orthogonal directions of maximum variance, and corresponding Eigenvalues quantify variance magnitude along those axes",
            "Eigenvectors invert matrix values to eliminate negative numbers",
            "Eigenvectors convert dense matrices into sparse diagonal matrices",
            "Eigenvectors project non-linear data into infinite dimensional space"
        ],
        "answer": "Eigenvectors specify orthogonal directions of maximum variance, and corresponding Eigenvalues quantify variance magnitude along those axes"
    },
    {
        "q": "Why is the condition number of a matrix crucial in solving linear systems `A * x = b`, and how does an ill-conditioned matrix affect ML model optimization?",
        "options": [
            "High condition number means small perturbations in input b cause massive errors in solution x, causing severe gradient instability during optimization",
            "Low condition number causes matrix multiplication to throw division-by-zero errors",
            "Ill-conditioned matrices cannot be transposed",
            "Condition number measures the total RAM occupied by matrix entries"
        ],
        "answer": "High condition number means small perturbations in input b cause massive errors in solution x, causing severe gradient instability during optimization"
    }
)

add_skill_qs(
    "AI/ML Engineer", "Big Data",
    {
        "q": "What distributed file system stores big data across commodity hardware clusters in Apache Hadoop?",
        "options": ["HDFS", "S3", "NFS", "GFS"],
        "answer": "HDFS"
    },
    {
        "q": "Which distributed compute engine processes data in-memory for fast big data processing?",
        "options": ["Apache Spark", "Apache Hadoop MapReduce", "Apache Hive", "Apache Pig"],
        "answer": "Apache Spark"
    },
    {
        "q": "What fundamental abstraction in Apache Spark represents an immutable distributed collection of elements?",
        "options": ["RDD (Resilient Distributed Dataset)", "DataFrame", "DataStream", "Dataset"],
        "answer": "RDD (Resilient Distributed Dataset)"
    },
    {
        "q": "What causes Data Skew during Spark shuffle transformations (e.g. `groupByKey`), and how can it be resolved?",
        "options": [
            "Uneven distribution of key values causes single partition executor tasks to bottleneck; resolved by salting keys or map-side aggregation",
            "Insufficient CPU cores on master node; resolved by adding master nodes",
            "Garbage collection overhead; resolved by converting DataFrames to RDDs",
            "File format incompatibility; resolved by saving as CSV"
        ],
        "answer": "Uneven distribution of key values causes single partition executor tasks to bottleneck; resolved by salting keys or map-side aggregation"
    },
    {
        "q": "When architecting a real-time feature store pipeline processing millions of event streams, what technology stack handles event streaming and feature lookup?",
        "options": [
            "Apache Kafka for event streaming + Spark Structured Streaming for windowed processing + Redis / Cassandra for low-latency feature serving",
            "Hadoop MapReduce jobs writing to HDFS flat files every 24 hours",
            "Python script reading raw JSON logs directly over SFTP",
            "Single SQLite database instance on worker node"
        ],
        "answer": "Apache Kafka for event streaming + Spark Structured Streaming for windowed processing + Redis / Cassandra for low-latency feature serving"
    }
)

# ==========================================
# 5. CYBER SECURITY ANALYST (11 Skills x 5 = 55 Qs)
# ==========================================

add_skill_qs(
    "Cyber Security Analyst", "Computer Network",
    {
        "q": "How many layers are in the OSI (Open Systems Interconnection) reference model?",
        "options": ["7", "4", "5", "6"],
        "answer": "7"
    },
    {
        "q": "Which protocol resolves IP addresses to MAC addresses on a local local network?",
        "options": ["ARP", "DNS", "DHCP", "ICMP"],
        "answer": "ARP"
    },
    {
        "q": "What TCP 3-Way Handshake flag sequence establishes a connection between client and server?",
        "options": ["SYN -> SYN-ACK -> ACK", "SYN -> ACK -> FIN", "FIN -> ACK -> RST", "ACK -> SYN-ACK -> SYN"],
        "answer": "SYN -> SYN-ACK -> ACK"
    },
    {
        "q": "What mechanism in TCP provides reliability and flow control to prevent sender from overwhelming receiver?",
        "options": [
            "Sliding Window Protocol and Acknowledgments with Retransmission Timers",
            "UDP Datagram Checksums",
            "BGP Route Advertisements",
            "ICMP Echo Requests"
        ],
        "answer": "Sliding Window Protocol and Acknowledgments with Retransmission Timers"
    },
    {
        "q": "How does BGP Route Hijacking disrupt global internet traffic, and what defense mechanism mitigates it?",
        "options": [
            "Rogue Autonomous Systems announce unauthorized IP prefixes diverting traffic; mitigated by RPKI (Resource Public Key Infrastructure)",
            "Attackers flood DNS resolvers with UDP packets; mitigated by DNSSEC",
            "Routers drop TCP packets with invalid checksums; mitigated by IPsec",
            "MAC addresses are spoofed on Wi-Fi APs; mitigated by WPA3"
        ],
        "answer": "Rogue Autonomous Systems announce unauthorized IP prefixes diverting traffic; mitigated by RPKI (Resource Public Key Infrastructure)"
    }
)

add_skill_qs(
    "Cyber Security Analyst", "OS",
    {
        "q": "What core component of an Operating System acts as the bridge between hardware and software application software?",
        "options": ["Kernel", "Shell", "Compiler", "File System"],
        "answer": "Kernel"
    },
    {
        "q": "Which CPU scheduling state indicates a process is waiting for an I/O operation to complete?",
        "options": ["Blocked / Waiting", "Running", "Ready", "Terminated"],
        "answer": "Blocked / Waiting"
    },
    {
        "q": "What condition occurs when two or more processes are permanently blocked waiting for resources held by each other?",
        "options": ["Deadlock", "Race Condition", "Starvation", "Context Switch"],
        "answer": "Deadlock"
    },
    {
        "q": "How does Virtual Memory Paging prevent memory fragmentation, and what causes a Page Fault?",
        "options": [
            "It maps non-contiguous physical RAM pages into contiguous virtual address space; a Page Fault triggers when referenced page isn't in RAM",
            "It allocates contiguous physical RAM to every process; Page Fault occurs on CPU overheat",
            "It encrypts process RAM; Page Fault happens on invalid password entry",
            "It disables swap space; Page Fault occurs on system shutdown"
        ],
        "answer": "It maps non-contiguous physical RAM pages into contiguous virtual address space; a Page Fault triggers when referenced page isn't in RAM"
    },
    {
        "q": "How do operating system kernels enforce hardware privilege separation via Supervisor Mode (Ring 0) vs User Mode (Ring 3)?",
        "options": [
            "Ring 0 grants direct access to execution instructions and memory; User applications run in Ring 3 requiring System Calls (`syscall`) to access hardware",
            "Ring 3 controls hardware drivers while Ring 0 runs web browsers",
            "Ring 0 disables interrupt handlers permanently",
            "Privilege rings are defined in software text files"
        ],
        "answer": "Ring 0 grants direct access to execution instructions and memory; User applications run in Ring 3 requiring System Calls (`syscall`) to access hardware"
    }
)

add_skill_qs(
    "Cyber Security Analyst", "Cyber Security Fundamentals",
    {
        "q": "What three core security principles make up the CIA Triad?",
        "options": [
            "Confidentiality, Integrity, Availability",
            "Control, Inspection, Authentication",
            "Cipher, Information, Authorization",
            "Compliance, Isolation, Audit"
        ],
        "answer": "Confidentiality, Integrity, Availability"
    },
    {
        "q": "What security strategy deploys multiple overlapping defensive controls across an IT infrastructure?",
        "options": ["Defense in Depth", "Single Point of Failure", "Air Gapping", "Least Privilege"],
        "answer": "Defense in Depth"
    },
    {
        "q": "What principle dictates that users and processes should be granted only the minimum access rights necessary to perform their job?",
        "options": ["Principle of Least Privilege", "Separation of Duties", "Need to Know", "Zero Trust"],
        "answer": "Principle of Least Privilege"
    },
    {
        "q": "How does a Zero Trust Security Model fundamentally differ from traditional Perimeter-based (Castle-and-Moat) security?",
        "options": [
            "Zero Trust assumes no implicit trust inside or outside the network, requiring continuous authentication, authorization, and micro-segmentation",
            "Zero Trust relies entirely on external network firewalls",
            "Zero Trust allows all internal IP addresses full access without credentials",
            "Zero Trust disables multi-factor authentication"
        ],
        "answer": "Zero Trust assumes no implicit trust inside or outside the network, requiring continuous authentication, authorization, and micro-segmentation"
    },
    {
        "q": "When responding to an ongoing enterprise security breach, what are the primary sequential phases of an Incident Response Plan (NIST SP 800-61)?",
        "options": [
            "Preparation -> Detection & Analysis -> Containment, Eradication & Recovery -> Post-Incident Activity",
            "Containment -> Eradication -> Password Reset -> Firing Staff",
            "Detection -> Legal Notification -> Encryption -> Backup Wipe",
            "Reconnaissance -> Scanning -> Exploitation -> Cleanup"
        ],
        "answer": "Preparation -> Detection & Analysis -> Containment, Eradication & Recovery -> Post-Incident Activity"
    }
)

add_skill_qs(
    "Cyber Security Analyst", "Ethical Hacking",
    {
        "q": "What is the initial passive phase of a penetration test where information is gathered about a target organization?",
        "options": ["Reconnaissance / Footprinting", "Exploitation", "Privilege Escalation", "Maintaining Access"],
        "answer": "Reconnaissance / Footprinting"
    },
    {
        "q": "Which open-source tool is widely used for network discovery, port scanning, and OS detection?",
        "options": ["Nmap", "Wireshark", "Metasploit", "Burp Suite"],
        "answer": "Nmap"
    },
    {
        "q": "What type of attack tricks users into revealing sensitive credentials by sending deceptive emails mimicking trusted organizations?",
        "options": ["Phishing", "Man-in-the-Middle", "SQL Injection", "Buffer Overflow"],
        "answer": "Phishing"
    },
    {
        "q": "How do web application security teams systematically audit applications against the OWASP Top 10 vulnerabilities (e.g., Broken Access Control, Injection)?",
        "options": [
            "By performing static code analysis (SAST), dynamic application scanning (DAST), manual penetration testing, and reviewing access boundaries",
            "By running antivirus software on database servers",
            "By setting server passwords to change every 24 hours",
            "By disabling HTTP GET requests"
        ],
        "answer": "By performing static code analysis (SAST), dynamic application scanning (DAST), manual penetration testing, and reviewing access boundaries"
    },
    {
        "q": "How do security teams secure enterprise environments against lateral movement following an initial endpoint compromise?",
        "options": [
            "Enforce network micro-segmentation, restrict local admin rights, disable LSASS memory dumping, and monitor Kerberos ticket requests (Kerberoasting)",
            "Install dual firewalls on external routers",
            "Change external domain DNS records",
            "Convert domain controllers to Linux web servers"
        ],
        "answer": "Enforce network micro-segmentation, restrict local admin rights, disable LSASS memory dumping, and monitor Kerberos ticket requests (Kerberoasting)"
    }
)

add_skill_qs(
    "Cyber Security Analyst", "Vulnerability Assessment",
    {
        "q": "What standardized metric system rates the severity of IT security vulnerabilities on a scale from 0.0 to 10.0?",
        "options": ["CVSS (Common Vulnerability Scoring System)", "CVE", "CWE", "NIST"],
        "answer": "CVSS (Common Vulnerability Scoring System)"
    },
    {
        "q": "Which tool is commonly utilized for automated vulnerability scanning of infrastructure and software assets?",
        "options": ["Nessus", "Wireshark", "John the Ripper", "Hydra"],
        "answer": "Nessus"
    },
    {
        "q": "What is the primary difference between a Vulnerability Assessment and a Penetration Test?",
        "options": [
            "A Vulnerability Assessment identifies and lists potential security flaws; a Penetration Test actively attempts to exploit them to verify risk",
            "Vulnerability assessment is illegal while penetration testing is legal",
            "Vulnerability assessment tests hardware only; penetration testing tests software",
            "There is no difference"
        ],
        "answer": "A Vulnerability Assessment identifies and lists potential security flaws; a Penetration Test actively attempts to exploit them to verify risk"
    },
    {
        "q": "What CVSS v3.1 metrics define the Exploitability Subscore of a vulnerability?",
        "options": [
            "Attack Vector (AV), Attack Complexity (AC), Privileges Required (PR), and User Interaction (UI)",
            "Confidentiality, Integrity, and Availability Impact",
            "Remediation Level and Report Confidence",
            "Financial Cost and Data Size"
        ],
        "answer": "Attack Vector (AV), Attack Complexity (AC), Privileges Required (PR), and User Interaction (UI)"
    },
    {
        "q": "How do security teams establish a scalable Vulnerability Management Lifecycle in a DevSecOps CI/CD pipeline?",
        "options": [
            "Integrate automated SAST/DAST/Container scanning, establish SLA-driven patching criteria by CVSS score, and track remediation via automated ticketers",
            "Scan production servers manually once per year",
            "Ignore low and medium severity vulnerabilities permanently",
            "Block all software releases until zero vulnerabilities exist in third-party libraries"
        ],
        "answer": "Integrate automated SAST/DAST/Container scanning, establish SLA-driven patching criteria by CVSS score, and track remediation via automated ticketers"
    }
)

add_skill_qs(
    "Cyber Security Analyst", "Cryptography",
    {
        "q": "Which cryptographic algorithm type uses the same key for both encryption and decryption?",
        "options": ["Symmetric Encryption", "Asymmetric Encryption", "Hashing", "Digital Signature"],
        "answer": "Symmetric Encryption"
    },
    {
        "q": "Which algorithm is a widely used cryptographic hash function producing a 256-bit hash digest?",
        "options": ["SHA-256", "AES-256", "RSA-2048", "Diffie-Hellman"],
        "answer": "SHA-256"
    },
    {
        "q": "How does Public Key Infrastructure (PKI) establish trust for SSL/TLS HTTPS website connections?",
        "options": [
            "Digital certificates issued and cryptographically signed by trusted Certificate Authorities (CAs) bind public keys to domain identities",
            "Servers send private keys to client web browsers over plain HTTP",
            "DNS servers encrypt web traffic using symmetric keys",
            "Browsers generate random passwords for website hosts"
        ],
        "answer": "Digital certificates issued and cryptographically signed by trusted Certificate Authorities (CAs) bind public keys to domain identities"
    },
    {
        "q": "What mathematical property enables Diffie-Hellman Key Exchange to securely establish a shared secret over an insecure channel?",
        "options": [
            "The computational difficulty of calculating Discrete Logarithms over finite fields",
            "The impossibility of multiplying prime numbers",
            "The speed of symmetric AES encryption",
            "The properties of XOR bitwise operation on strings"
        ],
        "answer": "The computational difficulty of calculating Discrete Logarithms over finite fields"
    },
    {
        "q": "Why are quantum computers poised to break RSA and ECC encryption, and what cryptographic paradigm addresses this threat?",
        "options": [
            "Shor's Algorithm on quantum computers efficiently solves prime factorization and discrete logs; mitigated by Post-Quantum Cryptography (PQC)",
            "Grover's Algorithm deletes cryptographic keys from server memory; mitigated by firewalls",
            "Quantum computers disable SHA-256 hash digests; mitigated by password complexity",
            "Quantum computers bypass TLS firewalls; mitigated by physical locks"
        ],
        "answer": "Shor's Algorithm on quantum computers efficiently solves prime factorization and discrete logs; mitigated by Post-Quantum Cryptography (PQC)"
    }
)

add_skill_qs(
    "Cyber Security Analyst", "Database Management",
    {
        "q": "What security vulnerability occurs when untrusted user input is directly concatenated into a database SQL query string?",
        "options": ["SQL Injection (SQLi)", "Cross-Site Scripting (XSS)", "Buffer Overflow", "Command Injection"],
        "answer": "SQL Injection (SQLi)"
    },
    {
        "q": "Which defense technique is most effective at preventing SQL Injection vulnerabilities?",
        "options": [
            "Using Parameterized Queries (Prepared Statements)",
            "Client-side JavaScript form validation",
            "Encrypting database hard drives",
            "Changing default database port numbers"
        ],
        "answer": "Using Parameterized Queries (Prepared Statements)"
    },
    {
        "q": "What ACID database property guarantees that committed transactions are permanently saved even during power failure?",
        "options": ["Durability", "Atomicity", "Consistency", "Isolation"],
        "answer": "Durability"
    },
    {
        "q": "How does Database Role-Based Access Control (RBAC) enforce security compliance?",
        "options": [
            "Permissions to SELECT, INSERT, UPDATE, or DELETE specific tables/views are granted to predefined roles rather than individual users",
            "Users are assigned full DBA admin privileges by default",
            "SQL queries are checked against antivirus databases",
            "Database logs are encrypted using browser cookies"
        ],
        "answer": "Permissions to SELECT, INSERT, UPDATE, or DELETE specific tables/views are granted to predefined roles rather than individual users"
    },
    {
        "q": "How do database security engineers implement Encryption at Rest and Transparent Data Encryption (TDE)?",
        "options": [
            "By encrypting database files, logs, and backups on disk using symmetric keys (AES-256) managed via a Hardware Security Module (HSM)",
            "By placing SSL certificates on web server frontends",
            "By hashing user passwords with Base64 encoding",
            "By storing database files on read-only optical discs"
        ],
        "answer": "By encrypting database files, logs, and backups on disk using symmetric keys (AES-256) managed via a Hardware Security Module (HSM)"
    }
)

add_skill_qs(
    "Cyber Security Analyst", "C",
    {
        "q": "Which operator returns the memory address of a variable in C?",
        "options": ["&", "*", "->", "%"],
        "answer": "&"
    },
    {
        "q": "What header file must be included to use functions like `printf()` and `scanf()` in C?",
        "options": ["<stdio.h>", "<stdlib.h>", "<string.h>", "<math.h>"],
        "answer": "<stdio.h>"
    },
    {
        "q": "What unsafe C library string function is notoriously vulnerable to buffer overflows because it lacks string length bounds checking?",
        "options": ["strcpy()", "strncpy()", "snprintf()", "memcpy()"],
        "answer": "strcpy()"
    },
    {
        "q": "How do modern compilers and operating systems mitigate C buffer overflow attacks using Stack Canaries and ASLR?",
        "options": [
            "Stack Canaries detect stack corruption before function return; ASLR randomizes memory addresses of stack/heap/libraries",
            "They convert C source code into Python scripts before execution",
            "They disable pointer dereferencing in memory",
            "They limit C arrays to 10 elements max"
        ],
        "answer": "Stack Canaries detect stack corruption before function return; ASLR randomizes memory addresses of stack/heap/libraries"
    },
    {
        "q": "How does a Use-After-Free (UAF) vulnerability manifest in C pointer management, and how can defensive programming prevent it?",
        "options": [
            "Accessing memory via a pointer after calling `free()` causes undefined behavior; prevented by setting pointers to NULL immediately after freeing",
            "Calling `malloc()` twice on the same variable; prevented by using `realloc()`",
            "Writing to read-only global constants; prevented by `const` keyword",
            "Dereferencing NULL pointers; prevented by `try...except`"
        ],
        "answer": "Accessing memory via a pointer after calling `free()` causes undefined behavior; prevented by setting pointers to NULL immediately after freeing"
    }
)

add_skill_qs(
    "Cyber Security Analyst", "C++",
    {
        "q": "Which access modifier restricts C++ class members so they are accessible only within the defining class?",
        "options": ["private", "public", "protected", "friend"],
        "answer": "private"
    },
    {
        "q": "Which C++ feature handles unexpected runtime errors in a structured manner using `try`, `catch`, and `throw`?",
        "options": ["Exception Handling", "Templates", "RTI", "Signals"],
        "answer": "Exception Handling"
    },
    {
        "q": "How does RAII (Resource Acquisition Is Initialization) prevent resource leaks in secure C++ development?",
        "options": [
            "Resource allocation is tied to object lifetime so resource cleanup occurs automatically in destructors when objects leave scope",
            "Resources are initialized lazily upon first method invocation",
            "Memory garbage collection runs every 5 milliseconds",
            "Global pointers manage allocated memory blocks"
        ],
        "answer": "Resource allocation is tied to object lifetime so resource cleanup occurs automatically in destructors when objects leave scope"
    },
    {
        "q": "What C++ memory safety issue occurs when virtual function tables (vtables) are corrupted by memory overwrites?",
        "options": [
            "Vtable Hijacking / Control Flow Hijacking, where redirected function pointers execute arbitrary code",
            "Template instantiation deadlock",
            "Stack overflow error in main loop",
            "Memory leak in static objects"
        ],
        "answer": "Vtable Hijacking / Control Flow Hijacking, where redirected function pointers execute arbitrary code"
    },
    {
        "q": "How do compiler exploit mitigations like DEP / NX bit and Control Flow Guard (CFG) defend C++ applications?",
        "options": [
            "DEP/NX prevents executing code in data segments (stack/heap); CFG validates indirect function call targets before branching",
            "DEP/NX encrypts hard drives; CFG scans incoming network packets",
            "DEP/NX restricts class inheritance; CFG checks standard library templates",
            "DEP/NX disables multi-threading; CFG blocks C++ compiler warnings"
        ],
        "answer": "DEP/NX prevents executing code in data segments (stack/heap); CFG validates indirect function call targets before branching"
    }
)

add_skill_qs(
    "Cyber Security Analyst", "Python",
    {
        "q": "Which standard library module in Python handles SSL/TLS encrypted network sockets?",
        "options": ["ssl", "socket", "http", "crypto"],
        "answer": "ssl"
    },
    {
        "q": "Which Python library is widely used for sending HTTP requests in security automation scripts?",
        "options": ["requests", "urllib", "http.client", "flask"],
        "answer": "requests"
    },
    {
        "q": "What security risk arises from deserializing untrusted user input using Python's `pickle` module?",
        "options": [
            "Arbitrary Code Execution via `__reduce__` magic method during unpickling",
            "Database table deletion via SQL injection",
            "Cross-Site Scripting in web browsers",
            "Memory leak in Python virtual environment"
        ],
        "answer": "Arbitrary Code Execution via `__reduce__` magic method during unpickling"
    },
    {
        "q": "How should secure Python applications handle password storage and comparison to prevent timing attacks?",
        "options": [
            "Hash passwords with bcrypt/Argon2id and compare hashes using constant-time comparison `hmac.compare_digest()`",
            "Compare plaintext strings using `==` operator",
            "Store passwords encrypted with Base64 in JSON files",
            "Hash passwords using simple MD5 algorithms"
        ],
        "answer": "Hash passwords with bcrypt/Argon2id and compare hashes using constant-time comparison `hmac.compare_digest()`"
    },
    {
        "q": "How do security automation frameworks use Python's `subprocess` module defensively while avoiding Command Injection?",
        "options": [
            "Pass command arguments as a list of strings with `shell=False` to prevent shell parser interpretation",
            "Execute shell strings using `shell=True` combined with `eval()`",
            "Concat user input directly into `os.system()` calls",
            "Encode command strings into HTML escape sequences"
        ],
        "answer": "Pass command arguments as a list of strings with `shell=False` to prevent shell parser interpretation"
    }
)

add_skill_qs(
    "Cyber Security Analyst", "Java",
    {
        "q": "What environment executes Java bytecode on target operating systems?",
        "options": ["JVM (Java Virtual Machine)", "JDK", "JRE", "JIT Compiler"],
        "answer": "JVM (Java Virtual Machine)"
    },
    {
        "q": "Which Java keyword prevents a variable value from being modified once initialized?",
        "options": ["final", "static", "const", "immutable"],
        "answer": "final"
    },
    {
        "q": "What security threat vulnerability famously affected the Apache Log4j Java logging library (Log4Shell)?",
        "options": [
            "JNDI Injection leading to Remote Code Execution (RCE) via untrusted log string lookup",
            "SQL Injection in database logging appenders",
            "Buffer overflow in Log4j C++ native extensions",
            "Cross-Site Request Forgery in admin UI"
        ],
        "answer": "JNDI Injection leading to Remote Code Execution (RCE) via untrusted log string lookup"
    },
    {
        "q": "How does Java Security Manager / AccessController enforce fine-grained sandbox permissions for untrusted code?",
        "options": [
            "By checking call stack permissions against defined Security Policy files before performing file, socket, or process operations",
            "By compiling Java bytecode to native assembly before execution",
            "By disabling multi-threading in untrusted applets",
            "By encrypting class files on disk"
        ],
        "answer": "By checking call stack permissions against defined Security Policy files before performing file, socket, or process operations"
    },
    {
        "q": "How do enterprise Java applications defend against XML External Entity (XXE) attacks during XML parsing?",
        "options": [
            "Disable `DOCTYPE` declarations and external general entities (`setFeature(\"http://apache.org/xml/features/disallow-doctype-decl\", true)`)",
            "Convert XML files to CSV format before parsing",
            "Parse XML documents using regex match strings",
            "Encrypt XML request bodies with RSA public keys"
        ],
        "answer": "Disable `DOCTYPE` declarations and external general entities (`setFeature(\"http://apache.org/xml/features/disallow-doctype-decl\", true)`)"
    }
)

# ==========================================
# 6. UI/UX DESIGNER (5 Skills x 5 = 25 Qs)
# ==========================================

add_skill_qs(
    "UI/UX Designer", "Figma",
    {
        "q": "Which Figma feature allows responsive layouts to adjust automatically when content changes?",
        "options": ["Auto Layout", "Smart Animate", "Components", "Variants"],
        "answer": "Auto Layout"
    },
    {
        "q": "What Figma feature groups related component variations (e.g. Hover, Active, Disabled states) into a single container?",
        "options": ["Variants", "Auto Layout", "Frames", "Styles"],
        "answer": "Variants"
    },
    {
        "q": "How do Figma Design Tokens streamline developer handoff across web and mobile platforms?",
        "options": [
            "By storing reusable design decisions (colors, typography, spacing) as structured JSON variables consumed directly by code bases",
            "By exporting frames as flattened JPEG images",
            "By generating HTML code automatically without CSS",
            "By creating animated GIF files of screens"
        ],
        "answer": "By storing reusable design decisions (colors, typography, spacing) as structured JSON variables consumed directly by code bases"
    },
    {
        "q": "What prototyping feature in Figma calculates transitions between matching layers across frames automatically?",
        "options": ["Smart Animate", "Instant Transition", "Dissolve", "Push/Slide"],
        "answer": "Smart Animate"
    },
    {
        "q": "When architecting an enterprise Figma Design System for multi-brand applications, how should component library hierarchy be structured?",
        "options": [
            "Separate foundational Primitive Tokens (colors, grid) from Semantic Tokens (surface-primary) and Component Sets (buttons) published as shared team libraries",
            "Place all screens and UI elements inside a single unorganized canvas file",
            "Detach component instances to edit properties directly on screens",
            "Export all UI components as SVG icons without variants"
        ],
        "answer": "Separate foundational Primitive Tokens (colors, grid) from Semantic Tokens (surface-primary) and Component Sets (buttons) published as shared team libraries"
    }
)

add_skill_qs(
    "UI/UX Designer", "Wireframing",
    {
        "q": "What is the primary purpose of a Low-Fidelity Wireframe?",
        "options": [
            "To map out layout structure, page flow, and content hierarchy without getting distracted by visual design details",
            "To finalize exact visual brand color choices",
            "To test micro-interaction animations",
            "To export final production CSS stylesheets"
        ],
        "answer": "To map out layout structure, page flow, and content hierarchy without getting distracted by visual design details"
    },
    {
        "q": "Which grid system is widely used in responsive wireframing for web page layouts?",
        "options": ["12-Column Grid", "4-Column Fixed Grid", "Isometric Grid", "Golden Ratio Spiral Grid"],
        "answer": "12-Column Grid"
    },
    {
        "q": "What design artifact visually maps the sequence of steps a user takes to complete a goal within an application?",
        "options": ["User Flow / Task Flow", "Mood Board", "Color Palette", "Site Map"],
        "answer": "User Flow / Task Flow"
    },
    {
        "q": "How does Information Architecture (IA) shape wireframe layout design?",
        "options": [
            "It organizes and structures digital content logically based on user mental models, ensuring intuition in navigation paths",
            "It selects visual font pairing combinations",
            "It calculates grid column pixel widths automatically",
            "It handles database schema normalization"
        ],
        "answer": "It organizes and structures digital content logically based on user mental models, ensuring intuition in navigation paths"
    },
    {
        "q": "When conducting early Usability Testing on low-fidelity wireframe paper prototypes, what insight is most critical to evaluate?",
        "options": [
            "Validating whether user mental models match the navigation structure and identifying points of confusion or drop-off in key tasks",
            "Evaluating visual color contrast ratios",
            "Measuring visual render latency of graphics",
            "Counting the number of UI buttons per screen"
        ],
        "answer": "Validating whether user mental models match the navigation structure and identifying points of confusion or drop-off in key tasks"
    }
)

add_skill_qs(
    "UI/UX Designer", "Prototyping",
    {
        "q": "What level of fidelity is a prototype that includes realistic visuals, interactive UI states, and realistic transitions?",
        "options": ["High-Fidelity Prototype", "Low-Fidelity Prototype", "Wireframe", "Paper Prototype"],
        "answer": "High-Fidelity Prototype"
    },
    {
        "q": "What user feedback response triggers interactive visual changes on hover or click in a prototype?",
        "options": ["Micro-interactions", "Wireframes", "Design Tokens", "Style Guides"],
        "answer": "Micro-interactions"
    },
    {
        "q": "How do advanced prototyping tools (e.g. ProtoPie, Figma) utilize Variables and Conditional Logic?",
        "options": [
            "They store dynamic user inputs and evaluate IF/ELSE conditions to simulate real application data state changes",
            "They write backend SQL database scripts automatically",
            "They export iOS Swift code without layout constraints",
            "They generate automated user testing recordings"
        ],
        "answer": "They store dynamic user inputs and evaluate IF/ELSE conditions to simulate real application data state changes"
    },
    {
        "q": "What usability testing metric measures the percentage of participants who complete a prototype task successfully?",
        "options": ["Task Completion Rate (Direct Success)", "Net Promoter Score (NPS)", "System Usability Scale (SUS)", "Click-Through Rate (CTR)"],
        "answer": "Task Completion Rate (Direct Success)"
    },
    {
        "q": "When prototyping complex multi-step mobile checkout flows, how do you design micro-interactions to minimize Cognitive Load?",
        "options": [
            "Provide immediate tactile visual feedback, use progressive disclosure to group input steps, and preserve user input state dynamically across screens",
            "Display all 25 form input fields on a single unscrollable screen",
            "Disable back button navigation between checkout steps",
            "Hide validation error messages until final submit button click"
        ],
        "answer": "Provide immediate tactile visual feedback, use progressive disclosure to group input steps, and preserve user input state dynamically across screens"
    }
)

add_skill_qs(
    "UI/UX Designer", "Typography",
    {
        "q": "Which font classification is characterized by small decorative strokes at the ends of character letterforms?",
        "options": ["Serif", "Sans-Serif", "Monospace", "Display"],
        "answer": "Serif"
    },
    {
        "q": "What term refers to the vertical distance between baselines of lines of text?",
        "options": ["Leading (Line Height)", "Kerning", "Tracking", "Baseline Offset"],
        "answer": "Leading (Line Height)"
    },
    {
        "q": "What is the key difference between Kerning and Tracking in typography?",
        "options": [
            "Kerning adjusts spacing between individual character pairs; Tracking adjusts uniform spacing across an entire word or passage",
            "Tracking adjusts vertical line height; Kerning adjusts horizontal font size",
            "Kerning applies only to Serif fonts; Tracking applies to Sans-Serif fonts",
            "There is no difference"
        ],
        "answer": "Kerning adjusts spacing between individual character pairs; Tracking adjusts uniform spacing across an entire word or passage"
    },
    {
        "q": "What Web Content Accessibility Guidelines (WCAG 2.1 AA) contrast ratio is required for normal body text against its background?",
        "options": ["4.5:1", "3.0:1", "7.0:1", "2.0:1"],
        "answer": "4.5:1"
    },
    {
        "q": "How do you construct a responsive Fluid Typographic Scale using CSS `clamp()` for multi-device digital design systems?",
        "options": [
            "Define min, viewport-preferred (`vw`), and max dynamic font size bounds (`clamp(1rem, 2.5vw, 2.5rem)`) linked to modular scale ratios",
            "Set static pixel (`px`) sizes inside fixed breakpoint media queries for every screen pixel width",
            "Multiply heading sizes by random floating point numbers",
            "Use monospace fonts exclusively across mobile viewports"
        ],
        "answer": "Define min, viewport-preferred (`vw`), and max dynamic font size bounds (`clamp(1rem, 2.5vw, 2.5rem)`) linked to modular scale ratios"
    }
)

add_skill_qs(
    "UI/UX Designer", "Color Theory",
    {
        "q": "Which color scheme uses colors that sit directly opposite each other on the color wheel?",
        "options": ["Complementary", "Analogous", "Monochromatic", "Triadic"],
        "answer": "Complementary"
    },
    {
        "q": "What popular UI design rule recommends distributing colors in 60% dominant, 30% secondary, and 10% accent proportions?",
        "options": ["60-30-10 Rule", "80-20 Rule", "Golden Ratio", "Rule of Thirds"],
        "answer": "60-30-10 Rule"
    },
    {
        "q": "What is the functional advantage of using the HSL (Hue, Saturation, Lightness) color model over HEX for UI design system themes?",
        "options": [
            "HSL allows intuitive mathematical adjustments of lightness and saturation for hover/active states while holding hue constant",
            "HSL uses less memory in browser rendering engines",
            "HSL supports more total colors than HEX",
            "HSL automatically converts text into vector paths"
        ],
        "answer": "HSL allows intuitive mathematical adjustments of lightness and saturation for hover/active states while holding hue constant"
    },
    {
        "q": "How do UI designers design accessible Light and Dark Theme color systems using Semantic Tokens?",
        "options": [
            "By mapping functional roles (e.g. surface-primary, text-on-surface) to dynamic tokens that rebind to different primitive color values per theme mode",
            "By inverting raw HEX color values mathematically using negative CSS filters",
            "By forcing dark backgrounds across all app screens regardless of user settings",
            "By using pure black (#000000) and pure white (#FFFFFF) exclusively"
        ],
        "answer": "By mapping functional roles (e.g. surface-primary, text-on-surface) to dynamic tokens that rebind to different primitive color values per theme mode"
    },
    {
        "q": "When designing digital interfaces for users with visual impairments (e.g. Red-Green Color Blindness / Deuteranopia), how do you ensure visual accessibility?",
        "options": [
            "Never rely solely on color to convey critical information; supplement color states with iconography, text labels, and structural patterns",
            "Increase screen brightness settings automatically",
            "Use only grayscale color palettes across the entire web application",
            "Replace colored buttons with standard underlined text links"
        ],
        "answer": "Never rely solely on color to convey critical information; supplement color states with iconography, text labels, and structural patterns"
    }
)

# ==========================================
# 7. CLOUD COMPUTING (5 Skills x 5 = 25 Qs)
# ==========================================

add_skill_qs(
    "Cloud Computing", "Cloud Security",
    {
        "q": "What security framework divides security obligations between the cloud provider (Security OF the cloud) and customer (Security IN the cloud)?",
        "options": ["Shared Responsibility Model", "Zero Trust Architecture", "Defense in Depth", "ISO 27001 Standard"],
        "answer": "Shared Responsibility Model"
    },
    {
        "q": "Which cloud security control manages user identities, roles, and granular access permissions?",
        "options": ["IAM (Identity and Access Management)", "WAF", "VPC", "KMS"],
        "answer": "IAM (Identity and Access Management)"
    },
    {
        "q": "What cloud service encrypts and decrypts sensitive data using managed master encryption keys?",
        "options": ["KMS (Key Management Service)", "IAM", "CloudTrail", "GuardDuty"],
        "answer": "KMS (Key Management Service)"
    },
    {
        "q": "How does Cloud Security Posture Management (CSPM) protect multi-cloud enterprise deployments?",
        "options": [
            "By continuously scanning cloud infrastructure configurations against security benchmarks (CIS) and compliance frameworks to detect misconfigurations",
            "By installing local antivirus software on physical host hypervisors",
            "By blocking incoming HTTP web traffic at domain registrars",
            "By auto-deleting cloud storage buckets every 30 days"
        ],
        "answer": "By continuously scanning cloud infrastructure configurations against security benchmarks (CIS) and compliance frameworks to detect misconfigurations"
    },
    {
        "q": "When mitigating data exfiltration risks in public cloud VPC networks, what network security architecture restricts outbound traffic?",
        "options": [
            "Deploy NAT Gateways with Egress Proxy Filtering / AWS Network Firewall and enforce strict VPC Endpoint Policies for S3/DynamoDB",
            "Allow open 0.0.0.0/0 inbound security group rules",
            "Disable SSL encryption on internal microservice calls",
            "Store root credentials in plain text environment variables"
        ],
        "answer": "Deploy NAT Gateways with Egress Proxy Filtering / AWS Network Firewall and enforce strict VPC Endpoint Policies for S3/DynamoDB"
    }
)

add_skill_qs(
    "Cloud Computing", "AWS",
    {
        "q": "Which AWS compute service provides scalable virtual servers in the cloud?",
        "options": ["EC2", "S3", "RDS", "Lambda"],
        "answer": "EC2"
    },
    {
        "q": "Which AWS storage service provides scalable object storage for files and media?",
        "options": ["S3 (Simple Storage Service)", "EBS", "EFS", "DynamoDB"],
        "answer": "S3 (Simple Storage Service)"
    },
    {
        "q": "What AWS serverless service executes code automatically in response to events without provisioning virtual servers?",
        "options": ["AWS Lambda", "AWS EC2", "AWS ECS", "AWS Fargate"],
        "answer": "AWS Lambda"
    },
    {
        "q": "How does AWS Auto Scaling combined with an Application Load Balancer (ALB) handle high traffic spikes?",
        "options": [
            "ALB distributes incoming HTTP traffic across healthy EC2 instances while Auto Scaling dynamically provisions/terminates instances based on CPU/traffic metrics",
            "Auto Scaling routes web traffic directly to S3 buckets",
            "ALB increases virtual server RAM without rebooting",
            "AWS Lambda converts static EC2 servers into database tables"
        ],
        "answer": "ALB distributes incoming HTTP traffic across healthy EC2 instances while Auto Scaling dynamically provisions/terminates instances based on CPU/traffic metrics"
    },
    {
        "q": "How do you architect a Multi-Region Active-Active disaster recovery solution on AWS for critical enterprise applications?",
        "options": [
            "Use Route 53 Latency-Based Routing + Aurora Global Database for cross-region replication + S3 Cross-Region Replication (CRR)",
            "Run single EC2 instance in us-east-1 and take manual weekly snapshots",
            "Export raw database dumps to local laptop hard drives daily",
            "Use single-AZ RDS deployments with read replicas"
        ],
        "answer": "Use Route 53 Latency-Based Routing + Aurora Global Database for cross-region replication + S3 Cross-Region Replication (CRR)"
    }
)

add_skill_qs(
    "Cloud Computing", "DevOps",
    {
        "q": "What DevOps practice automatically builds, tests, and validates code changes in a shared repository?",
        "options": ["Continuous Integration (CI)", "Continuous Deployment (CD)", "Infrastructure as Code (IaC)", "Monitoring"],
        "answer": "Continuous Integration (CI)"
    },
    {
        "q": "Which containerization platform packages applications and dependencies into lightweight portable containers?",
        "options": ["Docker", "Kubernetes", "Jenkins", "Terraform"],
        "answer": "Docker"
    },
    {
        "q": "Which Infrastructure as Code (IaC) tool uses declarative configuration files to provision multi-cloud resources?",
        "options": ["Terraform", "Docker", "Ansible", "Git"],
        "answer": "Terraform"
    },
    {
        "q": "What is the key difference between Blue-Green Deployment and Canary Deployment strategies?",
        "options": [
            "Blue-Green switches 100% traffic instantly between two identical environments; Canary gradually shifts a small percentage of traffic to the new version",
            "Canary deployment wipes the database before release; Blue-Green keeps old data",
            "Blue-Green applies only to mobile apps; Canary applies to backend APIs",
            "There is no operational difference"
        ],
        "answer": "Blue-Green switches 100% traffic instantly between two identical environments; Canary gradually shifts a small percentage of traffic to the new version"
    },
    {
        "q": "How does GitOps (e.g. ArgoCD / Flux) enforce continuous state reconciliation for Kubernetes container clusters?",
        "options": [
            "It treats Git repositories as single source of truth; controllers continuously monitor Git commits and sync actual cluster state to match target manifests",
            "It executes manual `kubectl apply` commands via developer SSH terminals",
            "It rebuilds physical server host hardware on every code push",
            "It stores production container passwords in public Git commits"
        ],
        "answer": "It treats Git repositories as single source of truth; controllers continuously monitor Git commits and sync actual cluster state to match target manifests"
    }
)

add_skill_qs(
    "Cloud Computing", "Networking",
    {
        "q": "What service maps human-readable domain names (e.g. `example.com`) to numeric IP addresses?",
        "options": ["DNS (Domain Name System)", "DHCP", "NAT", "BGP"],
        "answer": "DNS (Domain Name System)"
    },
    {
        "q": "What networking technology isolates cloud resources within a private virtual network segment?",
        "options": ["VPC (Virtual Private Cloud)", "VPN", "WAN", "LAN"],
        "answer": "VPC (Virtual Private Cloud)"
    },
    {
        "q": "In CIDR network notation, how many usable IP addresses are available in a `/24` subnet?",
        "options": ["254", "512", "128", "64"],
        "answer": "254"
    },
    {
        "q": "What is the operational difference between a Stateful Security Group and a Stateless Network ACL (NACL) in cloud VPCs?",
        "options": [
            "Security Groups evaluate return traffic automatically (stateful); NACLs require explicit inbound and outbound rules (stateless) processed by rule order",
            "NACLs apply to individual EC2 instances; Security Groups apply to subnets",
            "Security Groups block IP addresses; NACLs block domain names",
            "NACLs work only on IPv6 traffic"
        ],
        "answer": "Security Groups evaluate return traffic automatically (stateful); NACLs require explicit inbound and outbound rules (stateless) processed by rule order"
    },
    {
        "q": "How does a Content Delivery Network (CDN, e.g. CloudFront) optimize dynamic API latency and static asset delivery globally?",
        "options": [
            "By caching static assets at global Edge Locations close to users and establishing persistent TLS connection pools to origin servers",
            "By compressing database tables into ZIP files before transmission",
            "By executing web server code directly inside client browser engines",
            "By replacing TCP packets with UDP datagrams globally"
        ],
        "answer": "By caching static assets at global Edge Locations close to users and establishing persistent TLS connection pools to origin servers"
    }
)

add_skill_qs(
    "Cloud Computing", "Linux",
    {
        "q": "Which Linux command displays the current working directory path?",
        "options": ["pwd", "ls", "cd", "dir"],
        "answer": "pwd"
    },
    {
        "q": "Which Linux command changes file and directory permissions?",
        "options": ["chmod", "chown", "chgrp", "sudo"],
        "answer": "chmod"
    },
    {
        "q": "What numeric permission representation grants Read, Write, and Execute (rwx) to Owner, and Read/Execute (r-x) to Group and Others?",
        "options": ["755", "644", "777", "700"],
        "answer": "755"
    },
    {
        "q": "Which Linux command pipeline filters running system processes by name?",
        "options": [
            "ps aux | grep process_name",
            "cat /etc/processes | find process_name",
            "top --search process_name",
            "ls -la /proc | filter process_name"
        ],
        "answer": "ps aux | grep process_name"
    },
    {
        "q": "How do Linux cgroups (Control Groups) and namespaces provide foundational isolation for container runtimes (Docker/containerd)?",
        "options": [
            "cgroups restrict and meter hardware resource usage (CPU, RAM, I/O); namespaces isolate system view (Process IDs, Mounts, Network interfaces)",
            "cgroups compile C source code; namespaces handle SSH logins",
            "cgroups format hard drives; namespaces assign domain names",
            "cgroups compress system logs; namespaces manage user passwords"
        ],
        "answer": "cgroups restrict and meter hardware resource usage (CPU, RAM, I/O); namespaces isolate system view (Process IDs, Mounts, Network interfaces)"
    }
)

# ==========================================
# VERIFICATION & FILE WRITING
# ==========================================

print("Total Career Roles:", len(questions_data))
total_qs = 0
for r, skills in questions_data.items():
    print(f"Role '{r}' has {len(skills)} skills:")
    for sk, qs in skills.items():
        assert len(qs) == 5, f"Skill {sk} in {r} has {len(qs)} Qs instead of 5!"
        diffs = [q["difficulty"] for q in qs]
        assert diffs == ["Basic", "Beginner", "Intermediate", "Advanced", "Expert"], f"Invalid diff sequence in {r}->{sk}: {diffs}"
        total_qs += len(qs)

print(f"TOTAL QUESTIONS VERIFIED: {total_qs}")
assert total_qs == 255, f"Total questions is {total_qs}, expected 255!"

# Write out data/questions_data.py
output_path = r"c:\Users\Smile\OneDrive\Desktop\student skill gap analytics\data\questions_data.py"

with open(output_path, "w", encoding="utf-8") as f:
    f.write("# 255 Assessment Questions across 7 Career Roles and 51 Skill Categories\n")
    f.write("# Every skill in every career role contains EXACTLY 5 questions.\n")
    f.write("# Q1 = Basic, Q2 = Beginner, Q3 = Intermediate, Q4 = Advanced, Q5 = Expert\n\n")
    f.write("QUESTIONS_DATA = ")
    f.write(pprint.pformat(questions_data, indent=4, width=120))
    f.write("\n")

print(f"Successfully generated and wrote {total_qs} questions to {output_path}")
