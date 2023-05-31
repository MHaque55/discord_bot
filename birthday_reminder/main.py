import discord
import datetime
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = discord.Client(intents=intents)
TOKEN = 'MTExMzEzMTY2NDQyMDM5MzAxMA.Ges2Nz.WRgvJta4FCc-cuBqTFG4xyYJqGzh4U118tHT7k'

@bot.event
async def on_ready():
    members = []
    guild_ct = 0
    for guild in bot.guilds:
        print(f'- {guild.id} (name: {guild.name})')
        guild_ct += 1

    for member in guild.members:
        print(f'the member: {member}')
        print()

    print(f'{bot.user} is now running and in {guild_ct} guilds')

@bot.event
async def on_message(msg):
    if msg.content == "hello":
        await msg.channel.send("hey bro")


bot.run(TOKEN)
