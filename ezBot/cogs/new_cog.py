# -*- coding: ANSI -*-

from discord.ext import commands
import discord

class NewCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot





    #���� ���
    @commands.command()
    async def �����(self, ctx):
        await ctx.send("������")





async def setup(bot):
    await bot.add_cog(NewCog(bot))
