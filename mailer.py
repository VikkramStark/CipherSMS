import smtplib
from email.MIMEMiltipart import MIMEMultipart
from emnail.MIMEText import MIMEText
fromaddr = "edkinpi3#gmail.com"
toaddr = "d13sudarsonmv@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "vanakam"
server= smtblib.Smtp('smtp.gmail.com',25)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromaddr, "pioyytwcyocuojpf")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
