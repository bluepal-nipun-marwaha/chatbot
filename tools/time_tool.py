from langchain_core.tools import Tool
from datetime import datetime
import pytz
from tzlocal import get_localzone

def get_current_datetime(query: str = "") -> str:
    
    timezones = {
        "pst": "US/Pacific",
        "cst": "US/Central",
        "est": "US/Eastern",
        "mst": "US/Mountain",
        "ist": "Asia/Kolkata",
        "gmt": "Etc/GMT",
        "utc": "UTC",
        "jst": "Asia/Tokyo",
        "cet": "Europe/Paris",
        "bst": "Europe/London",
    }

    local_tz = get_localzone()
    local_now = datetime.now(local_tz)
    default_msg = local_now.strftime(f"Local Timezone: {str(local_tz)}\n %A, %d %B %Y\n %I:%M:%S %p")

    query = query.lower()
    for key, tz in timezones.items():
        if key in query:
            target_tz = pytz.timezone(tz)
            target_time = datetime.now(target_tz)
            return target_time.strftime(f"Timezone: {tz}\n %A, %d %B %Y\n %I:%M:%S %p")

    return default_msg


datetime_tool = Tool(
    name="get_current_datetime",
    func=get_current_datetime,
    description="Returns the current date and time. Specify a timezone like 'PST', 'IST', or 'UTC' in the query."
)

if __name__ == '__main__':
    print(get_current_datetime('pst'))