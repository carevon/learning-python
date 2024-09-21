import os

import requests
import jinja2
from dotenv import load_dotenv

load_dotenv()

DOMAIN = os.getenv("MAILGUN_DOMAIN")
template_loader = jinja2.FileSystemLoader(searchpath="./templates")
template_env = jinja2.Environment(loader=template_loader)


def render_template(template, **kwargs):
    return template_env.get_template(template).render(**kwargs)

def send_simple_message(to, subject, body, html):
    api_key = os.getenv("MAILGUN_API_KEY")
    return requests.post(
            f"https://api.mailgun.net/v3/{DOMAIN}/messages",
            auth=("api", f"{api_key}"),
            data={
                "from": f"Siege <mailgun@{DOMAIN}>",
                "to": [to],
                "subject": subject,
                "text": body,
                "html": html
                }
    )


def send_user_registration_email(email, username):
    return send_simple_message(
        email,
        "Stores Rest API - Registration",
        f"Hi, {username}! You have successfully signed up to the Stores Rest API.",
        render_template("email/action.html", username=username)
    )