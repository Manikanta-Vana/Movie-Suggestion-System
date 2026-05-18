import streamlit as st
import pandas as pd
import pickle

# Load movie data and similarity matrix
movies = pd.read_csv('movies_clean.csv')

with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

# Streamlit UI setup
st.title('🎬 Movie Recommendation System')
st.write("Enter a movie you like, and we'll recommend similar ones!")

# Use a dropdown with movie suggestions
movie_name = st.selectbox('Select or type a movie title:', movies['title'].values)

# Define the recommendation function
def recommend_movies(movie_name):
    if movie_name not in movies['title'].values:
        return ["Movie not found."]
    
    index = movies[movies['title'] == movie_name].index[0]
    sim_scores = list(enumerate(similarity[index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    recommended_movies = [movies.iloc[i[0]].title for i in sim_scores]
    return recommended_movies

# Show recommendations
if st.button('Get Recommendations'):
    recommendations = recommend_movies(movie_name)
    st.write('Here are some movies you might like:')
    for movie in recommendations:
        st.write(f'🎥 {movie}')
