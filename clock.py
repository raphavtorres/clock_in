from datetime import datetime


def get_curr_time():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    current_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    return current_timestamp
