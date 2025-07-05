import re
from langchain_core.tools import Tool
from dateutil import parser as dateparser
from datetime import datetime


def parse_mail_log(filepath="logs/mail_logs.txt", limit=None):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    emails = []
    current = {}
    body_lines = []
    collecting_body = False

    for line in lines:
        line = line.strip()

        if "Subject:" in line:
            if current and "Subject" in current:
                current["Body"] = "\n".join(body_lines)
                emails.append(current)

            current = {}
            body_lines = []
            collecting_body = False

            current["Subject"] = line.split("Subject:")[1].strip()

        elif "From:" in line:
            current["From"] = line.split("From:")[1].strip()

        elif "Date:" in line:
            current["Date"] = line.split("Date:")[1].strip()

        elif "Body:" in line:
            collecting_body = True

        elif "--------------------------------------------------" in line:
            collecting_body = False
            current["Body"] = "\n".join(body_lines)
            emails.append(current)
            current = {}
            body_lines = []

        elif collecting_body:
            body_lines.append(line.split("]")[-1].strip())

    if current and "Subject" in current:
        current["Body"] = "\n".join(body_lines)
        emails.append(current)

    return emails[-limit:] if limit else emails


def get_recent_emails(query: str = "") -> str:
    try:
        q = query.lower()
        sender_filter = None
        today_only = False
        count_mode = False

        # Extract sender 
        match_sender = re.search(r"(?:from|by|did)\s+([\w\s.@<>\"']+)", q)
        if match_sender:
            sender_filter = match_sender.group(1).strip()

        if "today" in q:
            today_only = True
        if "how many" in q:
            count_mode = True
        elif "did" in q:
            count_mode = "boolean"

        limit = 1 if count_mode else 5
        match_limit = re.search(r"(\d+)", q)
        if match_limit and not count_mode:
            limit = int(match_limit.group(1))

        emails = parse_mail_log(limit=None)
        today = datetime.now().date()

        filtered = []
        for email in emails:
            sender = email.get("From", "").lower()
            date_str = email.get("Date", "")
            try:
                mail_date = dateparser.parse(date_str).date()
            except Exception:
                continue

            if sender_filter and sender_filter.lower() not in sender:
                continue
            if today_only and mail_date != today:
                continue

            filtered.append(email)

        if count_mode == True:
            return f"{len(filtered)} email(s) from {sender_filter or 'the sender'} today."

        if count_mode == "boolean":
            return f"Yes, {sender_filter} sent you email(s) today." if filtered else f"No, nothing from {sender_filter} today."

        if not filtered:
            return "No matching emails found."

        output = []
        for i, email in enumerate(filtered[-limit:], 1):
            output.append(
                f"Email {i}:\n"
                f"Subject: {email.get('Subject', '[Missing]')}\n"
                f"From: {email.get('From', '[Missing]')}\n"
                f"Date: {email.get('Date', '[Missing]')}\n"
                f"Body:\n{email.get('Body', '[No Body]')}\n"
            )
        return "\n".join(output)

    except Exception as e:
        return f"Failed to parse email log: {e}"


email_reader_tool = Tool(
    name="read_email_log",
    func=get_recent_emails,
    description="Reads recent emails from the log. Accepts queries like 'last 3 emails', 'who sent the last email?', 'did John send a mail today?', or 'how many mails from alice today'."
)