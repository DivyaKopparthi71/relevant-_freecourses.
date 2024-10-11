# GenAI 
# 🌐 Course Search Application

## 🎓 Introduction
Welcome aboard the Course Search Application! Imagine a world where finding the perfect online course is as effortless as a click. This platform redefines your learning journey by harnessing the power of advanced embedding models and clustering techniques to make course discovery a breeze.

## 🚧 Problem Statement
In a vast ocean of online courses, searching for the right free course can feel like searching for a needle in a haystack. Traditional keyword-based search systems often leave users adrift, struggling to locate courses that resonate with their interests. This application transforms the search process, empowering users to navigate effortlessly and find courses that truly matter to them.

## 🔍 Methodology

### 📊 Data Collection
Our treasure trove of course data is sourced from the esteemed Analytics Vidhya Course Collection, culminating in a dynamic dataset of **50-70** carefully curated courses. Each entry encompasses:
- **Course Title**: Your guide to new knowledge.
- **Course Description**: A glimpse into what you'll learn.
- **Course Curriculum**: The roadmap of your educational journey.
- **Course URL**: Your gateway to discovery.

### 🔍 Text Embedding and Clustering
To craft an intuitive search experience, we deployed:
- **TF-IDF Vectorization:** This clever technique elevates word significance, ensuring the most pertinent terms shine brightly.
- **Clustering Models:** We embraced K-means and DBSCAN, two powerful algorithms, to seamlessly group similar courses and enhance recommendations.

## 🤖 Clustering Model Selection
- **K-means:** Think of it as your trusty compass, quickly guiding you to clusters of similar courses for swift access.
- **DBSCAN:** This method is like a skilled cartographer, adept at identifying diverse clusters and achieving a noteworthy Silhouette Score of **0.64701** with PCA, even in challenging terrains.

## 📈 Results and Evaluation
The true magic of our application is unveiled through rigorous evaluations, focusing on:
- **Silhouette Score:** A metric that reflects the quality of clustering.
- **Response Time:** Measuring how swiftly your queries are met.
- **User Satisfaction:** Real user feedback to ensure our recommendations hit the mark.

## ⚠️ Challenges and Limitations
The journey wasn’t without its hurdles. We encountered challenges like data quality issues and the model's occasional struggle to grasp the subtleties of user queries. These insights illuminate our path for future improvements and refinements.

## 🌟 Conclusion
The Course Search Application is a testament to the fusion of technology and education, showcasing how embedding models and clustering techniques can revolutionize course discovery. As we look to the future, our goals include expanding our dataset and continually refining our models based on the invaluable feedback from our users.

## 🌐 Live Application
Ready to embark on your learning adventure? Access the Course Search Application [here](https://relevant-freecourses-aq4xjvgwrez2jhfcfbx9x9.streamlit.app/) and find your next educational opportunity!
