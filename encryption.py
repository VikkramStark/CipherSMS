from cryptography.fernet import Fernet 
import time
from cryptography.fernet import Fernet
from gsmmodem.modem import GsmModem


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
cipher_suite = Fernet(secret_key)

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

if __name__ == "__main__":
    # Replace 'your_message_here' with the message you want to send
    plaintext_message = 'your_message_here'
    encrypted_message = encrypt_message(plaintext_message)
    send_sms(encrypted_message)
