import requests

url = 'https://www.imdb.com/india/top-rated-malayalam-movies'
source = requests.get(url).text

from bs4 import BeautifulSoup

soup = BeautifulSoup(source, 'lxml')

import csv

csv_file = open('movie_info.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Movie Name', 'Year of Release', 'Rating'])

all_movies = soup.find('tbody', class_="lister-list")
for movie in all_movies.find_all('tr'):
    movie_title = movie.find('td', class_='titleColumn').a.text
    movie_year = movie.find('td', class_='titleColumn').span.text.lstrip("(").rstrip(")")
    movie_rating = float(movie.find('td', class_='ratingColumn imdbRating').text.strip("\n"))
    csv_writer.writerow([movie_title, movie_year, movie_rating])

