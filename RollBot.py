import discord
from discord.ext import commands

import asyncio

import random
import time
import datetime
import calendar



def RandomBetween(x,y):
    randl = []
    for i in range(x,y+1):
        randl.append(i)
    random.shuffle(randl)
    return randl[0]


def IsANumber(c):
    return True if (48 <= ord(c) <= 57) else False

def RollToList(text, rollList):
    #print(rollList, '.'+text)
    if text[0] == ' ':
        if len(text) == 1:
            return rollList
        else:
            return RollToList(text[1:], rollList)
    elif IsANumber(text[0]):
        i = 0
        nb = ''
        while True:
            if len(text) == i:
                rollList.append(nb)
                return rollList
            if IsANumber(text[i]):
                nb += text[i]
            elif text[i] == 'd':
                if len(text) == i+1:
                    return 1
                elif not IsANumber(text[i+1]):
                    return 1
                else:
                    nb += 'd'
                    i+=1
                    while True:
                        if len(text) == i:
                            rollList.append(nb)
                            return rollList
                        if IsANumber(text[i]):
                            nb += text[i]
                        else:
                            rollList.append(nb)
                            return RollToList(text[i:], rollList)
                        i+=1
            else:
                rollList.append(nb)
                return RollToList(text[i:], rollList)
            i+=1
    elif text[0] == '(' or text[0] == ')' or text[0] == '+' or text[0] == '-' or text[0] == '*' or text[0] == '/':
        rollList.append(text[0])
        if len(text) == 1:
            return rollList
        else:
            return RollToList(text[1:], rollList)
    else:
        return 1



def RollAnalyse(rList):
    prevIsNb = False
    nbParenthesis = 0
    for i in range(len(rList)):
        if rList[i].isdigit() or 'd' in rList[i]:
            if prevIsNb:
                return 1
            prevIsNb = True
        elif rList[i] == '+' or rList[i] == '-' or rList[i] == '*' or rList[i] == '/':
            if not prevIsNb or i+1 == len(rList):
                return 1
            prevIsNb = False
        elif rList[i] == '(':
            if prevIsNb:
                return 1
            prevIsNb = False
            nbParenthesis += 1
        elif rList[i] == ')':
            if not prevIsNb:
                return 1
            prevIsNb = True
            nbParenthesis -= 1
            if nbParenthesis < 0:
                return 1


    if nbParenthesis != 0:
        return 1

    return 0




def Roll(text):
    rollList = []
    rollList = RollToList(text, rollList)
    if rollList == 1:
        return 'Bad syntax.', 'error'

    if RollAnalyse(rollList) == 1:
        return 'Bad formula.', 'error'

    rollRes = ''
    rollMsg = ''

    for e in rollList:
        if 'd' in e:
            index = e.index('d')
            rollRes += '('
            rollMsg += '('
            for i in range(int(e[:index])):
                rand = RandomBetween(1, int(e[index+1:]))
                rollRes += str(rand) +'+'
                rollMsg += " **|" + str(rand) +"|** :game_die:*" + e[index+1:] + '* +'
            rollRes = rollRes[:-1]
            rollMsg = rollMsg[:-1]
            rollRes += ')'
            rollMsg += ')'
        else:
            rollRes += e
            if e == '*':
                rollMsg += '\\*'
            else:
                rollMsg += e

    return rollMsg, str(eval(rollRes))




des = 'Le meilleur des bots de JDR dans ton jardin'

prefix = ''

client = commands.Bot(description=des, command_prefix=prefix)



@client.event
async def on_ready():
    print('The die will be rolled')
    client.loop.create_task(timer())




@client.event
async def on_message(message):
    if message.author == client.user and not message.content.startswith('!'):
        return

    msg = message.content.lower()


    if msg.startswith('!ping'):
        await client.send_message(message.channel, 'pong')


    if msg.startswith('!r'):
        if len(msg)<3:
            await client.send_message(message.channel, 'Roll something !')
        else:
            text = msg[2:]
            retourMsg, retour = Roll(text)
            if retour != 'error':
                await client.send_message(message.channel, '<@' + str(
                    message.author.id) + '> rolled :\n' + retourMsg + "\n\n**= " + retour + "**")
            else:
                await client.send_message(message.channel, '<@' + str(
                    message.author.id) + '> Error : ' + retourMsg)






