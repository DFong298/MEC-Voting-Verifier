import pandas
import sqlite3
from pprint import pprint

voter_list = pandas.read_excel('MEC_Voter_Data.xls')
con = sqlite3.connect('Verify_Voters.db')
cur = con.cursor()

try:
    cur.execute("CREATE TABLE valid_voters (first_name TINYTEXT, last_name TINYTEXT, party TINYTEXT)")
except sqlite3.OperationalError:
    pass

valid_voter_dict = {}
valid_parties = ["Socks and Crocs Reform League", "Pineapple Pizza Party", "Pronounced Jiff Union"]
voter_count = 0

for row in voter_list.itertuples():
    voter_name = row._1 + " " + row._2
    first_name = row._1.replace("'", "''")
    last_name = row._2.replace("'", "''")
    if voter_name not in valid_voter_dict:
        if row.Vote in valid_parties:
            cur.execute(f"INSERT INTO valid_voters VALUES ('{first_name}', '{last_name}', '{row.Vote}');")
            valid_voter_dict[voter_name]=row.Vote
            voter_count += 1

pprint(valid_voter_dict)
print(voter_count)

