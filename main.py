import mysql.connector as connector
from idlelib import query


class DBHelper:
    def __init__(self):
        self.con = connector.connect(host="localhost",
                                    port="3308",
                                    user="root",
                                    password="Abhi@2136",
                                    database="pythontest")
        query="create table if not exists user(userId int primary key,userName varchar(200),phone varchar(12))"
        cur=self.con.cursor()
        cur.execute(query)
        print("created")

    #INSERT
    def insert_user(self,userid,username,phone):
        query = """insert into user(userId,userName,phone)
        values({},'{}','{}')""".format(
            userid, username, phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")
    
    #fetch all
    def fetch_all(self):
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id : ", row[0])
            print("User Name: ", row[1])
            print("Phone : ", row[2])
            print()
            print()

helper=DBHelper()
# helper.insert_user(96,"DURGESh","23525")
# helper.insert_user(76,"fdbhswgfyhf","23456")
# helper.insert_user(36,"6757676fdhfsdbfh","456")
helper.fetch_all()

