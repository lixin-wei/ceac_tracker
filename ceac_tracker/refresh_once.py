from ceac_tracker.request import query_status
from ceac_tracker.db.sqlite_store import get_all_applications, get_all_records, add_record
import json
from ceac_tracker.notifications.email_notification import send_notification
import ceac_tracker.notifications.ding_talk_notification as ding_talk
from ceac_tracker.utils.my_logging import get_logger

logger = get_logger(__file__)


def refresh_once():
    for application_id, location, case_created, notification_email in get_all_applications():
        res = query_status(location, application_id)
        logger.info(f"Result got! Data = {json.dumps(res, indent=4)}")
        all_records = get_all_records(application_id)
        res_tuple = (res["case_last_updated"], res["status"], res["description"])

        if not all_records or all_records[0] != res_tuple:
            logger.info("Inserting new value!")
            msg = f"New visa status for {res['application_num']}: {res['status']}\n\nDescription: {res['description']}\n\nCase last updated: {res['case_last_updated']}"
            send_notification(msg, receiver=notification_email)
            ding_talk.send_notification(msg, notification_email)
            add_record(application_id, res["case_last_updated"], res["status"], res["description"])
        else:
            logger.info(f"Application {application_id} has no update now.")


if __name__ == "__main__":
    refresh_once()
