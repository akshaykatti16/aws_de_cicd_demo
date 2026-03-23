import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from datetime import datetime, timedelta

# Initialize Glue context
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read parquet data from S3
input_df = glueContext.create_dynamic_frame.from_options(
    "s3://your-bucket/path/to/parquet/",
    connection_type="s3",
    format="parquet"
)

# Convert to DataFrame for filtering
input_data = input_df.toDF()

# Filter data for the last 30 days
last_30_days = datetime.now() - timedelta(days=30)
filtered_data = input_data.filter(input_data['date_column'] >= last_30_days)

# Write to Redshift
filtered_data.write.format("com.databricks.spark.redshift") \
    .option("url", "jdbc:redshift://your-redshift-cluster:5439/yourdb") \
    .option("dbtable", "your_table") \
    .option("user", "your_user") \
    .option("password", "your_password") \
    .option("tempdir", "s3://your-bucket/temp/") \
    .mode("append") \
    .save()

# Commit job bookmark
job.commit()
