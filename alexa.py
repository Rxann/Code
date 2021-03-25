import discord
from discord.ext import commands
from discord.ext.commands.core import command
from discord.utils import MAX_ASYNCIO_SECONDS
from prsaw import RandomStuff

client = commands.Bot(command_prefix="<")
rs = RandomStuff(async_mode=True)
@client.event
async def on_ready():
    print("Alexa is online and availible")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("< || The intelligent Ai"))
@client.event
async def on_message(message):
    if client.user == message.author:
        return
    if message.channel.id == 823514397502341160:
        response = await rs.get_ai_response(message.content)
        await message.reply(response)
    await client.process_commands(message)
@client.command()
async def creator(ctx):
    await ctx.send("The creator of alexa is Rxan#8001")
@client.command()
async def version(ctx):
    await ctx.send("alexa is currently on the ver. 1.0")

@client.command()
async def about(ctx):
    await ctx.send("The purpose of alexa is to be your friend and always have someone to talk to.")
client.run("ODI0NzQyMzk1MDY5MzMzNTMz.YFzzNQ.R9bRVo1fq8VYi2DmR2GYny718sE")
