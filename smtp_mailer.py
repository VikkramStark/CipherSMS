# import smtplib 

# server = smtplib.SMTP("smtp.gmail.com", 587)  
# server.starttls() 

# server.login("edkinp911@gmail.com", "Raven@123")  
# server.sendmail("edkinp911@gmail.com", "d13sudarsonmv@gmail.com", "This is A test mail sent from python SMTP") 

# print("Mail Sent")   


import smtplib
import ssl
from email.message import EmailMessage

# Define email sender and receiver
email_sender = 'edkpi911@gmail.com'
email_password = 'cohkocebzbjsarhg' 
email_receiver = 'd13sudarsonmv@gmail.com'

def send_mail(): 

    # Set the subject and body of the email
    subject = 'Human Invasion Detected!' 
    body = f"""
        Danger!!
        Anamoly Detected through Sensors
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

send_mail() 