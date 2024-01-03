import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("moderation.py is ready!")

    #Clear Comman
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, count: int):
        await ctx.channel.purge(limit=count)

    #Kick Command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *,  modreason):
        await ctx.guild.kick(member)

        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Kicked:", value=f"{member.mention} has been kicked from the server by {ctx.author.mention}.", inline = False)
        conf_embed.add_field(name="Reason:", value=modreason, inline=False)

        await ctx.send(embed=conf_embed)

    #Ban Command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *,  modreason):
        await ctx.guild.ban(member)

        conf_embed = discord.Embed(title="Success!", color=discord.Color.red())
        conf_embed.add_field(name="Banned:", value=f"{member.mention} has been banned from the server by {ctx.author.mention}", inline = False)
        conf_embed.add_field(name="Reason:", value=modreason, inline=False)

        await ctx.send(embed=conf_embed)

    #Unban Command
    @commands.command(name="unban")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, userId):
        user = discord.Object(id=userId)
        await ctx.guild.unban(user)
    
    
        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Unbanned:", value=f"<@{userId}> has been unbanned from the server by {ctx.author.mention}", inline = False)

        await ctx.send(embed=conf_embed)

async def setup(client):
    await client.add_cog(moderation(client))