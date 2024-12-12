import requests
from bs4 import BeautifulSoup
import pandas as pd
def collect_user_rates(user_login):
     page_num = 1
     data = []

user_login = '4463972'
url = f'https://www.kinopoisk.ru/user/{user_login}/votes/'
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, 'lxml')
entries = soup.find_all('div', class_='item')
print(len(entries))
data = []
for entry in entries:
    div_film_name = entry.find('div', class_='nameRus')
    film_name = div_film_name.find('a').text
    div_rating = entry.find('div', class_='rating')
    rating = div_rating.find('b').text

    # Добавляем новую пару ключ-значение
    my_rating_div = entry.find('div', class_="vote")
    if my_rating_div is not None:
        my_rating = my_rating_div.text
    else:
        # Элемент не найден
        my_rating = "Элемент не найден"

    data.append({
        'film_name': film_name,
        'rating': rating,
        'my_rating': my_rating,
    })

print(data[:5])
