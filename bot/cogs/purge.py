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
from discord.app_commands import MissingPermissions


class PurgeCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name='purge', description='[Moderation] Clears messages')
    @app_commands.checks.has_permissions(administrator=True)
    async def purge(self, interaction: discord.Interaction, amount: int):
        if amount > 100:
            await interaction.response.send_message("You can only clear up to 100 messages at a time", ephemeral=True)
        else:
            await interaction.response.send_message(f"Succesfully purged {amount} messages", ephemeral=True)
            await interaction.channel.purge(limit=amount)


    @purge.error
    async def purge_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, MissingPermissions):
            await interaction.response.send_message("You do not have permission to use this command!", ephemeral=True)
        else:
            await interaction.response.send_message("An error occurred while trying to purge the messages.", ephemeral=True)

async def setup(client):
    await client.add_cog(PurgeCog(client))