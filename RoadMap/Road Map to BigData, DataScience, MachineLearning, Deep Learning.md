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
    02. String Functions: `concat()`, `instr()`, `length()`, `char_length()`, `left(column_name, number_of_characters)`, `right(column_name, number_of_characters)`, `substring(string, start_position [, length=end])`, `substring_index(string, delimiter, count)`, `lower(string)`, `upper(string)`, `lpad(string, length, pad_string)`, `rpad(string, length, pad_string)`, `ltrim(string)`, `rtrim(string)`, `trim(string)`, `replace(string, old_substring, new_substring)`, `find_in_set()`, `reverse(string)`, `locate(string)`, `initcap(string)`
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

### 01. Data Warehousing & Data Lakes

1. Data Warehouse Fundamentals
    1. OLAP **vs.** OLTP
    2. Dimension Table **vs.** Fact Table
    3. Data Modelling
        1. Star Schema **vs.** Snowflake Schema
        2. Slowly Changing Dimensions (`SCD`s)
        3. ER Modelling / Dimension Modelling
    4. ETL vs ELT
        1. Data Warehouse & Data Lake
        2. Data Warehouse **vs.** Data Lake **vs.** Data Mart
    5. Medallion Architecture
    6. Batch Processing **vs.** Stream Processing
    7. Streaming Tables and Materialized Views
2. Data Warehouse Tools/Frameworks
    1. Delta Live Tables (DLT) Framework
    2. Apache Hive Warehousing
    3. Azure DataLake Storage
    4. SnowFlake
    5. Google BigQuery
    6. Amazon RedShift

### 02. Batch Processing

1. Apache Hadoop
2. Apache Spark

#### 01. Apache Hadoop

1. Hadoop Ecosystem
2. Hadoop Distributed File System (`HDFS`)
    1. HDFS Architecture
    2. HDFS cmd-line & web-interface
3. Hadoop event stream processing
4. Complex Event Processing
5. MapReduce
    1. MapReduce Architecture [dataflow / architecture]
    2. MapReduce Features
    3. Shuffle & Sort
    4. Job Scheduling, Task Execution
    5. MapReduce Types
6. Hadoop Cluster, Specification, Configuration
7. Hadoop Administration- Security, Monitoring, Maintenance
8. Apache Hive SQL
    1. Apache Hive Architecture
    2. Apache Hive Programming
9. Apache HBase
    1. Apache HBase Basics
    2. Apache HBase Architecture
    3. Java Client API
    4. CRUD operations & Security
10. Apache Zookeeper

#### 02. Apache Spark

1. Apache Spark Fundamentals
    1. Spark Architecture
    2. initializing Spark
    3. RDDs
        1. RDD operations
        2. Key-Value Pairs
        3. Shuffle Operations
        4. RDD Persistence
        5. Removing Data
        6. RDD Operations
            1. Transformations: `map`, flatMa`p, fi`lter, etc.
            2. Actions: `count`, `reduce`, `reduceByKey`, etc.
        7. Shared Variables
            1. Broadcast
            2. Aggregators
    4. Spark DataFrames / Spark SQL
        1. Operations on DataFrames
            - `count`, `printSchema`, `show`, `select`, `filter`, `groupBy`, `registerTempTable`
    5. Datasets
    6. Job Optimization
    7. EDA using PySpark
    8. Spark MLib
    9. Deployment to cluster Spark Streaming
2. Apache Spark languages
    1. Scala
    2. Spark Java
    3. PySpark
    4. R
3. Connecting DBs with Spark
4. Apache Spark Tools
    1. Databricks
    2. Azure Synapse Analytics
    3. Amazon EMR
    4. GCP Cloud Dataproc
    5. AWS Glue

### 03. Stream/Real-Time Processing

1. Apache Kafka for streaming
2. Apache Flink
3. Rabbit MQ for Message queuing

#### 01. Apache Kafka

1. Kafka Fundamentals
    1. Pub-Sub Messaging Pattern
    2. Kafka Use cases in Data Engineering
    3. Kafka Architecture
