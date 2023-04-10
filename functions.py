from time import strptime

from create import create_exit, create_entrance

not_present = True


def format(x):
    return strptime(x, "%H:%M:%S")


def check_time(time_user):
    time_user = format(time_user)
    lateness = 0
    value = 0
    if time_user > format("10:45:00"):  # not necessary
        value = 0
    elif time_user > "10:00":
        value = 1
    elif time_user > "9:00":
        value = 2
    elif time_user > "8:15":
        value = 3
    elif time_user > "7:45":
        value = 4
    elif time_user > "7:30":
        lateness = 1  # WILL USE ONLY IF IS "ENTRANCE" 
        value = 5
    # elif time_user >= "7:25" and time_user <= "7:30":
    elif "7:30" >= time_user >= "7:25":
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
