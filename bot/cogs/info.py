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


class InfoCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name='info', description='Get information about a user')
    async def info(self, interaction: discord.Interaction, member: discord.Member = None):
        placeholder = discord.File("cogs/placeholder.png", filename='placeholder.png')
        user = member or interaction.user
        embed=discord.Embed(title=f"{user.name}", description=f"ID: {user.id}")
        embed.add_field(name="Joined Discord", value=user.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        embed.add_field(name="Roles", value=", ".join([role.mention for role in user.roles]), inline=False)
        embed.add_field(name="Badges", value=", ".join([badge.name for badge in user.public_flags.all()]), inline=False)
        embed.add_field(name="Activity", value=user.activity)
        if user.avatar == None:
            embed.set_thumbnail(url='attachment://placeholder.png')
            await interaction.response.send_message(file=placeholder, embed=embed)
        else:
            embed.set_thumbnail(url=user.avatar.url)
            await interaction.response.send_message(embed=embed)


async def setup(client):
    await client.add_cog(InfoCog(client))