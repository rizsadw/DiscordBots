import discord
import requests

TOKEN = "OTY2NjI1MzQ5NDQ4MzkyNzA0.YmEeAg.2cUYxb43Jveofw3zRNOx1BwhRoE"

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith("!joke"):
        r = requests.get('https://sv443.net/jokeapi/v2/joke/Miscellaneous,Pun,Spooky,Christmas?blacklistFlags=nsfw,racist,sexist&type=single').json()
        joke = r['joke']
        await message.channel.send(joke)

client.run(TOKEN)
