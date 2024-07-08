import discord
from discord import app_commands
from discord.ext import commands, tasks
from discord.ext.commands import BucketType
from discord.utils import get
from discord.app_commands import MissingPermissions
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


class ModerationCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command(name='kick', description='[Moderation] Kick someone')
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        await member.kick(reason=reason)
        embed = discord.Embed(title="", description="", color=discord.Color.green())
        if reason:
            embed.add_field(name="", value=f'{member.name} has been kicked for {reason}')
            await interaction.response.send_message(embed=embed)
        else:
            embed.add_field(name="", value=f'{member.name} has been kicked')
            await interaction.response.send_message(embed=embed)

    @kick.error
    async def kick_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, MissingPermissions):
            await interaction.response.send_message("You do not have permission to use this command!", ephemeral=True)
        else:
            await interaction.response.send_message("An error occurred while trying to kick the member.", ephemeral=True)


async def setup(client):
    await client.add_cog(ModerationCog(client))