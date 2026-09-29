from telegram import Update 
from telegram.ext import ContextTypes

async def help_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
   await update.message.reply_text(
        "⚡ *FolwvynnBot Commands*\n\n"
        "/start - Open the main menu\n"
        "/help - Show this help\n"
        "/about - About FolwvynnBot",
        parse_mode="Markdown"
   )

async def about_command(update:Update, contextg:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚡ *FolwvynnBot*\n\n"
        "A Telegram automation project built with Python.\n\n"
        "More Powerful automation featuers are coming in future versions.",
        parse_mode="Markdown",
    )