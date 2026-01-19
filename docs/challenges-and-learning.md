## ⚙️ Engineering Challenges & Solutions

### Challenges Encountered
- Event Hub connection failures due to missing `EntityPath` in the connection string  
- Databricks workspace restrictions on public DBFS paths  
- Streaming checkpoint failures without external storage  
- OAuth / Managed Identity configuration complexity for ADLS Gen2  
- Streaming queries terminating due to insufficient storage permissions  

---

### Resolution Strategy
- Corrected Event Hub connection string to explicitly include `EntityPath`
- Migrated all streaming **data paths and checkpoints** to ADLS Gen2 using `abfss://`
- Configured **external checkpoint storage** for fault-tolerant streaming
- Switched to **storage account key–based authentication** for MVP stability
- Explicitly configured Spark session with ADLS access
- Validated storage connectivity before launching streaming jobs

> **Engineering Decision**  
> Managed Identity (OAuth/MSI) was explored and documented. Due to cluster-level OAuth configuration complexity and project timelines, **key-based authentication was used for the MVP**.  
> IAM-based authentication is planned as part of production hardening.

---