2. Kafka Core Components
    1. Producers and Consumers
    2. Topics and Partitions
    3. Brokers and Clusters
    4. Zookeeper (in Older versions)
    5. KRaft (Kafka Raft) mode (in newer versions)
    6. Kafka Retention and Offset Management
3. Kafka Setup and Operations
    1. Installing Kafka (Local/Docker)
    2. Running Kafka and Zookeeper
    3. CLI tools for Topics, Consumers, etc.
    4. Kafka Configuration and Tuning
4. Kafka Ecosystem Tools
    1. Kafka Connect: Integration with Databases, S3, ElasticSearch, etc.
    2. Kafka Streams API
    3. Schema Registry: Avro, Protobuf support
    4. Kafka REST Proxy
5. Kafka with Spark
    1. Spark-Kafka Integration
    2. Setting Up Kafka Producer & Consumer in Spark
    3. Consuming Kafka Streams using Spark Structured Streaming
    4. Exactly-once Semantics
    5. Check-pointing in Spark
6. Kafka Monitoring and Observability
    1. Kafka Manager
    2. Prometheus and Grafana for Kafka Metrics
    3. Alerting and Lag Monitoring

#### 02. Apache Flink

1. Apache Flink Fundamentals
    1. Flink vs. Spark Streaming vs. Kafka Streams
    2. Use cases: Real-Time Analytics, Event-Driven Apps, ETL
2. Flink Architecture
    1. JobManager and TaskManager
    2. Flink Runtime and DataFlow Model
    3. Event TIme vs. Processing Time
    4. Watermarks and Late Data Handling
    5. Stateful vs, Stateless Processing
    6. Checkpoints and Savepoints
3. Flink Programming APIs
    1. DataStream API (for unbounded streams)
    2. DataSet API (for bounded/batch data - legacy)
    3. Table API and Flink SQL
    4. CEP (Complex Event Processing) API
4. Integrations and Connectors
    1. Kafka (Source/Sink)
    2. Filesystem, JDBC, Amazon S3, HDFS, ElasticSearch, etc.
    3. CDC (Change Data Capture) with Flink
    4. Flink with Apache Pulsar
5. Fault Tolerance and State Management
    1. RocksDB State Backend
    2. Exactly-once Processing Guarantees
    3. Savepoints for Stateful Recovery
    4. Distributed Snapshots
6. Flink Deployment
    1. Local and Standalone Cluster
    2. YARN, Kubernetes, and Mesos
    3. Integration with Docker
    4. Flink on AWS, Azure or GCP
7. Monitoring and Observability
    1. Flink UI
    2. Logs and Metrics
    3. Integration with Prometheus and Grafana
8. Tools and Ecosystem
    1. Apache Beam (runs on Flink runner)
    2. Stateful Functions (Flink sub-project for serverless)
    3. Ververica Platform (Commercial Flink offering)

#### 03. Rabbit MQ

- TBD

### 04. Data Orchestration

1. Schedulers

#### 01. Data Orchestration Tools

1. Pre-UNIX / Manual Era
    1. Manual Trigger based workflows
2. Early Computing Schedulers
    1. CRON (Linux/UNIX based)
    2. Windows Task Scheduler (`WTS`)
    3. AutoSys (by Broadcom)
    4. Control-M (by BMC)
    5. Informatica (includes orchestration + ETL)
3. Data & Open-Source Renaissance
    1. Luigi (by Spotify, python-based DAGs)
    2. Apache Oozie (Hadoop focused, XML based)
    3. Apache Azkaban (by Linkedin, Hadoop focused)
4. Modern Data Orchestration
    1. Apache Airflow (most-popular, Python, DAG-based)
    2. Prefect (modern Python orchestration, cloud-native)
    3. Dagster (type-safe, development-focused orchestration)
    4. Mage (simplified, modern Python orchestration)
    5. Argo workflows (Kubernetes-native workflows)

#### 02. Apache Airflow

1. Airflow Fundamentals
    1. Use cases: ETL, ML Pipelines, Reporting, Scheduling
