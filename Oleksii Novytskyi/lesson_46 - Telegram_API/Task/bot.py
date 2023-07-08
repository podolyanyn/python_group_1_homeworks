import logging
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram import Update, Bot
from telegram.ext import filters, MessageHandler, CallbackContext, Updater
from telegram.ext import InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import os
import django
import sys
from telegram.ext import Updater, MessageHandler
from telegram.ext.filters import MessageFilter
import telegram

# Отримати шлях до директорії "notes"
notes_dir = os.path.dirname(os.path.abspath(__file__))

# Додати директорію "notes" до шляху пошуку модулів
sys.path.append(notes_dir)


# Встановити значення змінної оточення DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notes_app.settings")
django.setup()


from notes.models import Notes


# bot = telegram.Bot("6036572513:AAGvMHuJKqrC45QvIAEFStGPZozBJiHqmn0")
# async def main():

#     async with bot:
#         # print(await bot.get_me())
#         print((await bot.get_updates())[0])
#         await bot.send_message(text='Hi John!', chat_id=409715641)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

    await context.bot.send_message(chat_id=update.effective_chat.id, text="To see your notes, use the /notes command.")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


if __name__ == '__main__':

    application = ApplicationBuilder().token('6036572513:AAGvMHuJKqrC45QvIAEFStGPZozBJiHqmn0').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    caps_handler = CommandHandler('caps', caps)
    inline_caps_handler = InlineQueryHandler(inline_caps)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)




    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(inline_caps_handler)
    application.add_handler(unknown_handler)


    application.run_polling()


