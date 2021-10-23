
class Voter:
    def __init__(self,name):
        self.name = name
    
    def vote_check(self):
        if self.name in valid_voter_dict:
            print("You have already Voted")

    def vote_now(self):
        print("\n These are your voting options \n (a) Socks and Crocs Reform League, (b) Pineapple Pizza Party, (c) Pronounced Jiff Union \n")
        option = " "
        while option not in ["a","b","c"]:
            option = input(" Please choose option a, b or c \n")
            parties = {"a":"Socks and Crocs Reform League","b":"Pineapple Pizza Party","c":"Pronounced Jiff Union"}
            valid_voter_dict[self.name] = parties[option]

p1 = Voter("Cairo Legge")
p1.vote_check()
p1.vote_now()    