#Парсер оценок фильмов с КиноПоиска

## Постановка задачи

Данный проект предназначен для парсинга оценок фильмов пользователя с платформы КиноПоиск. Скрипт извлекает информацию о названиях фильмов и дате релиза, их оценках, а также личных оценках пользователя и сохраняет эти данные в формате Excel. 

### Функционал:
- Извлечение названий фильмов с их датой релиза.
- Получение общего рейтинга фильмов.
- Получение индивидуальной оценки каждого фильма.
- Сохранение собранных данных в файл `user_ratings.xlsx`.

## Инструкция по сборке и запуску

### Системные требования
- Python 3.x
- Установленные библиотеки:
  - requests
  - beautifulsoup4
  - pandas
  - lxml (необходимо для парсинга HTML)


Перед запуском проекта убедитесь, что у вас установлен Python. Для установки необходимых библиотек выполните следующую команду:


pip install requests beautifulsoup4 pandas lxml




Запуск скрипта
1.Клонируйте репозиторий или скопируйте код в файл: Создайте файл с именем kinopoisk_parser.py и вставьте туда следующий код:


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

2.Сохраните файл и закройте текстовый редактор.

3.Запустите скрипт: Откройте терминал, перейдите к директории, где находится файл, и выполните команду:
python kinopoisk_parser.py

4.Проверьте результаты: После успешного выполнения скрипта будет создан файл user_ratings.xlsx в текущей директории. Откройте его, чтобы просмотреть собранные данные.

Примечание
Измените переменную user_login в коде на нужное имя пользователя КиноПоиска, чтобы получить его оценки.


### Как использовать:
1. Скопируйте данный текст в текстовый документ и сохраните его в файле `README.md` в корневом каталоге вашего проекта.
2. Вам просто нужно будет изменить или дополнить текст согласно изменениям, если они будут в вашем коде.
