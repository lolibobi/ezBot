# -*- coding: ANSI -*-

from discord.ext import commands
import discord

class NewCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot





    #Тест кам
    @commands.command()
    async def челик(self, ctx):
        await ctx.send("шмелик")





async def setup(bot):
    await bot.add_cog(NewCog(bot))
