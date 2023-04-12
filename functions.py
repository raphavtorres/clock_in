from time import strptime
from threading import Timer

not_present = True


def format(x):
    return strptime(x, "%H:%M:%S")


def check_time(time_user):
    time_user = format(time_user)
    lateness = 0
    value = 0
    if time_user > format("10:45:00"):  # not necessary
        value = 0
    elif time_user > format("10:00:00"):
        value = 1
    elif time_user > format("9:00:00"):
        value = 2
    elif time_user > format("8:15:00"):
        value = 3
    elif time_user > format("7:45:00"):
        value = 4
    elif time_user > format("7:30:00"):
        lateness = 1 
        value = 5
    elif format("7:30:00") >= time_user >= format("7:25:00"):
        value = 5
    return value, lateness


def check_entrance(time_entrance):
    not_present = False
    presence, lateness = check_time(time_entrance)
    return presence, lateness


def check_exit(time_exit):
    abscense, _ = check_time(time_exit)
    not_present = True
    return abscense


""" def timer():
    timer_variable = Timer(14400, create_exit)
    timer_variable.start()
 """