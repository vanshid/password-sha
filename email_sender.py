import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text()) 

email = EmailMessage()
email["from"] = "Vanshi Dalal"
email["to"] = "vanshid1904@gmail.com"
email["subject"] = "You suck V!!!!!"

email.set_content(html.substitute(name="JUST V"),"html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("vdvanshudalal19@gmail.com","vxd1904zxv")
    smtp.send_message(email)
    print("ALL GOOD BOSSS!!!")



