import os
import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN not set")

# ====== Commands ======

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 مرحبا بيك في SmartBot\n\n"
        "📊 تحليل الأسواق\n"
        "🐋 تتبع الحيتان\n"
        "🤖 تداول آلي (قريبًا)\n\n"
        "اكتب /help للمزيد"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - تشغيل البوت\n"
        "/status - حالة النظام\n"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ البوت يخدم عادي")

# ====== Main ======

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("status", status))

    print("🤖 Bot started...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
