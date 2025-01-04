def breader(bossname):
        bosspath = "bosses/" + bossname + ".txt"
        with open(bosspath, "r", encoding='utf-8') as file:
            return file.read()