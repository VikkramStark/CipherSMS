from cryptography.fernet import Fernet 

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