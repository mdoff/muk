import mconfig, re

def say(line, bot_socket):
  send = "PRIVMSG "+mconfig.CHANNEL+" :"+ line +"\r\n"
  bot_socket.send(send.encode('utf-8'))

def send(line, bot_socket):
  send = line
  bot_socket.send(send.encode('utf-8'))

def user_text(line):
  lines = line.split(' ')
  if(len(lines) > 2 and lines[1] == 'PRIVMSG'):
    msg = re.match('^:(.*?)!.*? PRIVMSG '+mconfig.CHANNEL+' :(.*)$', line)
    return [msg.group(1),msg.group(2)]
  else:
    return False

def user_nick(line):
  msg = re.match('^:(.*?)!.*?@.*? ', line)
  if(msg):
    return msg.group(1)
  else:
    return False
