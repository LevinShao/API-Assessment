# TMDb Movie Database Explorer

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A warm welcome to the TMDb Movie Database Explorer! This is a top-tier command-line application that interacts with The Movie Database (TMDb) API to search, browse, and discover movies. With this application, you can discover ANY movie. You could find detailed information about a movie, find a new movie to watch at home, discover upcoming releases to your nearby cinema, or even find your new favorite movie of all time!

## Features

- Search movies by title
- View detailed movie information (ratings, cast, budget, etc.)
- Browse currently popular movies
- Discover upcoming releases
- Filter movies by genre
- Get recommendations based on movies you like
- View your search history
- A comprehensive help guide that teaches you how to use the program

## How It Works

The program uses TMDb's Movie API to:
1. Fetch movie data in JSON format
2. Parse and display it in an organized table view
3. Maintain a local search history of your queries
4. Provide multiple ways to discover movies

All data is fetched in real-time from TMDb's servers.

However, TMDb APIs are subjected to rate limits, so be careful of that. But no worries, they are unlikely to occur unless if you are searching up LOTS of movies.

## Installation Procedure

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/tmdb-movie-explorer.git
   cd tmdb-movie-explorer
   ```
2. **Install dependencies from requirements.txt**
    ```
    pip install requests
    pip install datetime
    pip install time
    ```
3. **Run the program!**
    ```
    python main.py
    ```