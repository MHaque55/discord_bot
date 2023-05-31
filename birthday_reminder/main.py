import discord
import datetime
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

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

    print(f'{bot.user} is now running and in {guild_ct} servers')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    #msg = msg.lower()
    
    print(f'{message.author} said "{message.content}" in {message.channel}')

    if isinstance(message.channel, discord.channel.DMChannel):
        await message.author.send(f'Okay I am a bot and have no clue what are you on. But I gotcha you said {message.content}')

    elif (str(message.channel) == "just-for-bot-testing"):
        #print(f'the type of channel {type(message.channel)}')
        await message.channel.send(f'You said {message.content}')

bot.run(TOKEN)
