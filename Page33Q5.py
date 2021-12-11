# Advanced Challenge: import the 'datetime' module and use it to determine the 
# current time. This function should print message based on the time.
# For ex: if the current time is between 0900 and 1000, print the message "Morning Lecture time!"

def current_time(): 
    from datetime import datetime
    now = datetime.now()
    if(now.hour >= 9 and now.hour < 10):
         print('Morning lecture time ')
    if(now.hour >= 12 and now.hour < 13):
         print('Lunch time ')

current_time()

