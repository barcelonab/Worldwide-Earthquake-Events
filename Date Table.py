from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, sequence, explode, year, month, dayofmonth, quarter, dayofweek, date_format
from pyspark.sql.types import TimestampType, DateType

# Create Spark session
spark = SparkSession.builder.appName("DateTable").getOrCreate()

# Define start and end dates
start_date = "2025-01-01"
end_date = "2025-12-31"

# Create DataFrame with sequence of dates
df = spark.range(1).select(
    explode(
        sequence(
            lit(start_date).cast(DateType()), 
            lit(end_date).cast(DateType())
        )
    ).alias("date")
)

# Add useful columns
date_table = df.select(
    col("date").cast(TimestampType()).alias("date"),
    year("date").alias("year"),
    month("date").alias("month"),
    date_format("date", "MMM").alias("month_name"),
    dayofmonth("date").alias("day"),
    quarter("date").alias("quarter"),
    dayofweek("date").alias("day_of_week"),  # 1=Sunday, 7=Saturday
    date_format("date", "EEEE").alias("day_name")  # Full day name
)
# Save to Fabric Lakehouse (adjust path and database as needed)
date_table.write.mode("overwrite").saveAsTable("date")