import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"


def send_email(receiver_email,
               subject,
               body):

    message = MIMEMultipart()

    message["From"] = EMAIL
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(
        MIMEText(body, "plain")
    )

    try:

        server = smtplib.SMTP(
            SMTP_SERVER,
            SMTP_PORT
        )

        server.starttls()

        server.login(
            EMAIL,
            PASSWORD
        )

        server.sendmail(
            EMAIL,
            receiver_email,
            message.as_string()
        )

        server.quit()

        return True

    except Exception as error:

        print(error)

        return False


def birthday_email(name):

    return f"""
Happy Birthday {name}! 🎉

May your day be filled with happiness,
success, good health and unforgettable
memories.

Have a wonderful birthday!

- BirthdayVerse
"""


def motivation_email(name, quote):

    return f"""
Hello {name},

Today's Motivation:

"{quote}"

Keep believing in yourself.

- BirthdayVerse
"""