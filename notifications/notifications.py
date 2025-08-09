import etl.load.mysql_db as db
import notifications.email as email
from email.message import EmailMessage


def notify_users(date_str: str):
    """Method that calls dependent methods to compile and notify users who have marked a notification preference"""
    users_to_notify: list = db.get_users_to_notify()
    for user in users_to_notify:
        if user["NOTIFICATION_PREF"] == "e":
            user_email: str = user["EMAIL_ADDRESS"]
            email_subject: str = f"This is a reminder to submit your picks for the week of {date_str}"
            msg: EmailMessage = email.create(user_email, email_subject)
            email.send(msg)