import requests # essential if you want to work with APIs
from datetime import datetime # for search history time-logging

class TMDbMovieProgram: # will import this whole thing to main.py
    def __init__(self, api_key):
        self.API_KEY = api_key # Storage to store the API key for all future requests
        self.BASE_URL = "https://api.themoviedb.org/3/" # Base endpoint for all API calls to TMDb database
        self.search_history = [] # Storage to store search queries for the search history option
        self.genres = {
            28: "Action", 12: "Adventure", 35: "Comedy",
            18: "Drama", 27: "Horror", 10749: "Romance",
            878: "Science Fiction", 53: "Thriller",
            16: "Animation", 80: "Crime"
        } # The list of genres and their corresponding genre IDs. Currently there are only these 10 but more are coming soon

    def _fetch_tmdb_data(self, endpoint, params=None): # A helper method that fetches data for all the other methods
        """Method that attempts to fetch the data from the TMDb database"""
        # I added an underscore before "fetch" to symbolize that this is an internal method instead of an external one
        # Basically doing internal work (fetching data for external methods)
        # External methods are all the other methods that are exposed to the user for selection
        # This is just a python convention that's not necessary, but I used it anyways to make it look neat
        try:
            params = params or {} # Initialize the params
            params["api_key"] = self.API_KEY
            response = requests.get(f"{self.BASE_URL}{endpoint}", params=params) # Construct the full URL and make GET request
            response.raise_for_status() # Raise exception for any HTTP errors
            return response.json() # Parse and return JSON response
        except requests.exceptions.RequestException as e:
            # Handle any request-related errors (connection, timeout, etc.)
            print(f"Error fetching data: {e}")
            return None

    def search_movies(self):
        """Option 1: Search a movie by its title and display results with IDs"""
        query = input("\nEnter movie title: ").strip()

        # Validate input isn't empty
        if not query:
            print("Title should not be empty. Please try again")
            return
        
        # Send an API request to search endpoint with user's query
        # https://api.themoviedb.org/3/search/movie?api_key=2b556e2cf294ec2f4a6b5fa4770f3732&query=[MOVIE NAME]
        data = self._fetch_tmdb_data("search/movie", {"query": query})
        
        if data and data.get("results"): # Check if we got valid results
            print("\nSearch Results (ID | Title | Release Date):")
            print("-" * 70)  # Divider lines to make the output look neater
            for idx, movie in enumerate(data["results"][:20], 1): # Only show the top 20 movie results
                # Get movie title and ID
                movie_id = movie.get('id', 'N/A')
                title = movie.get('title', 'Untitled')
                
                # Get the release date
                release_date = movie.get('release_date')
                display_date = release_date if release_date else "No date available" # Display 'no data available' when release date is not found
                
                # Format the result into a neat table with consistent spacing
                print(f"{idx:2}. ID: {movie_id:<8} | {title:<30} | {display_date}")
            
            self.search_history.append((f"Search: {query}", datetime.now())) # Add query to search history
        else:
            print("No movies found!")

    def get_movie_details(self):
        """Option 2: Get specific details from a movie"""
        print("\nThis will use TMDb Movie IDs to ensure accuracy.")
        print("If you don't know the ID, use option 1 to search first.")
        
        movie_id = input("\nEnter TMDb Movie ID (e.g. 550 for 'Fight Club'): ").strip()
        
        if not movie_id.isdigit():
            # Check if movie ID is valid
            print("Invalid ID! Must be a number.")
            return

        # Send an API request to database
        # https://api.themoviedb.org/3/movie/[MOVIE ID]?api_key=2b556e2cf294ec2f4a6b5fa4770f3732&append_to_response=credits,release_dates
        data = self._fetch_tmdb_data(f"movie/{movie_id}", {"append_to_response": "credits,release_dates"})

        # If there are no results, display "Movie not found!"
        if not data:
            print("Movie not found!")
            return

        # Title and release date
        print(f"\nTitle: {data.get('title', 'No data available')}")
        print(f"Release Date: {data.get('release_date', 'No data available')}")

        # Rating and vote count
        rating = data.get('vote_average')
        vote_count = data.get('vote_count', 0)
        if rating and vote_count > 0:
            print(f"Rating: {rating:.2f}/10 ({vote_count} votes)") # Format rating to 2 decimal places
        else:
            print("Rating: Not rated yet")

        # Age certification
        certifications = data.get('release_dates', {}).get('results', [])
        us_cert = 'No data available'

        for cert in certifications:
            if cert.get('iso_3166_1') == 'US':
                release_dates = cert.get('release_dates', [{}])
                us_cert = release_dates[0].get('certification', 'No data available')
                break

        print(f"Age Classification: {us_cert}")

        # Runtime
        runtime = data.get('runtime', 0)
        print(f"Runtime: {runtime} mins" if runtime > 0 else "Runtime: No data available")

        # Languages
        spoken_languages = [lang['english_name'] for lang in data.get('spoken_languages', [])]
        print(f"Languages: {', '.join(spoken_languages) if spoken_languages else 'No data available'}")

        # Genres
        genres = [g['name'] for g in data.get('genres', [])]
        print(f"Genres: {', '.join(genres) if genres else 'No data available'}")

        # Plot overview
        print(f"\nPlot: {data.get('overview', 'No description available')}")

        # Budget and box office info
        print(f"\nBudget (USD): ${data.get('budget', 0):,}" 
            if data.get('budget', 0) > 0 else "Budget: No data available")
        print(f"Total Box Office (USD): ${data.get('revenue', 0):,}" 
            if data.get('revenue', 0) > 0 else "Box Office: No data available")

        # Director/s
        directors = [
            p['name'] for p in data.get('credits', {}).get('crew', []) 
            if p['job'] == 'Director'
        ]
        print(f"\nDirector(s): {', '.join(directors) if directors else 'No data available'}")

        # Top 5 actors
        print("\nTop Cast:")
        cast = data.get('credits', {}).get('cast', [])
        if cast:
            for actor in cast[:5]:
                name = actor.get('name', 'Unknown actor')
                character = actor.get('character', 'Unknown role')
                print(f"- {name} as {character}")
        else:
            print("- No cast data available")

        # Production companies
        companies = [c['name'] for c in data.get('production_companies', [])]
        print(f"\nProduction Companies: {', '.join(companies) if companies else 'No data available'}")

        # Add to search history
        self.search_history.append((f"Details: {data['title']}", datetime.now()))

    def get_popular_movies(self):
        """Option 3: Display the current most popular movies on TMDb"""
        # Send an API request
        # https://api.themoviedb.org/3/movie/popular?api_key=2b556e2cf294ec2f4a6b5fa4770f3732
        data = self._fetch_tmdb_data("movie/popular")

        if data and data.get("results"):
            print("\nCurrent Popular Movies ( ID | Title | Release Date):")
            print("-" * 60)  # Divider line
            for idx, movie in enumerate(data["results"][:20], 1):
                # For each movie in top 10 results, fetch and display their ID, title and release date
                movie_id = movie.get('id', 'N/A')
                title = movie.get('title', 'Untitled')
                release_date = movie.get('release_date', 'No date available')
                
                # Format the result into a neat table with consistent spacing
                print(f"{idx:2}. ID: {movie_id:<8} | {title:<25} | {release_date}")
            
            self.search_history.append(("Popular Movies", datetime.now())) # Add to search history
        else:
            print("No popular movies data available!") # Print no data available if data retrieval fails

    def get_upcoming_movies(self):
        """Option 4: Fetch upcoming releases"""
        # Send an API request
        # https://api.themoviedb.org/3/movie/upcoming?api_key=2b556e2cf294ec2f4a6b5fa4770f3732
        data = self._fetch_tmdb_data("movie/upcoming")

        if data and data.get("results"):
            print("\nUpcoming Movies:")
            print("-" * 60)  # Divider line
            for idx, movie in enumerate(data["results"][:10], 1):
                # For each movie in top 10 results, fetch and display their ID, title and release date
                movie_id = movie.get('id', 'N/A')
                title = movie.get('title', 'Untitled')
                release_date = movie.get('release_date', 'No date available')

                # Format neatly into a table
                print(f"{idx:2}. ID: {movie_id:<8} | {title:<30} | {release_date}")
            self.search_history.append(("Upcoming Movies", datetime.now())) # Add to search history
        else:
            print("No upcoming movies data available!") # Print no data available if data retrieval fails

    def search_by_genre(self):
        """Option 5: Filter movies by genre using the class's genre dictionary"""
        print("\nNote: The numbers beside the genre is their corresponding genre ID.")
        print("\nAvailable Genres:")
        
        # Reference to call back self.genres for the list of genres 
        for id, name in sorted(self.genres.items()):
            print(f"{id}: {name}")
        
        # Check if genre ID is valid
        genre_id = input("\nEnter genre ID: ").strip()
        if not genre_id.isdigit() or int(genre_id) not in self.genres:
            print("Invalid genre ID! Please enter a valid number from the list.")
            return
        
        # Fetch data from TMDb database and also make it show most popular first
        # https://api.themoviedb.org/3/discover/movie?api_key=2b556e2cf294ec2f4a6b5fa4770f3732&with_genres=[GENRE ID]&sort_by=popularity.desc
        data = self._fetch_tmdb_data("discover/movie", {"with_genres": genre_id, "sort_by": "popularity.desc"})
        
        if data and data.get("results"):
            print(f"\n{self.genres[int(genre_id)]} Movies (ID | Title | Release Date):")
            print("-" * 60) # Divider line
            for idx, movie in enumerate(data["results"][:20], 1):
                # For each movie in top 20 results, fetch and display ID, title and release date 
                movie_id = movie.get('id', 'N/A')
                title = movie.get('title', 'Untitled')
                release_date = movie.get('release_date', 'No date available')

                # Format neatly into a table
                print(f"{idx:2}. ID: {movie_id:<8} | {title:<30} | {release_date}") # Neat formatting by using consistent spacing
            
            self.search_history.append((f"Genre: {self.genres[int(genre_id)]}", datetime.now())) # Add to search history
        else:
            print("No movies found in this genre!")

    def get_recommendations(self):
        """Option 6: Get recommendations based on a specific movie (i.e. fetch similar movies)"""
        movie_id = input("Enter TMDb Movie ID (e.g. 550 for 'Fight Club'): ").strip()

        # Check if movie ID is valid
        if not movie_id.isdigit():
            print("Invalid ID! Please input a valid numeric ID (e.g. 550 for 'Fight Club')")
            return
        
        # Fetch recommendations that are similar to the movie
        # https://api.themoviedb.org/3/movie/[MOVIE ID]/recommendations?api_key=2b556e2cf294ec2f4a6b5fa4770f3732
        data = self._fetch_tmdb_data(f"movie/{movie_id}/recommendations")

        if data and data.get("results"):
            print(f"\nRecommendations for Movie ID {movie_id}:")
            print("-" * 60)  # Divider line
            for idx, movie in enumerate(data["results"][:10], 1):
                # For each movie in top 10 results, fetch and display their ID, title and release date
                movie_id = movie.get('id', 'N/A')
                title = movie.get('title', 'Untitled')
                release_date = movie.get('release_date', 'No date available')

                # Neatly format into a table
                print(f"{idx:2}. ID: {movie_id:<8} | {title:<30} | {release_date}")
            self.search_history.append((f"Recommendations for Movie ID: {movie_id}", datetime.now())) # Add to search history
        else:
            print("No recommendations found!") # When no data is available

    def view_search_history(self):
        """Option 7: Display past searches"""
        # Display "No search history yet" if there isn't anything in history
        if not self.search_history:
            print("No search history yet.")
            return
        
        print("\nSearch History:")
        # Loop through each entry in the search history storage, and provide details for each
        for idx, (query, time) in enumerate(self.search_history, 1):
            print(f"{idx}. {query} - Searched up on {time.strftime('%Y-%m-%d %H:%M:%S')}")

    def help_guide(self):
        """Option 8: A simple help guide for beginners, made using ONLY the print function"""

        # Just to look neat and satisfying
        print("\n" + "="*50) # Top divider line
        print("MOVIE DATABASE HELP GUIDE".center(50)) # Print the text in the center
        print("="*50) # Bottom divider line
        
        print("\nHOW TO USE THIS PROGRAM:")
        print("-"*50)
        print("1. SEARCH MOVIES (Option 1):")
        print("   - Enter any movie title (e.g., 'Avengers'), and the program will return the top 20 matches along with their TMDb movie IDs and release dates")
        print("   - Example: Enter 'Inception' to find Christopher Nolan's film")
        
        print("\n2. GET MOVIE DETAILS (Option 2):")
        print("   - Use this option to find out details about one specific movie. This shows full details such as the movie's rating, plot, cast, etc.")
        print("   - You'll have to use TMDb Movie IDs instead of movie titles to search for the movie to ensure the program knows which movie you're talking about")
        print("   - You can find out the TMDb Movie ID of a movie using the Search Movies function (Option 1)")
        print("   - Example: Enter '155' to get specific movie details for 'The Dark Knight'")
        
        print("\n3. POPULAR MOVIES (Option 3):")
        print("   - Pretty simple. It just displays the most popular movies based from the TMDb Popular Movies List")
        print("   - No input from the user is required within this option")
        
        print("\n4. UPCOMING RELEASES (Option 4):")
        print("   - Pretty simple too. It shows 10 movies that are coming soon to theaters worldwide")
        print("   - No input from the user is required within this option")

        print("\n5. SEARCH BY GENRE (Option 5):")
        print("   - Basically a search filter. Enter a genre ID from the listed options, and the program will return 20 movies that are within that genre")
        print("   - Don't worry, you won't have to spend time finding the genre IDs. They will be listed to you.")
        print("   - Example: Enter '28' for Action movies")
        
        print("\n6. RECOMMENDATIONS (Option 6):")
        print("   - Find movies that are similar in style and genre by entering a TMDb Movie ID")
        print("   - Example: Enter '680' (Pulp Fiction) to get Tarantino-style movie recommendations")
        
        print("\n7. VIEW HISTORY (Option 7):")
        print("   - Shows your past searches with timestamps. That's it. Nothing else needs to be said")
        print("   - Can be useful if you want to remember something that you searched up before, but have forgotten")
        
        print("\n8. THIS HELP GUIDE (Option 8)")
        
        print("\n9. EXIT THE PROGRAM (Option 9)")

        print("\n" + "="*50)
        print("FAQ:".center(50))
        print("="*50)

        print("\n 1. Why is it limited to only the top 20 search results for Option 1?")
        print("- This function works by searching up movies that CONTAIN your search query in their title.")
        print("- It doesn't just show the movies that have the exact same search query as their title")
        print("- So for example, if you search up 'J', there will probably be millions of search results since a lot of movies contain the letter J in their title")
        print("- So to fix this issue, the top-20-movies act as a limit to only show the most relevant movies. This process is calculated by the API, not the program.")
        print("- Pretty much the same can be said with any other option that features such limits.")

        print("\n 2. How long did you spend working on this program?")
        print("- A LOT OF TIME.")
        print("- Creating this has been a huge pain. Sometimes I stay up till late night searching through tons of webpages just to work on this project")
        print("- More options would've been implemented if I had more time, but due to time limitations I wasn't able to do so :sadface:")
        
        print("\n" + "="*50)
        print("TIPS:".center(50))
        print("="*50)

        print("\n- Genre and Movie IDs remain constant. Action will always be 28, and Pulp Fiction will always be 680.")
        print("- Your search history will contain ANY sort of query you've had while using the program, not just limited to movie searches.")
        print("- Press Enter after typing your choice (Pretty much everyone should know this, but I'm just saying it to ensure the program is HIGHLY USABLE AND ACCESSIBLE)")