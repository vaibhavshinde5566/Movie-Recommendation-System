from fastapi import FastAPI
import pickle

app = FastAPI()

# load data
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

movies = pickle.load(open(os.path.join(BASE_DIR, 'movies.pkl'), 'rb'))
similarity = pickle.load(open(os.path.join(BASE_DIR, 'similarity.pkl'), 'rb'))


@app.get("/")
def home():
    return {"message": "Movie Recommendation API is running"}


@app.get("/recommend")
def recommend(movie: str):
    
    movie = movie.lower()
    
    idx = movies[movies['title'].str.lower() == movie].index
    
    if len(idx) == 0:
        return {"error": "Movie not found"}
    
    idx = idx[0]
    
    distances = similarity[idx]
    
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]
    
    recommendations = []
    
    for i in movies_list:
        recommendations.append(movies.iloc[i[0]].title)
    
    return {"recommendations": recommendations}