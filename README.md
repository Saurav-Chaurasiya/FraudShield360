# FraudShield 360 🚨  
### Real-Time Financial Fraud Detection Platform on Azure

FraudShield 360 is an end-to-end data engineering project that simulates real-time financial transactions and processes them using cloud-native data pipelines to detect suspicious activity.

## Tech Stack
- Python
- PySpark (Structured Streaming)
- Azure Event Hubs
- Azure Databricks
- Azure Data Lake Gen2 (ADLS Gen2)
- Azure Data Factory
- Azure Synapse Analytics
- Power BI

## Project Objective
To build a scalable real-time data pipeline that ingests, processes, stores, and analyzes financial transaction data to detect fraud patterns.

┌───────────────────────────┐
│  Transaction Producer     │
│  (Python – Local Script)  │
│  • Generates fake payments│
│  • Sends JSON events      │
└─────────────┬─────────────┘
              │  (events)
              ▼
┌──────────────────────────┐
│     Azure Event Hubs     │
│  • Ingests real-time data│
│  • Acts as event buffer  │
│  • Kafka-like streaming  │
└─────────────┬────────────┘
              │  (stream)
              ▼
┌──────────────────────────┐
│  Azure Databricks        │
│  (PySpark Structured     │
│   Streaming Engine)      │
│                          │
│  • Reads from Event Hub  │
│  • Decodes binary → JSON │
│  • Enforces schema       │
│  • Streaming processing  │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│  ADLS Gen2 (Delta Lake)  │
│                          │
│  Bronze Layer            │
│  • Raw validated events  │
│  • Append-only Delta     │
│  • Checkpointed writes   │
│                          │
│  Silver Layer (Planned)  │
│  • Fraud rules applied   │
│  • Cleaned & enriched    │
│                          │
│  Gold Layer (Planned)    │
│  • Aggregated analytics  │
│  • BI-ready datasets     │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│ Analytics & Reporting    │
│                          │
│ • Azure Synapse          │
│ • Power BI Dashboards    │
│ • Fraud insights & KPIs  │
└──────────────────────────┘
---

## Key Features
- Real-time financial transaction simulation
- Event-driven ingestion using Azure Event Hubs
- Binary-to-JSON decoding of Event Hub messages
- Schema-based validation using PySpark
- Fault-tolerant streaming with checkpointing
- Bronze–Silver–Gold data modeling
- Rule-based fraud detection logic (in progress)
- Analytics-ready dataset design

---

## Streaming Ingestion & Bronze Layer (Implemented)

### What Works Today
- Real-time transaction events are produced using Python
- Events are ingested continuously from Azure Event Hubs into Databricks
- Binary messages are decoded and parsed into structured columns
- Streaming DataFrame is enriched with ingestion metadata
- Data is successfully written to **ADLS Gen2 as Delta tables (Bronze layer)**
- Checkpointing is enabled to ensure fault tolerance and exactly-once processing
- Streaming performance is monitored via Databricks Streaming UI

### Technologies Used
- Azure Event Hubs (Kafka-like event streaming)
- Databricks Structured Streaming
- Delta Lake on ADLS Gen2
- Explicit schema enforcement for streaming safety

---

## Project Status
🚧 **Active Development**  
Bronze streaming pipeline is fully operational. Silver and Gold layers are under development.
