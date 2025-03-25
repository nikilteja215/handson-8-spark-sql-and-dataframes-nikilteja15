from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col, lower, trim

spark = SparkSession.builder.appName("HashtagTrends").getOrCreate()
posts_df = spark.read.option("header", True).csv("input/posts.csv")

hashtags_df = posts_df.select(explode(split(col("Hashtags"), ",")).alias("Hashtag"))
hashtag_counts = hashtags_df.withColumn("Hashtag", trim(lower(col("Hashtag")))) \
    .groupBy("Hashtag").count().orderBy(col("count").desc())

hashtag_counts.coalesce(1).write.mode("overwrite").csv("outputs/hashtag_trends.csv", header=True)
