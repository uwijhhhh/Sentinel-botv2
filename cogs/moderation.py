import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.User, *, reason=None):
        await ctx.guild.ban(user, reason=reason)
        await ctx.send(f"{user} a été banni.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user: discord.User):
        await ctx.guild.unban(user)
        await ctx.send(f"{user} a été débanni.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, user: discord.Member, *, reason=None):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            muted_role = await ctx.guild.create_role(name="Muted", permissions=discord.Permissions(send_messages=False))
        
        await user.add_roles(muted_role)
        await ctx.send(f"{user} a été mis en sourdine pour {reason}.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, user: discord.Member):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await user.remove_roles(muted_role)
        await ctx.send(f"{user} a été débloqué.")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
