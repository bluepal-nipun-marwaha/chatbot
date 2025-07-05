from langchain_core.tools import Tool
from datetime import datetime


allowed_status = {
    'came to office',
    'work from home',
    'leave',
    'sick leave'
}

def update_txt_status(option:str):
    option = option.lower().strip()
    if option not in allowed_status:
        return f"Invalid status option. Please choose one of: {', '.join(allowed_status)}"
    
    
    timestamp = datetime.now().strftime('%D %I:%M:%S %p')
    
    entry = f'[{timestamp}] STATUS: {option.title()}\n'

    try:
        with open("logs\\status_logs.txt", "a", encoding="utf-8") as f:
            f.write(entry)
        return f"✅ Status '{option.title()}' logged at {timestamp}."
    except Exception as e:
        return str(f"Failed to log status: {e}")

log_status_tool = Tool(
    name= 'update_text_status',
    func= update_txt_status,
    description= 'writes your work status in the file based on the given option'
)