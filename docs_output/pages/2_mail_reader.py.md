# 2_mail_reader.py

## Overview:
The `2_mail_reader.py` file is a Streamlit application designed to manage and monitor email addresses. It utilizes a SQLite database to store email entries and provides a user interface for adding, resetting, and displaying emails. The application also includes functionality to start and stop an external monitoring process that presumably tracks email activity. The monitoring process is intended to track incoming emails and notify users of any new activity. Key components include database setup, functions for email management, and a Streamlit interface that allows users to interact with the application seamlessly.

## ClassDef or FunctionDef

### FunctionDef add_email(name, email)
The `add_email` function is responsible for inserting a new email entry into the SQLite database. It takes two parameters: `name` and `email`, which represent the user's name and their corresponding email address.

**Parameters**:
- `name` (str): The name of the user to be added to the database.
- `email` (str): The email address of the user to be added to the database.

**Returns**:
- `bool`: Returns `True` if the email was successfully added, or `False` if the name already exists in the database (due to the primary key constraint).

**Note**: It is important to ensure that the name provided is unique, as it serves as the primary key in the database. Attempting to add a duplicate name will result in an `IntegrityError`. Additionally, other exceptions may arise during database operations, so proper error handling is recommended.

#### Examples:
**Input Examples**: 
```python
add_email("Alice", "alice@example.com")
```
This input attempts to add Alice's email to the database.

**Output Example**:
```python
True
```
This output indicates that the email was successfully added.

---

### FunctionDef reset_email()
The `reset_email` function is designed to delete all entries from the `emails` table in the SQLite database. This function is useful for clearing the email list when needed.

**Parameters**: None

**Returns**:
- `bool`: Returns `True` if the reset operation was successful.

**Note**: This function will remove all email entries without any confirmation prompt, so it should be used with caution. There is no confirmation prompt before deletion.

#### Examples:
**Input Examples**: 
```python
reset_email()
```
This input calls the function to reset the email list.

**Output Example**:
```python
True
```
This output indicates that the email list was successfully reset.

---

### FunctionDef get_all_emails()
The `get_all_emails` function retrieves all email entries from the SQLite database. It returns the data in a list of tuples, where each tuple contains a name and an email address.

**Parameters**: None

**Returns**:
- `list`: A list of tuples containing all email entries from the database.

**Note**: This function does not handle any exceptions, so if the database is empty, it will return an empty list.

#### Examples:
**Input Examples**: 
```python
get_all_emails()
```
This input retrieves all email entries from the database.

**Output Example**:
```python
[("Alice", "alice@example.com"), ("Bob", "bob@example.com")]
```
This output shows a list of email entries retrieved from the database.

**Output Example (Empty Database)**:
```python
[]
```
This output indicates that there are no email entries in the database.

---

### FunctionDef write_emails()
The `write_emails` function exports all email entries from the database to a JSON file named `email_list.json`. This function is useful for exporting email data for external use.

**Parameters**: None

**Returns**: None

**Note**: The function will overwrite the existing `email_list.json` file each time it is called. Ensure that this behavior is acceptable before using the function.

#### Examples:
**Input Examples**: 
```python
write_emails()
```
This input calls the function to write the email list to a JSON file.

**Output Example**:
```json
[["Alice", "alice@example.com"], ["Bob", "bob@example.com"]]
```
This output represents the content of the `email_list.json` file after the function is executed.

---

## Streamlit App
The main part of the code creates a web application interface using Streamlit. It includes various components for user interaction, such as buttons for starting and stopping email monitoring, input fields for entering email data, and displays for showing monitored emails. This application provides a comprehensive solution for managing and monitoring email addresses through an intuitive web interface.

### Monitoring Process
The application uses a session state variable to track whether the email monitoring process is running. It provides buttons to start and stop the monitoring process using `subprocess.Popen` to run an external script (`monitor.py`). The external script is responsible for monitoring email activity and notifying users of any new emails.

### Email Input
Users can input a name and email address. When the "Save and Continue" button is clicked, it attempts to save the email using `add_email()`.

### Reset Button
The application provides functionality to reset the email list by calling `reset_email()`.

### Display Monitored Emails
The application fetches and displays all monitored emails from the database using `get_all_emails()`.

---

## Called_functions:
- **`sqlite3.connect`**: Establishes a connection to the SQLite database, allowing for data storage and retrieval.
- **`cursor.execute`**: Executes SQL commands to manipulate the database (e.g., creating tables, inserting data, deleting data).
- **`subprocess.Popen`**: Starts the external monitoring script (`monitor.py`), allowing the application to monitor emails in real-time.
- **`os.kill` and `proc.terminate`**: Used to stop the monitoring process based on the operating system.
- **`json.dump`**: Writes the list of emails to a JSON file for external use or storage.

Overall, this code provides a user-friendly interface for managing email addresses, monitoring email activity, and storing email data in a SQLite database. 

### Dependencies:
To run this application, ensure you have the following libraries installed:
- Streamlit: Install using `pip install streamlit`
- SQLite: This is included with Python's standard library, so no additional installation is required.

By implementing these suggestions, the documentation is clearer, more informative, and user-friendly, enhancing the overall understanding of the codebase.