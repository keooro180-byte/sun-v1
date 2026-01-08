import telebot
from flask import Flask
from threading import Thread
import datetime
import time

# --- إعدادات السيادة المحدثة ---
TOKEN = "8450727870:AAHT7kUZBJ2Mbt6VweXoutkNVFq2OJCFE8I"
ADMIN_ID = 7344005519 # آيدي القائد عبد الله
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

start_time = datetime.datetime.now()

@app.route('/')
def home():
    return f"Sun OS v17.1 is LIVE. Status: Supreme Health."

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# --- أوامر القائد ---

@bot.message_handler(commands=['start'])
def welcome(message):
    if message.from_user.id == ADMIN_ID:
        msg = "👑 **أهلاً بك سيدي القائد عبد الله.**\nنظام Sun OS v17.1 تحت تصرفك الآن من ألمانيا."
    else:
        msg = "🚀 **مرحباً بك في بوت Sky Mobile.**\nالنظام يعمل الآن بكفاءة عالية."
    bot.reply_to(message, msg, parse_mode="Markdown")

@bot.message_handler(commands=['status'])
def status(message):
    uptime = datetime.datetime.now() - start_time
    status_msg = (
        "📊 **تقرير السيادة:**\n"
        f"✅ النظام: Active\n"
        f"⏱ مدة التشغيل: {str(uptime).split('.')[0]}\n"
        "🌍 الموقع: Frankfurt Hub"
    )
    bot.reply_to(message, status_msg, parse_mode="Markdown")

def start_bot():
    while True:
        try:
            bot.infinity_polling(timeout=20)
        except Exception:
            time.sleep(5)

if __name__ == "__main__":
    Thread(target=run_flask).start()
    start_bot()

