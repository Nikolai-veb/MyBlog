import requests
import toc
import json
from yobit_pars import get_btc
from time import sleep
token = toc.token
#https://api.telegram.org/bot1328871730:AAGTqGl_NLzvDRRuXT6E9qrwiMyahh1SWGY/sendmessage?chat_id=868494782&text=hi
URL = "https://api.telegram.org/bot" + token + "/"

global last_update_id
last_update_id = 0

def get_updates():

    url = URL + "getupdates"
    r = requests.get(url)
    return r.json()


def get_message():

    data = get_updates()
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id = data['result'][-1]['message']['chat']['id']
        message_text = data['result'][-1]['message']['text']
        message = {'chat_id': chat_id,
                   'text': message_text
                  }
        return message
    return None


def send_message(chat_id, text='Wait a second, please.......'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
   # d = get_updates()
   # with open('update.json', 'w') as f:
   # json.dump(d, f, indent=2, ensure_ascii=False)
   while True:
       answer = get_message()
       if answer != None:
           chat_id = answer['chat_id']
           text = answer['text']
           bitcoin = ['/btc', 'bitcoin', 'bitoc', 'биткоин', 'Bitcoin', 'BITCOIN']
           if text in bitcoin:
               send_message(chat_id, get_btc())
       else:
           continue

       sleep(2)


if __name__ == '__main__':
    main()
