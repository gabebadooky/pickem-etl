from email.message import EmailMessage
import smtplib

def create(to: str, body: str) -> EmailMessage:
    """Method that instantiates the Email Message object with the inputted parameters"""
    msg = EmailMessage()
    msg["From"] = "no-reply@have-a-nice-pickem.com"
    msg["To"] = to
    msg["Subject"] = "Submit your picks!"
    msg.set_content(body)
    return msg


def send(msg: EmailMessage):
    """Method that accepts and sends an EmailMessage object"""
    with smtplib.SMTP("localhost") as s:
        s.send_message(msg)


