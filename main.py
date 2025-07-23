import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_TOKEN = '7928418839:AAGQu90YL7Sh1yp9q163YDOD8AUBPplnV9c'
TELEGRAM_CHAT_ID = '749827665'

@app.route('/', methods=['POST'])
def alert():
    data = request.get_json()
    
    message = f"""
🚨 تنبيه جديد من TradingView:
{data}
    """
    
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }

    r = requests.post(url, json=payload)
    return {'status': 'ok'}

@app.route('/', methods=['GET'])
def index():
    return 'TradingView Telegram Bot is running!'

if __name__ == '__main__':
    app.run()
