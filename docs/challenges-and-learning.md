## Engineering Challenges & Solutions

### Challenges Encountered
- Event Hub connection failures due to missing `EntityPath`
- Databricks workspace restrictions on public DBFS paths
- Checkpointing limitations without external storage
- OAuth / Managed Identity configuration complexity for ADLS Gen2
- Streaming queries terminating due to invalid storage access

### Resolution Strategy
- Corrected Event Hub connection string to include `EntityPath`
- Used ADLS Gen2 (`abfss://`) paths for both data and checkpoints
- Switched to **storage account key–based authentication** for MVP stability
- Explicitly configured Spark with ADLS access
- Validated storage access before starting streaming writes

> **Engineering decision:**  
> Managed Identity (OAuth/MSI) was explored and documented. Due to cluster-level OAuth configuration complexity and project timelines, key-based authentication was used for the MVP. IAM-based authentication is planned for production hardening.

---

## Current Pipeline Status

| Layer  | Status |
|------|------|
| Event Producer | ✅ Implemented |
| Event Hub Ingestion | ✅ Implemented |
| Bronze (Delta Lake) | ✅ Implemented |
| Silver (Fraud Rules) | 🚧 In Progress |
| Gold (Analytics) | ⏳ Planned |
| Power BI Dashboard | ⏳ Planned |

---

## Key Learnings
- Real-time systems require strict schema enforcement
- Event-driven pipelines behave differently from batch systems
- Checkpointing is critical for streaming reliability
- Cloud IAM can be complex; multiple authentication strategies should be understood
- Delivering a working MVP while documenting production alternatives is a real-world engineering skill

---