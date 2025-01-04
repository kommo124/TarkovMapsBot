import mysql.connector

DBUrl = "localhost"
DBUser = "root"
DBPass = "root"
DBName = "TarkovMapBot"


dbconnect = mysql.connector.connect(user=DBUser,password=DBPass,host=DBUrl,database=DBName)

cursor = dbconnect.cursor()

def addUserId(message):
    query = f'INSERT INTO UsersID(id) VALUES ("{message.chat.id}")'
    try:
        cursor.execute(query)
        dbconnect.commit()
    except:
        print('eror')

