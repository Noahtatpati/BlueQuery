import sqlite3

def run_query(sql):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except Exception as e:
        result = str(e)

    conn.close()
    return result