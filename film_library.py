import json

MOVIES_FILE = "./movies.json"


def load_movies():
    try:
        with open(MOVIES_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл не найден")
        return []


def save_movies(movies):
    with open(MOVIES_FILE, 'w') as file:
        json.dump(movies, file, indent=4)


def add_movie(movies, name):
    for movie in movies:
        if movie['name'] == name:
            print("Фильм уже существует.")
            return
    movies.append({"name": name, "ratings": {}})
    print("Фильм успешно добавлен.")


def delete_movie(movies, name):
    for movie in movies:
        if movie['name'] == name:
            movies.remove(movie)
            print("Фильм успешно удален.")
            return
    print("Фильм не найден.")


def list_movies(movies):
    sorted_movies = sorted(movies, key=lambda x: x['name'])
    print("-" * 40)
    print(f"{'Name':20}   |  {'Average Rating':12}")
    print("-" * 40)
    for movie in sorted_movies:
        ratings = movie['ratings']
        average_rating = sum(ratings.values()) / len(ratings) if ratings else "не оценивался"
        print(f"{movie['name']:20} |   {average_rating:<12}")
    print("-" * 40)


def rate_movie(movies, name, user, rating):
    for movie in movies:
        if name.lower() in movie['name'].lower():
            if rating == 0:
                if user in movie['ratings']:
                    del movie['ratings'][user]
                    print("Рейтинг успешно удален.")
                else:
                    print("Пользователь не оценил этот фильм")
                return
            try:
                rating = float(rating)
                if 0 <= rating <= 10:
                    movie['ratings'][user] = rating
                    print("Рейтинг успешно добавлен")
                else:
                    print("Оценка должна быть от 0 до 10.")
            except ValueError:
                print("Пожалуйста, введите число для оценки фильма.")
            return
    print("Фильм не найден")


def find_movie(movies, name):
    for movie in movies:
        if name.lower() in movie['name'].lower():
            print("-" * 32)
            print(f"Movie: {movie['name']}")
            if movie['ratings']:
                print("-" * 32)
                print(f"{'User':10} | {'Rating':10}")
                print("-" * 32)
                for user, rating in movie['ratings'].items():
                    print(f"{user:10} | {rating:<10}")
                print("-" * 32)
                average_rating = sum(movie['ratings'].values()) / len(movie['ratings'])
                print(f"Average Rating: {average_rating:.2f}")
            else:
                print("Фильм не оценивался")
            return
    print("Фильм не найден.")


def display_movies():
    movies = load_movies()
    while True:
        print("""
Menu:
1. List - Show movies
2. Find - Find a movie
3. Add - Add a movie
4. Delete - Delete a movie
5. Rate - Rate a movie
6. Exit 
        """)
        choice = input("Введите команду для дальнейших действий: ").lower()
        if choice == 'list':
            list_movies(movies)
        elif choice == 'find':
            movie_name = input("Введите название фильма, чтобы найти: ")
            find_movie(movies, movie_name)
        elif choice == 'add':
            movie_name = input("Введите название фильма, чтобы добавить: ").capitalize()
            add_movie(movies, movie_name)
        elif choice == 'delete':
            movie_name = input("Введите название фильма, что бы которую хотите удалить: ")
            delete_movie(movies, movie_name)
        elif choice == 'rate':
            movie_name = input("Введите название фильма, чтобы оценить: ").capitalize()
            user = input("Введите ваше имя: ").capitalize()
            rating = input("Введите оценку для фильма (0, чтобы удалить): ")
            rate_movie(movies, movie_name, user, rating)
        elif choice == 'exit':
            save_movies(movies)
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз..")


if __name__ == '__main__':
    display_movies()
