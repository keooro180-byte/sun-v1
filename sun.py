import os, asyncio, json, threading, psutil, httpx, aiosqlite, sys
from flask import Flask, render_template_string, session, redirect, request
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8450727870:AAHT7kUZBJ2Mbt6VweXoutkNVFq2OJCFE8I"
OWNER_ID = 7344005519
PASSWORD = "ABDULLAH_2026"
API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

web_app = Flask(__name__)
web_app.secret_key = "SUN_KEY"

@web_app.route('/')
def index():
    return "<h1>Sun OS v17.0 Sovereign - LIVE</h1>"

async def sun_ai_logic(prompt):
    async with httpx.AsyncClient(timeout=120.0) as client:
        try:
            r = await client.post(API_URL, headers={"Authorization": f"Bearer {API_KEY}"}, 
                json={"model": "meta-llama/llama-3.1-405b", "messages": [{"role": "user", "content": prompt}]})
            return r.json()['choices'][0]['message']['content'].strip()
        except: return "⚠️ Error connecting to Sun Core."

async def msg_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == OWNER_ID:
        res = await sun_ai_logic(update.message.text)
        await update.message.reply_text(res)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    threading.Thread(target=lambda: web_app.run(host='0.0.0.0', port=port), daemon=True).start()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, msg_handler))
    app.run_polling()
