from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import key
import arrow
import requests
import json
import string

## Import your API key ##

key = key.secret_token

## Print something to show that the bot is alive ##

print("bot is running....")

## Utility Functions to be used in the Command Functions ## 
## get creative! you can do whatever you want here ##

def response(input):
    s0 = input.lower()
    s1 = "".join([i for i in s0 if i not in string.punctuation])
    text = s1.split()
    
    hello_ls = ["hello", "hi", "hey", "oi"]
    check =  any(word in text for word in hello_ls)
    
    if check is True:
        return "Hello!"

    if input in ("who are you?"):
        return "i am bot!"
    
    if input in ("how are you?"):
        return "im fine, thank you. how about you?"

    return "I dont understand your question"

def report_time():
    utc = arrow.utcnow()
    date_time = utc.shift(hours=8)
    date_time = date_time.format('YYYY-MM-DD HH:mm')

    return "the time now is {}".format(date_time)

def random_fact():
## https://uselessfacts.jsph.pl/
  response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
  json_data = json.loads(response.text)
  data = json_data['text']
  
  return data

## Create Command functions ##

## update is what the bot will use to respond to user inputs
## context is a slightly more advanced concept where it can take a user's metadata and determine if certain functions should be executed for certain users or not. (switching functions on and off)

def start_command(update, context):
    update.message.reply_text('type something to begin')

def time_command(update, context):
    update.message.reply_text(report_time())

def fact_command(update,context):
    update.message.reply_text(random_fact())

def reply_msg(update, context):
    input = str(update.message.text)
    responses = response(input)

    update.message.reply_text(responses)

## Define main function to run the script ##

def main():
    updater = Updater(key, use_context = True)
    dp = updater.dispatcher  ## receives user inputs, and dispatches it to the various handlers

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("time", time_command))
    dp.add_handler(CommandHandler("funfact",fact_command))

    dp.add_handler(MessageHandler(Filters.text, reply_msg))

    updater.start_polling() 
    updater.idle()

main()
