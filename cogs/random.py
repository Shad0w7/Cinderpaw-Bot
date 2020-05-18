# random.py

import discord
from discord.ext import commands
import datetime
import random
import os
import wikipedia
CONNECTBOT = os.getenv('CONNECT_BOT_URL')
eightBallResponse = [ 'As I see it, yes.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Don’t count on it.', 'It is certain.', 'It is decidedly so.', 'Most likely.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.', 'Very doubtful.', 'Without a doubt.', 'Yes.', 'Yes – definitely.', 'You may rely on it.', ]
class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command(name='ping', help='Pong')
    async def ping(self, ctx):
        await ctx.send("pong :ping_pong:")
        pass


    @commands.command(name='pong', help='Ping')
    async def pong(self, ctx):
        await ctx.send("That's my line!!")
        pass


    @commands.command(name='fuck', help='ur mean')
    async def fBomb(self, ctx):
        await ctx.send("Thats not very nice! Here's some mousebile go do the elder's ticks!")
        pass


    @commands.command(name='shit', help='ur mean')
    async def shit(self, ctx):
        await ctx.send("Thats not very nice! Here's some mousebile go do the elder's ticks!")
        pass


    @commands.command(name='<3', help='I wuv u too!')
    async def heartlove(self, ctx):
        await ctx.send(":heart_decoration:  I love Fireheart, but you aren't bad either :heart_decoration: ")
        pass


    @commands.command(name='hate', help='I hate her so much')
    async def hate(self, ctx):
        await ctx.send(":frowning2: I hate Sandstorm ugh I wish Fireheart were mine.")
        pass


    @commands.command(name='dice', help='Rolls a Dice, and Returns Value!')
    async def dice(self, ctx):
        value = random.randint(1, 6)
        starters = [ 'You Rolled a', 'And the dice hit', 'Looks like its a', 'Finally! a', 'Unfortunately a', 'You got a',]
        starter = random.randint(0, len(starters) - 1)
        await ctx.send("```{0} {1}!```".format(starters[starter], value))
        pass


    @commands.command(name='credits', help='Prints bot credits')
    async def credits(self, ctx):
        await ctx.send("`~~~~~~~ Cinderpaw, by Shad0w7#0320 ~~~~~~~`")
        pass


    @commands.command(name='invite', help='Gives you the link to invite Cinderpaw to your server')
    async def invite(self, ctx):
        await ctx.send('Make sure you have the "manage server" permission on the server you are trying to target, and then paste this link into your browser. ```{}```'.format(CONNECTBOT))
        pass


    @commands.command(name='wiki', help='return wikipedia listing for search term.')
    async def wiki(self, ctx, args):
        try:
            z = wikipedia.summary(args)
        except: 
            l = wikipedia.suggest(args)
            z = "Did you mean {} Please be more specific!".format(l)
        await ctx.send('```{0}```'.format(z))
        pass


    @commands.command(name='8ball', help='8ball! What else do you need??')
    async def eightball(self, ctx):
        eightBallNum = random.randint(0, len(eightBallResponse) - 1)
        await ctx.send("```{0}```".format(eightBallResponse[eightBallNum]))
        pass

def setup(bot):
    bot.add_cog(Random(bot))