import pandas
import sqlite3

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
    if voter_name not in valid_voter_dict:
        if row.Vote in valid_parties:
            valid_voter_dict[voter_name]=row.Vote
            voter_count += 1

print(valid_voter_dict)
print(voter_count)

