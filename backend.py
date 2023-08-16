import requests


def get_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/images?include_image_language=en%2Cnull&language=en"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9"
                         ".eyJhdWQiOiIzMzcyYWRmNWFkNGY3MTg1ODY5OWI4OTBhNzk3MTE0NSIsInN1YiI6IjY0ZDc5MTRhZjE0ZGFkMDExZGZkMzVkMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.NIQ39ZkXrfDCbpFtQ27AmFnItBdn_Hp_nKCJrGVvu6E"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    filtered_data = data["posters"]
    return "https://image.tmdb.org/t/p/w500" + filtered_data[0].get("file_path")


if __name__ == "__main__":
    print(get_poster(206647))
