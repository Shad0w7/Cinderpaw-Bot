# cats.py

import discord
from discord.ext import commands
import datetime
import sys

# -- Loading Secret Stuff from .env 
load_dotenv()
CONNECTIONURL = os.getenv('CONNECTION_URL')
VERSION = os.getenv('VERSION')
CONNECTBOT = os.getenv('CONNECT_BOT_URL')

# -- Setting Up for MongoDB --
cluster = MongoClient(CONNECTIONURL)
db = cluster["UserData"] 
collection = db["UserData"]
# The way Cat Commands Work
'''
CINDERPAW|122S9991Z|happy person ig idek| 
Name
|
Rank (0: kit 1: app 2: war 3: elder 4: leader 5: deputy 6: medcat 7: loner 8: kittypet 9: Rouge)
Fur Color: [36 colors 0-9 a-z] Placeholder 2 for grey
SecondaryColor: [36 colors 0-9 a-z] Placeholder 2 for grey
Pattern: [36 0-9 a-z] Placeholder S for solid [Special Colors (tortie)]

Fighting Strength 0-9
Fighting Speed 0-9
Fighting Skill 0-9
Hunting Ability  0-9

Personality [0-9 a-z] Z for godlike :)

Bio: 500 character limit




'''

class CatCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # -- Add Cat --
    @commands.command(name='addcat', help='Add a cat to your library!')
    async def addcat(self, ctx, name="NULL", clan="NULL", imgURL = "NULL"):
        await ctx.send('STILL IN BETA')
        pass


def setup(bot):
    bot.add_cog(CatCommands(bot))