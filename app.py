# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import pandas as pd
import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=464a111556ac6f0575fc1e95ff720708&language=en-US".format(
        movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    recommended_movies_names = []
    recommended_movies_poster = []
    for i in movies_list[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movies_names.append(movies.iloc[i[0]].title)
        # fetch poster  from Api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies_names, recommended_movies_poster


movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
movie_list = movies['title'].values
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movie_list)

if st.button('Show Recommendations'):
    recommended_movies_names, recommended_movies_poster = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies_names[0])
        st.image(recommended_movies_poster[0])

    with col2:
        st.text(recommended_movies_names[1])
        st.image(recommended_movies_poster[1])

    with col3:
        st.text(recommended_movies_names[2])
        st.image(recommended_movies_poster[2])

    with col4:
        st.text(recommended_movies_names[3])
        st.image(recommended_movies_poster[3])

    with col5:
        st.text(recommended_movies_names[4])
        st.image(recommended_movies_poster[4])
