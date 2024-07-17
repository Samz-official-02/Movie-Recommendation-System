import pickle
import pandas as pd
import requests
import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Function to fetch movie poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path

# Function to download file from GitHub release
def download_file_from_github_release(url, file_name):
    response = requests.get(url)
    with open(file_name, 'wb') as file:
        file.write(response.content)

# Download precomputed similarity matrix from GitHub release if not present
similarity_file = 'model/similarity.pkl'
if not os.path.exists(similarity_file):
    github_release_url = 'https://github.com/Samz-alpha-02/Movie-Recommendation-System/releases/download/v0.0.1/similarity.pkl'
    download_file_from_github_release(github_release_url, similarity_file)

# Load movie_dict.pkl
with open('model/movie_dict.pkl', 'rb') as f:
    movies_dict = pickle.load(f)

movies = pd.DataFrame(movies_dict)

# Load precomputed similarity matrix
with open(similarity_file, 'rb') as f:
    similarity = pickle.load(f)

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

# Flask routes
@app.route('/')
def home():
    movie_list = movies['title'].values
    return render_template('index.html', movie_list=movie_list)

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    movie = request.form['movie']
    recommended_movie_names, recommended_movie_posters = recommend(movie)
    recommendations = [{'title': name, 'poster': poster} for name, poster in zip(recommended_movie_names, recommended_movie_posters)]
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
