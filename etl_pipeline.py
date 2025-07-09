from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ETL Pipeline with MinIO") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.access.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.secret.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
    .config("spark.hadoop.fs.s3a.connection.timeout", "60000") \
    .config("spark.hadoop.fs.s3a.connection.establish.timeout", "60000") \
    .config("spark.hadoop.fs.s3a.connection.maximum", "100") \
    .getOrCreate()

df = spark.read.csv("s3a://bucket1/input/hw_200.csv", header=True, inferSchema=True)
df.show(5)
df.write.mode("overwrite").parquet("s3a://bucket1/output/hw_200_parquet")
print("Transformacja zakończona. Oto kilka wierszy:")
df.show(5)
spark.stop()