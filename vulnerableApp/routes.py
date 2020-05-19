from flask import render_template,make_response,request
import mysql.connector
from mysql.connector import Error
from vulnerableApp import app
@app.route('/')
def cookie():
    if not request.cookies.get('TrackingId'):
        res = make_response("Hi, I am administrator look my password around here!")
        res.set_cookie('TrackingId', 'xTrH78RW01', max_age=60*60*24*365*2)
    else:
     try:
        database=mysql.connector.connect(host='localhost',user='root',passwd='*****',database='VulnerableApp')
        cursor=database.cursor(buffered=True)
        cookie = request.cookies.get('TrackingId')
        cursor.execute("SELECT * FROM cookie Where cookie='{}'".format(cookie))
        check = cursor.fetchall()
        if check:
         res = make_response("Hi, Welcome Back, I am administrator look my password around here!")
        else:
         res = make_response("Hi, I am administrator look my password around here!")
     except Error as e:
        res = make_response("Hi, I am administrator look my password around here!")
     finally:
        if (database.is_connected()):
         database.close()
         cursor.close()
    return res

if __name__ == "__main__":
     app.run(host='0.0.0.0')
