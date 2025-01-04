
def qreader(qeastparent , questname):
        questpath = "quests/" + qeastparent + "/" + questname + ".txt"
        with open(questpath, "r", encoding='utf-8') as file:
            return file.read()

def news():
        filepath = "newsfile.txt"
        with open(filepath, "r") as file:
            return file.read()   