async def timer():
    while not client.is_closed:
        await asyncio.sleep(60)
        if datetime.date.today().isoweekday() == 7 and datetime.datetime.now().hour == 10 and datetime.datetime.now().minute == 0:
            l1 =list(client.servers)
            for e in l1:
                l2 =list(e.channels)
                x=0
                while str(l2[x].id) != '231128267485085706' and str(l2[x].id) != '348154317464928267':
                    x+=1
                if str(l2[x].id) == '231128267485085706':
                    rand = random.randint(1, 5)
                    if rand == 1:
                        await client.send_message(l2[x], '@everyone On est dimanche, balancez les dispos de la semaine !')
                    elif rand == 2:
                        await client.send_message(l2[x], "@everyone Soon une session de JDR ? Balancez les dispos de la semaine !")
                    elif rand == 3:
                        await client.send_message(l2[x], "@everyone C'est l'heure d'organiser la prochaine session ! Balancez les dispos de la semaine !")
                    elif rand == 4:
                        await client.send_message(l2[x], "@everyone Le dimanche, c'est l'organisation du JDR. Balancez les dispos de la semaine !")
                    else:
                        await client.send_message(l2[x], "@everyone Dimanche ! Balancez les dispos de la semaine ! :heart: ")


        if datetime.datetime.now().hour == 15 and datetime.datetime.now().minute == 30:
        #if datetime.datetime.now().hour == 22 and datetime.datetime.now().minute == 47:
            l1 =list(client.servers)
            for e in l1:
                l2 =list(e.channels)
                x=0
                while str(l2[x].id) != '351819412950482955' and str(l2[x].id) != '348154317464928267':
                    x+=1
                if str(l2[x].id) == '351819412950482955':
                #if str(l2[x].id) == '348154317464928267':
                    await client.send_message(l2[x], '<@252399214028390400> Il est 17h30, profite ! ;)')
                    dejavu = []
                    i = 3
                    while i != 0:
                        rand = random.randint(1, 15)
                        if rand == 1 and not rand in dejavu:
                            await client.send_message(l2[x], 'https://giphy.com/gifs/cats-bukkate-rX9brH8mRTCNO')
                            dejavu.append(rand)
                            i -= 1
                        elif rand == 2 and not rand in dejavu:
                            await client.send_message(l2[x], "https://giphy.com/gifs/cat-RWCWxfLy8ZkBy")
                            dejavu.append(rand)
                            i -= 1
                        elif rand == 3 and not rand in dejavu:
                            await client.send_message(l2[x], "https://giphy.com/gifs/cat-13oMMCI9JVtmdW")
                            dejavu.append(rand)
                            i -= 1
                        elif rand == 4 and not rand in dejavu:
                            await client.send_message(l2[x], "https://giphy.com/gifs/cat-door-ZXc21cfsCB5Ty")
                            dejavu.append(rand)
                            i -= 1
                        elif rand == 5 and not rand in dejavu:
                            await client.send_message(l2[x], "https://giphy.com/gifs/cat-bobi-gdb5ZAU9DASVG")
                            dejavu.append(rand)
                            i -= 1
                        elif rand == 6 and not rand in dejavu:
                            await client.send_message(l2[x], "https://giphy.com/gifs/cat-tMgR6zWCY1tDy")
                            dejavu.append(rand)
                            i -= 1
                        elif rand == 7 and not rand in dejavu:
                            await client.send_message(l2[x], "https://giphy.com/gifs/tXH8ljWiohVi8")
                            dejavu.append(rand)
                            i -= 1
                        elif rand == 8 and not rand in dejavu:
                            await client.send_message(l2[x], "https://giphy.com/gifs/10ThIRwKyYyQWQ")
                            dejavu.append(rand)
                            i -= 1
                        elif rand == 9 and not rand in dejavu:
                            await client.send_message(l2[x], "https://giphy.com/gifs/TJ7hXERD1NmrS")
                            dejavu.append(rand)
                            i -= 1
                        elif rand == 10 and not rand in dejavu:
                            await client.send_message(l2[x], "https://giphy.com/gifs/cat-cute-kitten-kSaOwfjJYtY6A")
                            dejavu.append(rand)
                            i -= 1
                        elif rand == 11 and not rand in dejavu:
                            await client.send_message(l2[x], "https://giphy.com/gifs/kitten-playful-tickles-mPIFo41G2ktFu")
                            dejavu.append(rand)
                            i -= 1
                        elif rand == 12 and not rand in dejavu:
                            await client.send_message(l2[x], "https://giphy.com/gifs/GSrYXzTYQAMCI")
                            dejavu.append(rand)
                            i -= 1
                        elif rand == 13 and not rand in dejavu:
                            await client.send_message(l2[x], "https://giphy.com/gifs/cat-watermelon-fVpfLZs4qMnTO")
                            dejavu.append(rand)
                            i -= 1
                        elif rand == 14 and not rand in dejavu:
                            await client.send_message(l2[x], "https://giphy.com/gifs/cute-kitten-playful-kq52QKDmxKPeM")
                            dejavu.append(rand)
                            i -= 1
                        else:
                            await client.send_message(l2[x], "https://giphy.com/gifs/kitten-playful-USQV0hKcprdeM")
                            dejavu.append(rand)
                            i -= 1
                    dejavu.clear()







#348154317464928267   -> general TestForBot
#231128267485085706   -> organisation JDR
#351819412950482955   -> Detente Axel

"""

async def timer():
    while not client.is_closed:
        await asyncio.sleep(1)
        tt = datetime.datetime.now()
        print(tt)
        if datetime.datetime.now().second == 0:
            l1 =list(client.servers)
            for e in l1:
                l2 =list(e.channels)
                x=0
                while str(l2[x].id) != '348154317464928267':
                    x+=1
                rand = random.randint(1, 5)
                if rand == 1:
                    await client.send_message(l2[x], '@everyone On est dimanche, balancez les dispos de la semaine !')
                elif rand == 2:
                    await client.send_message(l2[x], "@everyone Soon une session de JDR ? Balancez les dispos de la semaine !")
                elif rand == 3:
                    await client.send_message(l2[x], "@everyone C'est l'heure d'organiser la prochaine session ! Balancez les dispos de la semaine !")
                elif rand == 4:
                    await client.send_message(l2[x], "@everyone Le dimanche, c'est l'organisation du JDR. Balancez les dispos de la semaine !")
                else:
                    await client.send_message(l2[x], "@everyone Dimanche ! Balancez les dispos de la semaine ! :heart: ")






"""



client.run('MzQ5MTI0MTY3MjI1OTY2NTk0.DHw6uw.TXQVt88gfSLA9MEjngHPtyGqTfg')
