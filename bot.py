import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

from ai_engine import ai_analyze
from trading import trade_signal

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN مش موجود")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 بوت تداول ذكي جاهز\n"
        "اكتب:\n"
        "/ai BTC\n"
        "/trade BTC"
    )

async def ai_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("استعمل: /ai BTC")
        return
    asset = context.args[0]
    reply = ai_analyze(f"حلل {asset} كأصل مالي")
    await update.message.reply_text(reply)

async def trade_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("استعمل: /trade BTC")
        return
    asset = context.args[0]
    await update.message.reply_text(trade_signal(asset))

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ai", ai_cmd))
    app.add_handler(CommandHandler("trade", trade_cmd))

    print("✅ BOT STARTED")
    app.run_polling()

if __name__ == "__main__":
    main()
