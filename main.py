import pandas

voter_list = pandas.read_excel('MEC_Voter_Data.xls')

valid_voter_list = []
valid_parties = ["Socks and Crocs Reform League", "Pineapple Pizza Party", "Pronounced Jiff Union"]
voter_count = 0

for row in voter_list.itertuples():
    voter_data = [row._1 + " " + row._2, row.Vote]
    if voter_data not in valid_voter_list:
        if voter_data[1] in valid_parties:
            valid_voter_list.append(voter_data)
            voter_count += 1

print(voter_count)

