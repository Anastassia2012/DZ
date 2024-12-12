# Парсер оценок пользователя на Кинопоиске

## Постановка задачи

Этот скрипт предназначен для сбора данных о пользовательских оценках фильмов на сайте Кинопоиск. Вы можете получить информацию о названии фильма, рейтинге на сайте и вашей личной оценке.

## Инструкция по сборке и запуску

1. **Установите зависимости**: Для работы этого парсера необходимы библиотеки `requests`, `BeautifulSoup4` и `pandas`. Установите их с помощью pip:
   
   
pip install requests beautifulsoup4 lxml pandas
   

2. **Запуск скрипта**: Откройте командную строку или терминал и запустите скрипт следующей командой:

   
   python kino.py
   
### Пример результатов работы парсера

После выполнения данного  скрипта, вывод на экран может выглядеть следующим образом:

[
    {'film_name': 'Титаник', 'rating': '8.5', 'my_rating': '9'},
    {'film_name': 'Интерстеллар', 'rating': '8.7', 'my_rating': '10'},
    {'film_name': 'Начало', 'rating': '8.8', 'my_rating': '9'},
    {'film_name': 'Матрица', 'rating': '8.7', 'my_rating': '10'},
    {'film_name': 'Парк Юрского периода', 'rating': '8.1', 'my_rating': '8'}
]
