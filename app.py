from flask import Flask, request
import requests
from datetime import datetime

app = Flask(__name__)

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzTguj7UsMoXgNLfmWp18x4sP7Pl7rxiM_T399hlo-iIWExThVSGzQeHOn3MG1iwxKdig/exec"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Полученные данные:", data)

    messages = data.get('messages', [])
    if not messages:
        print("Нет сообщений в данных!")
        return 'No messages', 400

    message_data = messages[0]

    # Корректные ключи именно из ваших данных
    phone = message_data.get('from') or message_data.get('chatId') or message_data.get('author') or 'unknown'
    message = message_data.get('body') or message_data.get('caption') or 'пустое сообщение'

    # Обработка поля времени
    timestamp_unix = message_data.get('time')
    if timestamp_unix:
        timestamp = datetime.fromtimestamp(timestamp_unix).strftime('%Y-%m-%d %H:%M:%S')
    else:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Если номер телефона содержит '@', удалим
    phone = phone.split('@')[0] if '@' in phone else phone

    params = {
        'phone': phone,
        'message': message,
        'timestamp': timestamp
    }

    print("Отправляемые параметры в Google Sheets:", params)

    requests.get(GOOGLE_SCRIPT_URL, params=params)

    return 'OK', 200

if __name__ == '__main__':
    app.run('0.0.0.0', port=10000)
