import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the saved DataFrame and embeddings from the pickle file
@st.cache_resource
def load_data():
    with open('course_finally_model.pkl', 'rb') as f:
        data = pickle.load(f)
    
    # Extract data from the loaded dictionary
    df = data['df']
    vectorizer = data['vectorizer']
    embeddings = np.array(data['embeddings'])  # Ensure this is a NumPy array
    
    return df, vectorizer, embeddings

# Function to search courses based on a query
def search_courses(query, embeddings, df, vectorizer):
    # Transform the user query to the same embedding space
    query_embedding = vectorizer.transform([query])
    
    # Calculate cosine similarity between the query embedding and course embeddings
    cosine_similarities = np.dot(embeddings, query_embedding.T).flatten()

    # Check for valid cosine similarities
    if not np.any(cosine_similarities):
        return pd.DataFrame()  # Return empty DataFrame if no valid similarities

    # Get the indices of the top 5 most similar courses
    top_indices = np.argsort(cosine_similarities)[-5:][::-1]
    
    # Return the top courses
    return df.iloc[top_indices]

# CSS for double-shaded background color with linear gradient
st.markdown("""
    <style>
    /* Target the main Streamlit app container */
    .stApp {
        background: linear-gradient(135deg, #ff7e5f, #feb47b); /* Shades of red to orange gradient */
        background-size: cover;
        background-position: center;
    }

    /* Optional: Adjust text color for better readability */
    .stApp * {
        color: #ffffff;
    }

    /* Optional: Style the course link boxes */
    .course-link {
        background-color: rgba(240, 240, 240, 0.8); /* Semi-transparent light gray */
        padding: 10px;
        border-radius: 5px;
        display: inline-block;
    }
    .course-link a {
        text-decoration: none;
        color: #007bff;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit app layout
st.title("🎓 Course Search Application")

# Load data and embeddings
df, vectorizer, embeddings = load_data()

# Search bar for querying courses
query = st.text_input("🔍 Enter course name or keyword")

if query:
    results = search_courses(query, embeddings, df, vectorizer)
    st.subheader("📚 Search Results")

    if results.empty:
        st.write("🚫 No courses found.")
    else:
        for index, row in results.iterrows():
            st.markdown(f"**📌 Course Title:** {row['Course Title']}")
            st.markdown(f"**📝 Course Description:** {row['Course Description']}")
            st.markdown(f"**📄 Course Curriculum:** {row['Course Curriculum']}")

            # Create a styled box for the course link using the CSS class
            st.markdown(
                f"""
                <div class="course-link">
                    <a href="{row['Course URL']}" target="_blank">🔗 Course Link</a>
                </div>
                """, 
                unsafe_allow_html=True
            )
            st.write("---")
