from time import strptime


def format(x):
    return strptime(x, "%H:%M:%S")


def check_time(time_user):
    time_user = format(time_user)
    lateness = 0
    value = 0
    #  and time_user < format("11:30:00")
    
    if time_user > format("10:45:00") and time_user < format("11:30:00"):
        value = 1
    elif time_user > format("10:45:00"):
        pass
    elif time_user > format("10:00:00"):
        value = 1
    elif time_user > format("09:00:00"):
        value = 2
    elif time_user > format("08:15:00"):
        value = 3
    elif time_user > format("07:45:00"):
        value = 4
    elif time_user > format("07:30:00"):
        lateness = 1 
        value = 5
    elif format("07:25:00") <= time_user <= format("07:30:00"):
        value = 5
    return value, lateness


def check_entrance(time_entrance):
    presence, lateness = check_time(time_entrance)
    return presence, lateness


def check_exit(time_exit):
    abscense, _ = check_time(time_exit)
    return abscense


""" def timer():
    timer_variable = Timer(14400, create_exit)
    timer_variable.start()
"""
