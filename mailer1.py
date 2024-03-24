import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # Set up the SMTP server
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 587,None,30)
    smtp_server.login(sender_email, sender_password)
    
    
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))
    
    # Send the email
    smtp_server.send_message(msg)
    
    # Close the connection
    smtp_server.quit()

