## Architecture Overview

1. Python generator simulates real-time transactions
2. Events are ingested using Azure Event Hubs
3. Data is processed using PySpark on Azure Databricks
4. Data is stored in Azure Data Lake using bronze–silver–gold layers
5. Batch pipelines are orchestrated using Azure Data Factory
6. Analytics is performed using Azure Synapse
7. Insights are visualized in Power BI

## Azure Architecture

The system follows a real-time streaming architecture:

- Python-based generator simulates financial transactions
- Azure Event Hubs ingests streaming data
- Azure Databricks processes data using PySpark
- Data is stored in Azure Data Lake Gen2 using bronze, silver, and gold layers
- Azure Data Factory orchestrates batch workflows
- Azure Synapse provides analytical querying
- Power BI visualizes fraud insights
