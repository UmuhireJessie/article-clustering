import streamlit as st
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import datetime
import os
import json

# Setting up the Streamlit page configuration
st.set_page_config(page_title="Latest News Clusters")

# News API settings
API_ENDPOINT = "https://newsapi.org/v2/top-headlines?country=us&apiKey=4a8422b7876b4fbb9628dc900e9c24d7"
API_KEY = "4a8422b7876b4fbb9628dc900e9c24d7"  # Please replace this with your actual News API key

# Define the number of clusters for article grouping
CLUSTER_COUNT = 10

# Function to retrieve or fetch news articles from the cache or API
def get_articles():
    cache_path = "article_cache.json"
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    # Check if cached data is available and up-to-date
    if os.path.isfile(cache_path):
        with open(cache_path, "r") as file:
            cached_data = json.load(file)
            if cached_data.get("date") == today:
                return cached_data["news"]
    
    # Fetch new articles if no valid cache is found
    response = requests.get(API_ENDPOINT.replace("YOUR_API_KEY", API_KEY))
    if response.ok:
        news_data = response.json().get("articles", [])
        # Cache the fetched articles
        with open(cache_path, "w") as file:
            json.dump({"date": today, "news": news_data}, file)
        return news_data
    return []

def cluster_news():
    st.title("Clustered News Articles")

    # Retrieve news articles
    news_articles = get_articles()

    # Preprocess articles to extract relevant content
    article_texts = [article["description"] or article["content"] for article in news_articles if article.get("description") or article.get("content")]

    # Apply TF-IDF Vectorization and K-Means Clustering
    vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(article_texts)
    kmeans = KMeans(n_clusters=CLUSTER_COUNT, random_state=42)
    labels = kmeans.fit_predict(tfidf_matrix)

    # Display the articles grouped by cluster
    for cluster_id in range(CLUSTER_COUNT):
        st.subheader(f"CLUSTER {cluster_id + 1}")
        for idx, cluster_label in enumerate(labels):
            if cluster_label == cluster_id:
                article = news_articles[idx]
                st.write(f"- [{article['title']}]({article['url']})")

# Run the main function when the script is executed
if __name__ == "__main__":
    cluster_news()
