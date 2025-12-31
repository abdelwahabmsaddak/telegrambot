import os
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler
)

# logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# token from environment
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("❌ TELEGRAM_BOT_TOKEN not found in environment variables")

# commands
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 SmartBot يعمل بنجاح!\n\n"
        "• تحليل السوق\n"
        "• إشارات ذكية\n"
        "• تداول آلي (قريبًا)\n"
        "• تجربة مجانية 15 يوم"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("اكتب /start للبدء")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