2. Airflow Architecture
    1. Scheduler
        1. Scheduling vs. Triggering
        2. Trigger rules
    2. Executor
    3. Webserver
    4. Metadata database
    5. Workers
3. Installation & Setup
4. Directed Acyclic Graphs (DAGs)
    1. DAG parameters: `dag_id`, `schedule_interval`, `start_date`, `catchup`, `default_args`
    2. Defining Task Dependencies: `>>`, `<<`, `.set_downstream()`, `set_upstream()`
5. Core Concepts
    1. Operators: `BashOperator`, `PythonOperator`, `DummyOperator`, `EmailOperator`, `BranchPythonOperator`, etc.
    2. Sensors: `TimeSensor`, `FileSensor`, `ExternalTaskSensor`
    3. Cross-Communications (`XComs`): Basics, `xcom_push`, `xcom_pull`, Cross-Task Communication
6. Variables and Connections
    1. Setting Up and using Connections (Database, AWS, Azure, etc.)
    2. Secrets Management (Vault, etc.)
7. Error Handling and Debugging
    1. Task instance states
    2. Retry strategies, `max_retries` and `on_failure_callback` functions
    3. Debugging DAGs locally, Skipped or failed task recovery
8. Monitoring and Logging
    1. Airflow UI: Gantt Charts, Tree View, Logs
    2. SLA Misses, Email Alerts
9. Advanced Concepts
    1. Parallelism and Concurrency
    2. Pooling, Queuing, Priority Weights
    3. SubDAGs (why they're often avoided)
10. Deployment & CI/CD
    1. Version Control and Workflow
        1. git for DAG versioning
        2. Git-based deployment flows
    2. Containerization
        1. Docker & Docker Compose
        2. Helm Charts for Kubernetes
    3. Managed Cloud providers for
        1. Astronomer
        2. Amazon Managed Workflows for Apache Airflow (`MWAA`)
        3. Google Cloud Compose

#### 03. Prefect

#### 04. Dagster

#### 05. Mage

#### 06. Argo workflows

### 05. ETL Data Pipelines

1. Data Warehousing for ETL Data Pipeline
2. Data Lake for ETL Data Pipeline
3. Data Pipeline Stages
    1. Data Ingestion
    2. Data Transformation
    3. Data Quality
    4. Data Visualization
    5. Machine Learning (`ML`) Lifecycle
4. Engine-Agnostic ETL Frameworks
    1. Apache Beam

#### 01. ETL Tools as per stages

1. Data Ingestion
    - Airbyte
    - Fivetran
    - Stitch
2. Data Transformation
    - dbt (Data Build Tool)
    - Spark/PySpark
3. Data Quality
    - Great Expectations (`GX`)
    - Soda SQL
4. Data Visualization
    - Tableau
    - Power BI
    - Looker
5. Machine Learning (`ML`) Lifecycle
      - mlflow

### 06. Deployment and Productionization

1. Docker vs. Kubernetes
2. Deployment patterns for data pipelines
3. CI/CD for ETL
4. Secrets, configs, infrastructure

### 08. DataOps and Observability

#### 01. Data Validation and Quality Tools

1. Great Expectations (`GX`)
2. Soda SQL
3. Amazon Deequ

#### 02. Data Lineage and Cataloging

1. Amundsen
2. OpenMetadata
3. Datahub

#### 03. Monitoring and Observability

1. Job Level Monitoring
    1. Prometheus
    2. Grafana
2. Workflow Monitoring
    1. Airflow
    2. StatsD metrics
3. Data Observability
    1. Datadog
    2. Monte Carlo

#### 04. Alerting

1. Airflow Alerting
2. PagerDuty
3. Slack integrations

### 09. Advanced Data Engineering Tools

- Tools
    - Learn some tools from Modern Data Stack, focus on core use case of that tool
        - DBT - Data Build Tool
- Deployment
    - Security, Networking & deployment
    - Kubernetes, Docker
- Use Cases
    - look at customer success story/case study of cloud platforms such as AWS, Azure, GCP, and observe how they solved some particular problem using some tool/service