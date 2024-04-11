import datetime

# Function to get upcoming birthdays
# Input: list of users
# Output: list of users with upcoming birthdays
def get_upcoming_birthdays(users: list) -> list:
    today = datetime.date.today()
    end_date = today + datetime.timedelta(days=7)

    upcoming_bd_users = list(filter(lambda user: 
                                int(user['birthday'][5:7]) >= today.month and 
                                int(user['birthday'][8:10]) >= today.day and 
                                int(user['birthday'][5:7]) <= end_date.month and 
                                int(user['birthday'][8:10]) <= end_date.day
                               , users))
    
    if not upcoming_bd_users:
        return list()
    
    # set congrats date to be not the weekend and remove birthday key
    for user in upcoming_bd_users:
        congrats_date = datetime.date(today.year, int(user['birthday'][5:7]), int(user['birthday'][8:10]))
        while congrats_date.weekday() > 4:
            congrats_date += datetime.timedelta(days=1)
        user['congratulation_date'] = congrats_date.strftime('%Y-%m-%d')
        user.pop('birthday')

    return sorted(upcoming_bd_users, key=lambda user: user['congratulation_date'])

users = [
    {
        "name": "John",
        "birthday": "1990-01-01"
    },
    {
        "name": "Jane",
        "birthday": "2000-03-21"
    },
    {
        "name": "Alice",
        "birthday": "1974-04-13"
    },
    {
        "name": "Bob",
        "birthday": "2011-04-12"
    }
]
print(get_upcoming_birthdays(users)) # should return Bob and Alice