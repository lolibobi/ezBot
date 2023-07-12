# -*- coding: ANSI -*-

import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="на члене"))

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')



    

bot.run('MTEyNzg0NTg5Njg2NDkyMzY1OA.GPjOVh.04ku-AkoJpaji6nEcMa5vZSrtDoz5C_dVmRbXw')