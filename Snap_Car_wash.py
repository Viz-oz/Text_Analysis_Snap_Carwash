#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel data
file_path = "D:\\Data_Analytics_Portfolio\\Projects\\SnapCarwash_Text_Analysis\\reviews.xlsx"
data = pd.read_excel(file_path)

# Convert NaN or blank cells to empty strings in the 'Review' column
data['Review'] = data['Review'].fillna('')

# Calculate sentiment for each review
data['Sentiment'] = data['Review'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Convert 'Rating' column to numeric (if it contains strings)
data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce')

# Filter out rows with non-date values in the 'Date' column
data = data[pd.to_datetime(data['Date'], errors='coerce').notna()]

# Group data by rating and date (assuming you have a 'Date' column)
data['Date'] = pd.to_datetime(data['Date'])  # Assuming you have a 'Date' column
rating_sentiments = data.groupby(['Rating', 'Date']).mean().reset_index()

# Separate ratings 1-3 and 4-5
ratings_1_3 = rating_sentiments[rating_sentiments['Rating'].between(1, 3)]
ratings_4_5 = rating_sentiments[rating_sentiments['Rating'].between(4, 5)]

# Plot line charts for sentiments over time for ratings 1-3
plt.figure(figsize=(10, 6))
sns.lineplot(data=ratings_1_3, x='Date', y='Sentiment', hue='Rating')
plt.title("Sentiment Over Time for Ratings 1-3")
plt.xlabel("Date")
plt.ylabel("Average Sentiment")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Rating')
plt.show()

# Plot line charts for sentiments over time for ratings 4-5
plt.figure(figsize=(10, 6))
sns.lineplot(data=ratings_4_5, x='Date', y='Sentiment', hue='Rating')
plt.title("Sentiment Over Time for Ratings 4-5")
plt.xlabel("Date")
plt.ylabel("Average Sentiment")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Rating')
plt.show()


# In[30]:


import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel data
file_path = "D:\\Data_Analytics_Portfolio\\Projects\\SnapCarwash_Text_Analysis\\reviews.xlsx"
data = pd.read_excel(file_path)

# Convert NaN or blank cells to empty strings in the 'Review' column
data['Review'] = data['Review'].fillna('')

# Calculate sentiment for each review
data['Sentiment'] = data['Review'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Convert 'Rating' column to numeric (if it contains strings)
data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce')

# Filter out rows with non-date values in the 'Date' column
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Separate ratings 1-3 and 4-5
ratings_1_3 = data[data['Rating'].between(1, 3)]
ratings_4_5 = data[data['Rating'].between(4, 5)]

# Get the total number of reviews for ratings 1-3 and 4-5
total_reviews_1_3 = ratings_1_3.shape[0]
total_reviews_4_5 = ratings_4_5.shape[0]

# Plot line charts for sentiments over time for ratings 1-3
plt.figure(figsize=(10, 6))
sns.lineplot(data=ratings_1_3, x='Date', y='Sentiment', hue='Rating')
plt.title("Sentiment Over Time for Ratings 1-3")
plt.xlabel("Date")
plt.ylabel("Average Sentiment")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Rating')
plt.text(0.5, -0.15, f'Total Reviews: {total_reviews_1_3}',
         horizontalalignment='center', transform=plt.gca().transAxes)
plt.show()

# Plot line charts for sentiments over time for ratings 4-5
plt.figure(figsize=(10, 6))
sns.lineplot(data=ratings_4_5, x='Date', y='Sentiment', hue='Rating')
plt.title("Sentiment Over Time for Ratings 4-5")
plt.xlabel("Date")
plt.ylabel("Average Sentiment")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Rating')
plt.text(0.5, -0.15, f'Total Reviews: {total_reviews_4_5}',
         horizontalalignment='center', transform=plt.gca().transAxes)
plt.show()


# In[32]:


import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel data
file_path = "D:\\Data_Analytics_Portfolio\\Projects\\SnapCarwash_Text_Analysis\\reviews.xlsx"
data = pd.read_excel(file_path)

# Convert NaN or blank cells to empty strings in the 'Review' column
data['Review'] = data['Review'].fillna('')

# Calculate sentiment for each review
data['Sentiment'] = data['Review'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Convert 'Rating' column to numeric (if it contains strings)
data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce')

# Filter out rows with non-date values in the 'Date' column
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Separate ratings 1 and 5
ratings_1 = data[data['Rating'] == 1]
ratings_5 = data[data['Rating'] == 5]

# Get the total number of reviews for ratings 1 and 5
total_reviews_1 = ratings_1.shape[0]
total_reviews_5 = ratings_5.shape[0]

# Plot line chart for sentiments over time for ratings 1 and 5
plt.figure(figsize=(10, 6))
sns.lineplot(data=ratings_1, x='Date', y='Sentiment', label='Rating 1')
sns.lineplot(data=ratings_5, x='Date', y='Sentiment', label='Rating 5')
plt.title("Sentiment Over Time for Ratings 1 and 5")
plt.xlabel("Date")
plt.ylabel("Average Sentiment")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Rating')
plt.text(0.5, -0.15, f'Total Reviews for Rating 1: {total_reviews_1}\nTotal Reviews for Rating 5: {total_reviews_5}',
         horizontalalignment='center', transform=plt.gca().transAxes)
plt.show()


# In[33]:


import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel data
file_path = "D:\\Data_Analytics_Portfolio\\Projects\\SnapCarwash_Text_Analysis\\reviews.xlsx"
data = pd.read_excel(file_path)

# Convert NaN or blank cells to empty strings in the 'Review' column
data['Review'] = data['Review'].fillna('')

# Calculate sentiment for each review
data['Sentiment'] = data['Review'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Convert 'Rating' column to numeric (if it contains strings)
data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce')

# Filter out rows with non-date values in the 'Date' column
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Separate ratings 1-3 and 4-5
ratings_1_3 = data[data['Rating'].between(1, 3)]
ratings_4_5 = data[data['Rating'].between(4, 5)]

# Get the total number of reviews for each graph
total_reviews_1_3 = len(ratings_1_3)
total_reviews_4_5 = len(ratings_4_5)

# Plot line charts for sentiments over time for ratings 1-3
plt.figure(figsize=(10, 6))
sns.lineplot(data=ratings_1_3, x='Date', y='Sentiment', hue='Rating')
plt.title("Sentiment Over Time for Ratings 1-3")
plt.xlabel("Date")
plt.ylabel("Average Sentiment")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Rating')
plt.text(0.5, -0.15, f'Total Reviews: {total_reviews_1_3}',
         horizontalalignment='center', transform=plt.gca().transAxes)
plt.show()

# Plot line charts for sentiments over time for ratings 4-5
plt.figure(figsize=(10, 6))
sns.lineplot(data=ratings_4_5, x='Date', y='Sentiment', hue='Rating')
plt.title("Sentiment Over Time for Ratings 4-5")
plt.xlabel("Date")
plt.ylabel("Average Sentiment")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title='Rating')
plt.text(0.5, -0.15, f'Total Reviews: {total_reviews_4_5}',
         horizontalalignment='center', transform=plt.gca().transAxes)
plt.show()

# Count of reviews over time for ratings 1-3
plt.figure(figsize=(10, 6))
ratings_1_3_count = ratings_1_3.groupby('Date').size()
ratings_1_3_count.plot(kind='bar', color='blue')
plt.title("Count of Reviews for Ratings 1-3 Over Time")
plt.xlabel("Date")
plt.ylabel("Count of Reviews")
plt.xticks(rotation=45)
plt.tight_layout()
plt.text(0.5, -0.15, f'Total Reviews: {total_reviews_1_3}',
         horizontalalignment='center', transform=plt.gca().transAxes)
plt.show()

# Count of reviews over time for ratings 4-5
plt.figure(figsize=(10, 6))
ratings_4_5_count = ratings_4_5.groupby('Date').size()
ratings_4_5_count.plot(kind='bar', color='green')
plt.title("Count of Reviews for Ratings 4-5 Over Time")
plt.xlabel("Date")
plt.ylabel("Count of Reviews")
plt.xticks(rotation=45)
plt.tight_layout()
plt.text(0.5, -0.15, f'Total Reviews: {total_reviews_4_5}',
         horizontalalignment='center', transform=plt.gca().transAxes)
plt.show()


# In[ ]:




