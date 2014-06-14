import mfunctions, re
from urllib.request import urlopen
def receive(line, bot_socket):
  text = mfunctions.user_text(line)
  if(text):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text[1])
    for u in urls:
      if(u[:17] != 'http://www.ircnet'):
        shorten = urlopen('http://to.ly/api.php?longurl='+u).read()
        mfunctions.say(shorten.decode("utf-8"),bot_socket)
