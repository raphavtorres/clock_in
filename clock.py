from datetime import datetime
from threading import Timer
from create import create_exit




def get_curr_time():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    current_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    return current_timestamp


def timer():
    timer_variable = Timer(14400, create_exit)
    timer_variable.start()


