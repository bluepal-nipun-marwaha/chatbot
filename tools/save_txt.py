from langchain_core.tools import Tool
from datetime import datetime

def save_to_txt(data: str, filename: str = 'logs\\saved_logs.txt'):
    timestamp = datetime.now().strftime('%D %H:%M:%S')
    formatted_text = f"------Research Output-------\n{timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding= 'utf-8') as f:
        f.write(formatted_text)
    
    return f'Data successfully saved to {filename}'

save_txt_tool = Tool(
    name= 'save_text_to_file',
    func= save_to_txt,
    description= 'saved structured data to a text file'
)