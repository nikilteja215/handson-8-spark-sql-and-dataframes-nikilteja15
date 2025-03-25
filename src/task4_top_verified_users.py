from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

spark = SparkSession.builder.appName("TopVerifiedUsers").getOrCreate()

# Load datasets
posts_df = spark.read.option("header", True).csv("input/posts.csv", inferSchema=True)
users_df = spark.read.option("header", True).csv("input/users.csv", inferSchema=True)

# Filter verified users
verified_users = users_df.filter(col("Verified") == True)

# Calculate reach (likes + retweets) per user
reach_df = posts_df.withColumn("Reach", col("Likes") + col("Retweets")) \
                   .groupBy("UserID") \
                   .agg(_sum("Reach").alias("Total_Reach"))

# Join to get usernames of verified users
top_verified = verified_users.join(reach_df, "UserID") \
                             .select("Username", "Total_Reach") \
                             .orderBy(col("Total_Reach").desc()) \
                             .limit(5)

top_verified.coalesce(1).write.mode("overwrite").option("header", "true").csv("outputs/top_verified_users")
