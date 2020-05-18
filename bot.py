# bot.py

# CREATED BY SHAD0W7#0320
# COPYRIGHT 2020 SHAD0W7#0320 SEE LICENCE FOR MORE INFO

# -- General Setup --
import os
import random
from dotenv import load_dotenv
import json
import re
import traceback
import datetime
import time
# discord
from discord.ext import commands
import discord
# pymongo
import pymongo
from pymongo import MongoClient
#wikipedia
import wikipedia
# external files
from resourceScripts.ships import *
from resourceScripts.pickname import *
from resourceScripts.randomCat import *

Verbose = False

# -- Loading Secret Stuff from .env 
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CONNECTIONURL = os.getenv('CONNECTION_URL')
VERSION = os.getenv('VERSION')
CONNECTBOT = os.getenv('CONNECT_BOT_URL')

Version = str(VERSION)

# -- Setting Up for MongoDB --
cluster = MongoClient(CONNECTIONURL)
db = cluster["UserData"] 
collection = db["UserData"]
'''
If you are using a local storage system like dotENV JSON or XML, then replace this, use the builtin data.json file for JSON.
'''

# -- Setting Up Bot Stuff --
bot = commands.Bot(command_prefix='$')
@bot.event
async def on_ready():
    print('{0} has connected to Discord! [ID:{1}]'.format(bot.user.name, bot.user.id))

# -- Track Messages [XP] --
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
                "xp": 5,
                "name": ctx.author,}
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
    
    await ctx.send("```** Here are your Stats! ** \n| User: {0} \n| Messages Sent: {1} \n| XP: {2}```".format(ctx.author, score, xp, ))



# External Imports

# -- [DEVELOPER] --
bot.load_extension("cogs.developer")

# -- Random Stuff --
bot.load_extension("cogs.random")

# -- Warriors --
bot.load_extension("cogs.warriors")


# -- Exception Handling --

@bot.event
async def on_command_error(error, ctx, *args, **kwargs):
    if isinstance(error, commands.BadArgument):
        await ctx.send("No Such Command, use $help to view all available commands")


@bot.event
async def on_error(event, *args, **kwargs):
    message = args[0] #Gets the message object
    #send the message to the channel

# -- Run With Token --
bot.run(TOKEN)