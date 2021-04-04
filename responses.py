import arrow
import requests 
import json

def sample_responses(input):
    user_msg = str(input).lower()

    if user_msg in ("hello", "hi"):
        return 'Hello!'

    if user_msg in ("oi", "oei"):
        return 'Rude'

    if user_msg in ("who are you?"):
        return "i am bot!"
    
    if user_msg in ("how are you?"):
        return "im fine, thank you. how about you?"
    
    if user_msg in ('what time is it?'):
        utc = arrow.utcnow()
        date_time = utc.shift(hours=8)
        date_time = date_time.format('YYYY-MM-DD HH:mm')

        return "the time now is {}".format(date_time)

    return "I dont understand your question"

def random_fact():
  response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
  json_data = json.loads(response.text)
  data = json_data['text']
  return data
