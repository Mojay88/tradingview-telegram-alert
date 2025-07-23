from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/", methods=["POST"])
def tradingview_alert():
    data = request.json
    message = data.get("message", "🚨 تنبيه جديد من TradingView")
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)
    return "OK"

@app.route("/", methods=["GET"])
def home():
    return "🚀 TradingView Webhook Bot is Running!"
