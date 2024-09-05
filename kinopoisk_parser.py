import requests
from bs4 import BeautifulSoup
import pandas as pd

user_login = '171729474'  # Укажите логин пользователя
url = f'https://www.kinopoisk.ru/user/{user_login}/votes/'

html_content = requests.get(url).text
soup = BeautifulSoup(html_content, 'lxml')

entries = soup.find_all('div', class_='item')
print(len(entries))

data = []
for entry in entries:
    # Получаем название фильма
    div_film_name = entry.find('div', class_='nameRus')
    film_name = div_film_name.find('a').text.strip()

    # Получаем оценку фильма
    div_rating = entry.find('div', class_='rating')
    rating = div_rating.find('b').text.strip()

    # Получаем свою оценку
    my_rating_div = entry.find('div', class_="vote")
    my_rating = my_rating_div.text.strip() if my_rating_div else "Элемент не найден"

    data.append({
        'Название фильма': film_name,
        'Рейтинг': rating,
        'Мой рейтинг': my_rating,
    })

# Создаем DataFrame из списка данных
df = pd.DataFrame(data)

# Сохраняем в Excel файл
df.to_excel('user_ratings.xlsx', index=False)

print(df.head())
