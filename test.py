import connect as con
from clock import get_curr_time
from functions import check_exit, check_entrance


current_time = '2023-04-12 10:00:00'
current_time_list = current_time.split(' ')

def db_commit(sql):
    for command in sql:
        con.cursor.execute(command)
        con.db.commit()


def create_entrance(rfID):
    presence, lateness = check_entrance('07:40:00')
    sql = [
        f"INSERT INTO entrance_table (timeEntrace, rfID) VALUES ('{current_time}', '{rfID}')",
        f"UPDATE students SET presenceStudent = {presence}, lateStudent = {lateness} WHERE rfID = {rfID}"
    ]
    db_commit(sql)

def create_exit(rfID):
    abscense = check_exit(current_time_list[1])
    sql = f"SELECT presenceStudent FROM students WHERE rfID = {rfID}"
    con.cursor.execute(sql)
    result = con.cursor.fetchall()
    presence = result[0][0]

    new_presence = int(presence) - int(abscense)

    sql = [
        f"INSERT INTO exit_table (timeExit, rfID) VALUES ('{current_time}', '{rfID}')",
        f"UPDATE students SET presenceStudent = {new_presence}, absenceStudent = {abscense} WHERE rfID = {rfID}"
    ]
    db_commit(sql)
    return current_time

create_entrance('0001')
""" create_exit('0001') """
