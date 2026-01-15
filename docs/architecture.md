## Architecture Overview

1. Python generator simulates real-time transactions
2. Events are ingested using Azure Event Hubs
3. Data is processed using PySpark on Azure Databricks
4. Data is stored in Azure Data Lake using bronze–silver–gold layers
5. Batch pipelines are orchestrated using Azure Data Factory
6. Analytics is performed using Azure Synapse
7. Insights are visualized in Power BI
