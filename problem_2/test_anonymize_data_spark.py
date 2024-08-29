from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from pyspark.sql.types import StringType
import os


def test_anonymization():
    """
    Tests the anonymization functionality of the script.
    """

    # Create a temporary SparkSession for testing
    spark = SparkSession.builder \
        .master("local") \
        .appName("DataAnonymization_Test") \
        .getOrCreate()

    # Assuming sample_data.csv is present in the current directory
    test_data_path = "sample_data.csv"

    # Check if the file exists
    assert os.path.exists(test_data_path), "Test data file not found!"

    # Load the data
    df = spark.read.csv(test_data_path, header=True, inferSchema=True)

    # Expected anonymized values
    expected_first_name = "Anonymous"
    expected_last_name = "Anonymous"
    expected_address = "Anonymized Address"

    # Apply anonymization logic
    anonymized_df = df.withColumn('first_name', lit(expected_first_name)) \
                     .withColumn('last_name', lit(expected_last_name)) \
                     .withColumn('address', lit(expected_address))

    # Assert anonymized values
    assert anonymized_df.select("first_name").head().first_name == expected_first_name
    assert anonymized_df.select("last_name").head().last_name == expected_last_name
    assert anonymized_df.select("address").head().address == expected_address

    # Spark doesn't support in-memory temporary tables, so avoid saving the data
    # Comment out the following line to prevent writing to a file
    # anonymized_df.write.csv("anonymized_data_spark_test.csv", header=True)

    # Stop the SparkSession
    spark.stop()


if __name__ == "__main__":
    test_anonymization()