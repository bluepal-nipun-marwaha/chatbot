# monitor.py
import time
import json
import email
import os
import imaplib

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

with open('email_list.json', 'r') as f:
    mail_list = json.load(f)

monitor_emails = set(email for _, email in mail_list)

EMAIL = os.getenv("MAIL_ID")
PASSWORD = os.getenv("MAIL_PW")
IMAP_SERVER = "imap.mail.yahoo.com"

TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
FROM_NUMBER = os.getenv('FROM_NUMBER')
TO_WHATSAPP = os.getenv('TO_WHATSAPP')


def fetch_unread_from_senders(senders: set):
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")

        status, messages = mail.search(None, '(UNSEEN)')
        if status != "OK":
            return []

        unread_ids = messages[0].split()
        matched = []

        for uid in unread_ids:
            res, msg_data = mail.fetch(uid, "(RFC822)")
            if res != "OK":
                continue

            msg = email.message_from_bytes(msg_data[0][1])
            from_header = email.utils.parseaddr(msg["From"])[1]

            if from_header in senders:
                matched.append(from_header)

        mail.logout()
        return matched
    
    except Exception as e:
        print(f"❌ Error during email check: {e}")
        return []

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

while True:
    matches = fetch_unread_from_senders(monitor_emails)
    if matches:
        print("🚨 ALERT: Unread email(s) from monitored contacts:")
        for match in set(matches):
            message = client.messages.create(
                        from_=FROM_NUMBER,
                        to=TO_WHATSAPP,
                        body=f'New unread email from {match}'
                    )
            print(f"→ {match}")
        print("===")
    else:
        print("✅ No alert. Checking again in 30 sec...")

    time.sleep(30)