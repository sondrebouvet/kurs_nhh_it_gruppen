import logging
import pandas as pd
from pandas import DataFrame
import json
import azure.functions as func

def read_logs() -> pd.DataFrame:
    """
    Reads logs as a csv file
    Returns:
        Pandas dataframe: logs dataframe
    """
    logs = pd.read_csv('data/logs.csv')
    logs['timestamp'] = pd.to_datetime(logs['timestamp'])
    return logs

def transactions_per_group_last_active_day(df : DataFrame, group_id : int) -> float:
    """
    Returns the transactions incurred in the last day for which there exists transactions for a single group. 
    Args:
        df (Pandas dataframe): logs dataframe
        group_id (int): 

    Returns:
        float: _description_
    """
    group_logs = df.query(f"groupId == {group_id}")
    # Get current hour
    last_active_hour  = group_logs['timestamp'].sort_values(ascending=False).tolist()
    if len(last_active_hour) == 0:
        return 0
    last_active_hour_datetime =  pd.to_datetime(last_active_hour[0].strftime('%Y-%m-%d'))
    group_logs_current = group_logs[group_logs['timestamp'] >= last_active_hour_datetime ]
    return group_logs_current['id'].count()


def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Main function. Handles input in body and URL query and returns a valid http response
    """

    logging.info('Python HTTP trigger function processed a request.')
    group_id = req.route_params.get('groupId')
    if  not group_id:
        # We could add a check for whether this is a post or get request
        try:
            # Missing body in post request
            logging.info("No group id in query. Check body")
            req_body = req.get_json()       
            if req.method == "GET":
                return func.HttpResponse("Try again with a post request ", status_code=403)
        except ValueError:
            pass
        else:
            group_id = req_body.get('groupId')

    if group_id:
        logging.info(f"Group id {group_id}")
        logs = read_logs()
        transactions = transactions_per_group_last_active_day(logs, group_id=group_id)
        payload = json.dumps({"data" : str(transactions)})
        return func.HttpResponse(payload, mimetype="application/json")
    else:
        # GroupId is empty
        return func.HttpResponse(
             "Groupid is empty",
             status_code=200
        )
