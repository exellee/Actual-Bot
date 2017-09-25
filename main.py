import traceback
import discord
import logging
import asyncio as asyncio
from discord import Game
from discord.ext import commands
import tokenfile

bot = commands.Bot(command_prefix=".")


logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='botlog.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@bot.event
async def on_ready():
    for s in bot.servers:
        print("Logged into: ""%s, as %s" % (s.name, bot.user.name))
        print("What can I do for you Tanu?")
        print("____________________________")

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

@bot.command()
async def test():
    await bot.say("Am I working? Hmmm...")

@bot.command()
async def echo(*, echo: str):
    await bot.say(":mega: " + echo)

@bot.command()
async def ping():
    await bot.say("Pong!")


bot.run(tokenfile.TOKEN)

