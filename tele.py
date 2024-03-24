from dotenv import load_dotenv 
import os 
import requests 

load_dotenv() 
tele_auth = os.getenv("TELE_AUTH") 
chat_id = os.getenv("TELE_CHAT_ID") 

base_url = f"https://api.telegram.org/bot{tele_auth}"

def send_telegram_message(message):
    message_url = base_url + f'/sendMessage?chat_id={chat_id}&text="{message}"'
    # print(message_url)
    res = requests.get(message_url)
    res = res.json() 
    # print(res)         
    return res['ok'] 
    