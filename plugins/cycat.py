import mfunctions, mconfig
from urllib.request import urlopen
from re import findall, DOTALL
def receive(line, bot_socket):
  text = mfunctions.user_text(line)
  if(text and text[1] == "!cycat"):
    mfunctions.say(cycat(),bot_socket)
  elif(text and text[1][:6] == "!cycat" and len(text[1]) > 12):
    add_cycat(text[1][7:])
    mfunctions.say(mconfig.NICK+" dodał cytata (^.^)",bot_socket)

def cycat():
    u = urlopen('http://quote.mdoff.net/?a=r')
    return u.read().decode('utf-8')

def add_cycat(cycat):
  urlopen('http://quote.mdoff.net/?a=a&b=' + cycat.replace(' ', '%20')).read()
