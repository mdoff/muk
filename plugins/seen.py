import mfunctions, random, time, datetime


def receive(line, bot_socket):
  text = mfunctions.user_text(line)
  user = mfunctions.user_nick(line)
  if(text):
    if(text[1][:5] == "!seen" and len(text[1]) > 8):
      mfunctions.say(getSeen(text[1][6:]), bot_socket)
  if(user):
    setSeen(user)


def setSeen(nick):
    plik = open("plugins/seen","r")
    readedFile = plik.read()
    plik.close()
    readedFile = readedFile.split('\n')
    newContent = ""
    added = False
    for line in readedFile:
        i = line.split(';')
        if(i[0] == nick):
            i[1] = str(time.time())
            added = True
        if(len(i) > 1):
            if(len(newContent) > 1):
                newContent = newContent + "\n" + ";".join(i)
            else:
                newContent = ";".join(i)
    if(not added):
        newContent = newContent + "\n" + nick + ";" + str(time.time())
    plik = open("plugins/seen","w")
    plik.write(newContent)
    plik.close()

def timeAgo(timestamp):
    dt1 = datetime.datetime.fromtimestamp(timestamp)
    dt2 = datetime.datetime.fromtimestamp(time.time())
    #rd = dateutil.relativedelta.relativedelta (dt2, dt1)
    rd = dt2 - dt1
    r = "last seen "
    g = False
    seconds = rd.total_seconds() - (rd.days*3600*24)

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    
    if(rd.days > 0 or g):
        if(rd.days != 1):
            r = r + str(rd.days) + " days "
        else:
            r = r + str(rd.days) + " day "
        g = True
    if(hours > 0 or g):
        if(hours != 1):
            r = r + str(hours) + " hours "
        else:
            r = r + str(hours) + " hour "
        g = True
    if(minutes > 0 or g):
        if(minutes > 0 or g):
            r = r + str(minutes) + " minutes "
        else:
            r = r + str(minutes) + " minute "
        g = True
    if(seconds > 0 or g):
        if(seconds != 1):
            r = r + str(seconds) + " seconds"
        else:
            r = r + str(seconds) + " second"
    return r + " ago"

def getSeen(nick):
    plik = open("plugins/seen","r")
    readedFile = plik.read()
    plik.close()
    readedFile = readedFile.split('\n')
    newContent = ""
    added = False
    for line in readedFile:
        i = line.split(';')
        if(i[0] == nick):
            return timeAgo(float(i[1]))
    return "didn't seen "+nick
