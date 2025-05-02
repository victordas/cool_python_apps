from dotenv import load_dotenv
from smtplib import SMTP_SSL
from ssl import create_default_context
from os import getenv

def send_mail(message):

    load_dotenv()

    host = "smtp.gmail.com"
    port = 465

    username = 'onlymyofficemails@gmail.com'
    password = getenv("GMAIL_APP_PASSWORD")

    context = create_default_context()
    
    with SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(from_addr=username, to_addrs=username, msg=message)
