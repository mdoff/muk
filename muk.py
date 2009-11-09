import sys,socket,string,os,random,urllib2,datetime,time
from re import findall, DOTALL

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

#tutaj mieszkaja zmienne globalne
s=socket.socket( )
s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
i=0

nic=''
sss=''
day='00'
#day = datetime.datetime.now().strftime("%d")
fname = datetime.datetime.now().strftime("logs/%d-%m-%y.html")
#fukcje bota
print fname
def say(tekst):
    s.send("PRIVMSG "+KANAL+" :"+ tekst +"\r\n")
    file = open(globals()['fname'],"r+")
    while(file.readline()):
        pass
    file.write(time.strftime("%H:%M") +" &lt;<b>" + NICK +"</b>&gt; "+tekst+"<br>\n")
    file.close()
            


def bash():
    u = urllib2.urlopen('http://bash.org.pl/random/')
    q = findall('<div class="quote">(.*?)</div>', u.read(), DOTALL)
    final = q[0].replace('&lt;', '<').replace('&gt;', '>').replace('<br />', '').replace('\n\r','').replace('\t','').replace('\n',' ')
#    final = q[0].replace('<br />', '').replace('\r','').replace('\t','')
   
#    print final
    return final

def ball():
    i = random.randint(0, 19)
    table = ['As I see it, yes','Reply hazy, try again',' Don\'t count on it',' It is certain','Ask again later','My reply is no',' Most likely','Better not tell you now','My sources say no',' Outlook good','Cannot predict now','Outlook not so good','Signs point to yes','Concentrate and ask again',' Very doubtful','Without a doubt','Yes','Yes - definitely','You may rely on it']
    return table[i]

def log(mesg):
    
    try:

        day1 = datetime.datetime.now().strftime("%d")

        if(globals()['day'] == day1):
            file = open(globals()['fname'],"r+")
            while(file.readline()):
                pass
            nick =  mesg.split("!")[0][1:]
            if(mesg.split(' ')[1] == 'PART' or mesg.split(' ')[1] == 'QUIT'):
                file.write(time.strftime("%H:%M -!- <b>") + nick +"</b> [" + mesg.split("!")[1].split(' ')[0] + "] has left <b>" +KANAL +" </b> <br>\n")
            if(mesg.split(' ')[1] == 'JOIN' ):
                file.write(time.strftime("%H:%M -!- <b>") + nick +"</b> [" + mesg.split("!")[1].split(' ')[0] + "] has joined <b>" +KANAL +" </b> <br>\n")

            sa = mesg.split("PRIVMSG "+KANAL)
            file.write(time.strftime("%H:%M") +" &lt;<b>" + nick +"</b>&gt; "+sa[1][2:]+"<br>\n")
#            print time.strftime("%H:%M") +" &lt;<b>" + mesg.split("!")[0][1:]+"</b>&gt; "+sa[1][2:]+"<br>\n"
            file.close()
        else:
            globals()['day'] = datetime.datetime.now().strftime("%d")
            globals()['fname']=datetime.datetime.now().strftime("logs/%d-%m-%y.html")
            file = open(fname,"w")
            sa = mesg.split("PRIVMSG "+KANAL)
            file.write(time.strftime("%H:%M") +" &lt;<b>" + mesg.split("!")[0][1:]+"</b>&gt; "+sa[1][2:]+"<br>\n")
            file.close()
    except:
#        print globals()['day']
        pass


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
#	print nic +' : '+ sss + '\n'
        print string.join(line) +'\n'
        
        log(string.join(line) +'\n')
        
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
            say("muk dodal cycat panie ^^")

	if (sss==' :!ping'):
            say("muk, mu.. ee.. pong! ^^\"")

        if (sss==' :!uptime'):
            say(os.popen('uptime').read())

        if (sss==' :!sru'):
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
            
        if (sss == " :!bash"):
            say(bash())
        
        if (sss[0:5] == " :!8b"):
            if(len(sss) < 8 ):
                   say('What\'s your question?')
            else:
                   say(ball())
        
        ii = 0
        cc = 0
        gg = 0
#        print len(sss)
        while(len(sss) > ii):
            
            if(sss[ii:ii+7]=='http://'):
                cc = ii
                gg = ii
                while((cc < len(sss)) and not(sss[cc] == ' ')):
                          cc = cc+1
                if not(sss[gg:gg+17] == 'http://www.ircnet'):
                    say(urllib2.urlopen('http://api.mrte.ch/go.php?action=shorturl&url='+sss[gg:cc]+'&format=text').read())
                print sss[gg:cc]
            
            ii = ii + 1

