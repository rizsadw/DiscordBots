import discord

TOKEN = "OTY2NjI1MzQ5NDQ4MzkyNzA0.YmEeAg.2cUYxb43Jveofw3zRNOx1BwhRoE"

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is now online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello there!')

client.run(TOKEN)
