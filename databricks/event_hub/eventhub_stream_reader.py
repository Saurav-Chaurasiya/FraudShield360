from pyspark.sql.types import *
from pyspark.sql.functions import *

event_hub_conf = {
    "eventhubs.connectionString": "<EVENT_HUB_CONNECTION_STRING>"
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
    .options(**event_hub_conf)
    .load()
)

parsed_df = raw_df.select(
    from_json(col("body").cast("string"), schema).alias("data")
).select("data.*")

bronze_df = parsed_df.withColumn(
    "ingest_date", to_date(col("event_time"))
)
