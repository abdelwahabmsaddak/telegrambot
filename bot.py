import os
import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# ====== أوامر ======

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 أهلاً بك في SmartBot\n"
        "📊 تحليل – 🐋 حيتان – 🤖 ذكاء اصطناعي\n\n"
        "اكتب /help للمساعدة"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - تشغيل البوت\n"
        "/analysis - تحليل ذكي\n"
        "/whales - تتبع الحيتان\n"
    )

async def analysis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 تحليل ذكي (نسخة أولية)\n"
        "سيتم ربط الذكاء الاصطناعي قريباً"
    )

async def whales(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐋 تتبع الحيتان (قيد التطوير)"
    )

# ====== رسائل عادية ======
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💡 تم استلام رسالتك\n"
        "الذكاء الاصطناعي سيُفعل لاحقاً"
    )

# ====== تشغيل البوت ======
async def main():
    if not TOKEN:
        raise RuntimeError("❌ TELEGRAM_BOT_TOKEN غير موجود")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("analysis", analysis))
    app.add_handler(CommandHandler("whales", whales))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("🤖 SmartBot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
