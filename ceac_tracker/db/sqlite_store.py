import sqlite3
from os import path
from ceac_tracker.utils.my_logging import get_logger

logger = get_logger(__file__)
db_root = path.dirname(__file__)

conn = sqlite3.connect(path.join(db_root, "data.db"))
cursor = conn.cursor()


def get_all_applications():
    global cursor
    res = cursor.execute("SELECT application_id, location, case_created, notification_email FROM application")
    return res.fetchall()


def get_all_records(application_id):
    global cursor
    res = cursor.execute("SELECT update_date, status, description FROM history WHERE application_id=? ORDER BY timestamp DESC", (application_id,))
    return res.fetchall()


def add_application(application_id, location, case_created, notification_email):
    global cursor, conn
    res = cursor.execute("INSERT INTO application(application_id, location, case_created, notification_email) VALUES(?, ?, ?, ?)", (application_id, location, case_created, notification_email))
    conn.commit()


def add_record(application_id, update_date, status, description):
    global cursor, conn
    res = cursor.execute(
        "INSERT INTO history(application_id, update_date, status, description) VALUES(?, ?, ?, ?)", (application_id, update_date, status, description)
    )
    conn.commit()


if __name__ == "__main__":
    with open(path.join(db_root, "ddl.sql"), "r") as ddl:
        sql = ddl.read()
        cursor.executescript(sql)
        conn.commit()
    add_application("AA00B7QPGN", "BEJ", "30-Aug-2022", "wlx65005@gmail.com")
    add_application("AA00B7FCP1", "BEJ", "26-Aug-2022", "1200012618yb@gmail.com")
    add_application("AA00B7BKKZ", "BEJ", "26-Aug-2022", "yexuesong@live.com")
    add_application("AA00B5R35V", "BEJ", "18-Aug-2022", "243481102@qq.com")
    # add_record("AA00B7QPGN", "31-Aug-2022", "Refused", "A U.S. consular officer has adjudicated and refused your visa application.  Please see the letter you received at the interview.", "wlx65005@gmail.com")
    # add_record("AA00B7QPGN", "31-Aug-2022", "Refused", "Wow")
    logger.info(get_all_applications())
    logger.info(get_all_records("AA00B7QPGN"))
