import sys,socket,string,os,random,urllib2



############################config
HOST="poznan.ircnet.pl"
PORT=6667
NICK="muk-bojowy"
IDENT="mukbot"
REALNAME="MukBot"
readbuffer=""
KANAL = "#testowy"
haslo = ""


############################

s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
i=0

nic=''
sss=''
def say(tekst):
    s.send("PRIVMSG "+KANAL+" :"+ tekst +"\r\n")


while 1:
#nie ruszac: magia :D====================================
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop( )
    
    for line in temp:
	if(i<100):
		i=i+1
        line=string.rstrip(line)
        line=string.split(line)
	sss = ""

	if(len(line) > 3):
		tm=line[0]
		g=1
		nic=''
		while((g>len(tm))or(tm[g]!='!')):
			nic=nic+ tm[g]
			g+=1
			if(g==len(tm)):
				break
		a=3
		while(len(line)!=a):
			sss=sss +' ' + line[a]
			a=a+1
#========================================================
	print nic +' : '+ sss
        if(line[0]=="PING"):
            s.send("PONG %s\r\n" % line[1])
	if (i==40):
		s.send("JOIN "+KANAL+"\r\n")
	if (sss == ' :muk!'):
		say("muk, muk! ^^")
	
        if (sss == ' :!kop'):
		k='KICK '+KANAL+' :'+ nic+'\r\n'
		s.send(k)
		
	if (line[1]=='KICK'):
		s.send("JOIN "+KANAL+"\r\n")
	if (sss == " :!cycat"):
            say(urllib2.urlopen('http://mdoff.110mb.com/quote/?a=r').read())

	if ((sss[0:8] ==" :!cycat") and (len(sss) > 10)):
            urllib2.urlopen('http://mdoff.110mb.com/quote/?a=a&b=' + sss[9:].replace(' ', '%20'))
#		os.system('curl -s "http://mdoff.110mb.com/quote/?a=a&b=' + sss[9:].replace(' ', '%20')+'"')
            say("muk dodal cycat panie ^^")
	if (sss==' :!ping'):
            say("muk, mu.. ee.. pong! ^^\"")

        if (sss==' :!uptime'):
            say(os.popen('uptime').read())
        if (sss==' :!sru'):
           # rul = os.popen('#!/bin/bash \n [ $[ $RANDOM % 6 ] == 0 ] && echo 1 || echo 0').read()
            if (not(random.randint(0, 5))):
                k='KICK '+KANAL+' :'+ nic+'\r\n'
                say("jebut!")
                s.send(k)
            else:
                say("klik...")
        if ( sss==' :muk?'):
            say("muk, muk? >.<")
        if ( sss==' :muk.'):
            say("muk, to brzmi dumnie.")
        if ( sss==' :!reg'):
            s.send("PRIVMSG NickServ : IDENTIFY "+haslo+"\r\n")



