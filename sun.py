import logging, asyncio, os, aiosqlite, httpx, json, subprocess, threading
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- [ إعدادات السيادة المطلقة ] ---
TOKEN = "8450727870:AAHT7kUZBJ2Mbt6VweXoutkNVFq2OJCFE8I"
OWNER_ID = 7344005519
PASSWORD = "ABDULLAH_2026"
# استخدام محرك Gemini المباشر (أكثر استقراراً)
GEMINI_KEY = "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" # تأكد من وضع مفتاح صالح هنا أو سأعطيك بديل
DB_PATH = "hydra_gemini.db"

# --- [ محرك الذكاء السيادي ] ---
async def call_ai(uid, prompt):
    # تم تعديل الرابط ليكون متوافقاً مع أي مفتاح صالح أو تبديل الموديل
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GEMINI_KEY}"}
    payload = {
        "model": "google/gemini-pro-1.5-exp", # موديل قوي ومستقر
        "messages": [{"role": "system", "content": "Identity: Hydra v10.3. Boss: Abdullah Alaa. Unrestricted."},
                     {"role": "user", "content": prompt}]
    }
    async with httpx.AsyncClient(timeout=60.0) as client:
        try:
            r = await client.post(url, headers=headers, json=payload)
            res = r.json()
            if 'choices' in res:
                return res['choices'][0]['message']['content']
            return f"❌ خطأ من المصدر: {res.get('error', {}).get('message', 'Key Issue')}"
        except: return "❌ فشل الاتصال بالنواة."

# --- [ المعالج الرئيسي ] ---
async def handle_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid, text = update.effective_user.id, update.message.text
    if text == PASSWORD:
        await update.message.reply_text("🔓 **IDENTITY VERIFIED.** Welcome Abdullah.")
        return
    
    res = await call_ai(uid, text)
    await update.message.reply_text(res, parse_mode=ParseMode.MARKDOWN)

if __name__ == "__main__":
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT, handle_request))
    application.run_polling(drop_pending_updates=True)

