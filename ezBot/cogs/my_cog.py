# -*- coding: ANSI -*-

from discord.ext import commands
import discord
import asyncio
from discord.ui import Button, View


intents = discord.Intents.default()
intents.members = True

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def команды(self, ctx):
        очистка_button = Button(label="Очистка", custom_id="очистка", style=discord.ButtonStyle.primary)
        кик_button = Button(label="Кик", custom_id="кик", style=discord.ButtonStyle.primary)
        бан_button = Button(label="Бан", custom_id="бан", style=discord.ButtonStyle.primary)
        разбан_button = Button(label="Разбан", custom_id="разбан", style=discord.ButtonStyle.primary)

        view = View()
        view.add_item(очистка_button)
        view.add_item(кик_button)
        view.add_item(бан_button)
        view.add_item(разбан_button)

        await ctx.send("Выберите команду:", view=view)

    @commands.Cog.listener()
    async def on_button_click(self, interaction: discord.Interaction):
        if interaction.custom_id == "очистка":
            def check(m):
                return m.author == interaction.user and m.channel == interaction.channel

            await interaction.send("Введите количество сообщений для удаления:")

            try:
                msg = await self.bot.wait_for('message', timeout=60.0, check=check)
                количество = int(msg.content)
                await interaction.channel.purge(limit=количество + 1)
                await interaction.send(f'Удалено {количество} сообщений.')
            except ValueError:
                await interaction.send("Некорректное количество сообщений.")
            except asyncio.TimeoutError:
                await interaction.send("Время ожидания истекло.")

        elif interaction.custom_id == "кик":
            def check(m):
                return m.author == interaction.user and m.channel == interaction.channel

            await interaction.send("Введите пользователя для кика и причину (в формате 'пользователь#дискриминатор причина'):")

            try:
                msg = await self.bot.wait_for('message', timeout=60.0, check=check)
                member_name, member_discriminator, причина = msg.content.split(' ', 2)
                member = discord.utils.get(interaction.guild.members, name=member_name, discriminator=member_discriminator)
                await member.kick(reason=причина)
                await interaction.send(f'Участник {member.mention} был кикнут.')
            except ValueError:
                await interaction.send("Некорректный формат ввода.")
            except asyncio.TimeoutError:
                await interaction.send("Время ожидания истекло.")
            except AttributeError:
                await interaction.send("Участник не найден.")

        elif interaction.custom_id == "бан":
            def check(m):
                return m.author == interaction.user and m.channel == interaction.channel

            await interaction.send("Введите пользователя для бана и причину (в формате 'пользователь#дискриминатор причина'):")

            try:
                msg = await self.bot.wait_for('message', timeout=60.0, check=check)
                member_name, member_discriminator, причина = msg.content.split(' ', 2)
                member = discord.utils.get(interaction.guild.members, name=member_name, discriminator=member_discriminator)
                await member.ban(reason=причина)
                await interaction.send(f'Участник {member.mention} был забанен.')
            except ValueError:
                await interaction.send("Некорректный формат ввода.")
            except asyncio.TimeoutError:
                await interaction.send("Время ожидания истекло.")
            except AttributeError:
                await interaction.send("Участник не найден.")

        elif interaction.custom_id == "разбан":
            def check(m):
                return m.author == interaction.user and m.channel == interaction.channel

            await interaction.send("Введите пользователя для разбана (в формате 'пользователь#дискриминатор'):")

            try:
                msg = await self.bot.wait_for('message', timeout=60.0, check=check)
                пользователь = msg.content
                banned_users = await interaction.guild.bans()
                member_name, member_discriminator = пользователь.split('#')

                for ban_entry in banned_users:
                    user = ban_entry.user

                    if (user.name, user.discriminator) == (member_name, member_discriminator):
                        await interaction.guild.unban(user)
                        await interaction.send(f'Пользователь {user.mention} был разбанен.')
                        return

                await interaction.send("Пользователь не найден в списке банов.")
            except ValueError:
                await interaction.send("Некорректный формат ввода.")
            except asyncio.TimeoutError:
                await interaction.send("Время ожидания истекло.")







async def setup(bot):
    await bot.add_cog(MyCog(bot))
