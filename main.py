import time # just purely for aesthetics, nothing else
# also, time (as well as datetime) are both part of the Python Standard Library and are installed by default.
# they are included and pre-installed with Python by default, meaning that you won't have to install them at all
# therefore they will not be included in the requirements.txt file since it should only contain third-party packages
from methods import TMDbMovieProgram # Import the program from methods.py (integration)

def main():
    """The main user interface for the program"""
    app = TMDbMovieProgram(api_key="2b556e2cf294ec2f4a6b5fa4770f3732") # API key
    # ^^^ Change this if you want to use your own API key
    
    # introduction
    print("\nWelcome to the TMDb Movie Database Explorer!")
    print("This is a movie database application powered by the TMDb API")
    print("\nIt is heavily recommended for you to use the help guide first, since some parts could be confusing on its own")
    print("Access the help guide by entering '8' below")
    time.sleep(2)
    
    # option selections
    while True:
        print("\nOptions:")
        print("1. Search Movies")
        print("2. Get Movie Details")
        print("3. View Current Most Popular Movies")
        print("4. View Upcoming Releases")
        print("5. Search by Genre")
        print("6. Get Recommendations")
        print("7. View Search History")
        print("8. Help")
        print("9. Exit")

        choice = input("\nEnter your choice: ").strip() # .strip will remove any leading and trailing whitespaces
        
        if choice == "1":
            app.search_movies()
        elif choice == "2":
            app.get_movie_details()
        elif choice == "3":
            app.get_popular_movies()
        elif choice == "4":
            app.get_upcoming_movies()
        elif choice == "5":
            app.search_by_genre()
        elif choice == "6":
            app.get_recommendations()
        elif choice == "7":
            app.view_search_history()
        elif choice == "8":
            app.help_guide()
        elif choice == "9":
            print("Thanks for using this program!")
            print("Goodbye and see you next time!")
            break
        else:
            print("Invalid choice! Please enter a valid number between 1-9")

if __name__ == "__main__":
    main()