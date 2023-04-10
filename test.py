import connect as con


con.cursor.execute(f"SELECT nameStudent FROM students WHERE rfID = '123'")


for sla in con.cursor:
    print(*sla)
