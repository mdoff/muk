import mfunctions, mconfig, random
def receive(line, bot_socket):
  text = mfunctions.user_text(line)
  if(text):
    if(text[1][:5] == "!slap" and len(text[1]) > 6 and text[1][6:] != mconfig.NICK):
      mfunctions.say("\x01ACTION "+slap(text[1][6:])+"\x01", bot_socket)

def slap(nick):
    plik = open("plugins/slap","r")
    tbl = plik.read()
    tbl = tbl.split('\n')
    tbl = tbl[0:len(tbl)-1]
    ran = random.randint(0,len(tbl)-1)
    return tbl[ran].replace('nick',nick)

