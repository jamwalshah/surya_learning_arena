# Review

🎉 Congratulations on reaching the end of the module! Take a moment to review everything you have learned:

## Data Orchestration Fundamentals

- Data Orchestration is the coordination and automation of data flow across various tools and systems to deliver quality data products and analytics
- The path to modern data orchestration solutions like Airflow had various evolutions starting with basic time-based scheduling tools (e.g., Cron, WTS), followed by proprietary software (e.g., AutoSys, Informatica), and finally older open-source solutions (e.g., Oozie, Luigi).

## Airflow for Data Orchestration

- Airflow is an open-source tool for programmatically authoring, scheduling, and monitoring data pipelines.
- Airflow is defined by key characteristics such as pipelines-as-code with Python, built-in observability, a large open-source community, and much more!
- Airflow is used across a variety of industries, data practitioners, and use-cases.
- Airflow has key considerations to account for when using it for streaming, data processing, and when it is scaled.

## Demystifying Airflow

- Airflow can be used by single developers, single teams, and multi-teams. In each case, the way it is run is different.
- Airflow can be run using a variety of architecture types (e.g., on-premise) and systems (e.g., cloud services)
- Airflow key terms to remember:
  - **DAG:** A directed acyclical graph that represents a single data pipeline
  - **Task:** An individual unit of work in a DAG
  - **Operator:** The specific work that a Task performs
- There are three main types of operators:
  - **Action:** Perform a specific action such as running code or a bash command
  - **Transfer:** Perform transfer operations that move data between two systems
  - **Sensor:** Wait for a specific condition to be met (e.g., waiting for a file to be present) before running the next task
