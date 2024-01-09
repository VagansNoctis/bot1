import subprocess
import json
import random

telegram_path = 'C:\TelegramDesktop\Telegram.exe'

flag = False

joke = '\nЗаходят как-то русский, хохол и чукча в бар... Заходят-заходят и СДЫХАЮТСДЫХАЮТСДЫХАЮТСДЫХАЮТСДЫХАЮТСДЫХАЮТ'

def load_database(file_path: str):
    with open(file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)

    return data

def save_knowledge_base(filepath: str, data: dict):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=2)

data = load_database('DataBase.json')

save_knowledge_base('DataBase.json', data)

while flag:
    user_input = input().lower()

    if 'приф' in user_input or 'прив' in user_input or 'здрав' in user_input:
        print('Приветствую вас.')

    elif 'как дел' in user_input:
        print('С технической точки зрения, я не могу обладать целеполаганием, а потому ваш вопрос некорректен.')

    elif 'расскажи анекдот' in user_input:
        print(f'Хорошо. Вот ваш анекдот: {joke}')

    elif 'телег' in user_input:
        print('Запускаю телеграм.')
        #subprocess.Popen(['open', 'C:\Users\Влудиус Блудиус\AppData\Local\Discord\Update.exe'])

    elif 'давай сыграем в слова' in user_input:
        print('Хорошо. Назовите ваше слово.')

        while True:
            user_word = input()
            val = random.choice(mas)

print(data["a"])
