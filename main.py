import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="$", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"¡Hola! Soy un bot con Bot class: {bot.user}")

@bot.command()
async def say(ctx, *, mensaje):
    await ctx.send(f"{mensaje}")

bot.run("")
