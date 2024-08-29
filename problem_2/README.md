What script does:

1. Generate a Sample CSV File
2. Anonymize the Data
3. Handling Larger Datasets with Distributed Computing

How to run:

1. Setup the environment:
   pip install pandas numpy faker pyspark
2. Generate the Sample CSV File using 'python generate_csv.py'
3. Generate anonymize data using 'python anonymize_data.py'
4. Run for higher volume data  using 'spark-submit anonymize_data_spark.py'

How to test:
1. python test_anonymize_data_spark.py