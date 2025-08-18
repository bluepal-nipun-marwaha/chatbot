```markdown
# mail_saver.py

## Overview:
The `mail_saver.py` file is designed to connect to an email server using the IMAP protocol, fetch recent emails, and log their details into a specified log file. The key components of this file include functions for logging messages, fetching emails based on a user-defined query, and handling email parsing. The code utilizes environment variables to securely manage email credentials, ensuring that sensitive information is not hardcoded. The main function, `fetch_and_log_emails`, processes emails from the past N days, where N can be specified by the user. The file also integrates with the `langchain_core.tools` library to create a tool that can be used in larger applications. 

**Note**: It is crucial to secure environment variables and not share them, as this is essential for maintaining the security of email credentials.

## FunctionDef log_to_file

The `log_to_file` function is responsible for logging messages to a specified log file with a timestamp. This function is essential for maintaining a record of the email details that are fetched.

### Method log_to_file
**Parameters**:
- `msg`: A string containing the message to log.

**Returns**: None

**Note**: This function appends messages to the log file, which means that previous log entries will not be overwritten. Ensure that the log file path is accessible and writable.

#### Examples:
**Input Examples**: 
```python
log_to_file("Email fetched successfully.")
```

**Output Example**:
```
[2023-10-01 12:00:00] Email fetched successfully.
```

## FunctionDef fetch_and_log_emails

The `fetch_and_log_emails` function connects to an email server, retrieves emails based on a specified query, and logs their details into a file. It is the core functionality of the script, allowing users to specify how many days back they want to search for emails.

### Method fetch_and_log_emails
**Parameters**:
- `query`: A string formatted as "log emails from last X days," where X is a positive integer indicating the number of days to look back for emails (default is an empty string).

**Returns**: A string message indicating the result of the operation, such as the number of emails logged or an error message.

**Note**: The function handles various exceptions, including connection issues and parsing errors. Users should ensure that their email credentials are correctly set in the environment variables.

#### Examples:
**Input Examples**: 
```python
fetch_and_log_emails("log emails from last 5 days")
```

**Output Example**:
```
Logged 3 emails from the past 5 day(s).
```

**Input Examples**: 
```python
fetch_and_log_emails("log emails from last 30 days")
```

**Output Example**:
```
No emails found from the past 30 day(s).
```

**Input Examples**: 
```python
fetch_and_log_emails("log emails from last 0 days")
```

**Output Example**:
```
No emails found from the past 0 day(s).
```

**Input Examples**: 
```python
fetch_and_log_emails("log emails from last -5 days")
```

**Output Example**:
```
Error: Invalid number of days specified.
```

## Called_functions:
- **`os.getenv()`**: This function retrieves the email ID and password from environment variables, ensuring that sensitive information is not hardcoded into the script. It is crucial for maintaining security.

- **`imaplib.IMAP4_SSL()`**: Establishes a secure connection to the email server using the IMAP protocol. This is essential for securely accessing email data.

- **`email.message_from_bytes()`**: Converts raw email bytes into a message object, allowing for easier manipulation and extraction of headers and body content.

- **`decode_header()`**: This function decodes email headers that may be encoded in different formats, ensuring that subjects and sender names are correctly displayed. It is important for handling internationalized email headers.

- **`open()`**: Used to open the log file for writing. The function clears the log file at the start of the logging process and appends new log entries thereafter.

## Error Handling:
The script includes basic error handling for various scenarios, such as:
- Invalid email credentials, which may raise an authentication error.
- Network issues that could prevent connection to the email server.
- Parsing errors when processing email content.

Users should be aware of these potential issues and ensure that their environment is correctly configured.

Overall, this code provides a robust solution for fetching and logging recent emails, making it easier for users to track their email communications. The handling of various email formats and the structured logging of information contribute to its effectiveness.
```