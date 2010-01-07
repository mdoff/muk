import sys,socket,string,os,random,urllib2,datetime,time
def witajka(nick):
    plik = open("witajka","r")
    tbl = plik.read()
    print tbl
    tbl = tbl.split('\n')
    tbl = tbl[0:len(tbl)-1]
    ran = random.randint(0,len(tbl)-1)
    
    print tbl[ran].replace('nick',nick)


witajka('mdoff')
