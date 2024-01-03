import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
import os
import asyncio
import json


client = commands.Bot(command_prefix="?", intents=discord.Intents.all())

bot_status = "type /help"

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(bot_status))

@client.event
async def on_ready():
    await client.tree.sync()
    print("Success: Bot is connected to discord")
    change_status.start()

@client.event
async def on_guild_join(guild):
    with open("cogs/jsonfiles/mutes.json", "r") as f:
        mute_role = json.load(f)

        mute_role[str(guild.id)] = None

    with open("cogs/jsonfiles/mutes.json", "w") as f:
            json.dump(mute_role, f, indent=4)
    
@client.event
async def on_guild_remove(guild):
    with open("cogs/jsonfiles/mutes.json", "r") as f:
        mute_role = json.load(f)

        mute_role.pop(str(guild.id))

    with open("cogs/jsonfiles/mutes.json", "w") as f:
        json.dump(mute_role, f, indent=4)

@client.tree.command(name="ping", description="Shows bot's latency in ms")
async def ping(interaction: discord.Interaction):
    bot_latency = round(client.latency * 1000)
    await interaction.response.send_message(f"Pong! {bot_latency} ms.")

@client.command(aliases=["8ball", "magic8"])
async def magic_eight_ball(ctx, *, question):
    with open("responses.txt", "r") as f:
        random_responses = f.readlines()
        response = random.choice(random_responses)

    await ctx.send(response)

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename[:-3]} is loaded! ")


async def main():
    async with client:
        await load()
        await client.start("MTE5MjA1MTcxMzkxODY1MjQ2Nw.GDDVYN.c0DkMKWO2583HdPk2gOPxVmNxgWj3QrqrGp6wc")

asyncio.run(main())