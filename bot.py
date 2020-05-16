# bot.py

# -- General Setup --
import os
import random
from dotenv import load_dotenv
from discord.ext import commands
import discord
import pymongo
from pymongo import MongoClient
import time
Verbose = False
Version = '0.1a'
# -- Command Based Imports
from resourceScripts.ships import *
from resourceScripts.pickname import *


# -- Loading Secret Stuff from .env 
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CONNECTIONURL = os.getenv('CONNECTION_URL')

# -- Setting Up for MongoDB
cluster = MongoClient(CONNECTIONURL)
db = cluster["UserData"]
collection = db["UserData"]

# -- Setting Up Bot Stuff --
bot = commands.Bot(command_prefix='$')
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord! [ID:{0}]'.format(bot.user.id))

# -- Track Messages --
@bot.event
async def on_message(ctx):
    if(ctx.author == bot.user): # make sure its not the bot doing stuff!
        return
    await bot.process_commands(ctx)
    if Verbose: print('Message by {0} ID: {1}'.format(ctx.author, ctx.author.id)) # Debug


    myQuery = { "_id": ctx.author.id }
    if (collection.count_documents(myQuery) == 0):
        post = {"_id": ctx.author.id, 
                "score": 1, 
                "xp": 5}
        collection.insert_one(post)
        await ctx.channel.send('`Congratulations! You sent your first message! Use $xp to see how much experience you have on the server!`')
        
    else:
        query = {"_id": ctx.author.id}
        user = collection.find(query)
        for result in user:
            score = result["score"]
        score = score + 1
        collection.update_one({"_id":ctx.author.id}, {"$set":{"score":score}})

        query2 = {"_id": ctx.author.id}
        user2 = collection.find(query2)
        for result in user2:
            xp = result["xp"]
        z1 = random.randint(1, 5)
        xp = xp + z1
        collection.update_one({"_id":ctx.author.id}, {"$set":{"xp":xp}})
        '''
        /////////    //////////   //////////
        //           //  //  //            //
        //           //  //  //            //
        //           //      //            //
        /////////    //      //   //////////
        '''

# -- Test Command --
@bot.command(name='test', help='Prints test message [Development Tool]')
async def test(ctx):
    await ctx.send("`>> Test Successful!`")


# -- Roll Dice --
@bot.command(name='dice', help='Rolls a Dice, and Returns Value!')
async def test(ctx):
    value = random.randint(1, 6)
    starters = [
        'You Rolled a',
        'And the dice hit',
        'Looks like its a',
        'Finally! a',
        'Unfortunately a',
        'You got a',
    ]
    starter = random.randint(0, len(starters) - 1)
    await ctx.send("```{0} {1}!```".format(starters[starter], value))


# -- Find ID [DEVELOPER] --
@bot.command(name='myID', help='Returns User ID [Development Tool]')
async def test(ctx):
    id = ctx.author.id
    await ctx.send("`>> Your ID is {0}`".format(id))


# -- 8 Ball --
eightBallResponse = [ 'As I see it, yes.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Don’t count on it.', 'It is certain.', 'It is decidedly so.', 'Most likely.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.', 'Very doubtful.', 'Without a doubt.', 'Yes.', 'Yes – definitely.', 'You may rely on it.', ]

@bot.command(name='8ball', help='8ball! What else do you need??')
async def test(ctx):
    eightBallNum = random.randint(0, len(eightBallResponse) - 1)
    await ctx.send("```{0}```".format(eightBallResponse[eightBallNum]))


# -- Get Messages Sent --
@bot.command(name='xp', help='Prints XP')
async def test(ctx):
    myQuery = {"_id" : ctx.author.id} 
    messagesSent = collection.find(myQuery)
    # new generator with messages sent.
    for x in messagesSent:
        operatorValue = x
    # now operatorValue has the value needed!
    a = str(operatorValue)
    y = a.split(':') 

    z = y[-1].split('}')
    xp = z[0].strip()
    
    f = y[-2].split(',')
    score = f[0]
    

    # Score FINALLY done!
    await ctx.send("```** Here are your Stats! ** \n| User: {0} \n| Messages Sent: {1} \n| XP: {2}```".format(ctx.author, score, xp, ))

# -- Credits --
@bot.command(name='credits', help='Prints bot credits')
async def test(ctx):
    await ctx.send("`~~~~~~~ Cinderpaw, by Shad0w7#0320 ~~~~~~~`")


# -- Random Stuff --
@bot.command(name='ping', help='Pong')
async def test(ctx):
    await ctx.send("pong :ping_pong:")

@bot.command(name='pong', help='Ping')
async def test(ctx):
    await ctx.send("That's my line!!")

@bot.command(name='version', help='Prints Version of Cinderpaw Bot Running! [Development Tools]')
async def test(ctx):
    await ctx.send('`>> Version: {0}`'.format(Version))
# -- Ships <3 <3!!!! --

@bot.command(name='ship', help='Do a ship, with the two names together and a "*" between them (Use Full Name). Example, $ship Firestar*Sandstorm')
async def test(ctx, arg):
    shipValue = ship(arg.split('*')[0], arg.split('*')[1])
    await ctx.send(":heartpulse: :heartpulse: {0} x {1} is {2}%!!! :heartpulse: :heartpulse:".format(arg.split('*')[0], arg.split('*')[1], shipValue))

# -- Names --

@bot.command(name='warriorname', help='Generate a Warrior Name!')
async def test(ctx):
    await ctx.send(warriorName())

@bot.command(name='clanname', help='Generate a Clan Name!')
async def test(ctx):
    await ctx.send(clanName())

@bot.command(name='kittyname', help='Generate a Kittypet Name!')
async def test(ctx):
    await ctx.send(kittypetName())

# -- Exception Handling --

@bot.event
async def on_command_error(error, ctx, *args, **kwargs):
    if isinstance(error, commands.BadArgument):
        await ctx.send("No Such Command, use $help to view all available commands")

# -- Run With Token --
bot.run(TOKEN)