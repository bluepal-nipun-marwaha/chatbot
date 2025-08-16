# Assistant Chat Bot

A modular, multi-agent chatbot built with -  
    [LangGraph](https://github.com/langchain-ai/langgraph),
    [OpenAI](https://platform.openai.com), and
    [Streamlit](https://streamlit.io)   
It was designed to perform local tasks, access online tools, and maintain a friendly chat interface.


## 🧠 Features

    LangGraph Supervisor Agent for multi-agent architecture  
    Search Assistant that can query the web, wikipedia, and arXiv  
    Local Assistant that can create timers, log statuses, and save chats  
    Date-Time Assistant that can give timezone-aware date and time responses  
    Email Log Parser that reads recent structured emails from logs  
    Email Logger that logs the past X days worth of emails  
    Email Notification that sends you a notification if a specific person emails you  
    Profile System so that you can select your own avatar and username  
    Dark Mode which has a blue-themed, modern and clean user interface  


## 📁 Folder Structure

<pre lang="text"> ```
txt project-root/ 
├── .streamlit/ 
│ └── config.toml # Main settings for the chatbot appearance 
├── chat_bot.py # Main interface
├── agent_supervisor.py # Agent framework
├── monitor.py # Monitoring the emails
├── pages/ 
│ ├── 1_User_Profile.py # Profile setup page 
│ └── 2_mail_reader.py # Mail reading setup
├── tools/ 
│ ├── search_tools.py 
│ ├── log_status.py 
│ ├── save_txt.py 
│ ├── timer.py 
│ ├── time_tool.py 
│ ├── mail_saver.py 
│ └── mail_reader.py 
├── images/ 
│ ├── cat.jpg 
│ ├── dog.jpg 
│ ├── robot.jpg
│ ├── supervisor.jpeg 
│ └── alien.jpg 
├── logs/ 
│ ├── about.txt     
│ ├── saved_logs.txt # (ignored in git) 
│ ├── status_logs.txt # (ignored in git) 
│ └── mail_logs.txt # (ignored in git) 
├── .env # Environment variables (ignored in git) 
├── .env.example # Template for environment setup 
├── requirements.txt # All dependencies 
├── .python-version 
├── pyproject.toml 
└── README.md 
``` </pre>

## ⚙️ Setup Instructions

### 1. Clone the repository

bash  
git clone https://github.com/nipun-marwaha/chatbot.git  
cd chatbot  

### 2. Create a virtual enviornment

python -m venv venv  
source venv/bin/activate   # Windows: venv\Scripts\activate  

### 3. Install the dependencies

pip install -r requirements.txt  

### 4. Set up your .env file

check out the .env.example file for an example  

### 5. Run the program

streamlit run chat_bot.py  


## ✅ Features to Explore

Switch user avatars in real time  
Automatically log daily statuses without going into another file    
Set and receive notifications for timers and emails from certain people
Read your own email log file using natural language  
Query online sources for research with LLM-backed agents  


## 🧩 Technologies Used

LangGraph   
LangChain  
OpenAI API  
Streamlit  
Python 3.10+  
Twilio


## 🙋‍♂️ Maintainer
Nipun Marwaha  
📧 nmarwaha135@gmail.com  |  nipun.marwaha@bluepal.com  
🔗 [GitHub](https://github.com/nipun-marwaha)  

