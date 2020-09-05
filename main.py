import discord
from discord.ext import commands
import os
bot = commands.Bot(command_prefix = '+')
@bot.remove_command("help")
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity('Annoying you 😋'))
    print("ready")
@bot.command()
async def help(ctx):
    emb = discord.Embed(
        title=f"Commands for {bot.user.name}",
        colour=discord.colour.Colour.from_rgb(81, 147, 252)
    )
    await ctx.send(embed=emb)
@bot.command()
async def ping(ctx):
    emb = discord.Embed(
        colour=discord.colour.Colour.from_rgb(81, 147, 252)
    )
    emb.add_field(name="Your Ping is ", value=f'```{round(bot.latency*1000)} ms              ```')
    await ctx.send("🏓 Pong!  ")
    await ctx.send(embed = emb)
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
home = os.environ['token']
bot.run(home)