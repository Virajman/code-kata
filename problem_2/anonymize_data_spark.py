from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.sql.types import StringType

# Initialize Spark session
spark = SparkSession.builder \
    .appName("DataAnonymization") \
    .getOrCreate()

# Load the CSV file
df = spark.read.csv('sample_data.csv', header=True, inferSchema=True)

# Anonymize columns
df = df.withColumn('first_name', lit('Anonymous')) \
       .withColumn('last_name', lit('Anonymous')) \
       .withColumn('address', lit('Anonymized Address'))

# Save anonymized data
df.write.csv('anonymized_data_spark.csv', header=True)

print("Spark-based anonymization complete.")
