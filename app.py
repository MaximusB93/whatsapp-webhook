from flask import Flask, request
import requests

app = Flask(__name__)

# Замените на URL вашего Google Apps Script
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzTguj7UsMoXgNLfmWp18x4sP7Pl7rxiM_T399hlo-iIWExThVSGzQeHOn3MG1iwxKdig/exec"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    phone = data['contact']['phone']
    message = data['message']['body']

    params = {
        'phone': phone,
        'message': message
    }

    # Отправляем данные в Google Таблицы
    requests.get(GOOGLE_SCRIPT_URL, params=params)

    return 'OK', 200

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
