from langchain_core.tools import Tool

from threading import Thread
from plyer import notification

import time
import re

def timer_thread(seconds, message):
    time.sleep(seconds)
    notification.notify(
        title = 'Timer Finished',
        message = message,
        timeout = 10
    )

def set_timer(user_input: str):
    match = re.search(r"(\d+\.?\d*)", user_input)
    if not match:
        return 'Please specify timer duration in minutes'
    
    minutes = float(match.group(1))
    seconds = int(minutes * 60)


    thread = Thread(target=timer_thread, args=(seconds, "Timer is Up!"))
    thread.daemon = False
    thread.start()
    return f'Timer is set up for {minutes} minute(s).'

timer_tool = Tool(
    name= 'set_timer',
    func= set_timer,
    description= 'set a timer specifying the duration in minutes, like "5 minutes" or "5.5 minutes"'
)