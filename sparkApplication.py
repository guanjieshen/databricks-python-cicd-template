from pipelines.jobs import airport
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
# Use this script to test executing the pipleines locally
airport.etl()
