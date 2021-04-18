from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from dotenv import load_dotenv
import responses as r

load_dotenv()

key = os.getenv('token')

print("bot started...")

def start_command(update, context):
    update.message.reply_text('type something to begin')

def help_command(update, context):
    update.message.reply_text('need help? google')

def fact_command(update,context):
    update.message.reply_text(r.random_fact())

def handle_msg(update, context):
    text = str(update.message.text).lower()
    responses = r.sample_responses(text)

    update.message.reply_text(responses)

def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(key, use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("funfact",fact_command))

    dp.add_handler(MessageHandler(Filters.text, handle_msg))

    dp.add_error_handler(error)

    updater.start_polling() 
    updater.idle()

main()