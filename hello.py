# an object of WSGI application
import sys
from flask import Flask,render_template,request
from flask_cors import CORS, cross_origin
import psycopg2
import json


app = Flask(__name__) # Flask constructor

CORS(app)

@app.route("/welcome")
def index():
    return render_template('index.html')

@app.route('/answer/<keyword>', methods=['GET'])
def hello(keyword):
	print(keyword)
	return pgSqlData(keyword)

def connectionDb():
	conn = psycopg2.connect(database='ANSWER_DB', user='postgres',password='admin', host='localhost',port='5432')
	return conn

def pgSqlData(quest):

	conn = connectionDb()
	print("Opened database successfully")
	#quest ='what is your name'
	cur = conn.cursor()
	cur.execute("select answer from ANSWER_TABLE where question = "+"'"+quest+"'")
	rows = cur.fetchall()
	for row in rows:
    		answer = row
	conn.commit()
	conn.close()
	json_output = json.dumps(answer)
	return json_output  


if __name__=='__main__':
	app.run()
