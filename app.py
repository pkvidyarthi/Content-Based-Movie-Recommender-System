import streamlit as st
import json
import pandas as pd
import requests

# Function for fetching poster
def posterFetching(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=009859e96aae00ca3e03550fbdafd804&language=en-US'
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')

# Function for recommending movies
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

# ✅ Load movie data from GitHub (raw link)
file_url = 'https://raw.githubusercontent.com/pkvidyarthi/Content-Based-Movie-Recommender-System/main/movie.json'
response = requests.get(file_url)
movies_dict = response.json()
movies = pd.DataFrame(movies_dict)

# ✅ Load similarity data from GitHub (raw link)
similarity_url = 'https://raw.githubusercontent.com/pkvidyarthi/Content-Based-Movie-Recommender-System/main/similarity.json'
similarity = pd.read_json(similarity_url)

st.title('🎬 Movie Recommender System')

# Selectbox from streamlit
option = st.selectbox(
    'Please select your favorite movie, as my job is to recommend some movies to you',
    movies['title'].values
)

# Button
if st.button('Recommend'):
    names, poster = Recommend(option)
    columns = st.columns(5)
    for i in range(5):
        with columns[i]:
            st.text(names[i])
            st.image(poster[i])
