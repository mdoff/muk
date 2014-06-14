import mfunctions
def receive(line, bot_socket):
  text = mfunctions.user_text(line)
  if(text):
    if(text[1] == "muk?"):
      mfunctions.say("muk, muk? >.<", bot_socket)
    elif(text[1] == "muk."):
      mfunctions.say("muk, to brzmi dumnie.", bot_socket)
    elif(text[1] == "muk!"):
      mfunctions.say("muk, muk! ^^", bot_socket)
    elif(text[1] == "muk?!"):
      mfunctions.say("mu.. mu.. że muk?!", bot_socket)
    elif(text[1] == "!ping"):
      mfunctions.say("muk, mu.. ee.. pong! ^^\"", bot_socket)
