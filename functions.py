from threading import Timer

from clock import get_curr_time
from create import create_exit


not_present = True


def get_curr_time():
    from datetime import datetime
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    current_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    return current_timestamp
    print("Ola, voce executou este arquivo em =", current_timestamp)


def check_time(time):
    if time > "10:45":
        value = 0
    elif time > "10:00":
        value = 1
    elif time > "9:00":
        value = 2
    elif time > "8:15":
        value = 3
    elif time > "7:45":
        value = 4
    elif time > "7:30":
        late = 1  # WILL USE ONLY IF IS "ENTRANCE" 
        value = 5
    elif time >= "7:25" and time <= "7:30":
        value = 5

def check_entrance(time_entrance):
    not_present = False
    presence = check_time(time_entrance)


def check_exit(rfID):
    time_exit = create_exit(rfID)
    abscense = check_time(time_exit)
    not_present = True 


def timer():
    timer_variable = Timer(14400, check_exit)
    timer_variable.start()
