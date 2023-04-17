import connect as con
from clock import get_curr_time
from functions import check_entrance, check_exit, format

current_time = get_curr_time()
current_time_list = current_time.split(' ')
current_time_list = [0, "11:00:00"]


def db_commit(sql):
    for command in sql:
        con.cursor.execute(command)
        con.db.commit()


def read_element(rfID, element):
    sql = f"SELECT {element} FROM students WHERE rfID = {rfID}"
    con.cursor.execute(sql)
    result = con.cursor.fetchall()
    return result[0][0]


def hit_point(rfID):
    presence = read_element(rfID, 'isPresent')

    if presence == 1:
        presence = 0
        create_exit(rfID)
    elif format(current_time_list[1]) >= format("07:25:00"):
        presence = 1
        create_entrance(rfID)

    sql = [f"UPDATE students SET isPresent = {presence} WHERE rfID = {rfID}"]
    db_commit(sql)        


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
    presence = read_element(rfID, 'presenceStudent')

    new_presence = int(presence) - int(abscense)
    new_abscence = 5 - int(new_presence)

    sql = [
        f"INSERT INTO exit_table (timeExit, rfID) VALUES ('{current_time}', '{rfID}')",
        f"UPDATE students SET presenceStudent = {new_presence}, absenceStudent = {new_abscence} WHERE rfID = {rfID}"
    ]
    db_commit(sql)
    return current_time


def read_user():
    ...
