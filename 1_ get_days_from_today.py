from datetime import datetime
import re

# Function to get the number of days between provided date and today
# Input: date in YYYY-MM-DD format
# Output: number of days between provided date and today
# Raises ValueError if date is not in YYYY-MM-DD format
# Example: get_days_from_today('2021-12-31') -> 100
# Example: get_days_from_today('2021-01-01') -> -100
def get_days_from_today(date: str) -> int:

    if(not re.search(r'^\d{4}-\d{2}-\d{2}$', date)):
        raise ValueError("Invalid date format. Please provide date in YYYY-MM-DD format")

    # We should set time to 00:00:00 to get the correct number of days
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    required_date = datetime.strptime(date, '%Y-%m-%d')
    
    return (required_date - today).days


try :
    print(get_days_from_today("2021-10-09")) # negative result means the date is in the past
    print(get_days_from_today("2099-12-31")) # positive result means the date is in the future
    print(get_days_from_today(datetime.now().strftime('%Y-%m-%d'))) # today's date returns 0
    print(get_days_from_today("2021-10-09T10:00:00")) # invalid date format
except ValueError as e:
    print(f"ValueError raised with error message: {e}")
except TypeError as e:
    print(f"TypeError raised with error message: {e}")
