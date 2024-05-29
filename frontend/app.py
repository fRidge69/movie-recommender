import pickle
from urllib import response

import streamlit as st
import pandas as pd
import requests

st.title('Movie Recommender System')

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similiarity = pickle.load(open('similiarity.pkl', 'rb'))
selected_movie_name =st.selectbox('Which Movie would you like to recommend?',movies['title'].values)


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similiarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

if st.button('Recommend'):
    recommenations = recommend(selected_movie_name)
    for i in recommenations:
        st.write(i)




