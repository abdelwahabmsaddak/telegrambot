import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from ai_engine import ai_analysis

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("smartbot")

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

if not BOT_TOKEN:
    raise RuntimeError("Missing TELEGRAM_BOT_TOKEN")
if not OPENAI_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "🤖 SmartBot AI جاهز ✅\n\n"
        "الأوامر:\n"
        "• /analysis BTC\n"
        "• /analysis GOLD\n"
        "• /analysis AAPL\n"
        "• /whales BTC (نسخة أولية)\n"
        "• /signal BTC (إشارة تعليمية)\n\n"
        "⚠️ هذا محتوى تعليمي وليس نصيحة مالية."
    )
    await update.message.reply_text(msg)

async def analysis_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("اكتب الأصل: /analysis BTC أو /analysis GOLD أو /analysis TSLA")
        return
    asset = " ".join(context.args)
    await update.message.reply_text("⏳ جارِ التحليل الاحترافي...")
    try:
        text = ai_analysis(f"حلل الأصل التالي: {asset}. أعطني تحليل احترافي حسب القالب.")
        await update.message.reply_text(text)
    except Exception as e:
        logger.exception("AI error")
        await update.message.reply_text(f"❌ صار خطأ في التحليل: {e}")

async def whales_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # نسخة أولية: AI يشرح كيف تراقب الحيتان وما هي المؤشرات
    if not context.args:
        await update.message.reply_text("اكتب الأصل: /whales BTC")
        return
    asset = " ".join(context.args)
    await update.message.reply_text("🐋 جارِ إعداد ملخص الحيتان (نسخة أولية)...")
    try:
        text = ai_analysis(
            f"اعطني تقرير تتبع حيتان للأصل {asset}: "
            "اشرح أهم المؤشرات: التدفقات للبورصات، المحافظ الكبيرة، الحركات غير العادية، "
            "وماذا يعني ذلك (تعليمي)."
        )
        await update.message.reply_text(text)
    except Exception as e:
        await update.message.reply_text(f"❌ خطأ: {e}")

async def signal_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # إشارات تعليمية فقط (مهم)
    if not context.args:
        await update.message.reply_text("اكتب الأصل: /signal BTC")
        return
    asset = " ".join(context.args)
    await update.message.reply_text("📌 جارِ توليد إشارة (تعليمية)...")
    try:
        text = ai_analysis(
            f"اعطني إشارة تداول تعليمية للأصل {asset} "
            "بصيغة: الاتجاه، الدخول، وقف الخسارة، أهداف 1/2/3، سبب الإشارة، درجة الثقة."
        )
        await update.message.reply_text(text + "\n\n⚠️ للتعليم فقط.")
    except Exception as e:
        await update.message.reply_text(f"❌ خطأ: {e}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("analysis", analysis_cmd))
    app.add_handler(CommandHandler("whales", whales_cmd))
    app.add_handler(CommandHandler("signal", signal_cmd))

    logger.info("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
