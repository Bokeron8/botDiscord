import os

import discord
import random

TOKEN = "NzY0NTcwMDI1MzA2NjE5OTI1.X4ILUw.IRm-8tllAgkvLOCUaykg7M3m8Z4"
SERVER = "Smote"

client = discord.Client()
#Bot connect
@client.event
async def on_ready():
    server = discord.utils.get(client.guilds, name=SERVER)
    print(
        f'{client.user} has connected to Discord!\n'
        f'{server.name}(id: {server.id})'
    )
#Join command?
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
#Frias command
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    friasAns = [
        'Frias es re puto',
        'Frias se la traga'
    ]

    if message.content == '!Frias':
        response = random.choice(friasAns)
        await message.channel.send(response)


client.run(TOKEN)