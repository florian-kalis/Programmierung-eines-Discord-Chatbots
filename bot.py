import discord
from discord.ext import commands
import datetime
import stats
from stats import stats
from stats import operators
from weather import weather

today = datetime.date.today()
client = discord.Client()
bot = commands.Bot(command_prefix="|")

#start up
@client.event
async def on_ready():
    print(f'{client.user.name} connected successfully')

#react to messages
@client.event
async def on_message(message):

    operatorInput = str()
    usernameInput = str()
    overview = ("Available commands:" + "\n"
                + "!datum" + " "*2 + "-" + " "*2 + "get current date" + "\n" 
                + "!wetter" + " "*2 + "-" + " "*2 + "get current weather" + "\n" 
                + "!stats + username" + " "*2 + "-" + " "*2 + "get stats for specified username" + "\n" 
                + "!operators + username" + " "*2 + "-" + " "*2 + "get operator stats for specified username" + "\n")

    if message.content.startswith("!stats "):
        usernameInput = (message.content.split()[1])
    elif message.content.startswith("!operators "):
        operatorInput = (message.content.split()[1])

    if message.author == client.user:
        return
    if message.content == "!help":
        await message.channel.send(overview)
    if message.content == "!hallo":
        await message.channel.send('Hallo!')
        return
    if message.content == "!datum":
        await message.channel.send('Datum: ' + str(today))
        return
    if message.content == "!wetter":
        await message.channel.send(weather())
        return
    if message.content == "!stats " + usernameInput:
        await message.channel.send(stats(usernameInput))
        return
    if message.content == "!operators " + operatorInput:
        await message.channel.send(operators(operatorInput))
        return

client.run("")
