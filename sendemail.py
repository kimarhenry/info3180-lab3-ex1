import smtplib 
from_addr = 'kimarhenry@gmail.com' 
to_addr  = 'kimarhenry@yahoo.com' 
from_name = 'kimarhenry'
to_name = 'kimarhenry'
subject = 'lab3'
message = """
From: 'kimarhenry' <kimarhenry@gmail.com>
To: 'kimarhenry' <kimarhenry@yahoo.com>
Subject: lab3
"""
msg= 'working well i guess'
message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg) 
# Credentials (if needed) 
username = '' 
password = '' 
# The actual mail send 
server = smtplib.SMTP('smtp.gmail.com:587') 
server.starttls() 
server.login(username, password) 
server.sendmail(from_addr, to_addr, message_to_send) 
server.quit()