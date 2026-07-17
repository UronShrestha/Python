"""
⭐ Mini Project 3 – Favorite Movies
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

for i in range(5):
    while True:
        movie = input(f"Enter movie {i+1} : ")
        if movie == '':
            print("Please Enter a Movie Name!")
            continue
        movies.append(movie)
        break

while True:
    print("\n=====MENU=====")
    print("1. Display all movies.")
    print("2. Add a movie.")
    print("3. Remove a movie.")
    print("4. Sort Movies")
    print("5. Exit")

    choice = input("\nChoose option between 1 to 5 : ")

    if choice == '1':
        if len(movies) == 0:
            print("NO MOVIES!")
        else:
            print("\nFavorite Movies:")
            index = 1
            for fav_movie in movies:
                print(f"Movie{index} : {fav_movie}")
                index += 1

    # Add a movie
    elif choice == "2":
        while True:
            movie = input("Add a movie : ").strip()
            if movie == "":
                print("Please Enter a Movie Name!")
                continue
            # else:

            movies.append(movie)
            print(f"Movie named {movie} added successfully!")

            print("\n-----New Movie List-----")
            index = 1
            for fav_movie in movies:
                print(f"Movie{index} : {fav_movie}")
                index += 1

            break

    

    #  Remove a movie
    elif choice == "3":
        while True:
            movie = input("Remove a movie : ").strip()
            if movie == "":
                print("Please Enter a Movie Name!")
                continue
            elif movie in movies:
                movies.remove(movie)
                print(f"\nMovie named {movie} removed successfully!")

                print("\n-----New Movie List-----")
                index = 1
                for fav_movie in movies:
                    print(f"Movie{index} : {fav_movie}")
                    index += 1
            else:
                print(f"{movie} does not exist in the list.")

            break
    
    # Sort Movies
    elif choice == "4":
        movies.sort()
        print("Movies Sorted Successfully!")
        print("\n=====Sorted=====")
        index = 1
        for fav_movie in movies:
            print(f"Movie{index} : {fav_movie}")
            index += 1

    # Exit Menu
    elif choice == "5":
        print("\nThank You!")

        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
