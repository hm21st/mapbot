import discord
from discord.ext import commands
import random
import asyncio

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="TAKE A MAP! .info"))
    print('Online')

@client.command()
async def info(info):
    embed = discord.Embed(title="Help with Map Bot", description=".crow = Shows a crow and some creepy text\n\n.outh = outh\n\n.ping = Pong!\n\n_Everything here developed by hm21st <3_", color=0xFFFF00)
    await info.channel.send(embed=embed)

@client.command()
async def ping(ping):
        embed = discord.Embed(title="Pong! :ping_pong:", description=f"`{round(client.latency * 1000)} ms`", color=0xFFFF00)
        embed.set_image(url="https://i.ytimg.com/vi/P22YWwsaIu0/mqdefault.jpg")
        await ping.channel.send(embed=embed)

@client.command()
async def crow(crow):
        embed = discord.Embed(description="Crow watches over you.", color=0xFFFF00)
        embed.set_image(url="https://ichef.bbci.co.uk/news/640/cpsprodpb/AFE8/production/_96723054_0d6ac4ea-ab1b-4700-ada9-4632cbea4908.jpg")
        await crow.channel.send(embed=embed)

@client.command()
async def outh(outh):
    embed = discord.Embed(color=0xFFFF00)
    embed.set_image(url='https://media.discordapp.net/attachments/900059287919931412/925862435859099668/IMG_6659.png')
    await outh.channel.send(embed=embed)

client.run('IDgoeshere')


#Developed by hm21st <3
