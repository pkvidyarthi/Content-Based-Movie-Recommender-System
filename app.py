import streamlit as st
import json
import pandas as pd
import requests
import os

# -------------------------------------------------
# ✅ Get correct absolute path for both local & Streamlit Cloud
# -------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -------------------------------------------------
# ✅ Load movie.json file
# -------------------------------------------------
movie_path = os.path.join(BASE_DIR, 'movie.json')
with open(movie_path, 'r', encoding='utf-8') as f:
    movies_dict = json.load(f)
movies = pd.DataFrame(movies_dict)

# -------------------------------------------------
# ✅ Load similarity.json file
# -------------------------------------------------
similarity_path = os.path.join(BASE_DIR, 'similarity.json')
with open(similarity_path, 'r', encoding='utf-8') as f:
    similarity = json.load(f)

# -------------------------------------------------
# ✅ Function to fetch movie poster
# -------------------------------------------------
def posterFetching(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=009859e96aae00ca3e03550fbdafd804&language=en-US'
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')

# -------------------------------------------------
# ✅ Function to recommend movies
# -------------------------------------------------
def Recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movie_index = int(movie_index)
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommendedMovies = []
    recommendPoster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommendedMovies.append(movies.iloc[i[0]].title)
        recommendPoster.append(posterFetching(movie_id))
    return recommendedMovies, recommendPoster

# -------------------------------------------------
# ✅ Streamlit UI
# -------------------------------------------------
st.title('🎬 Movie Recommender System')

option = st.selectbox(
    'Please select your favorite movie, as my job is to recommend some movies to you',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = Recommend(option)
    columns = st.columns(5)
    for i in range(5):
        with columns[i]:
            st.text(names[i])
            st.image(posters[i])
