import connect as con
from clock import get_curr_time
from functions import check_entrance, check_exit

current_time = get_curr_time()
current_time_list = current_time.split(' ')


def db_commit(sql):
    con.cursor.execute(sql)
    con.db.commit()


def create_entrance(rfID):
    presence, lateness = check_entrance(current_time_list[1])
    sql = [
        f"INSERT INTO entrance_table (timeEntrance, rfID) VALUES ({current_time}, {rfID})",
        f"UPDATE students SET presenceStudent = {presence}, WHERE rfID = {rfID}"
    ]
    db_commit(sql)


def create_exit(rfID):
    abscense = check_exit(current_time_list[1])
    # presence --> checar bd --> fazer conta == presence - abscense ==> presence e depois update
    db_commit(
        f"SELECT presenceStudent FROM students"
    )


    sql = [
        f"INSERT INTO entrance_table (timeEntrance, rfID) VALUES ({current_time}, {rfID})",
        f"INSERT INTO exit_table (timeExit, rfID) VALUES ({current_time}, {rfID})",
        f"UPDATE students SET presenceStudent = {presence}, absenceStudent = {abscense} WHERE rfID = {rfID}"
    ]
    db_commit(sql)
    return current_time


def read_user():
    ...
