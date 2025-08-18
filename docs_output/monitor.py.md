# monitor.py

## Overview:
The `monitor.py` script is designed to monitor unread emails from a specified list of email addresses and send notifications via WhatsApp using the Twilio API when new unread emails are detected. The script utilizes the IMAP protocol to connect to an email server, fetch unread emails, and parse the email data to identify the senders. It continuously checks for new unread emails in a loop, providing real-time alerts to the user.

Key components of the script include:
- **Email Monitoring**: The script connects to an email server and checks for unread emails from a predefined list of senders.
- **Twilio Integration**: It uses the Twilio API to send WhatsApp messages to notify the user of new unread emails.
- **Environment Configuration**: Sensitive information such as email credentials and Twilio API keys are managed using environment variables loaded from a `.env` file. To set up the `.env` file, create a file named `.env` in the same directory as the script and include the following variables:
  ```
  MAIL_ID=your_email@example.com
  MAIL_PW=your_email_password
  TWILIO_SID=your_twilio_sid
  TWILIO_AUTH_TOKEN=your_twilio_auth_token
  FROM_NUMBER=your_twilio_whatsapp_number
  TO_WHATSAPP=recipient_whatsapp_number
  ```
- **Error Handling**: The script includes basic error handling to manage issues that may arise during email fetching. It specifically handles exceptions such as `IMAP.error`, `ConnectionError`, and general exceptions, printing error messages if any issues occur during the email fetching process.

## FunctionDef fetch_unread_from_senders

The `fetch_unread_from_senders` function is responsible for connecting to the email server, searching for unread emails, and returning a list of senders who have unread emails. It takes a set of email addresses as input and checks for unread messages from those senders.

### Method fetch_unread_from_senders(senders: set)
This method connects to the email server using IMAP, logs in with the provided credentials, and searches for unread emails in the inbox. It then checks if the sender of each unread email is in the specified set of monitored senders.

**Parameters**:
- `senders`: A set of email addresses to monitor for unread emails.

**Returns**:
- A list of email addresses that have unread emails from the monitored senders. The returned list may be empty if no unread emails are found.

**Note**: 
- Ensure that the email credentials and IMAP server settings are correctly configured in the environment variables.
- The function handles exceptions and prints error messages if any issues occur during the email fetching process, including `IMAP.error`, `ConnectionError`, and other general exceptions.

#### Examples:
**Input Examples**: 
```python
monitor_emails = {"john@example.com", "jane@example.com"}
unread_senders = fetch_unread_from_senders(monitor_emails)
```
This input checks for unread emails from the specified senders.

**Output Example**:
```python
["john@example.com"]
```
This output indicates that there is an unread email from "john@example.com".

**Additional Input Examples**:
1. **No Unread Emails**:
```python
monitor_emails = {"nonexistent@example.com"}
unread_senders = fetch_unread_from_senders(monitor_emails)
```
Output:
```python
[]
```
This output indicates that there are no unread emails from the monitored senders.

2. **Multiple Unread Emails**:
```python
monitor_emails = {"alice@example.com", "bob@example.com"}
unread_senders = fetch_unread_from_senders(monitor_emails)
```
Output:
```python
["alice@example.com", "bob@example.com"]
```
This output indicates that there are unread emails from both "alice@example.com" and "bob@example.com".

## Called_functions:
- **`load_dotenv()`**: Loads environment variables from a `.env` file, which is essential for managing sensitive information securely. This function is called at the beginning of the script to ensure all necessary environment variables are available.

- **`imaplib.IMAP4_SSL()`**: Establishes a secure connection to the email server using the IMAP protocol, allowing for secure email fetching. This function is used within `fetch_unread_from_senders` to connect to the email server.

- **`email.message_from_bytes()`**: Converts the raw email bytes into a message object for easier manipulation and extraction of headers and body. This function is called when processing each unread email to extract relevant information.

- **`email.utils.parseaddr()`**: Parses the "From" header of the email to extract the sender's email address, which is crucial for identifying monitored senders. This function is used to determine if the sender of an unread email is in the monitored list.

- **`Client.messages.create()`**: Sends a message via Twilio's API, allowing notifications to be sent to WhatsApp when unread emails are detected. This function is called to send alerts for each matched sender.

Overall, this code implements a monitoring system that checks for unread emails from specified contacts and sends notifications via WhatsApp when new unread emails are detected. It effectively integrates email fetching and messaging functionalities, providing a useful tool for email management. This script is particularly useful for individuals who want to stay updated on important emails without constantly checking their inbox.