import discord
from discord import app_commands
from discord.ext import commands, tasks
from discord.ext.commands import BucketType
from discord.utils import get
import discord.ui
import random
from itertools import cycle
import os
import re
import time
import math
import asyncio
import datetime
from datetime import datetime, timedelta
import nacl
import matplotlib.pyplot as plt
import json
from typing import List
from PIL import Image, ImageDraw, ImageFont, ImageOps
import requests
from io import BytesIO


class FunCog(commands.Cog):
    def __init__(self, client):
        self.client = client


    @app_commands.command(name='8ball', description='Ask a random question!')
    async def ping(self, interaction: discord.Interaction, question: str):
        with open("cogs/responses/responses.txt", "r") as f:
            random_responses = f.readlines()
            response = random.choice(random_responses)

        embed = discord.Embed(title="", description="", color=discord.Colour.gold())
        embed.set_author(name="Magic 8", icon_url="https://cdn.jsdelivr.net/gh/twitter/twemoji@latest/assets/72x72/1f3b1.png")
        embed.add_field(name="Question", value=f"{question}")
        embed.add_field(name="Response", value=f"||{response}||")

        await interaction.response.send_message(embed=embed)

    @app_commands.command(name='dog', description='Get a random dog image!')
    async def dog(self, interaction: discord.Interaction):
        dog_url = "https://dog.ceo/api/breeds/image/random"
        dog_info = requests.get(dog_url)
        dog_data = dog_info.json()
        dog_link = dog_data['message']
        embed = discord.Embed(color=discord.Colour.greyple(), title="Here is a random dog for you! 🐶")
        embed.set_image(url=dog_link)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name='cat', description='Get a random cat image!')
    async def cat(self, interaction: discord.Interaction):
        cat_url = "https://api.thecatapi.com/v1/images/search"
        cat_info = requests.get(cat_url)
        cat_data = cat_info.json()
        cat_link = cat_data[0]['url']
        embed = discord.Embed(color=discord.Colour.greyple(), title="Here is a random cat for you! 🐈")
        embed.set_image(url=cat_link)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name='meme', description='Get a random meme!')
    async def meme(self, interaction: discord.Interaction):
        meme_url = "https://meme-api.com/gimme"
        meme_info = requests.get(meme_url)
        meme_data = meme_info.json()
        meme_link = meme_data['url']
        embed = discord.Embed(color=discord.Colour.greyple(), title="Here is a random meme for you!")
        embed.set_image(url=meme_link)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name='pfp', description='Gets a user\'s profile picture.')
    async def pfp(self, interaction: discord.Interaction, target_user: discord.Member = None):
        user = target_user or interaction.user  # Get target user (self or mentioned)

        if not user.avatar:
            # Handle case where user doesn't have a profile picture
            await interaction.response.send_message(f"{user.mention} doesn't have a profile picture yet!",
                                                    ephemeral=True)
            return

        # Directly send the profile picture URL without modification
        embed = discord.Embed(color=discord.Color.blurple(), title=f'Here is {user}s profile picture.')
        embed.set_image(url=f"{user.avatar.url}")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="roast", description='The bot will roast a selected user')
    async def roast(self, interaction: discord.Interaction, user: discord.Member):
        target_user = user or interaction.user
        mention = user.mention
        with open("cogs/roasts/roasts.txt", "r") as f:
            random_roast = f.readlines()
            roast = random.choice(random_roast).strip().format(user=mention)

        embed = discord.Embed(color=discord.Color.orange())
        embed.add_field(name="", value=f"{roast}")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="clap", description='make 👏 sentences 👏 look 👏 like 👏 this!')
    async def clap(self, interaction: discord.Interaction, text: str):
        embed = discord.Embed()
        check = text.strip().split()
        split = text.strip()
        if len(check) > 1:
            new = split.replace(" ", " 👏 ")
            embed.add_field(name="", value=f"{new}")
        else:
            embed.add_field(name="", value=f"👏 **{text}** 👏")

        await interaction.response.send_message(embed=embed)


async def setup(client):
    await client.add_cog(FunCog(client))
