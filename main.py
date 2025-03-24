# import requests

# https://api.telegram.org/bot<token>/METHOD_NAME
# token = "token"


# request_str = "https://api.telegram.org/bot7902405831:AAE1TIgtSRpxyQy1OWRf3S7yljIyPx2ySBU/getUpdates"

# resp = requests.get(request_str)
# data = resp.json()
# print(data)

# print(resp.text['ok'])
# print(resp.json()['ok'])

"""
    status codes

    404 - not found
    500 - server error
"""



import requests
import time
import os




update_id = None
loop = True
while loop:
    request_str = "https://api.telegram.org/bot7902405831:AAE1TIgtSRpxyQy1OWRf3S7yljIyPx2ySBU/getUpdates"
    resp = requests.get(request_str, params={'offset': update_id})
    data = resp.json()
    updates = data['result']
    
    
    for update in updates:
        name = update['message']['from']['first_name']
        update_id = update['update_id'] + 1
        
        request_str = "https://api.telegram.org/bot7902405831:AAE1TIgtSRpxyQy1OWRf3S7yljIyPx2ySBU/sendMessage"
        chat_id = update['message']['from']['id']
        
    
        if (update['message']['text'].lower() == "hello"):

            hello = "Hello! How can I help you? "


            requests.get(request_str, params={'chat_id': chat_id, 'text':hello+name })

        elif update['message']['text'].lower() == "how are u" or update['message']['text'].lower() == "how are you":
            answer = " Evrything is great!"
        
            requests.get(request_str, params={'chat_id': chat_id, 'text':name+answer})

        elif update['message']['text'] == "/start":
            answer2 = "Hello! I'm a bot. Here's a list of my commnds:\n/help - Lists the commands.\n/weather - Gives info of weather.\n/info - gives your ID"
            print("start")
            requests.get(request_str, params={'chat_id': chat_id, 'text':name+" "+answer2})
        elif update['message']['text'] == "/help":
            answer2 = "/help - gives list of commands.\n/weather - gives info about weather.\n/info - gives your ID"
            print("help")
            requests.get(request_str, params={'chat_id': chat_id, 'text':name+" "+answer2})
        elif update['message']['text'] == "/weather":
           answer2 = "The weather is great today!(maybe)"
           print("weather")
           requests.get(request_str, params={'chat_id': chat_id, 'text':name+" "+answer2})
        elif update['message']['text'] == "/info":
            answer2 = f" Here's your ID: {chat_id}"
            print("info")
            requests.get(request_str, params={'chat_id': chat_id, 'text':name+" "+answer2})
        elif update['message']['text'] == "/stop":
            answer2 = "I'm dying! HELP ME....I'm under.... thee.....water"
            requests.get(request_str, params={'chat_id': chat_id, 'text':name+" "+answer2})
            loop = False 
            
        else:
            message = "I don't know how to reply to that."
            requests.get(request_str, params={'chat_id': chat_id, 'text':name+" "+message})
                                         
            
        
    
        time.sleep(1)
print("Bot stopped")
#os._exit(0)



    
