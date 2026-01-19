from pyspark.sql.functions import when, col, lit

silver_df = bronze_df.withColumn(
    "is_fraud",
    when(col("amount") > 50000, 1)
    .when((col("amount") > 30000) & (col("status") == "FAILED"), 1)
    .when(
        (col("location").isin("Delhi", "Mumbai")) & (col("amount") > 40000),
        1
    )
    .otherwise(0)
).withColumn(
    "fraud_reason",
    when(col("amount") > 50000, "HIGH_AMOUNT")
    .when((col("amount") > 30000) & (col("status") == "FAILED"), "FAILED_HIGH_AMOUNT")
    .when(
        (col("location").isin("Delhi", "Mumbai")) & (col("amount") > 40000),
        "LOCATION_RISK"
    )
    .otherwise("NORMAL")
)

silver_checkpoint_path = "abfss://checkpoints@fraudshieldadls.dfs.core.windows.net/fraudshield/silver"
silver_data_path = "abfss://silver@fraudshieldadls.dfs.core.windows.net/transactions"

silver_query = (
    silver_df.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", silver_checkpoint_path)
    .option("mergeSchema", "true")
    .start(silver_data_path)
)

silver_path = "abfss://silver@fraudshieldadls.dfs.core.windows.net/transactions"

silver_df = (
    spark.readStream
    .format("delta")
    .load(silver_path)
)