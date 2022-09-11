from request import query_status
from sqlite_store import get_all_applications, get_all_records, add_record
import json
from notification import ding_talk_notice
from my_logging import get_logger

logger = get_logger(__file__)


def refresh_once():
    for application_id, location, case_created in get_all_applications():
        res = query_status(location, application_id)
        logger.info(f"Result got! Data = {json.dumps(res, indent=4)}")
        all_records = get_all_records(application_id)
        res_tuple = (res["case_last_updated"], res["status"], res["description"])

        if not all_records or all_records[0] != res_tuple:
            logger.info("Inserting new value!")
            ding_talk_notice(f"New visa status: {res['status']}, desc={res['description']}")
            add_record(application_id, res["case_last_updated"], res["status"], res["description"])
        else:
            logger.info(f"Application {application_id} has no update now.")


if __name__ == "__main__":
    refresh_once()
