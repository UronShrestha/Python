"""
⭐ Mini Project 3 : Favorite Movies
Store 5 movie names.
Then let the user:
    Display all movies.
    Add a movie.
    Remove a movie.
    Sort the list.
    Exit.

Use a while loop and if statements to create a simple menu.
"""

movies = []

# Store 5 movie names.
for i in range(5):
    while True:
        movie = input(f"Enter name of movie{i+1} : ")
        if movie == '':
            print("Please Enter Movie Name!")
            continue

        movies.append(movie)
        break

#  while loop and if statements to create a simple menu.
while True:
    print("\n=====MENU=====")
    print("1. Display all movies")
    print("2. Add a movie")
    print("3. Remove a movie")
    print("4. Sort the list")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5) : ")

# Display all movies
    if choice == "1":
        if movies == 0:
            print("NO MOVIES!")
        else:
            print("\nFavorite movies : ")
            for index, movie in enumerate(movies, start=1):
                print(f"Movie{index}. {movie}")

# Add a movie
    elif choice == "2":
        while True:
            movie = input("Enter a new movie name : ")
            if movie == "":
                print("Name not entered!")
                continue
            else:
                print(f"New movie '{movie}' added successfully! ")
                movies.append(movie)
                
                print("\n=====new movie list=====")
                for index, movie in enumerate(movies, start=1):
                    print(f"Movie{index}. {movie}")
            break

# Remove a movie
    elif choice == "3":
        while True:
            movie = input("Enter movie name to remove : ")
            if movie == "":
                    print("Name not entered!")
                    continue
            elif movie in movies:
                movies.remove(movie)
                print(f"{movie} removed successfully!")

                print("\n=====new movie list=====")
                for index, movie in enumerate(movies, start=1):
                    print(f"Movie{index}. {movie}")
                break
            else:
                print(f"{movie} does not exit in the list")
            
    # Sort the list.
    elif choice == "4":
        movies.sort()
        print("Movies have been sorted alphabetically!")
        print("\n=====sorted movie list=====")
        for index, movie in enumerate(movies, start=1):
            print(f"Movie{index} : {movie}")

    elif choice == "5":
        print("THANK YOU!")

        break
    else:
        print("Invalid choice. Choose betwwen 1 to 5 only!")






