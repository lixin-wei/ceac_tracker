import sqlite3
from my_logging import get_logger

logger = get_logger(__file__)

conn = sqlite3.connect("data.db")
cursor = conn.cursor()


def get_all_applications():
    global cursor
    res = cursor.execute("SELECT application_id, location, case_created FROM application")
    return res.fetchall()


def get_all_records(application_id):
    global cursor
    res = cursor.execute("SELECT update_date, status, description FROM history WHERE application_id=? ORDER BY timestamp DESC", (application_id,))
    return res.fetchall()


def add_application(application_id, location, case_created):
    global cursor, conn
    res = cursor.execute("INSERT INTO application(application_id, location, case_created) VALUES(?, ?, ?)", (application_id, location, case_created))
    conn.commit()


def add_record(application_id, update_date, status, description):
    global cursor, conn
    res = cursor.execute(
        "INSERT INTO history(application_id, update_date, status, description) VALUES(?, ?, ?, ?)", (application_id, update_date, status, description)
    )
    conn.commit()


if __name__ == "__main__":
    with open("ddl.sql", "r") as ddl:
        sql = ddl.read()
        cursor.executescript(sql)
        conn.commit()
    add_application("AA00B7QPGN", "BEJ", "30-Aug-2022")
    # add_record("AA00B7QPGN", "31-Aug-2022", "Refused", "A U.S. consular officer has adjudicated and refused your visa application.  Please see the letter you received at the interview.")
    add_record("AA00B7QPGN", "31-Aug-2022", "Refused", "Wow")
    logger.info(get_all_applications())
    logger.info(get_all_records("AA00B7QPGN"))
