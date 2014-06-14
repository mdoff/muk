import mfunctions, mconfig, os
def receive(line, bot_socket):
  lines = line.split(' ')
  text = mfunctions.user_text(line)
  if(lines[0] == "PING"):
    mfunctions.send("PONG %s\r\n" % lines[1],bot_socket)
    print('PONG '+lines[1])
  if(lines[0] == "KICK"):
    mfunctions.send("JOIN "+mconfig.CHANNEL+"\r\n",bot_socket)
  if(text):
    if(text[1] == "!uptime"):
      mfunctions.say(os.popen('uptime').read(),bot_socket)
    elif(text[1] == "!reg"):
          mfunctions.send("PRIVMSG NickServ : IDENTIFY "+mconfig.PASSWORD+"\r\n",bot_socket)
