import pymysql

def connect_db():
    try:
        connection = pymysql.Connect(host='localhost', port=3306, user='root', password='Pracha_ya@12',database='yash_db',charset='utf8')
        print("db connected")
    except:
        print("db connection failed")
    return connection

def disconnect_db(connection):
    try:
        connection.close()
        print("db disconnected")
    except:
        print("Error while disconnecting db")


connection = connect_db()
disconnect_db(connection)
if connection:
    disconnect_db(connection)