# Repository Documentation

This documentation provides a structured overview of the source code files in the repository. It includes file summaries, descriptions of classes and functions, input and return types, usage examples, and critical notes.

## 📁 Folder Structure

```plaintext
project-root/
├── .streamlit/
│   └── config.toml
├── chat_bot.py
├── agent_supervisor.py
├── monitor.py
├── pages/
│   ├── 1_User_Profile.py
│   └── 2_mail_reader.py
├── tools/
│   ├── search_tools.py
│   ├── log_status.py
│   ├── save_txt.py
│   ├── timer.py
│   ├── time_tool.py
│   ├── mail_saver.py
│   └── mail_reader.py
├── images/
│   ├── cat.jpg
│   ├── dog.jpg
│   ├── robot.jpg
│   ├── supervisor.jpeg
│   └── alien.jpg
├── logs/
│   ├── about.txt
│   ├── saved_logs.txt
│   ├── status_logs.txt
│   └── mail_logs.txt
├── .env
├── .env.example
├── requirements.txt
├── .python-version
├── pyproject.toml
└── README.md
```

## 📜 File Summaries

### 1. `.streamlit/config.toml`

#### Summary
Configuration for Streamlit app appearance and settings.

### 2. `chat_bot.py`

#### Summary
Main interface for the chatbot, responsible for handling user interactions.

#### Classes & Functions
- **Class: `ChatBot`**
  - **Methods:**
    - `__init__(self)`
      - Initializes the chatbot.
      - **Returns:** None
    - `run(self)`
      - Starts the chatbot loop.
      - **Returns:** None

#### Usage Example
```python
bot = ChatBot()
bot.run()
```

### 3. `agent_supervisor.py`

#### Summary
Framework for managing multiple agents within the chatbot.

#### Classes & Functions
- **Class: `AgentSupervisor`**
  - **Methods:**
    - `__init__(self)`
      - Initializes the supervisor with agents.
      - **Returns:** None
    - `manage_agents(self)`
      - Manages communication between agents.
      - **Returns:** None

### 4. `monitor.py`

#### Summary
File for monitoring email logs and interactions.

#### Functions
- **Function: `monitor_email_logs`**
  - Monitors email logs for activity.
  - **Parameters:** `log_path: str`
  - **Returns:** None

### 5. `pages/1_User_Profile.py`

#### Summary
Page for user profile setup in the chatbot.

#### Functions
- **Function: `setup_user_profile`**
  - Sets up the user profile.
  - **Parameters:** `username: str`, `avatar: str`
  - **Returns:** None

#### Usage Example
```python
setup_user_profile("john_doe", "cat.jpg")
```

### 6. `tools/search_tools.py`

#### Summary
Contains various search functions for querying online sources.

#### Functions
- **Function: `search_online(query: str) -> List[str]`**
  - Searches for a specific query and returns results.
  - **Parameters:** `query` - Search term.
  - **Returns:** A list of search results.

#### Usage Example
```python
results = search_online("latest AI trends")
```

### 7. `tools/log_status.py`

#### Summary
Log status related functionalities for maintaining chatbot status.

#### Functions
- **Function: `log_current_status(status: str)`**
  - Logs the current status of the chatbot.
  - **Parameters:** `status` - Current status as a string.
  - **Returns:** None

### 8. `tools/save_txt.py`

#### Summary
Utility for saving text data into files.

#### Functions
- **Function: `save_text_file(filename: str, content: str)`**
  - Saves content into a specified text file.
  - **Parameters:** 
    - `filename` - Name of the file to save.
    - `content` - Content to save.
  - **Returns:** None

### 9. `tools/timer.py`

#### Summary
Timer functionalities for setting alerts and reminders.

#### Functions
- **Function: `start_timer(duration: int)`**
  - Starts a timer for the specified duration.
  - **Parameters:** 
    - `duration` - Duration in seconds.
  - **Returns:** None

### 10. `tools/time_tool.py`

#### Summary
Utilities for handling date and time tasks.

#### Functions
- **Function: `get_current_time() -> str`**
  - Gets the current time as a formatted string.
  - **Returns:** Current time.

### 11. `tools/mail_saver.py`

#### Summary
Saves email logs from the system.

#### Functions
- **Function: `save_email(email_content: str)`**
  - Saves email content to a log.
  - **Parameters:** `email_content` - Content of the email.
  - **Returns:** None

### 12. `tools/mail_reader.py`

#### Summary
Reads and parses emails from logs.

#### Functions
- **Function: `read_emails(log_path: str) -> List[str]`**
  - Reads emails from specified log file.
  - **Parameters:** `log_path` - Path to the email log.
  - **Returns:** List of emails.

#### Usage Example
```python
emails = read_emails("/path/to/logs/mail_logs.txt")
```

## 🛠️ Important Notes & Dependencies

- Ensure that you have the required Python version (>=3.11) and dependencies listed in `requirements.txt` installed.
- The `.env` file must be configured properly per the `env.example` template to ensure the application runs smoothly.

## 🚀 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/nipun-marwaha/chatbot.git
   cd chatbot
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your `.env` file based on the `.env.example` template.

5. Run the program:
   ```bash
   streamlit run chat_bot.py
   ```

## Maintainer

Nipun Marwaha  
📧 nmarwaha135@gmail.com | nipun.marwaha@bluepal.com  
🔗 [GitHub](https://github.com/nipun-marwaha)  

---

This document serves as a comprehensive guide to understanding and utilizing the code within the repository. For more specific queries, refer to the source code comments directly within the files.