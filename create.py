import connect as con
from clock import get_curr_time
from functions import check_entrance, check_exit

current_time = get_curr_time()
current_time_list = current_time.split(' ')


def db_commit(sql):
    for command in sql:
        con.cursor.execute(command)
        con.db.commit()

def hit_point(rfID):
    #send to database True or False for "is_present"
    # if is_present:
    #    create_exit()
    # else:
    #    create_entrance()
    #
    # if time < 7:25
    #   value = null
    #   
    ...


# CALLED WHEN HIT
def create_entrance(rfID):
    presence, lateness = check_entrance(current_time_list[1])
    sql = [
        f"INSERT INTO entrance_table (timeEntrance, rfID) VALUES ('{current_time}', '{rfID}')",
        f"UPDATE students SET presenceStudent = {presence}, lateStudent = {lateness} WHERE rfID = {rfID}"
    ]
    db_commit(sql)


def create_exit(rfID):
    abscense = check_exit(current_time_list[1])

    """ sql = f"SELECT presenceStudent FROM students WHERE rfID = {rfID}"
    con.cursor.execute(sql)
    result = con.cursor.fetchall()
    presence = result[0][0] """

    new_presence = 5 - int(abscense)

    sql = [
        f"INSERT INTO exit_table (timeExit, rfID) VALUES ('{current_time}', '{rfID}')",
        f"UPDATE students SET presenceStudent = {new_presence}, absenceStudent = {abscense} WHERE rfID = {rfID}"
    ]
    db_commit(sql)
    return current_time


create_exit('0001')
def read_user():
    ...
