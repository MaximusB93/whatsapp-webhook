from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Полученные данные:", data)
    return 'OK', 200

if __name__ == '__main__':
    app.run('0.0.0.0', port=10000)
