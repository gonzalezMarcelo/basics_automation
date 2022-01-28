import smtplib
import ssl
from email.message import EmailMessage

subject = "Esse email foi enviado pelo Python"
body = "Isso é um teste de envio de email pelo Python"
sender_email = "lealmarcelo2004@gmail.com"
receiver_email = "lealmarcelo2004@gmail.com"
password = input("Digite sua senha: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Mandando o Email")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email enviado")
