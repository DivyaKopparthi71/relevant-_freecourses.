import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the saved DataFrame and embeddings from pickle files
@st.cache_resource
def load_data():
    with open('free_course_data.pkl', 'rb') as f:
        df = pickle.load(f)
    
    with open('course_embeddings.pkl', 'rb') as f:
        embeddings_data = pickle.load(f)
        vectorizer = embeddings_data['vectorizer']
        embeddings = embeddings_data['embeddings']
    
    return df, vectorizer, embeddings

# Function to search courses based on a query
def search_courses(query, embeddings, df, vectorizer):
    # Transform the user query to the same embedding space
    query_embedding = vectorizer.transform([query])
    
    # Calculate cosine similarity between the query embedding and course embeddings
    cosine_similarities = np.dot(embeddings, query_embedding.T).toarray().flatten()
    
    # Get the indices of the top 5 most similar courses
    top_indices = np.argsort(cosine_similarities)[-5:][::-1]
    
    # Return the top courses
    return df.iloc[top_indices]

# CSS for a background image
st.markdown("""
<style>
body {
    background-image: url('https://example.com/your-image.jpg'); /* Replace with your image URL */
    background-size: cover;
    background-position: center;
}
</style>
""", unsafe_allow_html=True)

# Streamlit app layout
st.title("Course Search Application")

# Load data and embeddings
df, vectorizer, embeddings = load_data()

# Search bar for querying courses
query = st.text_input("Enter course name or keyword")

if query:
    results = search_courses(query, embeddings, df, vectorizer)
    st.subheader("Search Results")

    if results.empty:
        st.write("No courses found.")
    else:
        for index, row in results.iterrows():
            st.write(f"**Course Title:** {row['Course Title']}")
            st.write(f"**Course Description:** {row['Course Description']}")
            st.write(f"**Course Curriculum:** {row['Course Curriculum']}")

            # Create a styled box for the course link
            st.markdown(
                f"""
                <div style="background-color: #f0f0f0; padding: 10px; border-radius: 5px; display: inline-block;">
                    <a href="{row['Course URL']}" style="text-decoration: none; color: #007bff;">Course Link</a>
                </div>
                """, 
                unsafe_allow_html=True
            )
            st.write("---")
