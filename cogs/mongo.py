# mongo.py

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
Verbose = True
CONNECTIONURL = os.getenv('CONNECTION_URL')
cluster = MongoClient(CONNECTIONURL)
db = cluster["UserData"] 
collection = db["UserData"]



class Mongo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, ctx):
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
            pass
    

def setup(bot):
    bot.add_cog(Mongo(bot))
