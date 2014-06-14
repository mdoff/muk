import mfunctions, mconfig, random
def receive(line, bot_socket):
  lines = line.split(' ')
  if(len(lines) > 2 and lines[1] == 'JOIN'):
    nick = mfunctions.user_nick(line)
    if(nick and nick != mconfig.NICK):
      mfunctions.say(witka(nick), bot_socket)

def witka(nick):
    plik = open("plugins/witajka","r")
    tbl = plik.read()
    tbl = tbl.split('\n')
    tbl = tbl[0:len(tbl)-1]
    ran = random.randint(0,len(tbl)-1)
    return tbl[ran].replace('nick',nick)
