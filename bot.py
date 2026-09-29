from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN

from handlers.start import start
from handlers.commands import help_command, about_command
from handlers.messages import handle_message


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    if query.data == "automations":

        text = (
            "⚡ *Automations*\n\n"
            "Automation engine coming in V2."
        )

    elif query.data == "reminders":

        text = (
            "⏰ *Reminders*\n\n"
            "Smart reminders coming in V2."
        )

    elif query.data == "ai":

        text = (
            "🤖 *AI Assistant*\n\n"
            "AI agent features coming in V4."
        )

    elif query.data == "settings":

        text = (
            "⚙️ *Settings*\n\n"
            "Settings will be added soon."
        )

    else:

        text = "Unknown option."

    await query.edit_message_text(
        text=text,
        parse_mode="Markdown",
    )


async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE
):

    print(f"ERROR: {context.error}")


def main():

    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .build()
    )

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("help", help_command)
    )

    app.add_handler(
        CommandHandler("about", about_command)
    )

    app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message
        )
    )

    app.add_error_handler(error_handler)

    print("⚡ FolwvynnBot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()