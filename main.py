import pandas
import sqlite3
from pprint import pprint

voter_list = pandas.read_excel('MEC_Voter_Data.xls') #creates an iteratable object of the given excel file
con = sqlite3.connect('Verify_Voters.db') #initializes connection to SQL database
cur = con.cursor() #initializes cursor object to navigate SQL Program 

#Creates table in database, if it doesn't exist already
try:
    cur.execute("CREATE TABLE valid_voters (first_name TINYTEXT, last_name TINYTEXT, party TINYTEXT)")
except sqlite3.OperationalError:
    pass

#Initialization of voting data
valid_voter_dict = {}
valid_parties = ["Socks and Crocs Reform League", "Pineapple Pizza Party", "Pronounced Jiff Union"]
voter_count = 0

#Adds all voters and data into dictionary and SQL database
for row in voter_list.itertuples():
    voter_name = row._1 + " " + row._2
    first_name = row._1.replace("'", "''") #Used to make names readable for SQL
    last_name = row._2.replace("'", "''") #Used to make names readable for SQL
    #Checks conditions for valid voting
    if voter_name not in valid_voter_dict:
        if row.Vote in valid_parties:
            cur.execute(f"INSERT INTO valid_voters VALUES ('{first_name}', '{last_name}', '{row.Vote}');") #Adds to SQL table
            valid_voter_dict[voter_name]=row.Vote
            voter_count += 1

#Creates voter object that is able to vote
class Voter:
    def __init__(self,name):
        self.name = name
    

    def vote_now(self):
        #Check if person already voted
        if self.name in valid_voter_dict:
            print("You have already Voted")
        else:
            print("\n These are your voting options \n (a) Socks and Crocs Reform League, (b) Pineapple Pizza Party, (c) Pronounced Jiff Union \n")
            option = " "
            #Forces user to vote for either a, b, c
            while option not in ["a","b","c"]:
                option = input(" Please choose option a, b or c \n")
                parties = {"a":"Socks and Crocs Reform League","b":"Pineapple Pizza Party","c":"Pronounced Jiff Union"}
                valid_voter_dict[self.name] = parties[option]
                global voter_count 
                voter_count += 1
                

p1 = Voter("Pillie Wai")
p1.vote_now()    


#Neatly displays voter data, organized by alphebetical order
pprint(valid_voter_dict)
print(voter_count)

