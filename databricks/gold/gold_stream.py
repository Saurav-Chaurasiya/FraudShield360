from pyspark.sql.functions import *

silver_path = "abfss://silver@fraudshieldadls.dfs.core.windows.net/transactions"
gold_path = "abfss://gold@fraudshieldadls.dfs.core.windows.net/metrics"

silver_df = spark.read.format("delta").load(silver_path)

gold_df = (
    silver_df
    .groupBy(
        to_date("event_time").alias("transaction_date"),
        "location"
    )
    .agg(
        count("*").alias("total_transactions"),
        sum("amount").alias("total_amount"),
        sum("is_fraud").alias("fraud_txn_count"),
        sum(when(col("is_fraud") == 1, col("amount")).otherwise(0)).alias("fraud_amount")
    )
)

gold_df.write.format("delta") \
  .mode("overwrite") \
  .save(gold_path)


## CONVERTING GOLD INTO PARQUET FORMAT
spark.read.format("delta") \
  .load("abfss://gold@fraudshieldadls.dfs.core.windows.net/metrics") \
  .write.mode("overwrite") \
  .parquet("abfss://gold@fraudshieldadls.dfs.core.windows.net/metrics_parquet")
