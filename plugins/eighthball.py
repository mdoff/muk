import mfunctions, random

def ball():
    i = random.randint(0, 18)
    table = ['As I see it, yes','Reply hazy, try again',' Don\'t count on it',' It is certain','Ask again later','My reply is no',' Most likely','Better not tell you now','My sources say no',' Outlook good','Cannot predict now','Outlook not so good','Signs point to yes','Concentrate and ask again',' Very doubtful','Without a doubt','Yes','Yes - definitely','You may rely on it']
    return table[i]

def receive(line, bot_socket):
  text = mfunctions.user_text(line)
  if(text):
    if(text[1][:3] == "!8b" and len(text[1]) > 8):
      mfunctions.say(ball(), bot_socket)
    elif(text[1][:3] == "!8b"):
      mfunctions.say('What\'s your question?', bot_socket)
