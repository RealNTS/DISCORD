import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

import random

bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")

botans = ["Hi!! This is 1st assistant, Sonbot2", "Good Morning Sir, I'm Sonbot2", "Hello, Sonbot2 here, Nice to meet you!!"]

dice = ["1","2","3","4","5","6"]

rps = ["✊Rock!!","🖐️Paper","✌️Scissor"]

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Son Bot Num1", url="http://www.twitch.tv/accountname"))
    print('My Ready is Body')


@bot.listen()
async def on_message(message):
    if "stutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('Some Command:')
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):        
    if "shello" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send(random.choice(botans))
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):        
    if "scat" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send("😺")
@bot.listen()
async def on_message(message):        
    if "sdice" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send(random.choice(dice))
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):        
    if "srps" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send(random.choice(rps))
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):        
    if "em an com chua" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send("Em chua 😒")
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):        
    if "srelationship" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send("Like my boss, I'm alone in every universes 😐")
        await bot.process_commands(message)
@bot.listen()
async def on_message(message):        
    if "syourboss" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send("Nguyen Thai Son | FB: https://www.facebook.com/thsonn0808/")
        await bot.process_commands(message)






bot.run('OTc4NTc4MDQ3MjMyMDE2NDI0.Gxxswo.08PwNAX6d1Kyaz3GiT6KLTBQ7TPdQHsqK-JLiU')