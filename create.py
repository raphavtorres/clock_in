import connect as con
from functions import get_curr_time

def create_entrance(rfID_user):
    current_time = get_curr_time()
    rfID = rfID_user
    sql = f"INSERT INTO entrance_table (timeEntrace, rfID) VALUES ({current_time}, {rfID})"
    con.cursor.execute(sql)
    con.db.commit()



def create_exit(rfID_user):
    current_time = get_curr_time()
    rfID = rfID_user
    sql = f"INSERT INTO exit_table (timeExit, rfID) VALUES ({current_time}, {rfID})"
    con.cursor.execute(sql)
    con.db.commit()
    return current_time



