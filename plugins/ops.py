import mfunctions, mconfig, random
def receive(line, bot_socket):
  text = mfunctions.user_priv(line)
  if(text):
    if(text[1][:3] == "!op" and len(text[1]) > 4 and text[1][4:] == mconfig.OP_PASSWD):
      mfunctions.send("MODE "+ mconfig.CHANNEL+' +o ' +text[0]+"\r\n", bot_socket)
