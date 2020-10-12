import os
import discord
import random
import asyncio
from discord.ext import commands
from animeBot import animeInf
TOKEN = "token"
SERVER = "Smote"

client = commands.Bot(command_prefix="!")
#Bot connect
@client.event
async def on_ready():
    print("Ready")

#anime info
@client.command()
async def inf(ctx, *, title):
    info = animeInf(title)
    await ctx.send(info)

#Frias command
@client.command()
async def Frias(ctx):
    friasAns = [
        'Frias es re puto',
        'Frias se la traga'
    ]
    
    response = random.choice(friasAns)
    await ctx.send(response)

#Dm command
@client.command()
async def msg(ctx):
    await ctx.author.send(f"Re puto {ctx.author}")

client.run(TOKEN)