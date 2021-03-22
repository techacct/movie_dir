MENU_PROPMT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by titl, or 'q' to quit: "
movies = []


def add_movies():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter thr movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def show_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Relase year: {movie['year']}")


def find_movie():
    search_title = input("Enter movie title you're looking for: ")

    for movie in movies:
        if movie['title'] == search_title:
            print_movie(movie)

user_options = {
    "a": add_movies,
    "l": show_movies,
    "f": find_movie
}

def menu():
    selection = input(MENU_PROPMT)
    while selection != 'q':
        if selection in user_options:
            selection_funtion = user_options[selection]
            selection_funtion()
        else:
            print('Unknown command. Please try again.')
        
        selection = input(MENU_PROPMT)

menu()