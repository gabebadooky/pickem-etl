from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

def send(message_body: str, user_phone: str, sender_phone: str):
    """Method that constructs text reminder"""
    account_sid: str = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token: str = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_body,
        from_=sender_phone,
        messaging_service_sid=os.getenv("TWILIO_MESSAGING_SERVICE_SID"),
        to=f"+1{user_phone}"
    )
    print(message.sid)


send(f"This is a reminder to submit your picks for the upcoming weekend. Have a nice pickem! :)\n\nhttps://have-a-nice-pickem.onrender.com/", "4804331773", "+18884931875")