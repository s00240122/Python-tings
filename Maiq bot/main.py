import discord
from discord.ext import commands
from discord.ui import Modal
from discord.components import TextInput
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


# todo:
# improve admin only commands (and cog load/unload/reload commands)
# error handler


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


async def load_cogs():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')


@bot.command()
async def load(ctx, cog):
    try:
        if ctx.author.guild_permissions.administrator:
            await bot.load_extension(f"cogs.{cog}")
            await ctx.send(f"Loaded cog `{cog}`")
        else:
            await ctx.send("Mai'q will not listen to you.")
    except Exception as e:
        await ctx.send(f"`{e}`")


@bot.command()
async def unload(ctx, cog):
    try:
        if ctx.author.guild_permissions.administrator:
            await bot.unload_extension(f"cogs.{cog}")
            await ctx.send(f"Unloaded cog `{cog}`")
        else:
            await ctx.send("Mai'q will not listen to you.")
    except Exception as e:
        await ctx.send(f"`{e}`")


@bot.command()
async def reload(ctx, cog):
    try:
        if ctx.author.guild_permissions.administrator:
            await bot.reload_extension(f"cogs.{cog}")
            await ctx.send(f"Reloaded cog `{cog}`")
        else:
            await ctx.send("Mai'q will not listen to you.")
    except Exception as e:
        await ctx.send(f"`{e}`")


@bot.command()  # this is bad don't use it
async def update(ctx, com, state):
    com = bot.get_command(com)
    if state == "enable":
        com.update(enabled=True)
        await ctx.send(f"!{com} is now {state}d")
    elif state == "disable":
        com.update(enabled=False)
        await ctx.send(f"!{com} is now {state}d")
    else:
        await ctx.send("what?")


asyncio.run(load_cogs())
bot.run(os.getenv('bot_key'))
