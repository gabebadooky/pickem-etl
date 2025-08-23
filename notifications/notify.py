import re
import etl.load.mysql_db as db
import notifications.email_notification as email_notification
import notifications.text_notification as text_notification
from email.message import EmailMessage


twilio_sender_number: str = "+18884931875"
notification_body: str = f"This is a reminder to submit your picks for the upcoming weekend. Have a nice pickem! :)\n\nhttps://have-a-nice-pickem.onrender.com/"


def notify_users():
    """Method that calls dependent methods to compile and notify users who have marked a notification preference"""
    users_to_notify: list = db.get_users_to_notify()
    
    for user in users_to_notify:
        if user["NOTIFICATION_PREF"] == "e":
            user_email: str = user["EMAIL_ADDRESS"]
            msg: EmailMessage = email_notification.create(user_email, notification_body)
            email_notification.send(msg)

        if user["NOTIFICATION_PREF"] == "p":
            user_phone: str = re.sub(r"\D", "", user["PHONE"])
            text_notification.send(notification_body, user_phone, twilio_sender_number)


