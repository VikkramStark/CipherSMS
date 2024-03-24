from cryptography.fernet import Fernet 
import time
from cryptography.fernet import Fernet
from gsmmodem.modem import GsmModem
import  RPi.GPIO as GPIO 
import requests 
import json 
from dotenv import load_dotenv, dotenv_values, find_dotenv 
# from mailer import send_email 
import os 
from twilio.rest import Client 
from tele import send_telegram_message

GPIO.setmode(GPIO.BCM)   

load_dotenv() 

# config = dotenv_values(".env") 
SENDER_MAIL = os.getenv("SENDER_MAIL") 
RECEIVER_MAIL = os.getenv("RECEIVER_MAIL") 
PASSWD = os.getenv("PASSWD") 

account_sid = os.getenv("account_sid") 
auth_token = os.getenv("auth_token")
twilio_number = os.getenv("twilio_number") 
receiver_phone = os.getenv("receiver_phone")   


# print(config) 

signal_gpio = 12 
ir_sensor = 6 

GPIO.setup(signal_gpio, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
print ("Alert system started…")
GPIO.setup(ir_sensor, GPIO.IN) 
print("IR Sensors Started!")



def encrypt(message):
    key = Fernet.generate_key() 
    fernet = Fernet(key) 
    encMessage = fernet.encrypt(message.encode())  
    return {"encrypted_message":encMessage, "key":key} 

def decrypt(encMessage, key):
    fernet = Fernet(key) 
    message = fernet.decrypt(encMessage).decode()  
    return message 

# def assymmetric_encrypt() 

# enc, key = encrypt("Hello World").values() 
# print(enc)  
# print(key)    
# print(decrypt(enc, key))  



# Replace with your GSM module's device and baud rate
gsm_device = '/dev/ttyUSB0'  # Change this to the correct device
baud_rate = 9600

# Replace with your secret key (make sure to keep it secret)
secret_key = b'your_secret_key_here'
# cipher_suite = Fernet(secret_key)

def encrypt_message(message):
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def send_sms(encrypted_message):
    modem = GsmModem(gsm_device, baud_rate)

    try:
        modem.connect()
        # Replace 'destination_number' with the recipient's phone number
        destination_number = 'replace_with_recipient_number'
        modem.sendSms(destination_number, encrypted_message)
        print("Encrypted SMS sent successfully.")
    except Exception as e:
        print(f"Error sending SMS: {e}")
    finally:
        modem.disconnect()

def send_text(text):  
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = text, #"This is a test Message from CipherSMS", 
        from_=twilio_number, 
        to=receiver_phone 
    ) 
    print(message.body) 


# def read_data():


if __name__ == "__main__":
    # Replace 'your_message_here' with the message you want to send
    plaintext_message = 'your_message_here'
    # encrypted_message = encrypt_message(plaintext_message)
    # send_sms(encrypted_message)
    print("Warming up Sensors!")  
    time.sleep(5) 
    
    while True:  
        print("Execution Started....")  
        i = GPIO.input(signal_gpio)   
        ir = GPIO.input(ir_sensor) 
        if i and not ir:  
            print(i, ir) 
            print("Human Activity Detected!") 
            headers = {"Content-Type":"application/json"} 
            message = f"IR Sensor :{ir}, PIR Sensor:{i}"
            data = {"message": message} 
            res = requests.post("http://localhost:3000/encrypt", headers = headers, json=data)       
            print(res) 
            if res.ok:
                r = res.json() 
                print(r)  
                data["status"] = "Security Breached!" 
                send_text("Human Invasion Detected!\nThis message is due to a security Breach!\nMotion Detected!")  
                # send_email(SENDER_MAIL,PASSWD,RECEIVER_MAIL,"Human Activity Detected", f"status:Motion-Detected,\n\nEncrypted Message:{r['encrypted_message']}\n\nkey:{r['key']}\n\nPlain-Text:{json.dumps(data)}")
            status = send_telegram_message("Human Invasion Detected!\nThis message is due to a security Breach!\nMotion Detected!") 
            if status:
                print("Message sent to Telegram") 
                print(message)  
            res = requests.post("http://localhost:5000/sendmail", headers={'Content-Type':"application/json"}, json = {}) 
            print(res) 
            # print(res.json())    
        print("Wait time Reached... wait for 10 seconds")  
        time.sleep(10) 
            
            # print(res.json()) 


