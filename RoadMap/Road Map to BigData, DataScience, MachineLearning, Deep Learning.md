# Road Map to DS

## 01. Programming Languages

### 01. Python Language

- DataTypes, DS,
- Loops, Control Statements
- Functions, Modules
- Viz(MatplotLib & Seaborn)
- OOP&Classes, Exceptions,
- Data Wrangling & Cleaning
- Image & Audio Files(Tkinter)
- PVM, Logging

### 02. R Language

- reading & Exporting Data
- DataTypes, DS
- Manipulation & Processing
- Control Statements [see if R Lang has loops]
- Functions
- Objects Within Objects
- Packages(Tidyverse, Dplyr, Tidyr, GGPlot)
- QueueingTheory

## 02. DataBases

### 01. Relational DB

- MySQL
- PostgreSQL
- Oracle SQL
- Microsoft SQL Server / Transact-SQL (`T-SQL`)

01. Basic SQL Syntax
02. Data Types
    - String Types: `CHAR`, `VARCHAR`, `BLOB`, `TEXT`, `ENUM`
    - Numeric Types: `INT(size)`, `FLOAT(p)`, `FLOAT(size, d)`, `DOUBLE(size, d)`, `BOOLEAN`, `DATE`, `TIME`, `DATETIME`, `TIMESTAMP`, `YEAR`
    - Conversion Function - `CAST AS [INT][FLOAT][STRING]`
03. SQL Commands' categories

    | Data QUery Language (DQL) | Data Definition Language (DDL) | Data Manipulation Language (DML) | Data Control Language (DCL) | Transaction Control Language (TCL) |
    | :--    | :--      | :--          | :--    | :--               |
    | SELECT | CREATE   | INSERT       | GRANT  | BEGIN TRANSACTION |
    |        | ALTER    | UPDATE       | REVOKE | COMMIT            |
    |        | DROP     | DELETE       |        | ROLLBACK          |
    |        | TRUNCATE | CALL         |        | SAVEPOINT         |
    |        | RENAME   | EXPLAIN PLAN |        | SET TRANSACTION   |
    |        | COMMENT  | LOCK         |        | SET CONSTRAINT    |

04. Clauses
    - USE, SHOW, DESC, ALIAS clauses
    - FROM, WHERE, ORDER BY, DISTINCT, LIMIT clauses
05. Operators in SQL
    1. Relational Operators: `>`, `>=`, `<`, `<=`, `!=` or `<>`, `=`, `<=>`
    2. Logical Operators: `NOT`, `AND`, `OR`
    3. Arithmetic operator: `()`, `**`, `%` or `MOD()`, `/`, `*`, `+`, `-`
06. Keys
    1. Super Key
    2. Primary Key
    3. Candidate Key
    4. Alternate Key
    5. Foreign Key
    6. Composite Key
    7. Surrogate Key
07. Pre-defined Functions
    01. Aggregate Functions
        - MIN, MAX, SUM, AVG, COUNT functions
        - GROUP BY, HAVING clauses
    02. Comparison Functions
        - `ISNULL()`, `LEAST(column1, column2)`, `GREATEST(column1, column2)`, `IN`, `BETWEEN`, `LIKE`, `COALESCE(expr1, expr2, ..., exprN)`
    02. String Functions: `concat()`, `instr()`, `length()`, `char_length()`, `left(column_name, number_of_characters)`, `right(column_name, number_of_characters)`, `substring(string, start_position [, length=end])`, `substring_index(string, delimiter, count)`, `lower(string)`, `upper(string)`, `lpad(string, length, pad_string)`, `rpad(string, length, pad_string)`, `ltrim(string)`, `rtrim(string)`, `trim(string)`, `replace(string, old_substring, new_substring)`, `find_in_set()`, `reverse(string)`, `locate(string)`, `initcap(string)`, 
    03. Math Functions: `abs(numeric_value)`, `floor(numeric_value)`, `round(numeric_value [, decimal_places])`, `truncate(numeric_value, decimal_places)`, `mod(numeric_expression, divisor)`, `pow(base, exponent)` or `power(base, exponent)`
    04. Control Flow Functions: `CASE...END`, `IF...ELSEIF...ELSE...END IF` or `IF(conditions, if_condition_true, if_condition_false)`, `IFNULL(expr1, expr2)`, `NULLIF(expr1, expr2)`
    05. Date and Time Functions: `NOW()` or `CURRENT_TIMESTAMP()`, `CURDATE()` or `CURRENT_DATE()`, `CURTIME(fsp)` or `CURRENT_TIME(fsp)`, `EXTRACT()`, `DATE_FORMAT()`, `STR_TO_DATE()`, `TIMESTAMP()`, `UNIX_TIMESTAMP()`, `FROM_UNIXTIME()`, `TIMESTAMPDIFF()`, `DATEDIFF()`, `TIMEDIFF()`, `DATE_ADD()`, `DATE_SUB()`, `ADDDATE()`, `SUBDATE()`
08. `JOIN` clause
    1. `INNER JOIN` or `JOIN`, `LEFT JOIN` or `LEFT OUTER JOIN`, `RIGHT JOIN` or `RIGHT OUTER JOIN`
    2. `FULL JOIN` or `FULL OUTER JOIN`
    3. `SELF JOIN`
    4. `CROSS JOIN`
09. Set Theory Clauses
    1. `UNION`
    2. `UNION ALL`
    3. `INTERSECTION`
    4. `EXCEPT` or `MINUS`
