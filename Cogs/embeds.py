import discord
from discord.ext import commands

class embeds(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("embeds.py is ready!")

    @commands.command()
    async def embed(self, ctx):
        embed_message = discord.Embed(title="Title of embed", description = "Description of embed", color=discord.Color.green())

        embed_message.set_author(name=f"Requested by {ctx.author.mention}", icon_url=ctx.author.avatar)
        embed_message.set_thumbnail(url=ctx.guild.icon)
        embed_message.set_image(url=ctx.guild.icon)
        embed_message.add_field(name="Field name", value="Field value", inline= False)
        embed_message.set_footer(text="This is the footer", icon_url=ctx.author.avatar)

        await ctx.send(embed= embed_message)

async def setup(client):
    await client.add_cog(embeds(client))