import smtplib, ssl
from email.messsage import EmailMessage

msg = EmailMessage()
msg.set_content("The body of the email is here")
msg["Subject"] = "An email alert"
msg["From"] = "edkinpi@gmail.com"
msg["To"] = "d13sudarsonmv@gmail.com"

context=ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
	smtp.starttls(context=context)
	smtp.login(msg["From"], "nivwmobvtjectpzh")
	smtp.send_message(msg)
