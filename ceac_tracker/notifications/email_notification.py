from ceac_tracker.config.keys import get_keys
import smtplib, ssl
from email.mime.text import MIMEText


def send_notification(message, receiver):
    port = 587  # For SSL
    sender_email_username = get_keys()["email_username"]
    sender_email_password = get_keys()["email_password"]

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP("smtp.office365.com", port) as server:
        server.starttls(context=context)
        server.login(sender_email_username, sender_email_password)
        email_message = MIMEText(message)
        email_message["Subject"] = "Visa Notification"
        email_message["From"] = f"Lixin Project <{sender_email_username}>"
        email_message["To"] = receiver
        server.sendmail(sender_email_username, receiver, email_message.as_string())


if __name__ == "__main__":
    send_notification("Hello!", "wlx65005@gmail.com")
