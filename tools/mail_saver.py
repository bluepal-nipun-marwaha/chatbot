import imaplib
import email
import datetime
import os
import re

from email.header import decode_header
from langchain_core.tools import Tool
from dotenv import load_dotenv
load_dotenv()

LOG_FILE = "logs/mail_logs.txt"

def log_to_file(msg):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    line = f"{timestamp} {msg}"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def fetch_and_log_emails(query: str = "") -> str:
    username = "nipun.marwaha@bluepal.com"
    password = os.getenv("MAIL_PW")
    imap_host = "imap.mail.yahoo.com"

    try:
        days = 7
        match = re.search(r"\d+", query)
        if match:
            days = int(match.group(0))

        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write('')

        since_date = (datetime.datetime.now() - datetime.timedelta(days=days)).strftime("%d-%b-%Y")

        imap = imaplib.IMAP4_SSL(imap_host)
        imap.login(username, password)
        imap.select("INBOX")

        status, messages = imap.search(None, f'SINCE {since_date}')
        if status != "OK":
            return "Failed to search emails."

        email_ids = messages[0].split()
        if not email_ids:
            return f"No emails found from the past {days} day(s)."

        for eid in email_ids:
            _, msg_data = imap.fetch(eid, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])

                    subject, encoding = decode_header(msg.get("Subject", "No Subject"))[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding or "utf-8", errors="ignore")

                    from_, encoding = decode_header(msg.get("From", "Unknown Sender"))[0]
                    if isinstance(from_, bytes):
                        from_ = from_.decode(encoding or "utf-8", errors="ignore")

                    date = msg.get("Date", "Unknown Date")

                    log_to_file(f"Subject: {subject}")
                    log_to_file(f"From: {from_}")
                    log_to_file(f"Date: {date}")
                    log_to_file("Body:")

                    body = ""
                    if msg.is_multipart():
                        for part in msg.walk():
                            if part.get_content_type() == "text/plain" and not part.get("Content-Disposition"):
                                try:
                                    body = part.get_payload(decode=True).decode(part.get_content_charset() or "utf-8", errors="ignore")
                                    break
                                except:
                                    continue
                    else:
                        payload = msg.get_payload(decode=True)
                        if payload:
                            try:
                                body = payload.decode(msg.get_content_charset() or "utf-8", errors="ignore")
                            except:
                                body = str(payload)

                    for line in body.strip().splitlines():
                        log_to_file(line.strip())

                    log_to_file("-" * 50)

        imap.logout()
        return f"Logged {len(email_ids)} emails from the past {days} day(s)."

    except Exception as e:
        return f"Error: {str(e)}"

email_logger_tool = Tool(
    name="log_recent_emails",
    func=fetch_and_log_emails,
    description="Logs all emails from the past N days into a file. Use like: 'log emails from last 5 days'"
)