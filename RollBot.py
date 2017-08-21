import discord
from discord.ext import commands

des = 'Le meilleur des bots de test dans ton jardin'

prefix = '!'

client = commands.Bot(description=des, command_prefix=prefix)

@client.event
async def on_ready():
    print('It works')


@client.command(pass_context=True)
async def roll(ctx):
    await client.say('Alea jacta est !')


client.run('MzQ5MTI0MTY3MjI1OTY2NTk0.DHw6uw.TXQVt88gfSLA9MEjngHPtyGqTfg')