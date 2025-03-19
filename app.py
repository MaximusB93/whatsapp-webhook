from flask import Flask, request
import requests
from datetime import datetime

app = Flask(__name__)

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzTguj7UsMoXgNLfmWp18x4sP7Pl7rxiM_T399hlo-iIWExThVSGzQeHOn3MG1iwxKdig/exec"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    phone = data.get('author') or data.get('chatId') or 'unknown'
    phone = phone.split('@')[0] if '@' in phone else phone
    message = data.get('body') or 'пустое сообщение'
    timestamp = datetime.fromtimestamp(data.get('time', datetime.now().timestamp())).strftime('%Y-%m-%d %H:%M:%S')

    params = {
        'phone': phone,
        'message': message,
        'timestamp': timestamp
    }

    requests.get(GOOGLE_SCRIPT_URL, params=params)

    return 'OK', 200

if __name__ == '__main__':
    app.run('0.0.0.0', port=10000)
