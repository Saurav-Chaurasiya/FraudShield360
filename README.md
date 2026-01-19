# FraudShield 360 🚨  
### Real-Time Financial Fraud Detection Platform on Azure

FraudShield 360 is an end-to-end data engineering project that simulates real-time financial transactions and processes them using cloud-native data pipelines to detect suspicious activity.

---

## Tech Stack & Tools
- Python (Data generator & business logic)
- Apache PySpark (Streaming injection & transformations)
- Azure Event Hubs (Real-time transaction ingestion)
- Azure Databricks (Distributed stream processing engine)
- Azure Data Lake Gen2 (Scalable Delta Lake storage)
- Power BI (Analytics & visualization)
- Git & GitHub (Version control and project collaboration)

---

## Project Objective
To build a *scalable*, *fault-tolerant real-time data pipeline* that:
- Ingests streaming financial transactions
- Processes data using structured streaming
- Stores data using *Medallion Architecture*
- Enables fraud analysis and business insights through analytics

---

## Analytics Objective
Provide actionable insights into:
- Fraud trends over time
- Fraud distribution by location
- Fraud rate analysis
- Business-level KPIs for decision-making

---

## 🏗️ Architecture Overview

<p align="center">
  <img src="/diagrams/architecture.png" alt="FraudShield 360 Architecture" width="900"/>
</p>

---

## Key Features
- Real-time financial transaction simulation
- Event-driven ingestion using Azure Event Hubs
- Binary-to-JSON decoding of Event Hub messages
- Schema-based validation using PySpark
- Fault-tolerant streaming with checkpointing
- Bronze–Silver–Gold data modeling
- Rule-based fraud detection logic 
- Analytics-ready dataset design

---

## Medallion Architecture

### Bronze Layer
- Raw transaction events from Event Hub
- Schema validation using PySpark
- Appended-only Delta tables
- Exactly-once processing with checkpointing

### Silver Layer
- Data cleansing and enrichment
- Rule-based fraud detection
- Fraud flags and fraud reasons added

### Gold Layer
- Fraud flags and fraud reasons added
- Fraud KPIs and summary tables
- Optimized for Power BI consumption

---

##  Power BI Dashboard
The Power BI dashboard includes:
- Total Transactions
- Total Fraud Amount
- Fraud Transactions Count
- Fraud Rate by Location
- Transactions Trend by Year
- Fraud vs Total Amount Comparison

---

## Why This Project Matters
FraudShield 360 reflects real-world data engineering practices used in:
- Banking & Financial services
- Payment gateways
- Risk & compilance systems
- Real-time analytics platforms

It demonstrates strong understanding of:
- Streaming systems
- Data modeling
- Analytics and visualization