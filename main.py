import discord
from discord.ext import commands
import os
bot = commands.Bot(command_prefix = '*')
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('playing *help'))
    print("ready")
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run("NzUwNDY0NzU2MTY2NTU3NzY4.X066xA.iQqGbPqAiYzwr0287ZKBabnoZSI")