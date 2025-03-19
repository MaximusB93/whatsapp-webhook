from flask import Flask, request
import requests
from datetime import datetime

app = Flask(__name__)

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzTguj7UsMoXgNLfmWp18x4sP7Pl7rxiM_T399hlo-iIWExThVSGzQeHOn3MG1iwxKdig/exec"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    phone = data.get('chatId', 'unknown').split('@')[0]
    message = data.get('body', '')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    params = {
        'phone': phone,
        'message': message,
        'timestamp': timestamp
    }

    # Отправляем данные в Google Sheets
    requests.get(GOOGLE_SCRIPT_URL, params=params)

    return 'OK', 200

if __name__ == '__main__':
    app.run('0.0.0.0', port=10000)
