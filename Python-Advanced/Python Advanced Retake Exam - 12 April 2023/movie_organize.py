def movie_organizer(*args):
    movies_info = {}

    for name, genre in args:
        if genre not in movies_info:
            movies_info[genre] = []

        movies_info[genre].append(name)

    sorted_movies_info = sorted(movies_info.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ""

    for item, value in sorted_movies_info:
        result += f"{item} - {len(value)}\n"

        for i in sorted(value):
            result += f"* {i}\n"

    return result
