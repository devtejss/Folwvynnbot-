from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context:ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton("⚡ Automations", callback_data="automations"),
            InlineKeyboardButton("⏰ Reminders", callback_data="reminders"),
        ],
        [
            InlineKeyboardButton("🤖 AI", callback_data="ai"),
            InlineKeyboardButton("⚙️ Settings", callback_data="settings")
        ],
    ]

    markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "⚡ *Welcome to FolwvynnBot*\n\n"
        "Your Personal Telegram automation assistant.\n\n"
        "Choose an option:",
        reply_markup=markup,
        parse_mode="Markdown",
    )