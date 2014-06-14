import os, socket, mconfig
import glob
import importlib.machinery

HOST=mconfig.HOST
PORT=mconfig.PORT
NICK=mconfig.NICK
IDENT=mconfig.IDENT
REALNAME=mconfig.REALNAME
CHANNEL = mconfig.CHANNEL
PASSWORD = mconfig.PASSWORD

readbuffer=b''

def connect():
  s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
  s.connect((HOST, PORT))
  send = "NICK "+NICK+"\r\n"
  s.send(send.encode())
  send = "USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME)
  s.send(send.encode())
  return s

def load_plugins():
  plugins = []
  plugin_files = glob.glob(os.path.dirname(__file__)+"plugins/*.py")
  plug_files = [ os.path.basename(f)[:-3] for f in plugin_files]
  plugins = []
  for p in plug_files:
    try:
      loader = importlib.machinery.SourceFileLoader(p, "plugins/"+p+".py")
      foo = loader.load_module()
      plugins.append(foo)
    except:
      print("ERROR in module: "+p)
  return plugins

plugins = load_plugins()
bot_socket = connect()

i = 0
while 1:
  readbuffer=bot_socket.recv(2048)
  buffer2 = readbuffer.decode("utf-8")
  temp=buffer2.split("\r\n")
  a=3
  for line in temp:
    if(i<100):
      i=i+1
    if (i==40):
      send = "JOIN "+CHANNEL+"\r\n"
      bot_socket.send(send.encode("utf-8"))
    print(line)
    for plug in plugins:
      try:
        plug.receive(line, bot_socket)
      except:
        print('ERROR in running plugins')
