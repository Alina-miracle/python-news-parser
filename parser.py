import requests
from bs4 import BeautifulSoup
import csv

# URL для страницы с вопросами на StackOverflow
url = 'https://stackoverflow.com/questions'

# Отправляем запрос
response = requests.get(url)
response.raise_for_status()  # Если возникнет ошибка, будет выброшено исключение

# Парсим HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Находим все карточки с вопросами
question_cards = soup.find_all('div', class_='s-post-summary')

# Список для хранения данных
questions_data = []

# Извлекаем данные из каждой карточки
for card in question_cards:
    title = card.find('a', class_='s-link').text.strip() if card.find('a', class_='s-link') else 'Без названия'
    author = card.find('div', class_='s-user-card').text.strip() if card.find('div', class_='s-user-card') else 'Без автора'
    votes = card.find('span', class_='s-post-summary--stats-item-number').text.strip() if card.find('span', class_='s-post-summary--stats-item-number') else 'Без голосов'
    answers = card.find('div', class_='s-post-summary--stats-item').text.strip() if card.find('div', class_='s-post-summary--stats-item') else 'Без ответов'

    # Добавляем в список
    questions_data.append([title, author, votes, answers])

# Сохраняем данные в CSV
with open('stackoverflow_questions.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Author', 'Votes', 'Answers'])
    writer.writerows(questions_data)

print("Данные успешно сохранены в 'stackoverflow_questions.csv'")
