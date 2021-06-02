#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database='ANSWER_DB', user='postgres',password='admin', host='localhost',port='5432')
print("Opened database successfully")
quest ='what is your name'
cur = conn.cursor()
cur.execute("select answer from ANSWER_TABLE where question = "+"'"+quest+"'")
rows = cur.fetchall()
for row in rows:
    answer = row
conn.commit()
conn.close()
print(str(answer))