# handson-08-sparkSQL-dataframes-social-media-sentiment-analysis

## **Prerequisites**

Before starting the assignment, ensure you have the following software installed and properly configured on your machine:

1. **Python 3.x**:
   - [Download and Install Python](https://www.python.org/downloads/)
   - Verify installation:
     ```bash
     python3 --version
     ```

2. **PySpark**:
   - Install using `pip`:
     ```bash
     pip install pyspark
     ```

3. **Apache Spark**:
   - Ensure Spark is installed. You can download it from the [Apache Spark Downloads](https://spark.apache.org/downloads.html) page.
   - Verify installation by running:
     ```bash
     spark-submit --version
     ```

4. **Docker & Docker Compose** (Optional):
   - If you prefer using Docker for setting up Spark, ensure Docker and Docker Compose are installed.
   - [Docker Installation Guide](https://docs.docker.com/get-docker/)
   - [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

## **Setup Instructions**

### **1. Project Structure**

Ensure your project directory follows the structure below:

```
SocialMediaSentimentAnalysis/
├── input/
│   ├── posts.csv
│   └── users.csv
├── outputs/
│   ├── hashtag_trends.csv
│   ├── engagement_by_age.csv
│   ├── sentiment_engagement.csv
│   └── top_verified_users.csv
├── src/
│   ├── task1_hashtag_trends.py
│   ├── task2_engagement_by_age.py
│   ├── task3_sentiment_vs_engagement.py
│   └── task4_top_verified_users.py
├── docker-compose.yml
└── README.md
```



- **input/**: Contains the input datasets (`posts.csv` and `users.csv`)  
- **outputs/**: Directory where the results of each task will be saved.
- **src/**: Contains the individual Python scripts for each task.
- **docker-compose.yml**: Docker Compose configuration file to set up Spark.
- **README.md**: Assignment instructions and guidelines.

### **2. Running the Analysis Tasks**

You can run the analysis tasks either locally or using Docker.

#### **a. Running Locally**

1. **Navigate to the Project Directory**:
   ```bash
   cd SocialMediaSentimentAnalysis/
   ```

2. **Execute Each Task Using `spark-submit`**:
   ```bash
 
     spark-submit src/task1_hashtag_trends.py
     spark-submit src/task2_engagement_by_age.py
     spark-submit src/task3_sentiment_vs_engagement.py
     spark-submit src/task4_top_verified_users.py
     
   ```

3. **Verify the Outputs**:
   Check the `outputs/` directory for the resulting files:
   ```bash
   ls outputs/
   ```

#### **b. Running with Docker (Optional)**

1. **Start the Spark Cluster**:
   ```bash
   docker-compose up -d
   ```

2. **Access the Spark Master Container**:
   ```bash
   docker exec -it spark-master bash
   ```

3. **Navigate to the Spark Directory**:
   ```bash
   cd /opt/bitnami/spark/
   ```

4. **Run Your PySpark Scripts Using `spark-submit`**:
   ```bash
   
   spark-submit src/task1_hashtag_trends.py
   spark-submit src/task2_engagement_by_age.py
   spark-submit src/task3_sentiment_vs_engagement.py
   spark-submit src/task4_top_verified_users.py
   ```

5. **Exit the Container**:
   ```bash
   exit
   ```

6. **Verify the Outputs**:
   On your host machine, check the `outputs/` directory for the resulting files.

7. **Stop the Spark Cluster**:
   ```bash
   docker-compose down
   ```

## **Overview**

In this assignment, you will leverage Spark Structured APIs to analyze a dataset containing employee information from various departments within an organization. Your goal is to extract meaningful insights related to employee satisfaction, engagement, concerns, and job titles. This exercise is designed to enhance your data manipulation and analytical skills using Spark's powerful APIs.

## **Objectives**

By the end of this assignment, you should be able to:

1. **Data Loading and Preparation**: Import and preprocess data using Spark Structured APIs.
2. **Data Analysis**: Perform complex queries and transformations to address specific business questions.
3. **Insight Generation**: Derive actionable insights from the analyzed data.

## **Dataset**

## **Dataset: posts.csv **

You will work with a dataset containing information about **100+ users** who rated movies across various streaming platforms. The dataset includes the following columns:

| Column Name     | Type    | Description                                           |
|-----------------|---------|-------------------------------------------------------|
| PostID          | Integer | Unique ID for the post                                |
| UserID          | Integer | ID of the user who posted                             |
| Content         | String  | Text content of the post                              |
| Timestamp       | String  | Date and time the post was made                       |
| Likes           | Integer | Number of likes on the post                           |
| Retweets        | Integer | Number of shares/retweets                             |
| Hashtags        | String  | Comma-separated hashtags used in the post             |
| SentimentScore  | Float   | Sentiment score (-1 to 1, where -1 is most negative)  |


---

## **Dataset: users.csv **
| Column Name | Type    | Description                          |
|-------------|---------|--------------------------------------|
| UserID      | Integer | Unique user ID                       |
| Username    | String  | User's handle                        |
| AgeGroup    | String  | Age category (Teen, Adult, Senior)   |
| Country     | String  | Country of residence                 |
| Verified    | Boolean | Whether the account is verified      |

---

### **Sample Data**

Below is a snippet of the `posts.csv`,`users.csv` to illustrate the data structure. Ensure your dataset contains at least 100 records for meaningful analysis.

```
PostID,UserID,Content,Timestamp,Likes,Retweets,Hashtags,SentimentScore
101,1,"Loving the new update! #tech #innovation","2023-10-05 14:20:00",120,45,"#tech,#innovation",0.8
102,2,"This app keeps crashing. Frustrating! #fail","2023-10-05 15:00:00",5,1,"#fail",-0.7
103,3,"Just another day... #mood","2023-10-05 16:30:00",15,3,"#mood",0.0
104,4,"Absolutely love the UX! #design #cleanUI","2023-10-06 09:10:00",75,20,"#design,#cleanUI",0.6
105,5,"Worst experience ever. Fix it. #bug","2023-10-06 10:45:00",2,0,"#bug",-0.9
```

---

```
UserID,Username,AgeGroup,Country,Verified
1,@techie42,Adult,US,True
2,@critic99,Senior,UK,False
3,@daily_vibes,Teen,India,False
4,@designer_dan,Adult,Canada,True
5,@rage_user,Adult,US,False
```

---
## ✅ Explanations, Approach, and Results

### 📌 Approach Overview
This project uses **PySpark DataFrames and Spark SQL** to analyze social media posts and user data. The analysis extracts key insights into trending hashtags, engagement patterns across age groups, sentiment-driven engagement, and the influence of verified users.

- **Data Loading:** CSV datasets loaded into Spark DataFrames.
- **Data Processing:** 
  - Exploding hashtags for trend analysis
  - Joining user and post data
  - Categorizing sentiment based on sentiment scores
  - Aggregating likes and retweets
- **Output:** Results exported as CSV files into the `outputs/` folder.

---

## **Assignment Tasks**

You are required to complete the following three analysis tasks using Spark Structured APIs. Ensure that your analysis is well-documented, with clear explanations and any relevant visualizations or summaries.

### **1. Hashtag Trends **

**Objective:**

Identify trending hashtags by analyzing their frequency of use across all posts.

**Tasks:**

- **Extract Hashtags**: Split the `Hashtags` column and flatten it into individual hashtag entries.
- **Count Frequency**: Count how often each hashtag appears.
- **Find Top Hashtags**: Identify the top 10 most frequently used hashtags.

 **Process:** 
  - Split comma-separated hashtags
  - Flatten using `explode`
  - Aggregate and sort by frequency

**Explanation:**
- `explode()` and `split()` break the comma-separated hashtags into individual rows.
- `trim()` and `lower()` clean each hashtag (removing spaces and making lowercase).
- Group by the cleaned `Hashtag` and count their occurrences.
- Order the result in descending order of count.
- `coalesce(1)` ensures the output is written into a single file.


**Expected Outcome:**  
A ranked list of the most-used hashtags and their frequencies.

**Example Output:**

| Hashtag     | Count |
|-------------|-------|
| #tech       | 120   |
| #mood       | 98    |
| #design     | 85    |

---

### **2. Engagement by Age Group**

**Objective:**  
Understand how users from different age groups engage with content based on likes and retweets.

**Tasks:**

- **Join Datasets**: Combine `posts.csv` and `users.csv` using `UserID`.
- **Group by AgeGroup**: Calculate average likes and retweets for each age group.
- **Rank Groups**: Sort the results to highlight the most engaged age group.

**Process:** 
  - Join posts and users data
  - Group by `AgeGroup`
  - Calculate average likes and retweets

**Explanation:**
- Joins `posts.csv` with `users.csv` on `UserID`.
- Groups the combined data by `AgeGroup`.
- Uses `avg()` to compute the average likes and retweets for each age group.
- Orders the results based on `Avg_Likes` in descending order.
- `coalesce(1)` writes the output into a single CSV file.

**Expected Outcome:**  
A summary of user engagement behavior categorized by age group.

**Example Output:**

| Age Group | Avg Likes | Avg Retweets |
|-----------|-----------|--------------|
| Adult     | 67.3      | 25.2         |
| Teen      | 22.0      | 5.6          |
| Senior    | 9.2       | 1.3          |

---

### **3. Sentiment vs Engagement**

**Objective:**  
Evaluate how sentiment (positive, neutral, or negative) influences post engagement.

**Tasks:**

- **Categorize Posts**: Group posts into Positive (`>0.3`), Neutral (`-0.3 to 0.3`), and Negative (`< -0.3`) sentiment groups.
- **Analyze Engagement**: Calculate average likes and retweets per sentiment category.

**Process:** 
  - Categorize posts as Positive, Neutral, or Negative
  - Calculate average likes and retweets per sentiment group

**Explanation:**
- Creates a new `Sentiment` column based on `SentimentScore`:
  - Positive: `SentimentScore > 0.3`
  - Negative: `SentimentScore < -0.3`
  - Neutral: Between -0.3 and 0.3
- Groups the posts by `Sentiment`.
- Calculates average likes and retweets for each sentiment group using `avg()`.
- Orders the output by `Avg_Likes` in descending order.
- Writes the final output as a single CSV file.

**Expected Outcome:**  
Insights into whether happier or angrier posts get more attention.

**Example Output:**

| Sentiment | Avg Likes | Avg Retweets |
|-----------|-----------|--------------|
| Positive  | 85.6      | 32.3         |
| Neutral   | 27.1      | 10.4         |
| Negative  | 13.6      | 4.7          |

---

### **4. Top Verified Users by Reach**

**Objective:**  
Find the most influential verified users based on their post reach (likes + retweets).

**Tasks:**

- **Filter Verified Users**: Use `Verified = True` from `users.csv`.
- **Calculate Reach**: Sum likes and retweets for each user.
- **Rank Users**: Return top 5 verified users with highest total reach.

**Process:** 
  - Filter verified users
  - Calculate total reach per user
  - Rank top 5 by total reach

**Explanation:**
- Filters verified users from `users.csv`.
- Calculates each post’s reach (`Likes + Retweets`).
- Aggregates total reach per `UserID`.
- Joins the reach data with verified users to fetch `Username`.
- Orders users by `Total_Reach` and selects the top 5.
- `coalesce(1)` ensures the output is consolidated into a single file.

**Expected Outcome:**  
A leaderboard of verified users based on audience engagement.

**Example Output:**

| Username       | Total Reach |
|----------------|-------------|
| @techie42      | 1650        |
| @designer_dan  | 1320        |

---


## 📬 Submission Checklist

- [✅] PySpark scripts in the `src/` directory  
- [✅] Output files in the `outputs/` directory  
- [✅] Datasets in the `input/` directory  
- [✅] Completed `README.md`  
- [✅] Commit everything to GitHub Classroom  
- [✅] Submit your GitHub repo link on canvas

---

### ✅ Conclusion:
This project showcases how Spark SQL and DataFrames can efficiently analyze large-scale social media datasets to uncover:
- Popular hashtags
- Demographic engagement trends
- Sentiment-driven behaviors
- Influencer rankings

All results were saved as CSV files in the `outputs/` directory.
