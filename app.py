import streamlit as st
import pickle
import pandas as pd
from backend import get_poster


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # finding the index of the movie
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
                  1:6]  # finding the 5 most similar movies
    recommend_movies = []
    movie_id = []
    recommend_overview = []
    recommend_genres = []
    recommend_cast = []
    recommend_crew = []
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
        movie_id.append(movies.iloc[i[0]].id)
        recommend_overview.append(movies.iloc[i[0]].overview1)
        recommend_genres.append(movies.iloc[i[0]].genres)
        recommend_cast.append(movies.iloc[i[0]].cast)
        recommend_crew.append(movies.iloc[i[0]].crew)

    return recommend_movies, movie_id, recommend_overview, recommend_genres, recommend_cast, recommend_crew


movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

option = st.selectbox('How would like to be contented?', movies['title'].values)


if st.button('Recommend'):
    recommend_name, recommend_id, recommend_over, recommend_gen, recommend_cas, recommend_cre = recommend(option)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(recommend_name[0])
        st.image(get_poster(recommend_id[0]))
        st.write(recommend_over[0])

    with col2:
        st.subheader(recommend_name[1])
        st.image(get_poster(recommend_id[1]))
        st.write(recommend_over[1])

    with col1:
        st.header(recommend_name[2])
        st.image(get_poster(recommend_id[2]))
        st.write(recommend_over[2])

    with col2:
        st.header(recommend_name[3])
        st.image(get_poster(recommend_id[3]))
        st.write(recommend_over[3])

    with col1:
        st.header(recommend_name[4])
        st.image(get_poster(recommend_id[4]))
        st.write(recommend_over[4])

