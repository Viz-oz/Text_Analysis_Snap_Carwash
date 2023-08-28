#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# Path to retrieve the review data
file_path = "D:\\Data_Analytics_Portfolio\\Projects\\SnapCarwash_Text_Analysis\\reviews.xlsx"

# Loading the Excel data
data = pd.read_excel(file_path)

# Convert NaN or blank cells to empty strings in the 'Review' column
data['Review'] = data['Review'].fillna('')

# Convert 'Rating' column to numeric (if it contains strings)
data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce')

# Perform topic modeling for each rating group
for rating in range(1, 6):
    rating_group = data[data['Rating'] == rating]
    if len(rating_group) > 0:
        print(f"Topic Modeling Results for Rating {rating}:")
        vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
        X = vectorizer.fit_transform(rating_group['Review'])

        lda = LatentDirichletAllocation(n_components=5, random_state=42)
        lda.fit(X)

        for idx, topic in enumerate(lda.components_):
            top_words = [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]]
            print(f"Topic #{idx + 1}: {', '.join(top_words)}")

        print("Number of Reviews:", len(rating_group))
        print("\n")
        


# In[5]:


# Calculate total number of all reviews
total_reviews = len(data)
print("Total Number of All Reviews:", total_reviews)

# Calculate the count of reviews for each rating
rating_counts = data['Rating'].value_counts().sort_index()
print("\nCount of Reviews for Each Rating:")
print(rating_counts)


# In[6]:


# Calculate the average rating
average_rating = data['Rating'].mean()

print("Average Rating:", average_rating)


# In[17]:


# Filter reviews with ratings 1, 2, and 3
filtered_reviews = data[data['Rating'].isin([1, 2, 3])]

# Print the filtered reviews
for idx, review in enumerate(filtered_reviews['Review'], start=1):
    print(f"Review #{idx}:\n{review}\n")


# In[ ]:





# In[ ]:




