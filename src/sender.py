import mysql.connector

DBUrl = "localhost"
DBUser = "root"
DBPass = "root"
DBName = "TarkovMapBot"


dbconnect = mysql.connector.connect(user=DBUser,password=DBPass,host=DBUrl,database=DBName)

cursor = dbconnect.cursor()

def sendAll(bot,message_text):
    cursor.execute("SELECT id FROM UsersID")
    result = cursor.fetchall()
    for id in result:
        print(id)
        fid = id[0]
        bot.send_message(fid, message_text)
        dbconnect.commit()


def sendAllPhoto(bot,message_text):
    cursor.execute("SELECT id FROM UsersID")
    result = cursor.fetchall()
    for id in result:
        nph = open('newsphoto.png', 'rb')
        print(id)
        fid = id[0]
        bot.send_photo(int(fid),nph,caption=message_text)
        dbconnect.commit()
        nph.close()