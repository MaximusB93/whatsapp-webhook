from flask import Flask, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    phone = data['contact']['phone']
    message = data['message']['body']
    timestamp = data['message']['timestamp']

    send_to_google_sheets(phone, message, timestamp)

    return 'OK', 200

def send_to_google_sheets(phone, message, timestamp):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open('WhatsApp Messages').sheet1
    sheet.append_row([phone, message, timestamp])

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
