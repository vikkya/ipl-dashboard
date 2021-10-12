from pymongo import MongoClient
# import csv
# from datetime import datetime
# import os
# from dotenv import dotenv_values

# config = dotenv_values(".env")
# username=config("user")
# pwd=config("pwd")

# print(username, pwd)


CONNECTION_STRING = "mongodb+srv://user:pwd@host/dbname?ssl_cert_reqs=CERT_NONE&ssl=true"

client = MongoClient(CONNECTION_STRING)

db = client.get_database()
col = db['match']


# with open("ipldata.csv", "r") as f:
#     csv_content = csv.DictReader(f)
#     for i in csv_content:
#         print(datetime.strptime(i['date'], '%m/%d/%Y'))
#         col.insert_one({"id":i["id"], "date": datetime.strptime(i['date'], '%m/%d/%Y'), "player_of_match": i['player_of_match'], "venue": i['venue'], "team1": i['team1'], "team2": i['team2'], "toss_winner": i['toss_winner'], "toss_decision": i['toss_decision'], "winner": i['winner'], "result": i['result'], "result_margin": i['result_margin'], "umpire1": i['umpire1'], "umpire2" :i['umpire2']})
