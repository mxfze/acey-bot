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



class PingCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name='ping', description = 'gives the bots latency (ping)')
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Pong! {round(self.client.latency * 1000)}ms', ephemeral=True)
        

async def setup(client):
    await client.add_cog(PingCog(client))