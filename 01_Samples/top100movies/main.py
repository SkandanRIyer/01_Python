from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")
titles = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in titles]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")