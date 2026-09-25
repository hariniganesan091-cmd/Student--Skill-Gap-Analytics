# Script to populate full QUESTIONS_DATA with 255 questions (5 per skill, strictly Basic -> Beginner -> Intermediate -> Advanced -> Expert)

import json
import os

questions_data = {
    "Data Analyst": {
        "Python": [
            {
                "q": "Which Python library is primarily used for data manipulation and structure analysis?",
                "options": ["NumPy", "Pandas", "SciPy", "Matplotlib"],
                "answer": "Pandas",
                "difficulty": "Basic"
            },
            {
                "q": "Which Pandas method is used to remove rows or columns containing missing (NaN) values?",
                "options": ["df.dropna()", "df.fillna()", "df.remove_null()", "df.clean()"],
                "answer": "df.dropna()",
                "difficulty": "Beginner"
            },
            {
                "q": "How do you combine two Pandas DataFrames based on a shared key column, similar to a database JOIN?",
                "options": ["pd.concat()", "pd.merge()", "pd.join_tables()", "pd.append()"],
                "answer": "pd.merge()",
                "difficulty": "Intermediate"
            },
            {
                "q": "What is the result of executing `df.groupby('Category')['Sales'].transform('mean')` on a DataFrame?",
                "options": [
                    "It returns an aggregated DataFrame grouped by Category with mean Sales",
                    "It returns a Series with the same index as df, containing the Category mean for each row",
                    "It modifies the original df in-place by removing non-mean rows",
                    "It throws a KeyError if Category is a string column"
                ],
                "answer": "It returns a Series with the same index as df, containing the Category mean for each row",
                "difficulty": "Advanced"
            },
            {
                "q": "When optimizing a Memory-Constrained Data Analysis pipeline in Pandas handling 10GB+ CSV files, which strategy is most effective?",
                "options": [
                    "Use chunksize in pd.read_csv() and downcast numeric data types with pd.to_numeric()",
                    "Increase Python recursion limit using sys.setrecursionlimit()",
                    "Convert all string columns into standard Python lists before processing",
                    "Call df.apply() recursively on single rows with multithreading"
                ],
                "answer": "Use chunksize in pd.read_csv() and downcast numeric data types with pd.to_numeric()",
                "difficulty": "Expert"
            }
        ],
        "SQL": [
            {
                "q": "Which SQL clause is used to filter records BEFORE any GROUP BY aggregation takes place?",
                "options": ["HAVING", "WHERE", "ORDER BY", "GROUP FILTER"],
                "answer": "WHERE",
                "difficulty": "Basic"
            },
            {
                "q": "Which SQL JOIN type returns all rows from the left table and only matching rows from the right table?",
                "options": ["INNER JOIN", "RIGHT JOIN", "LEFT JOIN", "FULL OUTER JOIN"],
                "answer": "LEFT JOIN",
                "difficulty": "Beginner"
            },
            {
                "q": "Which SQL window function computes a cumulative moving average across ordered rows in a partition?",
                "options": [
                    "AVG(amount) OVER (PARTITION BY category ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)",
                    "SUM(amount) GROUP BY category ORDER BY date",
                    "CUMULATIVE_AVG(amount) BY category",
                    "ROW_NUMBER() OVER (ORDER BY date) * AVG(amount)"
                ],
                "answer": "AVG(amount) OVER (PARTITION BY category ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)",
                "difficulty": "Intermediate"
            },
            {
                "q": "In a data warehouse, what is the key difference between `RANK()` and `DENSE_RANK()` window functions when encountering identical values?",
                "options": [
                    "RANK() skips subsequent rank numbers after ties, whereas DENSE_RANK() assigns consecutive rank numbers without gaps",
                    "DENSE_RANK() skips numbers while RANK() leaves no gaps",
                    "RANK() works only on integer columns, while DENSE_RANK() works on text",
                    "There is no functional difference between RANK() and DENSE_RANK()"
                ],
                "answer": "RANK() skips subsequent rank numbers after ties, whereas DENSE_RANK() assigns consecutive rank numbers without gaps",
                "difficulty": "Advanced"
            },
            {
                "q": "When investigating a slow analytical query featuring multiple correlated subqueries on an unindexed 50M-row table, what query refactoring technique yields the highest performance improvement?",
                "options": [
                    "Replace correlated subqueries with CTEs / Window Functions and create composite B-Tree indexes on join and filter columns",
                    "Add OPTION (RECOMPILE) and replace INNER JOIN with CROSS JOIN",
                    "Wrap the query inside a CURSOR loop and execute fetch next row by row",
                    "Convert all date columns to VARCHAR string format in the WHERE clause"
                ],
                "answer": "Replace correlated subqueries with CTEs / Window Functions and create composite B-Tree indexes on join and filter columns",
                "difficulty": "Expert"
            }
        ],
        "Excel": [
            {
                "q": "Which Excel formula looks up a value in the leftmost column of a table and returns a value in the same row from a specified column?",
                "options": ["HLOOKUP", "VLOOKUP", "CONCATENATE", "COUNTIF"],
                "answer": "VLOOKUP",
                "difficulty": "Basic"
            },
            {
                "q": "What feature in Microsoft Excel allows users to dynamically summarize, group, and explore large datasets without writing formulas?",
                "options": ["Pivot Table", "Data Validation", "Goal Seek", "Solver"],
                "answer": "Pivot Table",
                "difficulty": "Beginner"
            },
            {
                "q": "Which combination of Excel formulas provides a flexible two-way lookup that does not require the lookup column to be the leftmost column?",
                "options": ["INDEX and MATCH", "VLOOKUP and HLOOKUP", "SUMIF and COUNTIF", "INDIRECT and OFFSET"],
                "answer": "INDEX and MATCH",
                "difficulty": "Intermediate"
            },
            {
                "q": "What array formula or dynamic array function in modern Excel extracts unique rows from a range filtered by multiple dynamic conditions?",
                "options": [
                    "=UNIQUE(FILTER(array, include_condition))",
                    "=DISTINCT(SUMIFS(array, condition))",
                    "=INDEX(MATCH(UNIQUE(array)))",
                    "=VLOOKUP_MULTI(array, condition)"
                ],
                "answer": "=UNIQUE(FILTER(array, include_condition))",
                "difficulty": "Advanced"
            },
            {
                "q": "In complex financial modeling, why is nesting dynamic indirect references (`INDIRECT`) inside large iterative recalculation loops discouraged?",
                "options": [
                    "INDIRECT is a volatile function that forces Excel to recalculate the entire formula tree on every worksheet edit, severely degrading performance",
                    "INDIRECT cannot reference cells in other worksheets within the same workbook",
                    "INDIRECT limits table arrays to a maximum of 256 rows",
                    "INDIRECT alters original cell values permanently upon calculation"
                ],
                "answer": "INDIRECT is a volatile function that forces Excel to recalculate the entire formula tree on every worksheet edit, severely degrading performance",
                "difficulty": "Expert"
            }
        ],
        "Power BI": [
            {
                "q": "What functional language is primarily used in Power BI for creating custom calculated columns, measures, and tables?",
                "options": ["M Code", "DAX", "SQL", "VBA"],
                "answer": "DAX",
                "difficulty": "Basic"
            },
            {
                "q": "Which core component in Power BI is utilized to extract, clean, reshape, and transform raw data before loading into the model?",
                "options": ["Power Query Editor", "Power View", "Power Pivot", "Power Service"],
                "answer": "Power Query Editor",
                "difficulty": "Beginner"
            },
            {
                "q": "In Power BI data modeling, what type of schema structure (combining Fact and Dimension tables) is best practice for performance?",
                "options": ["Star Schema", "Snowflake Schema with deep nesting", "Flat single-table schema", "Circular Relationship Schema"],
                "answer": "Star Schema",
                "difficulty": "Intermediate"
            },
            {
                "q": "Which DAX function alters the current evaluation context by overriding active filters or adding new filter conditions?",
                "options": ["CALCULATE()", "FILTER()", "SUMX()", "ALLSELECTED()"],
                "answer": "CALCULATE()",
                "difficulty": "Advanced"
            },
            {
                "q": "When diagnosing a Power BI report with severe render latency, what strategy addresses memory spikes caused by high-cardinality columns in a Star Schema?",
                "options": [
                    "Remove high-cardinality columns from Fact tables, split datetime columns into separate Date and Time keys, and replace calculated columns with DAX measures",
                    "Enable Bidirectional Cross-filtering across all dimension relationships",
                    "Convert all DirectQuery sources into Import mode without aggregations",
                    "Replace all DAX measures with custom M Query custom column formulas"
                ],
                "answer": "Remove high-cardinality columns from Fact tables, split datetime columns into separate Date and Time keys, and replace calculated columns with DAX measures",
                "difficulty": "Expert"
            }
        ],
        "Statistics": [
            {
                "q": "What measure of central tendency represents the middle value in a numerically sorted dataset?",
                "options": ["Mean", "Median", "Mode", "Variance"],
                "answer": "Median",
                "difficulty": "Basic"
            },
            {
                "q": "Which statistical hypothesis test is used to compare the means of two independent sample groups?",
                "options": ["Two-sample t-test", "Chi-Square test of independence", "ANOVA", "Pearson correlation test"],
                "answer": "Two-sample t-test",
                "difficulty": "Beginner"
            },
            {
                "q": "What does a p-value less than an alpha significance level (e.g., p < 0.05) indicate in hypothesis testing?",
                "options": [
                    "Reject the null hypothesis; the observed effect is statistically significant",
                    "Accept the null hypothesis; there is no significant difference",
                    "The sample size was too small to draw conclusions",
                    "The probability of Type II error is 100%"
                ],
                "answer": "Reject the null hypothesis; the observed effect is statistically significant",
                "difficulty": "Intermediate"
            },
            {
                "q": "What fundamental theorem explains why sample means tend toward a normal distribution as sample size grows, regardless of population distribution shape?",
                "options": ["Central Limit Theorem", "Law of Large Numbers", "Bayes' Theorem", "Chebyshev's Theorem"],
                "answer": "Central Limit Theorem",
                "difficulty": "Advanced"
            },
            {
                "q": "In multivariate linear regression, how do you diagnose and resolve severe Multicollinearity among predictor variables?",
                "options": [
                    "Calculate Variance Inflation Factor (VIF > 5-10) and remove or combine highly correlated predictors or apply Ridge/Lasso regularization",
                    "Perform log transformation on the dependent variable only",
                    "Switch from Ordinary Least Squares to simple K-Means clustering",
                    "Increase p-value threshold from 0.05 to 0.50"
                ],
                "answer": "Calculate Variance Inflation Factor (VIF > 5-10) and remove or combine highly correlated predictors or apply Ridge/Lasso regularization",
                "difficulty": "Expert"
            }
        ],
        "Tableau": [
            {
                "q": "In Tableau, what type of field contains qualitative categorical values (such as Customer Name, Region, or Product ID)?",
                "options": ["Dimension", "Measure", "Parameter", "Set"],
                "answer": "Dimension",
                "difficulty": "Basic"
            },
            {
                "q": "What color visual cue indicates a CONTINUOUS field in Tableau worksheet pills?",
                "options": ["Green", "Blue", "Red", "Yellow"],
                "answer": "Green",
                "difficulty": "Beginner"
            },
            {
                "q": "Which calculation type in Tableau computes values at a specified level of detail independently of dimensions in the view?",
                "options": ["Level of Detail (LOD) Expression", "Table Calculation", "Quick Table Calculation", "Row-level expression"],
                "answer": "Level of Detail (LOD) Expression",
                "difficulty": "Intermediate"
            },
            {
                "q": "What is the key difference between `{FIXED}` and `{INCLUDE}` LOD expressions in Tableau regarding view level filters?",
                "options": [
                    "{FIXED} computes aggregations using only specified dimensions, ignoring view dimensions, whereas {INCLUDE} adds specified dimensions to view dimensions",
                    "{FIXED} always respects Context Filters while {INCLUDE} ignores all filters",
                    "{FIXED} works only on measures, whereas {INCLUDE} works only on dimensions",
                    "There is no difference in execution order or scope"
                ],
                "answer": "{FIXED} computes aggregations using only specified dimensions, ignoring view dimensions, whereas {INCLUDE} adds specified dimensions to view dimensions",
                "difficulty": "Advanced"
            },
            {
                "q": "When optimizing a Tableau dashboard connected to a live multi-million row enterprise database, which optimization yields the fastest load times?",
                "options": [
                    "Use Extract data source with aggregated dimensions, replace Quick Filters with Parameter/Action filters, and optimize database indexing",
                    "Add 15 floating text boxes and use multiple nested table calculations",
                    "Convert all discrete dimensions into continuous green pills",
                    "Disable extract refreshes and force row-level calculation rendering"
                ],
                "answer": "Use Extract data source with aggregated dimensions, replace Quick Filters with Parameter/Action filters, and optimize database indexing",
                "difficulty": "Expert"
            }
        ]
    }
}
