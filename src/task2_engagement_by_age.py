from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col

spark = SparkSession.builder.appName("EngagementByAgeGroup").getOrCreate()

# Load datasets
posts_df = spark.read.option("header", True).csv("input/posts.csv", inferSchema=True)
users_df = spark.read.option("header", True).csv("input/users.csv", inferSchema=True)

# TODO: Implement the task here


# Save result
engagement_df.coalesce(1).write.mode("overwrite").csv("outputs/engagement_by_age.csv", header=True)
