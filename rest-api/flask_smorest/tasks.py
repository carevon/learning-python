import os

import requests
from dotenv import load_dotenv

load_dotenv()

DOMAIN = os.getenv("MAILGUN_DOMAIN")

def send_simple_message(to, subject, body):
    api_key = os.getenv("MAILGUN_API_KEY")
    return requests.post(
            f"https://api.mailgun.net/v3/{DOMAIN}/messages",
            auth=("api", f"{api_key}"),
            data={"from": f"Felipe <mailgun@{DOMAIN}>",
                "to": [to],
                "subject": subject,
                "text": body}
    )


def send_user_registration_email(email, username):
    return send_simple_message(
        email,
        "Stores Rest API - Registration",
        f"Hi, {username}! You have successfully signed up to the Stores Rest API."
    )