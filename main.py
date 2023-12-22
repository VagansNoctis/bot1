import subprocess

telegram_path = 'C:\TelegramDesktop\Telegram.exe'

flag = True

joke = '\nЗаходят как-то русский, хохол и чукча в бар... Заходят-заходят и СДЫХАЮТСДЫХАЮТСДЫХАЮТСДЫХАЮТСДЫХАЮТСДЫХАЮТ'

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
        subprocess.Popen(['open', 'C:\Users\Влудиус Блудиус\AppData\Local\Discord\Update.exe'])



