from telegram import Update
from telegram.ext import ContextTypes

from services.automation import process_message


async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if not update.message or not update.message.text:
        return

    response = process_message(update.message.text)

    if response:
        await update.message.reply_text(response)
    else:
        await update.message.reply_text(
            "🤖 I received your message.\n\n"
            "I'm still learning how to automate this."
        )