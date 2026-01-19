from pyspark.sql.types import *
from pyspark.sql.functions import *

connection_string = ("<EVENT_HUB_CONNECTION_STRING>;"
                     "EntityPath=<EVENT_HUB_NAME>"
)

eh_conf = {
    "eventhubs.connectionString":
        sc._jvm.org.apache.spark.eventhubs.EventHubsUtils.encrypt(connection_string)
}

schema = StructType([
    StructField("transaction_id", StringType()),
    StructField("user_id", StringType()),
    StructField("amount", DoubleType()),
    StructField("currency", StringType()),
    StructField("transaction_type", StringType()),
    StructField("merchant_id", StringType()),
    StructField("location", StringType()),
    StructField("device_id", StringType()),
    StructField("status", StringType()),
    StructField("event_time", StringType())
])

raw_df = (
    spark.readStream
    .format("eventhubs")
    .options(**eh_conf)
    .load()
)

parsed_df = raw_df.select(
    from_json(col("body").cast("string"), schema).alias("data")
).select("data.*")

bronze_df = parsed_df.withColumn(
    "ingest_date", to_date(col("event_time"))
)

checkpoint_path = "abfss://checkpoints@fraudshieldadls.dfs.core.windows.net/fraudshield/bronze"
data_path = "abfss://bronze@fraudshieldadls.dfs.core.windows.net/transactions"

query = (
    bronze_df.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", checkpoint_path)
    .start(data_path)
)

query
