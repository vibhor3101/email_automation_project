import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

EMAIL_SERVER = "smtp.gmail.com"
PORT = 587

# Load environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"


load_dotenv(envars)  

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

print("User:", EMAIL_USER)
print("Password:", EMAIL_PASSWORD)


def send_email(subject, receiver_email, name, due_date, invoice_no, amount):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Singla Technologies", f"{EMAIL_USER}"))
    msg["To"] = receiver_email
    msg["BCC"] = EMAIL_USER

    # Plain text version
    msg.set_content(
        f"""\
Hi {name},
I hope you are well.
I just wanted to drop you a quick note to remind you that {amount} USD in respect of our
invoice {invoice_no} is due for payment on {due_date}.
I would be really grateful if you could confirm that everything is on track for payment.
Best regards,
Vibhor Singla
"""
    )

    # HTML version
    msg.add_alternative(
        f"""\
<html>
  <body>
    <p>Hi {name},</p>
    <p>I hope you are well.</p>
    <p>I just wanted to drop you a quick note to remind you that <strong>{amount} USD</strong> in respect of our invoice 
    {invoice_no} is due for payment on <strong>{due_date}</strong>.</p>
    <p>I would be really grateful if you could confirm that everything is on track for payment.</p>
    <p>Best regards,</p>
    <p>YOUR NAME</p>
  </body>
</html>
""",
        subtype="html",
    )

    # Send email
    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)

    print(f"Email successfully sent to {receiver_email}")

# Run the function
if __name__ == "__main__":
    send_email(
        subject="Invoice Reminder",
        name="Rekha Singla",
        receiver_email="rekhasingla13@gmail.com",
        due_date="11 Oct 2025",
        invoice_no="INV-21-12-009",
        amount="5",
    )
