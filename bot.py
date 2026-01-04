import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from ai_engine import analyze

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN غير موجود")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 SmartBot AI\n"
        "استعمل: /analysis BTC أو /analysis GOLD"
    )

async def analysis_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("اكتب الأصل: /analysis BTC")
        return
    asset = " ".join(context.args)
    await update.message.reply_text("⏳ جارِ التحليل...")
    result = analyze(asset)
    await update.message.reply_text(result)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("analysis", analysis_cmd))
    app.run_polling()

if __name__ == "__main__":
    main()
