SIMPLIFIED_GENRES = {
    "Hip Hop": [
        "Conscious Hip Hop",
        "West Coast Hip Hop",
        "East Coast Hip Hop",
        "Political Hip Hop",
        "Gangsta Rap",
        "Abstract Hip Hop",
    ],
    "Heavy Metal": ["NWOBHM"],
}


def simplify_genres(genres: str):
    genre_list = genres.split(",")
    for genre in genre_list:
        genre = genre.strip()

        for genre_tag, unnecessary_genre_list in SIMPLIFIED_GENRES.items():
            for unnecessary_genre in unnecessary_genre_list:
                if genre == unnecessary_genre:
                    genres = genres.replace(unnecessary_genre, genre_tag)

    return genres


if __name__ == "__main__":
    simplify_genres("French House, Alternative Rock, Conscious Hip Hop")
