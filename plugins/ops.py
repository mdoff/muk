import mfunctions, mconfig, random

"""
  To perform action as OP send muk a private message in format:
  <action> <password> (<optional>)
  eg: !op qwerty
      !topic qwerty New channel topic
  actions:
    !op   - gives user OP on channel
    !topic  - set channel topic
"""
def receive(line, bot_socket):
  text = mfunctions.user_priv(line)
  if(text):
    if(text[1][:3] == "!op" and len(text[1]) > 4 and text[1][4:] == mconfig.OP_PASSWD):
      mfunctions.send("MODE "+ mconfig.CHANNEL+' +o ' +text[0]+"\r\n", bot_socket)
    if( text[1][:6] == "!topic" and len(text[1]) > 4 and text[1][7:len(mconfig.OP_PASSWD)+7] == mconfig.OP_PASSWD ):
      mline = "TOPIC "+ mconfig.CHANNEL+' :' +text[1][8+len(mconfig.OP_PASSWD):]+"\r\n"
      mfunctions.send(mline, bot_socket)
