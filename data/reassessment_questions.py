# Reassessment Question Bank
# Contains NEW, non-repeating questions organized strictly by difficulty level:
# - Basic
# - Beginner
# - Intermediate
# - Advanced
# - Expert
#
# Guaranteed 100% unique question content distinct from initial assessment questions.

REASSESSMENT_QUESTIONS_DATA = {
    "Python": [
        {
            "id": "re_py_1",
            "difficulty": "Basic",
            "q": "Which built-in Python function returns the length (number of items) of an object?",
            "options": ["len()", "count()", "size()", "length()"],
            "answer": "len()"
        },
        {
            "id": "re_py_2",
            "difficulty": "Beginner",
            "q": "What is the result of using list comprehension `[x**2 for x in range(4)]` in Python?",
            "options": ["[0, 1, 4, 9]", "[1, 4, 9, 16]", "[0, 2, 4, 6]", "[1, 2, 3, 4]"],
            "answer": "[0, 1, 4, 9]"
        },
        {
            "id": "re_py_3",
            "difficulty": "Intermediate",
            "q": "Which module in Python's standard library provides generic key-value mapping objects like `defaultdict` and `Counter`?",
            "options": ["collections", "itertools", "functools", "datastructures"],
            "answer": "collections"
        },
        {
            "id": "re_py_4",
            "difficulty": "Advanced",
            "q": "How does Python handle memory management and prevent circular reference memory leaks?",
            "options": [
                "Reference counting combined with a generational garbage collector",
                "Manual stack allocation with free pointers",
                "Pure mark-and-sweep garbage collection running on every loop",
                "Automatic static deallocation at compile time"
            ],
            "answer": "Reference counting combined with a generational garbage collector"
        },
        {
            "id": "re_py_5",
            "difficulty": "Expert",
            "q": "What is the primary function of Python's `asyncio` event loop when handling thousands of non-blocking I/O operations?",
            "options": [
                "Cooperative multitasking using coroutines and futures on a single thread",
                "Preemptive multithreading across hardware CPU cores bypassing the GIL",
                "Forking new OS child processes for every incoming network request",
                "JIT compiling bytecode into C native machine instructions"
            ],
            "answer": "Cooperative multitasking using coroutines and futures on a single thread"
        }
    ],

    "SQL": [
        {
            "id": "re_sql_1",
            "difficulty": "Basic",
            "q": "Which SQL clause is used to filter rows returned by a SELECT statement based on specified conditions?",
            "options": ["WHERE", "ORDER BY", "GROUP BY", "SELECT"],
            "answer": "WHERE"
        },
        {
            "id": "re_sql_2",
            "difficulty": "Beginner",
            "q": "Which SQL aggregate function computes the average value of a numeric column?",
            "options": ["AVG()", "MEAN()", "COUNT()", "SUM()"],
            "answer": "AVG()"
        },
        {
            "id": "re_sql_3",
            "difficulty": "Intermediate",
            "q": "What is the main difference between `WHERE` and `HAVING` clauses in SQL?",
            "options": [
                "`WHERE` filters individual rows before grouping; `HAVING` filters aggregated groups after `GROUP BY`",
                "`HAVING` filters individual rows; `WHERE` filters aggregated groups",
                "`WHERE` works only with string types; `HAVING` works only with numeric types",
                "`HAVING` can only be used in Subqueries"
            ],
            "answer": "`WHERE` filters individual rows before grouping; `HAVING` filters aggregated groups after `GROUP BY`"
        },
        {
            "id": "re_sql_4",
            "difficulty": "Advanced",
            "q": "Which SQL window function assigns a unique sequential integer to rows within a partition starting at 1?",
            "options": ["ROW_NUMBER()", "DENSE_RANK()", "RANK()", "LEAD()"],
            "answer": "ROW_NUMBER()"
        },
        {
            "id": "re_sql_5",
            "difficulty": "Expert",
            "q": "How does an ACID-compliant RDBMS ensure durability during sudden power loss or system failure?",
            "options": [
                "Write-Ahead Logging (WAL) and Transaction Commit Logs written to disk prior to buffer page updates",
                "In-memory RAM snapshots copied to network storage asynchronously every 10 minutes",
                "Automatic database schema rebuilding upon system reboot",
                "Disabling transaction locks during write operations"
            ],
            "answer": "Write-Ahead Logging (WAL) and Transaction Commit Logs written to disk prior to buffer page updates"
        }
    ],

    "Excel": [
        {
            "id": "re_xl_1",
            "difficulty": "Basic",
            "q": "Which Excel formula sums values in a cell range based on a single specific condition?",
            "options": ["SUMIF", "COUNTIF", "VLOOKUP", "AVERAGEIF"],
            "answer": "SUMIF"
        },
        {
            "id": "re_xl_2",
            "difficulty": "Beginner",
            "q": "Which feature in Microsoft Excel is used to summarize, analyze, explore, and present summary data in a dynamic table?",
            "options": ["PivotTable", "Conditional Formatting", "Data Validation", "Goal Seek"],
            "answer": "PivotTable"
        },
        {
            "id": "re_xl_3",
            "difficulty": "Intermediate",
            "q": "Which modern formula combination offers more flexibility than `VLOOKUP` by searching in any column and returning values from another?",
            "options": ["INDEX & MATCH / XLOOKUP", "CONCATENATE & TEXT", "SUMIFS & COUNTIFS", "IF & AND"],
            "answer": "INDEX & MATCH / XLOOKUP"
        },
        {
            "id": "re_xl_4",
            "difficulty": "Advanced",
            "q": "What does an Excel Array Formula (or Dynamic Array formula like `FILTER`) return when applied to dataset criteria?",
            "options": [
                "An array of multiple values that automatically spills into neighbor cells",
                "A single boolean value TRUE or FALSE in the active cell",
                "A static copy saved to a separate worksheet",
                "An encrypted macro script string"
            ],
            "answer": "An array of multiple values that automatically spills into neighbor cells"
        },
        {
            "id": "re_xl_5",
            "difficulty": "Expert",
            "q": "Which advanced Excel tool in Power Pivot uses DAX formulas to create dynamic aggregated metrics over multi-table data models?",
            "options": ["DAX Measures", "VBA UserForms", "Solver Add-in", "Consolidate Range"],
            "answer": "DAX Measures"
        }
    ],

    "Power BI": [
        {
            "id": "re_pbi_1",
            "difficulty": "Basic",
            "q": "What is the dedicated data transformation editor in Power BI used to clean and reshape data before loading?",
            "options": ["Power Query Editor", "DAX Studio", "Report Builder", "Data Analysis Visualizer"],
            "answer": "Power Query Editor"
        },
        {
            "id": "re_pbi_2",
            "difficulty": "Beginner",
            "q": "Which DAX function is most commonly used to evaluate an expression under modified filter contexts?",
            "options": ["CALCULATE()", "FILTER()", "SUMX()", "ALL()"],
            "answer": "CALCULATE()"
        },
        {
            "id": "re_pbi_3",
            "difficulty": "Intermediate",
            "q": "What schema layout is recommended as best practice for Power BI data modeling to optimize performance?",
            "options": ["Star Schema (Fact and Dimension tables)", "Flat Single Table", "Snowflake Schema with deep normalization", "Hierarchical Network Model"],
            "answer": "Star Schema (Fact and Dimension tables)"
        },
        {
            "id": "re_pbi_4",
            "difficulty": "Advanced",
            "q": "What is the key functional distinction between DAX Calculated Columns and DAX Measures in Power BI?",
            "options": [
                "Calculated Columns store pre-computed values per row in memory; Measures evaluate dynamically at query time based on visual filter context",
                "Measures increase dataset file size on disk; Calculated Columns do not take space",
                "Calculated Columns can only use text data; Measures can only use numeric data",
                "Calculated Columns can only be used in Slicers"
            ],
            "answer": "Calculated Columns store pre-computed values per row in memory; Measures evaluate dynamically at query time based on visual filter context"
        },
        {
            "id": "re_pbi_5",
            "difficulty": "Expert",
            "q": "When configuring Incremental Refresh in Power BI Service for massive datasets, which two Power Query parameters must be defined?",
            "options": ["RangeStart and RangeEnd", "MinDate and MaxDate", "FilterFrom and FilterTo", "BatchStart and BatchEnd"],
            "answer": "RangeStart and RangeEnd"
        }
    ],

    "Statistics": [
        {
            "id": "re_stat_1",
            "difficulty": "Basic",
            "q": "Which measure of central tendency represents the middle value in a dataset when ordered from lowest to highest?",
            "options": ["Median", "Mean", "Mode", "Variance"],
            "answer": "Median"
        },
        {
            "id": "re_stat_2",
            "difficulty": "Beginner",
            "q": "What does the standard deviation of a sample dataset measure?",
            "options": [
                "The amount of dispersion or variation of data points relative to the mean",
                "The difference between the maximum and minimum values",
                "The total sum of all values divided by count",
                "The probability of rejecting the null hypothesis"
            ],
            "answer": "The amount of dispersion or variation of data points relative to the mean"
        },
        {
            "id": "re_stat_3",
            "difficulty": "Intermediate",
            "q": "What fundamental statistics theorem states that the sampling distribution of the sample mean approaches a normal distribution as sample size increases?",
            "options": ["Central Limit Theorem", "Bayes Theorem", "Law of Large Numbers", "Chebyshev Theorem"],
            "answer": "Central Limit Theorem"
        },
        {
            "id": "re_stat_4",
            "difficulty": "Advanced",
            "q": "In statistical hypothesis testing, what is a Type I error (Alpha error)?",
            "options": [
                "Rejecting the null hypothesis when it is actually true (False Positive)",
                "Failing to reject the null hypothesis when it is false (False Negative)",
                "Calculating an incorrect p-value due to sample bias",
                "Using a non-parametric test on normally distributed data"
            ],
            "answer": "Rejecting the null hypothesis when it is actually true (False Positive)"
        },
        {
            "id": "re_stat_5",
            "difficulty": "Expert",
            "q": "What is the primary objective of applying Benjamini-Hochberg procedure in multi-variable statistical testing?",
            "options": [
                "Controlling the False Discovery Rate (FDR) during multiple hypothesis testing",
                "Converting skewed datasets into standard z-score normal distributions",
                "Calculating exact confidence intervals for non-linear regression models",
                "Estimating missing values in longitudinal time-series data"
            ],
            "answer": "Controlling the False Discovery Rate (FDR) during multiple hypothesis testing"
        }
    ],

    "Tableau": [
        {
            "id": "re_tb_1",
            "difficulty": "Basic",
            "q": "In Tableau, what visual indicator distinguishes Dimensions (categorical fields) from Measures (numerical fields)?",
            "options": [
                "Dimensions are Blue icons/pills; Measures are Green icons/pills",
                "Dimensions are Green icons/pills; Measures are Blue icons/pills",
                "Dimensions are Red; Measures are Yellow",
                "Dimensions are bold text; Measures are italic text"
            ],
            "answer": "Dimensions are Blue icons/pills; Measures are Green icons/pills"
        },
        {
            "id": "re_tb_2",
            "difficulty": "Beginner",
            "q": "Which Tableau feature enables interactive filtering across multiple worksheets on a single dashboard layout?",
            "options": ["Dashboard Actions (Filter Action)", "Parameters", "Sets", "Calculated Fields"],
            "answer": "Dashboard Actions (Filter Action)"
        },
        {
            "id": "re_tb_3",
            "difficulty": "Intermediate",
            "q": "What type of Level of Detail (LOD) expression in Tableau computes aggregations independently of fields present in the view visualization?",
            "options": ["FIXED LOD", "INCLUDE LOD", "EXCLUDE LOD", "TABLE LOD"],
            "answer": "FIXED LOD"
        },
        {
            "id": "re_tb_4",
            "difficulty": "Advanced",
            "q": "What is the correct order of operations (filtering hierarchy) in Tableau?",
            "options": [
                "Extract Filters -> Context Filters -> Dimension Filters -> Measure Filters -> Table Calc Filters",
                "Dimension Filters -> Context Filters -> Extract Filters -> Table Calc Filters",
                "Measure Filters -> Dimension Filters -> Context Filters -> Extract Filters",
                "Table Calc Filters -> Measure Filters -> Dimension Filters -> Context Filters"
            ],
            "answer": "Extract Filters -> Context Filters -> Dimension Filters -> Measure Filters -> Table Calc Filters"
        },
        {
            "id": "re_tb_5",
            "difficulty": "Expert",
            "q": "When optimizing Tableau workbook query speed against massive Data Warehouses, how do Table Extensions and Data Engine Extracts improve dashboard rendering?",
            "options": [
                "By materializing pre-aggregated Hyper extract files locally and pushing down SQL queries via native drivers",
                "By rendering all graphics on the client web browser GPU",
                "By converting all Tableau visualizations into static JPEG images",
                "By disabling caching on Tableau Server"
            ],
            "answer": "By materializing pre-aggregated Hyper extract files locally and pushing down SQL queries via native drivers"
        }
    ],

    "DSA using Python": [
        {
            "id": "re_dsa_1",
            "difficulty": "Basic",
            "q": "What is the average time complexity of searching for an element in a balanced Binary Search Tree (BST)?",
            "options": ["O(log n)", "O(n)", "O(1)", "O(n^2)"],
            "answer": "O(log n)"
        },
        {
            "id": "re_dsa_2",
            "difficulty": "Beginner",
            "q": "Which linear data structure operates on a Last-In, First-Out (LIFO) principle?",
            "options": ["Stack", "Queue", "Linked List", "Array"],
            "answer": "Stack"
        },
        {
            "id": "re_dsa_3",
            "difficulty": "Intermediate",
            "q": "Which algorithm finds the shortest path from a single source vertex to all other vertices in a weighted graph with non-negative edge weights?",
            "options": ["Dijkstra's Algorithm", "Kruskal's Algorithm", "Floyd-Warshall Algorithm", "Breadth-First Search"],
            "answer": "Dijkstra's Algorithm"
        },
        {
            "id": "re_dsa_4",
            "difficulty": "Advanced",
            "q": "What technique is used in Dynamic Programming to avoid redundant computations by storing subproblem results?",
            "options": ["Memoization / Tabulation", "Greedy Choice", "Backtracking", "Divide and Conquer"],
            "answer": "Memoization / Tabulation"
        },
        {
            "id": "re_dsa_5",
            "difficulty": "Expert",
            "q": "In Python, how does `collections.deque` achieve O(1) time complexity for appending and popping from both ends compared to `list` O(n)?",
            "options": [
                "Using a doubly-linked list of fixed-length memory blocks (chunks)",
                "Using contiguous dynamic array reallocations",
                "Using hash tables mapping indices to memory offsets",
                "Using C-level memory copying on every insert"
            ],
            "answer": "Using a doubly-linked list of fixed-length memory blocks (chunks)"
        }
    ],

    "OOPs using Python": [
        {
            "id": "re_oops_1",
            "difficulty": "Basic",
            "q": "What parameter is used inside Python class methods to refer to the current instance of the class?",
            "options": ["self", "this", "cls", "inst"],
            "answer": "self"
        },
        {
            "id": "re_oops_2",
            "difficulty": "Beginner",
            "q": "Which OOP principle hides internal implementation details and exposes only essential interfaces to the user?",
            "options": ["Encapsulation", "Inheritance", "Polymorphism", "Abstraction"],
            "answer": "Encapsulation"
        },
        {
            "id": "re_oops_3",
            "difficulty": "Intermediate",
            "q": "What special double-underscore method is invoked in Python when instantiating a new class object?",
            "options": ["__init__", "__new__", "__construct__", "__create__"],
            "answer": "__init__"
        },
        {
            "id": "re_oops_4",
            "difficulty": "Advanced",
            "q": "How does Python determine method resolution order (MRO) when inheriting from multiple parent classes?",
            "options": [
                "C3 Linearization algorithm",
                "First parent class declared in syntax always wins",
                "Depth-First Search (DFS) left-to-right without linearization",
                "Random selection based on class hash keys"
            ],
            "answer": "C3 Linearization algorithm"
        },
        {
            "id": "re_oops_5",
            "difficulty": "Expert",
            "q": "What is a Metaclass in Python, and what method is called to customize class creation before instantiation?",
            "options": [
                "A class of a class that defines how classes behave; customized via `type.__new__` or `__metaclass__`",
                "A wrapper decorator applied only to abstract methods",
                "A built-in module for serializing class objects to JSON",
                "A static interface definition enforced at runtime"
            ],
            "answer": "A class of a class that defines how classes behave; customized via `type.__new__` or `__metaclass__`"
        }
    ],

    "Flask": [
        {
            "id": "re_fl_1",
            "difficulty": "Basic",
            "q": "Which decorator in Flask binds a view function to an incoming URL path?",
            "options": ["@app.route()", "@app.get()", "@app.url()", "@app.bind()"],
            "answer": "@app.route()"
        },
        {
            "id": "re_fl_2",
            "difficulty": "Beginner",
            "q": "Which templating engine is built into Flask for rendering dynamic HTML templates?",
            "options": ["Jinja2", "Mustache", "Handlebars", "Blade"],
            "answer": "Jinja2"
        },
        {
            "id": "re_fl_3",
            "difficulty": "Intermediate",
            "q": "What feature in Flask allows modularizing application routes into reusable components?",
            "options": ["Blueprints", "App Contexts", "Middleware", "Services"],
            "answer": "Blueprints"
        },
        {
            "id": "re_fl_4",
            "difficulty": "Advanced",
            "q": "How does Flask handle thread-safe global objects like `request` and `g` during concurrent HTTP requests?",
            "options": [
                "Using Context Locals (Werkzeug LocalProxy bound to request/app context)",
                "Using process locks on global dictionary variables",
                "Using static global singletons shared across threads",
                "By creating new Python interpreter processes for each request"
            ],
            "answer": "Using Context Locals (Werkzeug LocalProxy bound to request/app context)"
        },
        {
            "id": "re_fl_5",
            "difficulty": "Expert",
            "q": "In production WSGI deployments (e.g. Gunicorn + Nginx + Flask), why are eventlet/gevent worker classes preferred for long-polling API endpoints?",
            "options": [
                "They use greenlets for asynchronous non-blocking I/O without needing multiple OS thread overhead",
                "They compile Flask routes into C extensions automatically",
                "They bypass Python GIL by executing code directly on Nginx threads",
                "They store all session data in hardware memory registers"
            ],
            "answer": "They use greenlets for asynchronous non-blocking I/O without needing multiple OS thread overhead"
        }
    ],

    "Django": [
        {
            "id": "re_dj_1",
            "difficulty": "Basic",
            "q": "Which Django architectural pattern organizes the application into Models, Views, and Templates?",
            "options": ["MVT (Model-View-Template)", "MVC (Model-View-Controller)", "MVVM", "Microservices"],
            "answer": "MVT (Model-View-Template)"
        },
        {
            "id": "re_dj_2",
            "difficulty": "Beginner",
            "q": "Which command in Django creates new database migration scripts based on changes detected in `models.py`?",
            "options": ["python manage.py makemigrations", "python manage.py migrate", "python manage.py buildmodels", "python manage.py dbupdate"],
            "answer": "python manage.py makemigrations"
        },
        {
            "id": "re_dj_3",
            "difficulty": "Intermediate",
            "q": "Which ORM method in Django prevents N+1 query problems when accessing related ForeignKey objects by performing SQL JOINs?",
            "options": ["select_related()", "prefetch_related()", "filter_related()", "join_related()"],
            "answer": "select_related()"
        },
        {
            "id": "re_dj_4",
            "difficulty": "Advanced",
            "q": "How does Django Middleware process incoming HTTP requests and outgoing HTTP responses?",
            "options": [
                "Through a chain of callables executing `process_request`, `process_view`, and `process_response` in order",
                "By executing background Celery tasks asynchronously",
                "By compiling URL patterns into regex trees during startup",
                "Through direct database triggers"
            ],
            "answer": "Through a chain of callables executing `process_request`, `process_view`, and `process_response` in order"
        },
        {
            "id": "re_dj_5",
            "difficulty": "Expert",
            "q": "In high-traffic Django production environments, how does `atomic()` transaction management interact with database savepoints during nested database writes?",
            "options": [
                "It creates internal SQL SAVEPOINT instances that allow partial rollbacks of nested blocks without aborting the outer transaction",
                "It disables database locks for outer blocks",
                "It automatically commits transactions after every model `save()` call regardless of exceptions",
                "It writes changes to local JSON log files before updating PostgreSQL"
            ],
            "answer": "It creates internal SQL SAVEPOINT instances that allow partial rollbacks of nested blocks without aborting the outer transaction"
        }
    ],

    "REST API": [
        {
            "id": "re_rest_1",
            "difficulty": "Basic",
            "q": "Which HTTP method is typically used to create a new resource on a RESTful server?",
            "options": ["POST", "GET", "PUT", "DELETE"],
            "answer": "POST"
        },
        {
            "id": "re_rest_2",
            "difficulty": "Beginner",
            "q": "Which HTTP status code category represents successful client requests (e.g. 200 OK, 201 Created)?",
            "options": ["2xx", "4xx", "5xx", "3xx"],
            "answer": "2xx"
        },
        {
            "id": "re_rest_3",
            "difficulty": "Intermediate",
            "q": "What property of REST API endpoints guarantees that making multiple identical requests yields the same server state as a single request?",
            "options": ["Idempotency", "Statelessness", "Caching", "Coupling"],
            "answer": "Idempotency"
        },
        {
            "id": "re_rest_4",
            "difficulty": "Advanced",
            "q": "What web standard token format is commonly used for stateless authentication in REST APIs?",
            "options": ["JWT (JSON Web Token)", "XML SAML", "OAuth Session Cookie", "Base64 String"],
            "answer": "JWT (JSON Web Token)"
        },
        {
            "id": "re_rest_5",
            "difficulty": "Expert",
            "q": "In REST architecture, what principle (HATEOAS) mandates that clients navigate API resources dynamically via hypermedia links included in responses?",
            "options": [
                "Hypermedia As The Engine Of Application State",
                "Heterogeneous API Transport Protocol for Open Systems",
                "Hierarchical Application Tracking and Orchestration Service",
                "High Availability Transport Encoding for Object Storage"
            ],
            "answer": "Hypermedia As The Engine Of Application State"
        }
    ],

    "HTML": [
        {
            "id": "re_html_1",
            "difficulty": "Basic",
            "q": "Which HTML tag is used to create a hyperlink to another web page?",
            "options": ["<a>", "<link>", "<href>", "<url>"],
            "answer": "<a>"
        },
        {
            "id": "re_html_2",
            "difficulty": "Beginner",
            "q": "Which semantic HTML5 element represents self-contained content such as a blog post or news item?",
            "options": ["<article>", "<section>", "<div>", "<aside>"],
            "answer": "<article>"
        },
        {
            "id": "re_html_3",
            "difficulty": "Intermediate",
            "q": "What attribute on an `<img>` element provides alternative text for screen readers and missing images?",
            "options": ["alt", "title", "src", "caption"],
            "answer": "alt"
        },
        {
            "id": "re_html_4",
            "difficulty": "Advanced",
            "q": "What is the primary operational difference between `<script defer>` and `<script async>` loading in HTML5?",
            "options": [
                "`defer` downloads scripts in parallel and executes them in document order after HTML parsing; `async` downloads in parallel and executes immediately when ready, interrupting parsing",
                "`async` executes scripts after DOMContentLoaded event; `defer` executes before document creation",
                "`defer` works only with external files; `async` works only with inline script tags",
                "There is no operational difference"
            ],
            "answer": "`defer` downloads scripts in parallel and executes them in document order after HTML parsing; `async` downloads in parallel and executes immediately when ready, interrupting parsing"
        },
        {
            "id": "re_html_5",
            "difficulty": "Expert",
            "q": "How does the HTML5 Web Components standard (Custom Elements + Shadow DOM + HTML Templates) achieve true encapsulation?",
            "options": [
                "Shadow DOM scopes DOM trees and CSS styles so internal styles do not bleed out and external styles do not leak in",
                "Custom Elements compile template markup into WebAssembly bytecode",
                "HTML Templates automatically sandbox JavaScript execution in isolated web workers",
                "By requiring HTTPS client certificates for element rendering"
            ],
            "answer": "Shadow DOM scopes DOM trees and CSS styles so internal styles do not bleed out and external styles do not leak in"
        }
    ],

    "CSS": [
        {
            "id": "re_css_1",
            "difficulty": "Basic",
            "q": "Which CSS property changes the text color of an HTML element?",
            "options": ["color", "text-color", "font-color", "background-color"],
            "answer": "color"
        },
        {
            "id": "re_css_2",
            "difficulty": "Beginner",
            "q": "In the CSS Box Model, what space lies between the content area and the element's border?",
            "options": ["Padding", "Margin", "Outline", "Gap"],
            "answer": "Padding"
        },
        {
            "id": "re_css_3",
            "difficulty": "Intermediate",
            "q": "Which CSS layout module provides a 2D grid-based layout system with rows and columns?",
            "options": ["CSS Grid", "Flexbox", "Float Layout", "Position Absolute"],
            "answer": "CSS Grid"
        },
        {
            "id": "re_css_4",
            "difficulty": "Advanced",
            "q": "How is CSS selector specificity calculated when determining which rule applies to an element?",
            "options": [
                "Inline styles (1000) > IDs (100) > Classes/Attributes/Pseudo-classes (10) > Elements/Pseudo-elements (1)",
                "Elements (100) > Classes (50) > IDs (10) > Inline styles (1)",
                "Order of rule appearance in stylesheet always overrides specificity",
                "Number of words in selector string"
            ],
            "answer": "Inline styles (1000) > IDs (100) > Classes/Attributes/Pseudo-classes (10) > Elements/Pseudo-elements (1)"
        },
        {
            "id": "re_css_5",
            "difficulty": "Expert",
            "q": "What triggers a GPU-accelerated Composite Layer creation in modern browser rendering engines (Blink/WebKit)?",
            "options": [
                "Applying `transform: translateZ(0)` or `will-change: transform` to force hardware composition off main thread",
                "Setting `position: relative` with high z-index",
                "Increasing element padding and margin properties",
                "Using CSS Grid with auto-fill minmax repeat functions"
            ],
            "answer": "Applying `transform: translateZ(0)` or `will-change: transform` to force hardware composition off main thread"
        }
    ],

    "JavaScript": [
        {
            "id": "re_js_1",
            "difficulty": "Basic",
            "q": "Which keyword in modern JavaScript declares a block-scoped variable that can be reassigned?",
            "options": ["let", "const", "var", "static"],
            "answer": "let"
        },
        {
            "id": "re_js_2",
            "difficulty": "Beginner",
            "q": "What method converts a JavaScript object or value into a JSON formatted string?",
            "options": ["JSON.stringify()", "JSON.parse()", "Object.toJSON()", "String.fromJSON()"],
            "answer": "JSON.stringify()"
        },
        {
            "id": "re_js_3",
            "difficulty": "Intermediate",
            "q": "What JavaScript feature allows an inner function to retain access to variables defined in its outer lexical scope even after the outer function has returned?",
            "options": ["Closure", "Callback", "Promise", "Generator"],
            "answer": "Closure"
        },
        {
            "id": "re_js_4",
            "difficulty": "Advanced",
            "q": "How does the JavaScript Event Loop handle execution between the Call Stack, Microtask Queue, and Macrotask (Task) Queue?",
            "options": [
                "Microtasks (Promises, process.nextTick) are fully drained after each Call Stack execution before the next Macrotask (setTimeout, I/O) is processed",
                "Macrotasks take precedence over Microtasks in all execution ticks",
                "Microtasks and Macrotasks execute simultaneously on web worker threads",
                "Tasks are picked randomly from queues based on memory size"
            ],
            "answer": "Microtasks (Promises, process.nextTick) are fully drained after each Call Stack execution before the next Macrotask (setTimeout, I/O) is processed"
        },
        {
            "id": "re_js_5",
            "difficulty": "Expert",
            "q": "In V8 Engine optimization, what causes a JavaScript function to be de-optimized ('bailed out') back to unoptimized Ignition bytecode from TurboFan machine code?",
            "options": [
                "Type Mutation / Polymorphic inline caches breaking monomorphic call site assumptions",
                "Calling console.log() inside tight loops",
                "Using ES6 arrow functions instead of function declarations",
                "Declaring let variables inside if statements"
            ],
            "answer": "Type Mutation / Polymorphic inline caches breaking monomorphic call site assumptions"
        }
    ],

    "React.js": [
        {
            "id": "re_react_1",
            "difficulty": "Basic",
            "q": "Which React Hook is used to add and manage local component state in functional components?",
            "options": ["useState", "useEffect", "useContext", "useReducer"],
            "answer": "useState"
        },
        {
            "id": "re_react_2",
            "difficulty": "Beginner",
            "q": "What syntax extension allows writing HTML-like tags directly inside JavaScript React files?",
            "options": ["JSX", "TSX", "JSON", "HTMLX"],
            "answer": "JSX"
        },
        {
            "id": "re_react_3",
            "difficulty": "Intermediate",
            "q": "Which Hook should be used to memoize expensive calculation results between renders in React?",
            "options": ["useMemo", "useCallback", "useRef", "useImperativeHandle"],
            "answer": "useMemo"
        },
        {
            "id": "re_react_4",
            "difficulty": "Advanced",
            "q": "How does React's Virtual DOM Reconciliation algorithm (Fiber) optimize UI updates?",
            "options": [
                "By computing a diff between new and old Fiber trees and batching minimal real DOM mutations",
                "By directly mutating real DOM nodes in real time during state changes",
                "By reloading the entire web page on component updates",
                "By compiling components to WebAssembly"
            ],
            "answer": "By computing a diff between new and old Fiber trees and batching minimal real DOM mutations"
        },
        {
            "id": "re_react_5",
            "difficulty": "Expert",
            "q": "In React 18 Concurrent Rendering, how do `useTransition` and `useDeferredValue` prevent input lag during heavy UI updates?",
            "options": [
                "By marking state updates as non-urgent transitions, allowing high-priority user events (clicks/typing) to interrupt rendering",
                "By executing state updates on secondary web worker threads",
                "By disabling component re-renders completely until idle",
                "By converting functional components into class components"
            ],
            "answer": "By marking state updates as non-urgent transitions, allowing high-priority user events (clicks/typing) to interrupt rendering"
        }
    ],

    "C++": [
        {
            "id": "re_cpp_1",
            "difficulty": "Basic",
            "q": "Which keyword in C++ is used to instantiate memory on the heap?",
            "options": ["new", "malloc", "create", "alloc"],
            "answer": "new"
        },
        {
            "id": "re_cpp_2",
            "difficulty": "Beginner",
            "q": "Which STL container in C++ implements a contiguous array that supports fast O(1) random access?",
            "options": ["std::vector", "std::list", "std::set", "std::map"],
            "answer": "std::vector"
        },
        {
            "id": "re_cpp_3",
            "difficulty": "Intermediate",
            "q": "Which smart pointer in C++11 enforces exclusive single ownership of a dynamically allocated object?",
            "options": ["std::unique_ptr", "std::shared_ptr", "std::weak_ptr", "std::auto_ptr"],
            "answer": "std::unique_ptr"
        },
        {
            "id": "re_cpp_4",
            "difficulty": "Advanced",
            "q": "What feature in C++ enables Move Semantics to eliminate unnecessary deep copying of temporary objects?",
            "options": ["Rvalue References (&&) and std::move", "Lvalue References (&)", "Const pointers", "Virtual Functions"],
            "answer": "Rvalue References (&&) and std::move"
        },
        {
            "id": "re_cpp_5",
            "difficulty": "Expert",
            "q": "How does Vtable (Virtual Table) dispatch work in C++ when invoking a virtual function via a base class pointer?",
            "options": [
                "The object contains a hidden `vptr` pointing to a class-wide Vtable array of function pointers resolved at runtime",
                "The compiler replaces virtual functions with inline macros at compile time",
                "The OS kernel dispatches virtual functions using CPU interrupt tables",
                "Virtual function calls are evaluated via string hash maps"
            ],
            "answer": "The object contains a hidden `vptr` pointing to a class-wide Vtable array of function pointers resolved at runtime"
        }
    ],

    "C": [
        {
            "id": "re_c_1",
            "difficulty": "Basic",
            "q": "Which operator returns the memory address of a variable in C?",
            "options": ["&", "*", "->", "."],
            "answer": "&"
        },
        {
            "id": "re_c_2",
            "difficulty": "Beginner",
            "q": "Which header file must be included in C to use functions like `printf()` and `scanf()`?",
            "options": ["<stdio.h>", "<stdlib.h>", "<string.h>", "<math.h>"],
            "answer": "<stdio.h>"
        },
        {
            "id": "re_c_3",
            "difficulty": "Intermediate",
            "q": "What occurs when attempting to access memory through an uninitialized or NULL pointer in C?",
            "options": ["Segmentation Fault (SIGSEGV)", "Stack Overflow", "Compilation Warning only", "Memory Leak"],
            "answer": "Segmentation Fault (SIGSEGV)"
        },
        {
            "id": "re_c_4",
            "difficulty": "Advanced",
            "q": "What is the function of the `volatile` keyword when qualifying a variable declaration in C?",
            "options": [
                "Prevents the compiler from optimizing out reads/writes, forcing direct memory access on every invocation (e.g. for hardware registers)",
                "Allocates memory in CPU registers for maximum speed",
                "Restricts variable modification to read-only constant status",
                "Encapsulates variable scope within thread storage"
            ],
            "answer": "Prevents the compiler from optimizing out reads/writes, forcing direct memory access on every invocation (e.g. for hardware registers)"
        },
        {
            "id": "re_c_5",
            "difficulty": "Expert",
            "q": "In bare-metal embedded Systems, how does strict memory alignment (e.g. `__attribute__((aligned(16)))`) affect SIMD vector operations?",
            "options": [
                "It enables single-instruction hardware vector loads (e.g. AVX/NEON) without triggering unaligned memory access traps",
                "It reduces program binary size by compressing instructions",
                "It automatically encrypts pointers stored in memory",
                "It turns dynamic memory allocation into static stack variables"
            ],
            "answer": "It enables single-instruction hardware vector loads (e.g. AVX/NEON) without triggering unaligned memory access traps"
        }
    ],

    "Java": [
        {
            "id": "re_java_1",
            "difficulty": "Basic",
            "q": "Which component of Java converts compiled bytecode (.class files) into native machine instructions at runtime?",
            "options": ["JVM (Java Virtual Machine)", "JDK", "JRE", "Javac"],
            "answer": "JVM (Java Virtual Machine)"
        },
        {
            "id": "re_java_2",
            "difficulty": "Beginner",
            "q": "Which interface in the Java Collections Framework represents an ordered collection that allows duplicate elements?",
            "options": ["List", "Set", "Map", "Queue"],
            "answer": "List"
        },
        {
            "id": "re_java_3",
            "difficulty": "Intermediate",
            "q": "What keyword is used in Java to enforce mutual exclusion across thread execution of a method or block?",
            "options": ["synchronized", "volatile", "transient", "final"],
            "answer": "synchronized"
        },
        {
            "id": "re_java_4",
            "difficulty": "Advanced",
            "q": "What is the key functional difference between `HashMap` and `ConcurrentHashMap` in Java?",
            "options": [
                "`ConcurrentHashMap` achieves thread safety using lock striping / bucket-level locking; `HashMap` is non-thread-safe",
                "`HashMap` locks the entire database; `ConcurrentHashMap` locks single objects",
                "`HashMap` allows duplicate keys; `ConcurrentHashMap` does not",
                "`ConcurrentHashMap` stores data on disk; `HashMap` stores data in RAM"
            ],
            "answer": "`ConcurrentHashMap` achieves thread safety using lock striping / bucket-level locking; `HashMap` is non-thread-safe"
        },
        {
            "id": "re_java_5",
            "difficulty": "Expert",
            "q": "How does the Z Garbage Collector (ZGC) in modern Java (JDK 15+) achieve low pause times (<1ms) even on terabyte heaps?",
            "options": [
                "By using colored pointers and load barriers to perform concurrent marking and compaction while application threads run",
                "By disabling heap allocations for short-lived objects",
                "By delegating memory management entirely to OS swap space",
                "By compiling all Java code ahead-of-time (AOT) into assembly"
            ],
            "answer": "By using colored pointers and load barriers to perform concurrent marking and compaction while application threads run"
        }
    ],

    "Machine Learning": [
        {
            "id": "re_ml_1",
            "difficulty": "Basic",
            "q": "Which type of machine learning uses labeled training data to predict continuous numerical targets?",
            "options": ["Supervised Learning (Regression)", "Unsupervised Learning (Clustering)", "Reinforcement Learning", "Self-Supervised Learning"],
            "answer": "Supervised Learning (Regression)"
        },
        {
            "id": "re_ml_2",
            "difficulty": "Beginner",
            "q": "What condition occurs when a machine learning model fits training data too closely and performs poorly on unseen test data?",
            "options": ["Overfitting", "Underfitting", "Convergence", "Generalization"],
            "answer": "Overfitting"
        },
        {
            "id": "re_ml_3",
            "difficulty": "Intermediate",
            "q": "Which evaluation metric represents the harmonic mean of Precision and Recall?",
            "options": ["F1-Score", "Accuracy", "ROC-AUC", "Mean Squared Error"],
            "answer": "F1-Score"
        },
        {
            "id": "re_ml_4",
            "difficulty": "Advanced",
            "q": "What is the structural difference between Bagging (e.g. Random Forest) and Boosting (e.g. XGBoost)?",
            "options": [
                "Bagging trains weak learners independently in parallel; Boosting trains weak learners sequentially to correct previous errors",
                "Boosting trains models in parallel; Bagging trains models sequentially",
                "Bagging works only for regression; Boosting works only for classification",
                "Boosting eliminates feature selection requirements"
            ],
            "answer": "Bagging trains weak learners independently in parallel; Boosting trains weak learners sequentially to correct previous errors"
        },
        {
            "id": "re_ml_5",
            "difficulty": "Expert",
            "q": "How does SHAP (SHapley Additive exPlanations) calculate feature importance values for complex black-box machine learning models?",
            "options": [
                "By computing marginal contributions of each feature across all possible sub-coalitions using game theory",
                "By calculating linear correlation coefficients with the target variable",
                "By setting feature weights to zero during training iterations",
                "By training a single decision tree on predictions"
            ],
            "answer": "By computing marginal contributions of each feature across all possible sub-coalitions using game theory"
        }
    ],

    "Deep Learning": [
        {
            "id": "re_dl_1",
            "difficulty": "Basic",
            "q": "Which activation function outputs values between 0 and 1, often used in the output layer for binary classification?",
            "options": ["Sigmoid", "ReLU", "Tanh", "Leaky ReLU"],
            "answer": "Sigmoid"
        },
        {
            "id": "re_dl_2",
            "difficulty": "Beginner",
            "q": "Which neural network architecture is specially suited for spatial grid data like images?",
            "options": ["Convolutional Neural Network (CNN)", "Recurrent Neural Network (RNN)", "Multi-Layer Perceptron (MLP)", "Self-Organizing Map"],
            "answer": "Convolutional Neural Network (CNN)"
        },
        {
            "id": "re_dl_3",
            "difficulty": "Intermediate",
            "q": "What regularization technique randomly deactivates a fraction of neurons during training to prevent co-adaptation?",
            "options": ["Dropout", "Batch Normalization", "L2 Weight Decay", "Gradient Clipping"],
            "answer": "Dropout"
        },
        {
            "id": "re_dl_4",
            "difficulty": "Advanced",
            "q": "What attention mechanism in Transformer models allows tokens to compute contextual relationships with all other tokens in a sequence?",
            "options": ["Scaled Dot-Product Self-Attention", "Additive Bahdanau Attention", "Spatial Convolutional Attention", "Recurrent Cell Gating"],
            "answer": "Scaled Dot-Product Self-Attention"
        },
        {
            "id": "re_dl_5",
            "difficulty": "Expert",
            "q": "How does FlashAttention optimize the computation of Self-Attention on modern GPUs (e.g. NVIDIA A100)?",
            "options": [
                "By tiling attention queries/keys/values to fit inside fast GPU SRAM without materializing large N x N attention matrices in High-Bandwidth Memory (HBM)",
                "By quantizing all float32 weights into binary 1-bit representations",
                "By skipping soft-max calculations completely",
                "By delegating attention calculations to CPU host memory"
            ],
            "answer": "By tiling attention queries/keys/values to fit inside fast GPU SRAM without materializing large N x N attention matrices in High-Bandwidth Memory (HBM)"
        }
    ],

    "Linear Algebra": [
        {
            "id": "re_la_1",
            "difficulty": "Basic",
            "q": "What operation combines two vectors by multiplying corresponding components and summing the products?",
            "options": ["Dot Product (Inner Product)", "Cross Product", "Outer Product", "Determinant"],
            "answer": "Dot Product (Inner Product)"
        },
        {
            "id": "re_la_2",
            "difficulty": "Beginner",
            "q": "What is a matrix called if its transpose is equal to its original matrix ($A^T = A$)?",
            "options": ["Symmetric Matrix", "Identity Matrix", "Orthogonal Matrix", "Singular Matrix"],
            "answer": "Symmetric Matrix"
        },
        {
            "id": "re_la_3",
            "difficulty": "Intermediate",
            "q": "In the equation $A v = \\lambda v$, what do $v$ and $\\lambda$ represent for matrix $A$?",
            "options": ["$v$ is Eigenvector; $\\lambda$ is Eigenvalue", "$v$ is Singular Vector; $\\lambda$ is Variance", "$v$ is Normal Vector; $\\lambda$ is Gradient", "$v$ is Constant; $\\lambda$ is Scalar"],
            "answer": "$v$ is Eigenvector; $\\lambda$ is Eigenvalue"
        },
        {
            "id": "re_la_4",
            "difficulty": "Advanced",
            "q": "What factorization technique decomposes any real matrix $A$ into $U \\Sigma V^T$?",
            "options": ["Singular Value Decomposition (SVD)", "LU Decomposition", "QR Factorization", "Cholesky Decomposition"],
            "answer": "Singular Value Decomposition (SVD)"
        },
        {
            "id": "re_la_5",
            "difficulty": "Expert",
            "q": "How does Principal Component Analysis (PCA) utilize Eigen-decomposition of the Covariance Matrix to reduce dimensionality?",
            "options": [
                "By projecting data onto orthogonal eigenvectors corresponding to the largest eigenvalues to maximize preserved variance",
                "By eliminating negative values from input feature matrices",
                "By computing non-linear kernel transformations in infinite dimensional Hilbert spaces",
                "By zeroing out diagonal elements of the distance matrix"
            ],
            "answer": "By projecting data onto orthogonal eigenvectors corresponding to the largest eigenvalues to maximize preserved variance"
        }
    ],

    "Big Data": [
        {
            "id": "re_bd_1",
            "difficulty": "Basic",
            "q": "Which distributed storage component of Apache Hadoop breaks large files into blocks and stores them across cluster nodes?",
            "options": ["HDFS (Hadoop Distributed File System)", "YARN", "MapReduce", "Hive"],
            "answer": "HDFS (Hadoop Distributed File System)"
        },
        {
            "id": "re_bd_2",
            "difficulty": "Beginner",
            "q": "Which Apache framework processes large-scale data streams in real time with high throughput and low latency?",
            "options": ["Apache Kafka", "Apache Sqoop", "Apache Flume", "Apache Oozie"],
            "answer": "Apache Kafka"
        },
        {
            "id": "re_bd_3",
            "difficulty": "Intermediate",
            "q": "What columnar file format is optimized for fast big data analytics queries in Apache Spark and Hive?",
            "options": ["Apache Parquet", "CSV", "JSON", "TXT"],
            "answer": "Apache Parquet"
        },
        {
            "id": "re_bd_4",
            "difficulty": "Advanced",
            "q": "What architectural model combines batch and real-time stream processing layers (Lambda / Kappa Architecture)?",
            "options": [
                "Lambda processes batch and speed layers in parallel; Kappa processes all data through a single stream engine",
                "Kappa processes batch only; Lambda processes streaming only",
                "Lambda uses relational databases; Kappa uses flat files",
                "There is no difference between them"
            ],
            "answer": "Lambda processes batch and speed layers in parallel; Kappa processes all data through a single stream engine"
        },
        {
            "id": "re_bd_5",
            "difficulty": "Expert",
            "q": "When optimizing a multi-terabyte Spark join, why is Broadcast Hash Join preferred over Shuffle Hash Join?",
            "options": [
                "It broadcasts the smaller dataset to all executor nodes, avoiding expensive network shuffles of the large dataset",
                "It writes shuffle spill files directly to local SSDs",
                "It disables memory garbage collection during join operations",
                "It converts Spark DataFrames into single-threaded Python dictionaries"
            ],
            "answer": "It broadcasts the smaller dataset to all executor nodes, avoiding expensive network shuffles of the large dataset"
        }
    ],

    "Computer Network": [
        {
            "id": "re_cn_1",
            "difficulty": "Basic",
            "q": "Which layer of the OSI model handles logical IP addressing and packet routing across network nodes?",
            "options": ["Network Layer (Layer 3)", "Transport Layer (Layer 4)", "Data Link Layer (Layer 2)", "Application Layer (Layer 7)"],
            "answer": "Network Layer (Layer 3)"
        },
        {
            "id": "re_cn_2",
            "difficulty": "Beginner",
            "q": "Which transport protocol provides reliable, connection-oriented data transmission with error checking and flow control?",
            "options": ["TCP (Transmission Control Protocol)", "UDP (User Datagram Protocol)", "ICMP", "IP"],
            "answer": "TCP (Transmission Control Protocol)"
        },
        {
            "id": "re_cn_3",
            "difficulty": "Intermediate",
            "q": "Which network protocol translates domain names (e.g. www.example.com) into numerical IP addresses?",
            "options": ["DNS (Domain Name System)", "DHCP", "ARP", "NAT"],
            "answer": "DNS (Domain Name System)"
        },
        {
            "id": "re_cn_4",
            "difficulty": "Advanced",
            "q": "How does the TCP 3-Way Handshake establish a connection between client and server?",
            "options": [
                "Client sends SYN -> Server responds SYN-ACK -> Client sends ACK",
                "Client sends ACK -> Server responds SYN -> Client sends FIN",
                "Server sends SYN -> Client responds ACK -> Server sends CONNECT",
                "Client sends DATA -> Server responds RECEIVE -> Client sends DONE"
            ],
            "answer": "Client sends SYN -> Server responds SYN-ACK -> Client sends ACK"
        },
        {
            "id": "re_cn_5",
            "difficulty": "Expert",
            "q": "How does BGP (Border Gateway Protocol) prevent routing loops across Autonomous Systems (AS) on the global internet?",
            "options": [
                "By tracking the complete AS-PATH attribute in route advertisements and rejecting updates containing its own AS number",
                "By enforcing maximum hop counts of 15 like RIP",
                "By pinging all global routers every 10 seconds",
                "By using centralized SDN domain controllers"
            ],
            "answer": "By tracking the complete AS-PATH attribute in route advertisements and rejecting updates containing its own AS number"
        }
    ],

    "OS": [
        {
            "id": "re_os_1",
            "difficulty": "Basic",
            "q": "What mechanism in an Operating System switches CPU context from execution in user mode to kernel mode?",
            "options": ["System Call / Interrupt", "Thread Join", "Process Kill", "Memory Allocation"],
            "answer": "System Call / Interrupt"
        },
        {
            "id": "re_os_2",
            "difficulty": "Beginner",
            "q": "What CPU scheduling algorithm assigns CPU time to processes in equal time slices round-robin?",
            "options": ["Round Robin (RR)", "First-Come, First-Served (FCFS)", "Shortest Job First (SJF)", "Priority Scheduling"],
            "answer": "Round Robin (RR)"
        },
        {
            "id": "re_os_3",
            "difficulty": "Intermediate",
            "q": "What condition occurs when two or more processes are permanently blocked waiting for resources held by each other?",
            "options": ["Deadlock", "Starvation", "Race Condition", "Thrashing"],
            "answer": "Deadlock"
        },
        {
            "id": "re_os_4",
            "difficulty": "Advanced",
            "q": "What algorithm is used by operating systems to safely avoid deadlocks by analyzing resource allocation states?",
            "options": ["Banker's Algorithm", "Peterson's Algorithm", "Dijkstra's Algorithm", "Page Replacement LRU"],
            "answer": "Banker's Algorithm"
        },
        {
            "id": "re_os_5",
            "difficulty": "Expert",
            "q": "In Virtual Memory management, what causes 'Thrashing' and how do OS kernels mitigate it using Working Set Models?",
            "options": [
                "Paging overhead dominates CPU time because total working set size exceeds physical RAM; mitigated by swapping out entire low-priority processes",
                "Disk fragmentation causing bad sector read errors",
                "CPU cache line invalidation during multithreading",
                "Kernel panic caused by corrupted page tables"
            ],
            "answer": "Paging overhead dominates CPU time because total working set size exceeds physical RAM; mitigated by swapping out entire low-priority processes"
        }
    ],

    "Cyber Security Fundamentals": [
        {
            "id": "re_sec_1",
            "difficulty": "Basic",
            "q": "What does the CIA triad stand for in information security?",
            "options": [
                "Confidentiality, Integrity, Availability",
                "Control, Identification, Authentication",
                "Cyber, Information, Assets",
                "Certificates, Inspection, Authorization"
            ],
            "answer": "Confidentiality, Integrity, Availability"
        },
        {
            "id": "re_sec_2",
            "difficulty": "Beginner",
            "q": "What social engineering attack tricks users into revealing sensitive credentials via deceptive emails?",
            "options": ["Phishing", "Man-in-the-Middle", "SQL Injection", "DDoS"],
            "answer": "Phishing"
        },
        {
            "id": "re_sec_3",
            "difficulty": "Intermediate",
            "q": "Which security control mandates that users and systems receive only the minimum permissions necessary to perform their duties?",
            "options": ["Principle of Least Privilege", "Defense in Depth", "Zero Trust", "Separation of Duties"],
            "answer": "Principle of Least Privilege"
        },
        {
            "id": "re_sec_4",
            "difficulty": "Advanced",
            "q": "What framework architecture assumes no user or network location is inherently trusted, requiring verification for every access request?",
            "options": ["Zero Trust Architecture (ZTA)", "Perimeter Defense Model", "Air-Gapped Network", "Demilitarized Zone (DMZ)"],
            "answer": "Zero Trust Architecture (ZTA)"
        },
        {
            "id": "re_sec_5",
            "difficulty": "Expert",
            "q": "In enterprise SIEM security operations, how does Automated Threat Hunting utilize MITRE ATT&CK TTP mapping to detect advanced persistent threats (APTs)?",
            "options": [
                "By correlating endpoint telemetry logs against adversary tactics, techniques, and procedures across attack stages",
                "By blocking all incoming external network packets at the firewall level",
                "By running daily antivirus file scans on domain controllers",
                "By resetting domain administrator passwords automatically every hour"
            ],
            "answer": "By correlating endpoint telemetry logs against adversary tactics, techniques, and procedures across attack stages"
        }
    ],

    "Ethical Hacking": [
        {
            "id": "re_eh_1",
            "difficulty": "Basic",
            "q": "Which open-source tool is widely used for network discovery, port scanning, and vulnerability auditing?",
            "options": ["Nmap", "Wireshark", "Burp Suite", "Metasploit"],
            "answer": "Nmap"
        },
        {
            "id": "re_eh_2",
            "difficulty": "Beginner",
            "q": "What web application vulnerability allows attackers to inject malicious scripts into trusted websites executed by user browsers?",
            "options": ["Cross-Site Scripting (XSS)", "SQL Injection (SQLi)", "Cross-Site Request Forgery (CSRF)", "Buffer Overflow"],
            "answer": "Cross-Site Scripting (XSS)"
        },
        {
            "id": "re_eh_3",
            "difficulty": "Intermediate",
            "q": "Which penetration testing framework is standard for developing, testing, and executing exploit code against remote targets?",
            "options": ["Metasploit Framework", "John the Ripper", "Hydra", "OWASP ZAP"],
            "answer": "Metasploit Framework"
        },
        {
            "id": "re_eh_4",
            "difficulty": "Advanced",
            "q": "How does a Blind SQL Injection attack differ from an In-Band (Error-based) SQL Injection attack?",
            "options": [
                "Blind SQLi returns no error messages or data directly in HTTP responses; performance/boolean responses must be inferred byte-by-byte",
                "Blind SQLi requires physical access to database hardware",
                "In-Band SQLi cannot extract database contents",
                "Blind SQLi works only over encrypted HTTPS connections"
            ],
            "answer": "Blind SQLi returns no error messages or data directly in HTTP responses; performance/boolean responses must be inferred byte-by-byte"
        },
        {
            "id": "re_eh_5",
            "difficulty": "Expert",
            "q": "In Red Team offensive operations, how does Process Hollowing bypass EDR (Endpoint Detection and Response) memory hooks?",
            "options": [
                "By spawning a legitimate process in suspended state, unmapping its code section, writing malicious payload memory, and resuming thread execution",
                "By disabling host network interface card drivers",
                "By deleting Windows Event Log files",
                "By modifying local hosts DNS files"
            ],
            "answer": "By spawning a legitimate process in suspended state, unmapping its code section, writing malicious payload memory, and resuming thread execution"
        }
    ],

    "Vulnerability Assessment": [
        {
            "id": "re_va_1",
            "difficulty": "Basic",
            "q": "Which standard scoring system provides an open industry metric for assessing the severity of computer system vulnerabilities?",
            "options": ["CVSS (Common Vulnerability Scoring System)", "CVE", "CWE", "NIST"],
            "answer": "CVSS (Common Vulnerability Scoring System)"
        },
        {
            "id": "re_va_2",
            "difficulty": "Beginner",
            "q": "What automated scanner is widely deployed to perform credentialed and non-credentialed vulnerability scans across networks?",
            "options": ["Nessus", "Wireshark", "Hashcat", "Putty"],
            "answer": "Nessus"
        },
        {
            "id": "re_va_3",
            "difficulty": "Intermediate",
            "q": "What dictionary catalog assigns unique, standardized identifiers to publicly known cybersecurity vulnerabilities?",
            "options": ["CVE (Common Vulnerabilities and Exposures)", "CWE", "CAPEC", "OWASP Top 10"],
            "answer": "CVE (Common Vulnerabilities and Exposures)"
        },
        {
            "id": "re_va_4",
            "difficulty": "Advanced",
            "q": "What is the key functional distinction between Vulnerability Scanning and Penetration Testing?",
            "options": [
                "Vulnerability Scanning automatically identifies potential security flaws; Penetration Testing actively exploits flaws to verify real-world risk and impact",
                "Vulnerability Scanning is manual; Penetration Testing is automated",
                "Vulnerability Scanning is illegal without a court order; Penetration Testing is always legal",
                "Vulnerability Scanning tests hardware only; Penetration Testing tests software only"
            ],
            "answer": "Vulnerability Scanning automatically identifies potential security flaws; Penetration Testing actively exploits flaws to verify real-world risk and impact"
        },
        {
            "id": "re_va_5",
            "difficulty": "Expert",
            "q": "How does Risk-Based Vulnerability Management (RBVM) prioritize patching over traditional CVSS v3.1 base metrics?",
            "options": [
                "By combining CVSS severity with Threat Intelligence (EPSS score, active weaponization in the wild, asset criticality context)",
                "By patching vulnerabilities in alphabetical order of CVE name",
                "By ignoring vulnerabilities on Linux systems",
                "By evaluating patch file size"
            ],
            "answer": "By combining CVSS severity with Threat Intelligence (EPSS score, active weaponization in the wild, asset criticality context)"
        }
    ],

    "Cryptography": [
        {
            "id": "re_crypto_1",
            "difficulty": "Basic",
            "q": "Which symmetric encryption algorithm uses a 128-bit block size and key lengths of 128, 192, or 256 bits as the global standard?",
            "options": ["AES (Advanced Encryption Standard)", "DES", "RSA", "Blowfish"],
            "answer": "AES (Advanced Encryption Standard)"
        },
        {
            "id": "re_crypto_2",
            "difficulty": "Beginner",
            "q": "What type of cryptography uses a public key for encryption and a private key for decryption?",
            "options": ["Asymmetric Cryptography (Public-Key)", "Symmetric Cryptography", "Hashing", "Steganography"],
            "answer": "Asymmetric Cryptography (Public-Key)"
        },
        {
            "id": "re_crypto_3",
            "difficulty": "Intermediate",
            "q": "Which mathematical property ensures that cryptographic hash functions cannot be easily reversed to produce original inputs?",
            "options": ["One-Way Property (Pre-image resistance)", "Reversibility", "Commutativity", "Linearity"],
            "answer": "One-Way Property (Pre-image resistance)"
        },
        {
            "id": "re_crypto_4",
            "difficulty": "Advanced",
            "q": "What cryptographic key exchange protocol allows two parties to establish a shared secret over an insecure channel without transmitting the key?",
            "options": ["Diffie-Hellman Key Exchange", "RSA Encryption", "SHA-256 Hashing", "HMAC Authentication"],
            "answer": "Diffie-Hellman Key Exchange"
        },
        {
            "id": "re_crypto_5",
            "difficulty": "Expert",
            "q": "How does Perfect Forward Secrecy (PFS) in TLS 1.3 protect past session communications if a server's private key is compromised in the future?",
            "options": [
                "By generating ephemeral Diffie-Hellman key pairs for every individual session that are discarded immediately after use",
                "By re-encrypting past session logs on disk every 24 hours",
                "By storing private keys in cloud Hardware Security Modules (HSMs)",
                "By using 4096-bit static RSA keys"
            ],
            "answer": "By generating ephemeral Diffie-Hellman key pairs for every individual session that are discarded immediately after use"
        }
    ],

    "Database Management": [
        {
            "id": "re_db_1",
            "difficulty": "Basic",
            "q": "What property of database transactions ensures that all operations succeed completely or all are rolled back?",
            "options": ["Atomicity", "Consistency", "Isolation", "Durability"],
            "answer": "Atomicity"
        },
        {
            "id": "re_db_2",
            "difficulty": "Beginner",
            "q": "Which normal form eliminates partial dependencies by ensuring all non-key attributes depend on the complete primary key?",
            "options": ["Second Normal Form (2NF)", "First Normal Form (1NF)", "Third Normal Form (3NF)", "BCNF"],
            "answer": "Second Normal Form (2NF)"
        },
        {
            "id": "re_db_3",
            "difficulty": "Intermediate",
            "q": "Which B-Tree index structure speeds up data retrieval in relational databases?",
            "options": ["B+ Tree Index", "Binary Search Tree", "Hash Map", "Flat File"],
            "answer": "B+ Tree Index"
        },
        {
            "id": "re_db_4",
            "difficulty": "Advanced",
            "q": "What transaction isolation level prevents Dirty Reads, Non-Repeatable Reads, and Phantom Reads completely?",
            "options": ["SERIALIZABLE", "REPEATABLE READ", "READ COMMITTED", "READ UNCOMMITTED"],
            "answer": "SERIALIZABLE"
        },
        {
            "id": "re_db_5",
            "difficulty": "Expert",
            "q": "In distributed database architectures, how does the CAP Theorem constrain system design during network partitions?",
            "options": [
                "A system can guarantee at most two of Consistency, Availability, and Partition Tolerance simultaneously during network partitions",
                "All databases achieve 100% Availability and Consistency under all workloads",
                "Consistency can only be achieved using NoSQL document stores",
                "Partition tolerance is only necessary for single-node SQL databases"
            ],
            "answer": "A system can guarantee at most two of Consistency, Availability, and Partition Tolerance simultaneously during network partitions"
        }
    ],

    "Figma": [
        {
            "id": "re_fig_1",
            "difficulty": "Basic",
            "q": "Which core layout feature in Figma allows design frames and buttons to resize dynamically when text content changes?",
            "options": ["Auto Layout", "Smart Animate", "Constraints", "Component Variants"],
            "answer": "Auto Layout"
        },
        {
            "id": "re_fig_2",
            "difficulty": "Beginner",
            "q": "What visual building blocks in Figma allow UI elements to be reused consistently across multiple artboards?",
            "options": ["Components", "Frames", "Groups", "Slices"],
            "answer": "Components"
        },
        {
            "id": "re_fig_3",
            "difficulty": "Intermediate",
            "q": "Which feature in Figma enables grouping component states (e.g. Default, Hover, Active, Disabled) into a single master container?",
            "options": ["Component Variants", "Design Systems", "Styles", "Plugins"],
            "answer": "Component Variants"
        },
        {
            "id": "re_fig_4",
            "difficulty": "Advanced",
            "q": "How does Smart Animate match layers between two prototype frames to generate smooth transitions?",
            "options": [
                "By matching layer names and hierarchy structure across frames",
                "By analyzing pixel color distributions",
                "By converting frames to video files",
                "By requiring custom JavaScript scripts"
            ],
            "answer": "By matching layer names and hierarchy structure across frames"
        },
        {
            "id": "re_fig_5",
            "difficulty": "Expert",
            "q": "How do Design Tokens and Figma Variables (Color, Number, String, Boolean) streamline multi-brand design system updates?",
            "options": [
                "By aliasing core design values to semantic tokens, enabling instant theme switching (e.g. Light/Dark Mode, Brand Themes) across entire UI kits",
                "By exporting CSS files directly to web servers",
                "By generating automatic vector icons from text prompts",
                "By locking layout dimensions on desktop screens"
            ],
            "answer": "By aliasing core design values to semantic tokens, enabling instant theme switching (e.g. Light/Dark Mode, Brand Themes) across entire UI kits"
        }
    ],

    "Wireframing": [
        {
            "id": "re_wf_1",
            "difficulty": "Basic",
            "q": "What is the primary purpose of Low-Fidelity (Low-Fi) Wireframes during the early stages of UI/UX design?",
            "options": [
                "To outline visual structure, layout hierarchy, and user flow without getting distracted by colors and visual details",
                "To showcase final marketing branding visuals to client executives",
                "To test production database backend query speeds",
                "To generate automatic HTML/CSS code"
            ],
            "answer": "To outline visual structure, layout hierarchy, and user flow without getting distracted by colors and visual details"
        },
        {
            "id": "re_wf_2",
            "difficulty": "Beginner",
            "q": "Which structural grid system is standard for designing responsive wireframes on web and mobile screens?",
            "options": ["12-Column Grid", "3-Column Grid", "Diagonal Grid", "Random Pixel Offset"],
            "answer": "12-Column Grid"
        },
        {
            "id": "re_wf_3",
            "difficulty": "Intermediate",
            "q": "What user-centered artifact maps out the sequential steps a user completes to accomplish a task within an app wireframe?",
            "options": ["User Flow Diagram", "Persona Profile", "Site Map", "Empathy Map"],
            "answer": "User Flow Diagram"
        },
        {
            "id": "re_wf_4",
            "difficulty": "Advanced",
            "q": "In wireframe information architecture, what principle dictates placing critical actions and high-value navigation elements above the fold?",
            "options": [
                "Visual Hierarchy & F-Shaped / Z-Shaped Reading Pattern",
                "Color Contrast Compliance",
                "Symmetric Axis Balance",
                "Skinner Box Gamification"
            ],
            "answer": "Visual Hierarchy & F-Shaped / Z-Shaped Reading Pattern"
        },
        {
            "id": "re_wf_5",
            "difficulty": "Expert",
            "q": "How does rapid wireframe paper prototyping with usability testing reduce engineering costs prior to high-fidelity design?",
            "options": [
                "By validating task completion rates and structural navigation flaws before code implementation or detailed UI rendering begins",
                "By eliminating the need for frontend developers",
                "By replacing product requirements documentation completely",
                "By guaranteeing 100% conversion rates on landing pages"
            ],
            "answer": "By validating task completion rates and structural navigation flaws before code implementation or detailed UI rendering begins"
        }
    ],

    "Prototyping": [
        {
            "id": "re_proto_1",
            "difficulty": "Basic",
            "q": "What is an interactive prototype in UI/UX design?",
            "options": [
                "A clickable simulation of user interface interactions and screens",
                "A static printout of design artboards",
                "A written document describing software feature requirements",
                "A live production web application backend"
            ],
            "answer": "A clickable simulation of user interface interactions and screens"
        },
        {
            "id": "re_proto_2",
            "difficulty": "Beginner",
            "q": "Which interaction trigger in UI prototyping tool executes when a user hovers their mouse pointer over a button element?",
            "options": ["While Hovering", "On Click / On Tap", "On Drag", "Key Press"],
            "answer": "While Hovering"
        },
        {
            "id": "re_proto_3",
            "difficulty": "Intermediate",
            "q": "What micro-interaction feedback reassures users that their button click action has been registered by the system?",
            "options": ["Visual Feedback (Button hover state change / loader spinner)", "Page reload", "Displaying raw error log", "Audio alert"],
            "answer": "Visual Feedback (Button hover state change / loader spinner)"
        },
        {
            "id": "re_proto_4",
            "difficulty": "Advanced",
            "q": "What prototyping technique simulates complex conditional logic and variable inputs (e.g., dynamic form validation)?",
            "options": [
                "High-Fidelity Logic Prototyping with Variables & Conditions",
                "Static Screen Hotspots",
                "Animated GIF Overlays",
                "Paper Sketch Swapping"
            ],
            "answer": "High-Fidelity Logic Prototyping with Variables & Conditions"
        },
        {
            "id": "re_proto_5",
            "difficulty": "Expert",
            "q": "How does measuring System Usability Scale (SUS) scores during interactive prototype usability testing inform product iteration?",
            "options": [
                "By providing a standardized 10-item quantitative metric (0-100 score) assessing ease of use, learnability, and user satisfaction",
                "By calculating the exact render time of graphic GPUs",
                "By measuring server CPU load during prototype sessions",
                "By estimating Google Search ranking positions"
            ],
            "answer": "By providing a standardized 10-item quantitative metric (0-100 score) assessing ease of use, learnability, and user satisfaction"
        }
    ],

    "Typography": [
        {
            "id": "re_typo_1",
            "difficulty": "Basic",
            "q": "What type of typeface features small decorative strokes attaching to the main body of letters (e.g. Times New Roman)?",
            "options": ["Serif", "Sans-Serif", "Monospace", "Display"],
            "answer": "Serif"
        },
        {
            "id": "re_typo_2",
            "difficulty": "Beginner",
            "q": "What typographic term refers to adjusting the proportional space between two specific individual characters?",
            "options": ["Kerning", "Tracking", "Leading", "Baseline"],
            "answer": "Kerning"
        },
        {
            "id": "re_typo_3",
            "difficulty": "Intermediate",
            "q": "What typographic term refers to the vertical distance between lines of text in a paragraph?",
            "options": ["Leading (Line Height)", "Tracking", "Kerning", "X-Height"],
            "answer": "Leading (Line Height)"
        },
        {
            "id": "re_typo_4",
            "difficulty": "Advanced",
            "q": "How does establishing a Typographic Scale (e.g. Major Third 1.250 ratio) improve digital visual design?",
            "options": [
                "It creates harmonious, predictable mathematical relationships across heading levels (H1-H6) and body text",
                "It guarantees faster font downloading speeds over 4G networks",
                "It forces all text to fit inside fixed square grid boxes",
                "It converts text into vector shapes"
            ],
            "answer": "It creates harmonious, predictable mathematical relationships across heading levels (H1-H6) and body text"
        },
        {
            "id": "re_typo_5",
            "difficulty": "Expert",
            "q": "How do Variable Fonts (OpenType Font Variations) optimize web typography performance while offering flexible weight and slant axes?",
            "options": [
                "By packaging multiple font weights and styles into a single compact font file file, reducing HTTP requests and overall payload size",
                "By rendering all text using standard browser default system fonts",
                "By converting text into SVG canvas elements",
                "By removing capital letters from font files"
            ],
            "answer": "By packaging multiple font weights and styles into a single compact font file file, reducing HTTP requests and overall payload size"
        }
    ],

    "Color Theory": [
        {
            "id": "re_ct_1",
            "difficulty": "Basic",
            "q": "Which color scheme combines colors positioned directly opposite each other on the color wheel (e.g., Blue and Orange)?",
            "options": ["Complementary", "Analogous", "Monochromatic", "Triadic"],
            "answer": "Complementary"
        },
        {
            "id": "re_ct_2",
            "difficulty": "Beginner",
            "q": "What UI rule suggests using 60% dominant neutral color, 30% secondary structural color, and 10% accent color?",
            "options": ["60-30-10 Rule", "80-20 Rule", "Golden Ratio", "Rule of Thirds"],
            "answer": "60-30-10 Rule"
        },
        {
            "id": "re_ct_3",
            "difficulty": "Intermediate",
            "q": "According to WCAG 2.1 AA accessibility guidelines, what is the minimum required contrast ratio for standard body text against background?",
            "options": ["4.5:1", "3:1", "7:1", "2:1"],
            "answer": "4.5:1"
        },
        {
            "id": "re_ct_4",
            "difficulty": "Advanced",
            "q": "What color space model represents color using Hue, Saturation, and Lightness, making design color palette adjustments intuitive?",
            "options": ["HSL", "RGB", "CMYK", "HEX"],
            "answer": "HSL"
        },
        {
            "id": "re_ct_5",
            "difficulty": "Expert",
            "q": "How do Perceptually Uniform Color Spaces (e.g. OKLCH / CIELAB) solve color blending artifacts found in standard sRGB space?",
            "options": [
                "They align numerical lightness values with human eye perceptual brightness, ensuring smooth gradients and consistent contrast across hues",
                "They increase GPU color processing speed by 50%",
                "They eliminate dark mode theme requirements",
                "They convert 24-bit colors into 8-bit indexed palettes"
            ],
            "answer": "They align numerical lightness values with human eye perceptual brightness, ensuring smooth gradients and consistent contrast across hues"
        }
    ],

    "Cloud Security": [
        {
            "id": "re_cs_1",
            "difficulty": "Basic",
            "q": "In cloud computing, what model defines security obligations split between the Cloud Provider and the Customer?",
            "options": ["Shared Responsibility Model", "Zero Trust Architecture", "Public Cloud Contract", "ISO 27001 Standard"],
            "answer": "Shared Responsibility Model"
        },
        {
            "id": "re_cs_2",
            "difficulty": "Beginner",
            "q": "Which AWS service manages user authentication, authorization, and access control policies?",
            "options": ["AWS IAM (Identity and Access Management)", "AWS KMS", "AWS Shield", "AWS WAF"],
            "answer": "AWS IAM (Identity and Access Management)"
        },
        {
            "id": "re_cs_3",
            "difficulty": "Intermediate",
            "q": "What cloud security tool automatically monitors cloud infrastructure for misconfigurations and compliance violations?",
            "options": ["CSPM (Cloud Security Posture Management)", "CASB", "CWPP", "SIEM"],
            "answer": "CSPM (Cloud Security Posture Management)"
        },
        {
            "id": "re_cs_4",
            "difficulty": "Advanced",
            "q": "How does envelope encryption work in cloud Key Management Services (e.g., AWS KMS)?",
            "options": [
                "Data is encrypted using a unique Data Encryption Key (DEK), and the DEK is encrypted using a Master Key (KMS Key)",
                "Data is encrypted twice using the same password",
                "Master keys are stored in unencrypted S3 buckets",
                "Encryption keys are shared publicly across cloud regions"
            ],
            "answer": "Data is encrypted using a unique Data Encryption Key (DEK), and the DEK is encrypted using a Master Key (KMS Key)"
        },
        {
            "id": "re_cs_5",
            "difficulty": "Expert",
            "q": "In Kubernetes multi-tenant security, how do eBPF-based security agents (e.g. Cilium / Falco) enforce network microsegmentation?",
            "options": [
                "By attaching sandbox programs directly inside Linux kernel socket and syscall probes without injecting sidecar containers",
                "By modifying iptables rules every 5 seconds",
                "By proxying all cluster traffic through external hardware firewalls",
                "By restarting pods whenever an unauthenticated API call is detected"
            ],
            "answer": "By attaching sandbox programs directly inside Linux kernel socket and syscall probes without injecting sidecar containers"
        }
    ],

    "AWS": [
        {
            "id": "re_aws_1",
            "difficulty": "Basic",
            "q": "Which AWS compute service provides resizable virtual server instances in the cloud?",
            "options": ["Amazon EC2", "Amazon S3", "Amazon RDS", "AWS Lambda"],
            "answer": "Amazon EC2"
        },
        {
            "id": "re_aws_2",
            "difficulty": "Beginner",
            "q": "Which AWS serverless compute service executes code automatically in response to events without provisioning servers?",
            "options": ["AWS Lambda", "Amazon ECS", "AWS Fargate", "Amazon Elastic Beanstalk"],
            "answer": "AWS Lambda"
        },
        {
            "id": "re_aws_3",
            "difficulty": "Intermediate",
            "q": "Which AWS service provides high-performance object storage with industry-leading scalability and data availability?",
            "options": ["Amazon S3", "Amazon EBS", "Amazon EFS", "Amazon Glacier"],
            "answer": "Amazon S3"
        },
        {
            "id": "re_aws_4",
            "difficulty": "Advanced",
            "q": "How does Amazon Route 53 DNS Latency-Based Routing direct client web traffic?",
            "options": [
                "By measuring network latency to AWS regions and routing queries to the region providing the lowest response delay for the user",
                "By distributing traffic randomly across all regions",
                "By routing all queries to the US-East-1 primary region",
                "By inspecting client HTTP cookies"
            ],
            "answer": "By measuring network latency to AWS regions and routing queries to the region providing the lowest response delay for the user"
        },
        {
            "id": "re_aws_5",
            "difficulty": "Expert",
            "q": "In multi-region AWS architectures, how does AWS Global Accelerator optimize global application performance over Amazon's private network?",
            "options": [
                "By providing static Anycast IP addresses that route user traffic to the nearest AWS Edge Location and over the private AWS global network",
                "By running local EC2 instances on client devices",
                "By converting all TCP traffic into encrypted email attachments",
                "By bypassing local DNS resolvers completely"
            ],
            "answer": "By providing static Anycast IP addresses that route user traffic to the nearest AWS Edge Location and over the private AWS global network"
        }
    ],

    "DevOps": [
        {
            "id": "re_devops_1",
            "difficulty": "Basic",
            "q": "Which open-source containerization platform packages applications and dependencies into isolated lightweight containers?",
            "options": ["Docker", "Kubernetes", "Jenkins", "Terraform"],
            "answer": "Docker"
        },
        {
            "id": "re_devops_2",
            "difficulty": "Beginner",
            "q": "What Infrastructure as Code (IaC) tool uses declarative configuration files (HCL) to provision cloud infrastructure across providers?",
            "options": ["Terraform", "Ansible", "Puppet", "Chef"],
            "answer": "Terraform"
        },
        {
            "id": "re_devops_3",
            "difficulty": "Intermediate",
            "q": "Which deployment strategy gradually shifts traffic from an old application version to a new version to verify stability?",
            "options": ["Canary Deployment / Blue-Green Deployment", "Recreate Deployment", "In-place Overwrite", "Big Bang Deployment"],
            "answer": "Canary Deployment / Blue-Green Deployment"
        },
        {
            "id": "re_devops_4",
            "difficulty": "Advanced",
            "q": "In GitOps workflows (e.g. using ArgoCD or Flux), what component acts as the single source of truth for cluster state?",
            "options": ["Git Repository", "Docker Registry", "Kubernetes Master API Server", "Jenkins Server"],
            "answer": "Git Repository"
        },
        {
            "id": "re_devops_5",
            "difficulty": "Expert",
            "q": "How does Kubernetes Horizontal Pod Autoscaler (HPA) compute replica scaling requirements based on custom Prometheus metrics?",
            "options": [
                "By querying Custom Metrics APIs and applying formula: `desiredReplicas = ceil[currentReplicas * (currentMetricValue / targetMetricValue)]`",
                "By restarting nodes whenever memory usage hits 90%",
                "By deploying static replica sets on every worker node",
                "By monitoring local SSH connection attempts"
            ],
            "answer": "By querying Custom Metrics APIs and applying formula: `desiredReplicas = ceil[currentReplicas * (currentMetricValue / targetMetricValue)]`"
        }
    ],

    "Networking": [
        {
            "id": "re_net_1",
            "difficulty": "Basic",
            "q": "What protocol dynamically assigns IP addresses, subnet masks, and default gateways to devices on a local network?",
            "options": ["DHCP", "DNS", "ARP", "SNMP"],
            "answer": "DHCP"
        },
        {
            "id": "re_net_2",
            "difficulty": "Beginner",
            "q": "Which network component connects multiple local subnets together and routes traffic based on IP addresses?",
            "options": ["Router", "Switch", "Hub", "Repeater"],
            "answer": "Router"
        },
        {
            "id": "re_net_3",
            "difficulty": "Intermediate",
            "q": "What technology maps private IPv4 addresses from a local area network to a single public IP address for internet access?",
            "options": ["NAT (Network Address Translation)", "VLAN", "VPN", "CIDR"],
            "answer": "NAT (Network Address Translation)"
        },
        {
            "id": "re_net_4",
            "difficulty": "Advanced",
            "q": "What is the CIDR notation mask equivalent to the IPv4 subnet mask `255.255.255.0`?",
            "options": ["/24", "/16", "/32", "/8"],
            "answer": "/24"
        },
        {
            "id": "re_net_5",
            "difficulty": "Expert",
            "q": "How does VXLAN (Virtual Extensible LAN) encapsulate Layer 2 Ethernet frames over Layer 3 IP networks to overcome 4094 VLAN limits?",
            "options": [
                "By adding a 50-byte header containing a 24-bit VXLAN Network Identifier (VNI), supporting up to 16 million virtual networks",
                "By compressing IPv4 packets into IPv6 headers",
                "By encrypting Layer 2 frames with AES-256 keys",
                "By replacing Ethernet switches with optical fiber splitters"
            ],
            "answer": "By adding a 50-byte header containing a 24-bit VXLAN Network Identifier (VNI), supporting up to 16 million virtual networks"
        }
    ],

    "Linux": [
        {
            "id": "re_lx_1",
            "difficulty": "Basic",
            "q": "Which Linux command changes file and directory permissions (e.g. `chmod 755`)?",
            "options": ["chmod", "chown", "chgrp", "ls -l"],
            "answer": "chmod"
        },
        {
            "id": "re_lx_2",
            "difficulty": "Beginner",
            "q": "Which Linux command displays active processes and real-time system resource utilization (CPU, RAM)?",
            "options": ["top / htop", "ps aux", "df -h", "free -m"],
            "answer": "top / htop"
        },
        {
            "id": "re_lx_3",
            "difficulty": "Intermediate",
            "q": "Which system service daemon in modern Linux distributions manages system initialization, services, and log journals?",
            "options": ["systemd", "init.d", "sysvinit", "upstart"],
            "answer": "systemd"
        },
        {
            "id": "re_lx_4",
            "difficulty": "Advanced",
            "q": "What numerical octal permission representation grants `rwxr-xr--` (User: read/write/execute, Group: read/execute, Others: read)?",
            "options": ["754", "777", "644", "755"],
            "answer": "754"
        },
        {
            "id": "re_lx_5",
            "difficulty": "Expert",
            "q": "How do Linux cgroups v2 (Control Groups) and Namespaces combine to isolate container processes?",
            "options": [
                "Namespaces isolate system visibility (PID, NET, MNT, IPC, USER); cgroups constrain hardware resource utilization (CPU, Memory, I/O)",
                "cgroups isolate process IDs; Namespaces encrypt file systems",
                "Namespaces allocate virtual swap space; cgroups manage network ports",
                "cgroups compile kernel modules; Namespaces manage user passwords"
            ],
            "answer": "Namespaces isolate system visibility (PID, NET, MNT, IPC, USER); cgroups constrain hardware resource utilization (CPU, Memory, I/O)"
        }
    ]
}
