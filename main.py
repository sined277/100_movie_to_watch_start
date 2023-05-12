# Importing the necessary libraries
from bs4 import BeautifulSoup
import requests

# Defining the URL of the webpage to be scraped
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Sending a GET request to the webpage and getting the HTML content
response = requests.get(URL)
website_html = response.text

# Creating a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(website_html, 'html.parser')

# Finding all the movie titles on the webpage
all_movies = soup.find_all(name='h3', class_='title')

# Extracting the text from the movie title tags and storing them in a list
all_names_movie = [movie.getText() for movie in all_movies]

# Reversing the order of the list of movie titles
all_names_movie_reverse = all_names_movie[::-1]

# Writing the list of movie titles to a text file
with open('movies.txt', 'w', encoding='utf-8') as data_file:
    for movie in all_names_movie_reverse:
        data_file.write(f"{movie}\n")
