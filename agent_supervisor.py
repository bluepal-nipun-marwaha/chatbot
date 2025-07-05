from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor

from dotenv import load_dotenv
load_dotenv()

from tools.search_tools import arxiv_tool, wiki_tool, web_search_tool
from tools.log_status import log_status_tool
from tools.save_txt import save_txt_tool
from tools.timer import timer_tool
from tools.time_tool import datetime_tool
from tools.mail_reader import email_reader_tool
from tools.mail_saver import email_logger_tool

from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver()

search_agent = create_react_agent(
    model= 'openai:gpt-4o-mini',
    tools= [arxiv_tool, wiki_tool, web_search_tool],
    prompt= '''You are a search assistant, that helps the user search things online
            If you are asked about certain research, use the `arxiv_tool` to search.''',
    name= 'search_assistant'
)

local_agent = create_react_agent(
    model= 'openai:gpt-4o-mini',
    tools= [save_txt_tool, log_status_tool],
    prompt='''You are a local assistant that performs tasks on the user's device.
            You can:
            - Save text to a file using `save_txt_tool`
            - Log user status using `log_status_tool`

            Only use a tool if you are sure it is required.''',
    name= 'local_assistant'
)

timer_agent = create_react_agent(
    model= 'openai:gpt-4o-mini',
    tools= [timer_tool],
    prompt= 'You are an assistant that helps set up a timer on the local device',
    name= 'timer_assistant'
)

datetime_agent = create_react_agent(
    model= 'openai:gpt-4o-mini',
    tools= [datetime_tool],
    prompt= 'You are a date and time assistant, which outputs the current date and time',
    name= 'datetime_assistant'
)

email_logging_agent = create_react_agent(
    model= 'openai:gpt-4o-mini',
    tools= [email_logger_tool],
    prompt= 'You are an email logging assistant, which looks through the emails and saves them in a log file',
    name= 'email_logging_assistant'
)

email_search_agent = create_react_agent(
    model= 'openai:gpt-4o-mini',
    tools= [email_reader_tool],
    prompt= 'You are an email assistant, which looks through the email logs and gives out the desired response',
    name= 'email_search_assistant'
)

supervisor = create_supervisor(
    agents= [search_agent, local_agent, datetime_agent, timer_agent, email_search_agent, email_logging_agent],
    model= ChatOpenAI(model= 'gpt-4o-mini'),
    prompt= '''You are a supervisor managing the following agents:
            - `search_assistant` for online research using tools like Arxiv, Wikipedia, or Web Search.
            - `local_assistant` for file and status logging tasks.
            - `datetime_assistant` for reporting date and time.
            - `timer_assistant` for setting timers.
            - `email_search_assistant` for reading previously saved email logs.
            - `email_logging_assistant` for retrieving recent emails from the inbox and saving them to logs using the `log_recent_emails` tool. If the user asks to "log", "fetch", "save" or "record" emails from a date or duration (e.g. 'last 3 days'), this tool should be used.

            Use the best-suited agent for each user request.'''
).compile(checkpointer=memory)