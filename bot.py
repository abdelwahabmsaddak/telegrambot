import os
from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# تخزين مؤقت (لاحقًا DB)
users = {}

def is_trial_active(user_id):
    user = users.get(user_id)
    if not user:
        return False
    return datetime.utcnow() < user["trial_end"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in users:
        users[user_id] = {
            "start_date": datetime.utcnow(),
            "trial_end": datetime.utcnow() + timedelta(days=15)
        }

    trial_end = users[user_id]["trial_end"].strftime("%Y-%m-%d")

    await update.message.reply_text(
        f"""🤖 مرحبًا بك في SmartBot AI

🧠 تحليل ذكي للأسواق
🐋 تتبع الحيتان
📊 قرارات مدعومة بالذكاء الاصطناعي

🎁 تجربتك المجانية تنتهي في:
📅 {trial_end}

الأوامر:
/analyze BTC
/whales ETH
/help
"""
    )

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if not is_trial_active(user_id):
        await update.message.reply_text(
            "⛔ انتهت التجربة المجانية.\nاشترك لمتابعة التحليل 💳"
        )
        return

    if not context.args:
        await update.message.reply_text("استعمل: /analyze BTC")
        return

    symbol = context.args[0].upper()

    # تحليل مبدئي (AI لاحقًا)
    analysis = f"""
📊 تحليل {symbol}

الاتجاه: صاعد ⚡
الدعم: قوي
المقاومة: قريبة

🧠 AI Insight:
السوق يظهر زخم إيجابي، لكن يُنصح بالحذر عند المقاومة.

⚠️ ليس نصيحة استثمارية
"""

    await update.message.reply_text(analysis)

async def whales(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if not is_trial_active(user_id):
        await update.message.reply_text("⛔ انتهت التجربة المجانية.")
        return

    if not context.args:
        await update.message.reply_text("استعمل: /whales BTC")
        return

    symbol = context.args[0].upper()

    await update.message.reply_text(
        f"""🐋 Whale Watch — {symbol}

تحركات كبيرة تم رصدها
- تحويلات إلى البورصات
- احتمالية تقلب عالي

🧠 AI Context:
الحيتان تتحضر لحركة سعرية
"""
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """/start — بدء البوت
/analyze BTC — تحليل ذكي
/whales BTC — تتبع الحيتان
"""
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("analyze", analyze))
    app.add_handler(CommandHandler("whales", whales))
    app.add_handler(CommandHandler("help", help_command))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
