import datetime
 
current_date = datetime.date.today().isoformat()

def writeLog(log_text):
    current_date = datetime.date.today().isoformat() 
    current_time = datetime.datetime.now().time()
    file = open(current_date,"w", encoding='utf-8')
    file.write(str(current_time) + " - " + log_text + "\n")
    file.close()

