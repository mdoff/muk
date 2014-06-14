import mfunctions
from urllib.request import urlopen
from re import findall, DOTALL
def receive(line, bot_socket):
  text = mfunctions.user_text(line)
  if(text and text[1] == "!bash"):
    t = bash()
    t = t.split('\n')
    for a in t:
      mfunctions.say(a,bot_socket)

def bash():
    u = urlopen('http://bash.org.pl/random/')
    q = findall('<div class="quote post-content post-body">(.*?)</div>', u.read().decode('utf-8'), DOTALL)
    final = q[0].replace('&lt;', '<').replace('&gt;', '>').replace('<br />', '').replace('\r','').replace('\t','').replace('&quot;','"')
    return final
