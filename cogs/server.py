# server.py

import discord
from discord.ext import commands
import datetime
import sys
from dotenv import load_dotenv
import os
import pymongo
from pymongo import MongoClient
from typing import Optional
from discord.ext.commands import has_permissions, MissingPermissions
from discord import utils, Activity, ActivityType, Client, Embed, Colour
from discord import Member as DiscordMember
from discord.errors import Forbidden
from discord.ext.commands import has_permissions, Bot, Greedy
from discord.ext.commands import BadArgument, CommandNotFound, MissingPermissions

# -- Loading Secret Stuff from .env 
load_dotenv()
CONNECTIONURL = os.getenv('CONNECTION_URL')
VERSION = os.getenv('VERSION')
CONNECTBOT = os.getenv('CONNECT_BOT_URL')

# -- Setting Up for MongoDB --
cluster = MongoClient(CONNECTIONURL)
db = cluster["ServerData"] 
collection = db["ServerData"]


class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # -- Add Cat --
    # @commands.command(name='addcat', help='Add a cat to your library!')
    # async def addcat(self, ctx, name="NULL", clan="NULL", imgURL = "NULL"):
    #     await ctx.send('STILL IN BETA')
    #     pass

    # FIXME

    # @commands.command(name='kick', help='kick somone, must have kick permissions')


def setup(bot):
    bot.add_cog(Server(bot))