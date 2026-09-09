import os
import logging
from PIL import Image
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters,
)

# تنظیمات اولیه لاگ‌ها
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# توکن از محیط Render خوانده می‌شود
TOKEN = os.getenv("TOKEN")

# آیدی عددی خودت را از @userinfobot بگیر و اینجا بگذار
ADMIN_ID = 5748185793

# آیدی کانال سیگنال
CHANNEL_ID = https://t.me/+SRXZPAIZm3g4YTRk

LOGO_PATH = "logo.png"

PHOTO, NAME, TF, ZONE, REWARD = range(5)

daily_signals = []
weekly_signals = []


def is_admin(update: Update) -> bool:
    """فقط ادمین اجازه استفاده دارد"""
    return update.effective_user.id == ADMIN_ID


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        await update.message.reply_text("❌ فقط ادمین اجازه استفاده دارد.")
        return ConversationHandler.END

    await update.message.reply_text("📸 تصویر چارت تریدینگ‌ویو را ارسال کن.")
    return PHOTO


async def get_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        return ConversationHandler.END

    photo = update.message.photo[-1]
    file = await photo.get_file()
    await file.download_to_drive("chart.jpg")

    context.user
