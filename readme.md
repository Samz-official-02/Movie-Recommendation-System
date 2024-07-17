# Movie Recommendation System

# Overview

**This project is a movie recommendation system built using Python, Flask, and Select2 for an enhanced user interface. It recommends movies based on cosine similarity, allowing users to select or type a movie name and receive a list of similar movies along with their posters.**

# Business Use Case

## Problem Statement:

The entertainment industry, particularly streaming services and movie theaters, face the challenge of effectively recommending movies to users. With vast libraries of content, users often struggle to find movies that match their preferences, leading to dissatisfaction and potential loss of subscribers or customers.

## Business Use Case:

A streaming service wants to implement a movie recommendation system to enhance user engagement and satisfaction. The system should help users discover movies they are likely to enjoy, thereby increasing the time they spend on the platform and reducing churn rates.

## Solution:

The Movie Recommendation System leverages cosine similarity to recommend movies based on user-selected inputs. By integrating this system into a streaming platform or a movie recommendation website, the business can provide personalized recommendations to users, improving their overall experience.

# How This System Solves the Problem:
1. **Personalized Recommendations:** The system uses cosine similarity to recommend movies similar to the one selected by the user. This personalization helps users discover new movies aligned with their tastes, increasing user satisfaction and engagement.

2. **Enhanced User Experience:** The user-friendly interface, enhanced with Select2 for search-enabled dropdowns, ensures that users can easily find and select movies. This seamless experience keeps users engaged and encourages them to explore more content.

3. **Visual Appeal:** Displaying movie posters along with titles makes the recommendations visually appealing, enticing users to check out the suggested movies. This visual element can increase click-through rates and movie viewings.

4. **Scalability:** The system can be easily scaled to handle large libraries of movies, making it suitable for streaming services with extensive catalogs. The use of Flask ensures that the application can handle multiple user requests efficiently.

5. **Data-Driven Insights:** By analyzing user interactions with the recommendation system, businesses can gain insights into user preferences and viewing patterns. This data can inform content acquisition and marketing strategies.

## Implementation in a Streaming Service:

1. **Integration:** The streaming service integrates the Movie Recommendation System into its platform. This involves setting up the backend with Flask, loading the necessary data, and deploying the application on a scalable cloud platform like Render.

2. **User Interaction:** Users interact with the system by selecting or typing a movie name in the dropdown box. The system processes this input and recommends similar movies, displaying their posters and titles.

3. **Continuous Improvement:** The service continuously updates the movie data and cosine similarity matrix to reflect new releases and changing user preferences. This ensures that recommendations remain relevant and up-to-date.

4. **Marketing and Engagement:** The platform uses the recommendation system to create personalized marketing campaigns. For example, sending tailored movie suggestions via email or push notifications based on users' viewing history and preferences.

5. **Feedback Loop:** The service collects feedback from users on the recommended movies, refining the recommendation algorithm to improve accuracy over time. This feedback loop helps in delivering increasingly relevant suggestions.

By implementing the Movie Recommendation System, the streaming service can enhance user satisfaction, increase engagement, and reduce churn rates, ultimately driving growth and revenue.

# Cloud Deployment Link:

The application is deployed on a Cloud Platform `Render`.

You can access the application using the given Deployment Link: [Movie Recommendation System](https://movie-recommendation-system-573d.onrender.com/)

# Features

* Recommends movies based on cosine similarity.
* Allows users to select a movie from a dropdown list.
* Displays movie posters and titles.
* User-friendly interface with a search-enabled dropdown (Select2).

# Prerequisites

* Python 3.x
* Flask
* Pandas
* Scikit-learn
* Requests

# Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

2. Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install the required packages:

```
pip install -r requirements.txt
```

# Usage

### Local Machine

1. Run the Flask app:

```
python app.py
```

2. Open your web browser and go to:

```
http://127.0.0.1:8000/
```

# Project Details

* `app.py`

The main Flask application file. It contains routes to handle the home page and movie recommendations. It also includes functions to load the necessary data and calculate recommendations.

* `templates/index.html`

The HTML template file for the home page. It includes the structure and styling for the user interface, incorporating Select2 for the enhanced dropdown menu.

* `static/background.jpg`

A background image used in the web page for a better visual appeal.

* `model/movie_dict.pkl`

A pickle file containing the movie data used for recommendations.

* `model/similarity.pkl`

A pickle file containing the precomputed cosine similarity matrix.

## Functions and Their Purpose

* `fetch_poster(movie_id)`

Fetches the movie poster using The Movie Database (TMDb) API.

* `download_file_from_github_release(url, file_name)`

Downloads a file from a GitHub release URL.

* `recommend(movie)`

Calculates movie recommendations based on cosine similarity.

## Flask Routes

* `/`

Renders the home page with the movie dropdown list.

* `/recommend`

Accepts a POST request with the selected movie and returns a list of recommended movies in JSON format.

# How to Use the Application

* Select or type a movie name in the dropdown box.
* Click the "Show Recommendation" button.
* The recommended movies along with their posters will be displayed on the page.


# Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to your branch and create a pull request.

# License

This project is licensed under the MIT License.