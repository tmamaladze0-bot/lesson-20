import json

def save_json(path, data):
    with open(path, 'w' , encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

save_json("student.json", {
    "name": "ნინო",
    "scores": [90, 85],
    "pair": (1, 2)
})
def load_json(path, default=None):
    try:
        with open(path, 'r' , encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return default
    except json.decoder.JSONDecodeError:
        return default

loaded = load_json("student.json")
print(loaded)
print(type(loaded["pair"]))

print(load_json("missing.json", default={}))
print(load_json("broken.json", default="არასწორი ფაილი"))

import json
from dataclasses import dataclass, field, asdict


@dataclass
class Movie:
    title: str
    year: int = 2000
    rating: float = 0.0
    genres: list[str] = field(default_factory=list)

    def __post_init__(self):
        if self.rating < 0 or self.rating > 10:
            raise ValueError("რეიტინგი უნდა იყოს 0-დან 10-მდე")


def best_movies(movies, min_rating):
    selected = [
        movie for movie in movies
        if movie.rating >= min_rating
    ]
    return sorted(selected, key=lambda movie: movie.rating, reverse=True)


movie1 = Movie("მონანიება", 1984, 9.1, ["დრამა"])
movie2 = Movie("გზა", 2020, 7.5)
movie3 = Movie(
    "მოგზაურობა",
    rating=8.2,
    genres=["თავგადასავალი"]
)

movies = [movie1, movie2, movie3]

print(movie1)
print(movie1 == Movie("მონანიება", 1984, 9.1, ["დრამა"]))

movie2.genres.append("კომედია")
print(movie2.genres, movie3.genres)

for movie in best_movies(movies, 8):
    print(movie.title, movie.rating)

text = json.dumps(asdict(movie1), ensure_ascii=False)
print(text)

try:
    Movie("ცუდი", 2000, 11)
except ValueError as error:
    print("შეცდომა:", error)





