🎬 Movie Recommendation System (AI/ML Project)
🚀 Overview

This project is a content-based Movie Recommendation System that suggests similar movies based on metadata such as genres, overview, cast, keywords, and director.

The system uses Natural Language Processing (NLP) and Machine Learning techniques to compute similarity between movies and provide accurate recommendations.

🎯 Features
🎥 Recommend top 5 similar movies
🧠 Uses TF-IDF for text vectorization
📊 Cosine similarity for matching
⚡ FastAPI backend (REST API)
🌌 Streamlit UI with dark universe theme
👻 Horror-themed interactive design
🧠 Tech Stack
Python
Pandas
Scikit-learn
FastAPI
Streamlit
Pickle
📊 Machine Learning Approach

1. Feature Engineering
Combined multiple features:
Overview
Genres
Keywords
Cast
Crew (Director)
Created a single tags column

2. Vectorization
Applied TF-IDF Vectorizer
Converted text into numerical vectors

3. Similarity Calculation
Used Cosine Similarity:
similarity(A,B) = (A · B) / (||A|| ||B||)
Measures angle between vectors
Higher score = more similar movies

⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender

2. Install dependencies
pip install -r requirements.txt

3. Run Backend API
uvicorn api:app --reload

4. Run Frontend
streamlit run app.py

🌐 API Usage
Endpoint:
GET /recommend?movie=avatar
Response:
{
  "recommendations": [
    "Movie 1",
    "Movie 2",
    "Movie 3"
  ]
}
