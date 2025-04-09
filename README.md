# **TMDb Movie Database Explorer**
![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A warm welcome to the TMDb Movie Database Explorer! This is a top-tier command-line application that interacts with The Movie Database (TMDb) API to search, browse, and discover movies. With this application, you can discover ANY movie. You could find detailed information about a movie, find a new movie to watch at home, discover upcoming releases to your nearby cinema, or even find your new favorite movie of all time!

## **Features**
- Search movies by title
- View detailed movie information (ratings, cast, budget, etc.)
- Browse currently popular movies
- Discover upcoming releases
- Filter movies by genre
- Get recommendations based on movies you like
- View your search history
- A comprehensive help guide that teaches you how to use the program

## **How It Works**
The program uses TMDb's REST API to:
1. Fetch movie data in JSON format
2. Parse and display it in an organized table view
3. Maintain a local search history of your queries
4. Provide multiple ways to discover movies

All data is fetched in real-time from TMDb's servers.

However, TMDb APIs are subjected to rate limits, so be careful of that. But no worries, they are unlikely to occur unless if you are searching up LOTS of movies.

## **Requirements**
For this application, only the **requests** dependency is required, as it plays a huge role in sending HTTP requests to the TMDb API as well as fetching the data. Other than that, no other dependencies are required for usage!

## **Installation Procedure**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/LevinShao/tmdb-movie-database-explorer.git
   cd tmdb-movie-database-explorer
   ```
   OR:
   **Press this green button called Code in GitHub.**
   ![Image 1](images/Instructions%20for%20Installation/Instruction.png)
   **You should now see an option to download a ZIP folder of the repository. Click it and a ZIP folder should download.**

   ![Image 2](images/Instructions%20for%20Installation/Instruction2.png)
   
   **Then, extract the zip folder.**
   ![Image 3](images/Instructions%20for%20Installation/Instruction3.png)
   **Import and open the newly extracted folder into Visual Studio Code, and proceed to the next few steps!**
2. **Install dependencies from requirements.txt**
    ```
    pip install requests
    ```
    OR
    ```
    pip install -r requirements.txt
    ```
    **NOTE: MAKE SURE TO TAKE OUT REQUIREMENTS.TXT FROM ANY FOLDER IT IS IN, AS pip install -r requirements.txt WILL NOT WORK IF IT IS IN ANY FOLDER.**
3. **Run the program!**
    ```
    python main.py
    ```
## **Configuration**
The program comes pre-configured with a working API key. If you still want to use your own API key, follow these steps:

1. Get a free API key from [TMDb](https://developer.themoviedb.org/reference/intro/getting-started)
2. Replace the api_key value in main.py with your own API key:

```python
app = TMDbMovieProgram(api_key="YOUR_NEW_API_KEY")
```

## **Usage**
### **After launching the program:**
1. Select options from the menu (1-9)

2. Follow on-screen instructions

3. View formatted results

### **Example workflow:**
- Choose "1. Search Movies" and enter a title

- Note the ID of your desired movie

- Choose "2. Get Movie Details" and enter the ID

- Explore other options like genre filtering or recommendations
## **Thanks for Choosing the TMDb Movie Database Explorer**
Once again, thank you for using this application! This took a lot of time and effort to develop, I would appreciate if you enjoyed using it! 

Without further ado, **get started and have fun!**