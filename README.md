# 🏦 End-to-End Snowflake Data Pipeline: Czech Banking Project  
**Enterprise-Scale Cloud Data Engineering & Automation**

![Snowflake](https://img.shields.io/badge/Snowflake-Cloud%20Data%20Platform-blue)  
![AWS S3](https://img.shields.io/badge/AWS%20S3-Connected-green)  
![SQL](https://img.shields.io/badge/SQL-Fully%20Automated-orange)  
![Tasks](https://img.shields.io/badge/Tasks-Enabled-informational)

---

## 📌 Project Overview

This project simulates a **real-time enterprise data warehouse** using Snowflake’s cloud-native tools integrated with AWS S3. The data represents operations of a Czech bank — covering customer profiles, transactions, loans, and credit cards.

🔧 Technologies Used:
- **Snowflake** for data warehouse & transformation  
- **AWS S3** for staging/landing zone  
- **Snowpipe** for auto-ingestion from cloud storage  
- **SQL Tasks + Stored Procedures** for ETL automation  

---

## 🧱 Architecture & Workflow

### 🔄 Automated Data Flow

```mermaid
graph TD
A[Raw CSVs in AWS S3] --> B(Snowflake External Stage)
B --> C[Snowpipes - Auto Ingest CSVs]
C --> D[Staging Tables in Snowflake]
D --> E[Stored Procedures - Transformations]
E --> F[Automated Scheduled Tasks]
F --> G[Final Reporting Tables]
````

---

## 🗃️ Database Schema

### ✅ Tables Created

* `DISTRICT`
* `ACCOUNT`
* `ORDER_LIST`
* `LOAN`
* `TRANSACTIONS`
* `CLIENT`
* `DISPOSITION`
* `CARD`

Each table is related via foreign keys, following normalized schema design (see `ERD.pdf` in repo).

---

## 🚀 Step-by-Step Setup

### 1️⃣ Create Database & Tables

```sql
CREATE DATABASE BANK;
USE BANK;
-- Create tables: DISTRICT, ACCOUNT, ORDER_LIST, LOAN, TRANSACTIONS, CLIENT, DISPOSITION, CARD
```

> SQL scripts available in [`/SQL_SCRIPT/cont_data_load.sql`](SQL_SCRIPT/cont_data_load.sql)

---

### 2️⃣ Connect to AWS S3 via External Stage

```sql
CREATE OR REPLACE STORAGE INTEGRATION s3_int
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = S3
ENABLED = TRUE
STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::441615131317:role/bankrole'
STORAGE_ALLOWED_LOCATIONS = ('s3://czechbankdata/');

CREATE OR REPLACE STAGE BANK
URL = 's3://czechbankdata'
FILE_FORMAT = (TYPE = 'CSV')
STORAGE_INTEGRATION = s3_int;
```

---

### 3️⃣ Snowpipe Configuration for Auto-Ingest

Each folder in S3 is mapped to its respective Snowflake table:

```sql
CREATE OR REPLACE PIPE BANK_SNOWPIPE_ACCOUNT AUTO_INGEST = TRUE AS
COPY INTO BANK.PUBLIC.ACCOUNT
FROM @BANK/Account/
FILE_FORMAT = (TYPE = 'CSV');
```

✅ Pipes created for:

* `ACCOUNT`, `TRANSACTIONS`, `DISPOSITION`, `DISTRICT`
* `CLIENT`, `ORDER_LIST`, `LOAN`, `CARD`

---

### 4️⃣ Load & Validate Data

Manually trigger a pipe (for testing):

```sql
ALTER PIPE BANK_SNOWPIPE_ACCOUNT REFRESH;
```

Validate data counts:

```sql
SELECT COUNT(*) FROM ACCOUNT;
SELECT COUNT(*) FROM TRANSACTIONS;
-- etc.
```

---

### 5️⃣ Automate ETL using Stored Procedures + Tasks

Use modular SQL logic to update and transform records.

Sample Stored Procedure:

```sql
CREATE OR REPLACE PROCEDURE UPDATE_BALANCES()
LANGUAGE SQL
AS
$$
BEGIN
  -- Your transformation logic here
END;
$$;
```

Automate execution every 1 minute:

```sql
CREATE OR REPLACE TASK BAL_UPDATE_TASK
WAREHOUSE = COMPUTE_WH
SCHEDULE = '1 MINUTE'
AS CALL UPDATE_BALANCES();

ALTER TASK BAL_UPDATE_TASK RESUME;
```

---

## 📂 Repository Structure

```
📦 End-To-End-Data-Analytics-Project_Banking/
│
├── SQL_SCRIPT/                 # All SQL scripts
│   └── cont_data_load.sql
│
├── Datasets_Raw/              # Original CSVs
├── Datasets_Cleaned/          # Transformed versions
├── Diagram/                   # PNG/PDF of dashboards & ERD
├── Snowflake_continuous_data_loading.docx
├── czec_bank_json_policies.txt
└── README.md                  # ← This file
```

---

## 📊 Sample Visual Outputs

* `DASHBOARD_PBI.pdf` – Power BI dashboard snapshot
* `BANKING_KPI_PUBLISH_PBI_SERVICE.png` – Published analytics visuals
* `SNOWFLAKE_PBI_CONNECTION.png` – ODBC connector flow

---

## 📈 Business Value

| Feature              | Benefit                                 |
| -------------------- | --------------------------------------- |
| 💡 Auto Ingestion    | Real-time updates from S3               |
| 🔄 Task Automation   | No manual triggers needed               |
| 🧩 Normalized Schema | High-quality structure for BI reporting |
| 📊 Modular SQL       | Maintainable ETL pipeline               |

---

## 📫 Contact Me

I’m always open to discussing data projects and collaboration opportunities. Feel free to reach out:

* **Email:** [masteravinashrai@gmail.com](mailto:masteravinashrai@gmail.com)
* **LinkedIn:** [Avinash Analytics](https://www.linkedin.com/in/avinashanalytics/)
* **HackerRank:** [AvinashAnalytics](https://www.hackerrank.com/AvinashAnalytics)
* **Twitter (X):** [@AvinashAnalytiX](https://x.com/AvinashAnalytiX)

---

## 💬 Analytical Philosophy

> **"Data beats emotions. Every business decision should start with 'What do the numbers say?'"**
> – Avinash's adaptation of W. Edwards Deming's principle

---

**Let’s connect and explore how data can drive your business forward! 🚀**

```
