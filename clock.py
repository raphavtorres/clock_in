def get_curr_time():

    from datetime import datetime

    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    current_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Ola, voce executou este arquivo em =", current_timestamp)


get_curr_time()