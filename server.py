
from encryption import encrypt, decrypt 
from flask import Flask, request, jsonify 
from RPi import GPIO 

# GPIO.setmode(GPIO.BOARD) 

app = Flask(__name__) 

@app.get("/")
def hello():
    return "Hello World" #jsonify({"message":"Hello World"}) 

@app.post("/encrypt")
def encrypt_data():
    message = request.json.get("message") 
    data = encrypt(message) 
    encrypted_message, key = data["encrypted_message"].decode(), data["key"].decode() 
    return jsonify({"encrypted_message":encrypted_message, "key":key})  

@app.post("/decrypt")    
def decrypt_data():
    encMessage = request.json.get("encrypted_message").encode() 
    key = request.json.get("key").encode() 
    message = decrypt(encMessage, key)
    return jsonify({"message":message})   


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True, port = 3000)  