10. Sub-Queries
    - Scalar Sub-queries, Row Sub-queries, Column Sub-queries, Multiple Row Sub-queries
    - Correlated and Non-Correlated Sub-Queries
    - Nested Sub-Queries
11. Views
    - `CREATE VIEW`, Query a view, Alter a view, `DROP VIEW`
12. Indexes
    1. Clustered Index
    2. Non-Clustered Index
        1. CREATE INDEX
    3. Types of Indexes: `B-Tree Index`, `R-Trees Index` or `Spatial Index`, `Hashed Index`, `Full Text Index`
    - Optimize Query Using Index
13. Constraints
    1. `PRIMARY KEY` constraint
    2. `FOREIGN KEY` constraint
    3. `UNIQUE` constraint
    4. `NOT NULL` constraint
    5. `CHECK` constraint
14. Transactions
    1. ACID properties
    2. `BEGIN`, `COMMIT`
    3. `ROLLBACK`, `SAVEPOINT`
    4. Isolation Levels
15. Data Integrity & Security
    1. Data Integrity Constraints
        1. Referential Integrity
        2. Entity Integrity
    2. Permissions/control commands: `GRANT` and `REVOKE`
    3. DB Security Best Practices
16. Stored Functions
    - Create Functions
    - Using Functions In Queries
17. Stored Procedures
    - CREATE PROCEDURE
    - EXEC
18. TRIGGERS
    - Creating & Using Triggers
    - Types of Triggers
19. Normalization
    - Types
20. PARTITION
    - Creating & Using Partitions
    - Sharding
21. Regular Expressions
    - REGEXP: `.`, `*`, `+`, `?`, `^`, `$`
22. Schema Management
    - CREATE, ALTER, DROP schema
23. Error Handling
    - Try-CatchBlocks
    - Raising Custom Exceptions
24. Performance Optimization
    - Query Optimization Techniques
        - Indexes
        - Optimizing Joins
        - Reducing Sub-Queries
    - Performance Tuning Best Practices
25. Advanced SQL Concepts
    1. Window Functions
        1. `OVER()` clause
        2. Types of Window Functions
            1. Aggregate Window Functions
                - `SUM(expr)`, `AVG(expr)`, `COUNT(expr)`, `MAX(expr)`, `MIN(expr)`
                - `STDDEV_POP()`, `STDDEV_SAMP()` or `STDDEV()` or `STD()`, `VAR_POP()`, `VAR_SAMP()` or `VARIANCE()`, `BIT_AND()`, `BIT_OR()`, `BIT_XOR()`, `JSON_ARRAYAGG()`, `JSON_OBJECTAGG()`
            2. Non-Aggregate Window Functions
                1. Ranking Window Functions
                    - `ROW_NUMBER()`
                    - `RANK()`, `DENSE_RANK()`
                    - `PERCENT_RANK()`, `CUME_DIST()``NTILE(n_buckets)`
                2. Relative Row Window Functions
                    - `LEAD(expr[, offset[, default_value]])`, `LAG(expr[, offset[, default_value]])`
                3. Value Window Functions
                    - `FIRST_VALUE(expr)`, `LAST_VALUE(expr)`, `NTH_VALUE(expr, n)`
        3. QUALIFY clause (used in Teradata, Databricks, T-SQL)
    2. CTEs (Common Table Expressions)
    3. Recursive Queries
    4. Pivot & Un-pivot Operations
    5. DynamicSQL
26. MERGE Statement
    - for upsert
28. Sequences And Identity Columns
    - Creating & Using Sequences/IdentityColumns
29. Advanced Sql Types
    - BLOB, CLOB, ENUM, SET, etc.
30. Temporal Tables
    - Creating & Using Temporal Tables
31. Cursors
    - Understanding Cursors
    - Using Cursors - DECLARE, OPEN, CLOSE, DEALLOCATE

### 02. NoSQL DB

#### 01. Data Models

- XML
- JSON

#### 02. Document DB

1. MongoDB
    1. MongoDB Architecture
    2. MongoDB vs. Cassandra
2. CouchDB

#### 03. Columnar DB

1. Apache Cassandra
    1. Cassandra Architecture
    2. MongoDB vs. Cassandra
2. Amazon Redshift
3. ClickHouse

#### 04. Key-Value DB

1. Redis
2. DynamoDB
3. Riak

#### 05. Vector DB

1. Pinecone
2. Weaviate
3. FAISS
4. Milvus
5. Qdrant

### 03. DataBases Concepts

1. Data Warehousing
2. Connecting DBs with Python
3. Data Driven Decisions
4. Enterprise Data Management
5. Data Preparation
6. Data Cleaning

## 03. Big Data

1. 5 V's of Big Data
2. Background of Big Data

### 01. Data Warehouse

1. Data Warehouse Fundamentals
    1. OLAP **vs.** OLTP
    2. Dimension Table **vs.** Fact Table
    3. Slowly Changing Dimensions (`SCD`s)
    4. ER Modelling / Dimension Modelling
    5. ETL vs ELT
        1. Data Warehousing & Data Lakes
        2. Data Warehouse **vs.** Data Lake **vs.** Data Mart
2. Data Warehouse Tools
    1. Apache Hive Warehousing
    2. Azure DataLake Storage
    3. Delta Live Tables (DLT)
    4. SnowFlake
    5. Google BigQuery
    6. Amazon RedShift

### 02. Batch Processing

1. Apache Hadoop
2. Apache Spark
3. Apache Flink
