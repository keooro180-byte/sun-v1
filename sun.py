import telebot
from flask import Flask
from threading import Thread
import datetime
import time
import os

# --- إعدادات السيادة الأمنية ---
TOKEN = "7650805373:AAH79i5Ait7271uW1YIn_T0C2-v6pU_9T_Q"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# تسجيل وقت البدء لحساب مدة التشغيل (Uptime)
start_time = datetime.datetime.now()

# --- واجهة الويب لضمان الإدارة الدائمة (Koyeb Health Check) ---
@app.route('/')
def home():
    return f"Sun OS v17.1 is Online. System Uptime: {datetime.datetime.now() - start_time}"

def run_flask():
    # استخدام المنفذ 8080 الذي حددناه في إعدادات Koyeb
    app.run(host='0.0.0.0', port=8080)

# --- أوامر البوت الاحترافية لمشروع Sky Mobile ---

@bot.message_handler(commands=['start'])
def welcome(message):
    user_name = message.from_user.first_name
    msg = (
        f"👑 **أهلاً بك سيدي القائد {user_name}**\n\n"
        "تم تفعيل نظام **Sun OS v17.1** بنجاح على السيرفرات السحابية.\n"
        "هذا النظام يعمل الآن بإدارة مستقلة ودائمة 24/7.\n\n"
        "📌 **قائمة التحكم:**\n"
        "🔹 /status - فحص قوة السيرفر والوقت\n"
        "🔹 /about - رؤية مشروع Sky Mobile\n\n"
        "🚀 *المستقبل يبدأ من هنا.*"
    )
    bot.reply_to(message, msg, parse_mode="Markdown")

@bot.message_handler(commands=['status'])
def status(message):
    uptime = datetime.datetime.now() - start_time
    status_msg = (
        "📊 **تقرير الحالة السيادية:**\n"
        "━━━━━━━━━━━━━━━\n"
        "✅ **النظام:** Sun OS v17.1 (Active)\n"
        "🌍 **السيرفر:** Frankfurt Cloud Hub\n"
        "⏱ **مدة العمل:** " + str(uptime).split('.')[0] + "\n"
        "📡 **الاتصال:** مستقر ومحمي للأبد\n"
        "━━━━━━━━━━━━━━━"
    )
    bot.reply_to(message, status_msg, parse_mode="Markdown")

@bot.message_handler(commands=['about'])
def about(message):
    about_msg = (
        "🏗 **مشروع Sky Mobile**\n\n"
        "منصة إدارة مستقلة تهدف لفرض السيادة الرقمية وتوفير حلول برمجية متطورة.\n\n"
        "👤 **المطور الرئيسي:** عبد الله (CEO of Sun)\n"
        "📅 **التاريخ:** 8 يناير 2026"
    )
    bot.reply_to(message, about_msg, parse_mode="Markdown")

# --- بروتوكول التشغيل والتعافي الذاتي ---
def start_bot():
    while True:
        try:
            print("Sun OS is deploying globally...")
            bot.infinity_polling(timeout=10, long_polling_timeout=5)
        except Exception as e:
            print(f"Alert: {e}. Re-engaging in 5 seconds...")
            time.sleep(5)

if __name__ == "__main__":
    # تشغيل Flask لتجاوز فحص الصحة في Koyeb
    t = Thread(target=run_flask)
    t.daemon = True
    t.start()
    
    # إطلاق قلب النظام
    start_bot()

