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
    async def �������(self, ctx):
        �������_button = Button(label="�������", custom_id="�������", style=discord.ButtonStyle.primary)
        ���_button = Button(label="���", custom_id="���", style=discord.ButtonStyle.primary)
        ���_button = Button(label="���", custom_id="���", style=discord.ButtonStyle.primary)
        ������_button = Button(label="������", custom_id="������", style=discord.ButtonStyle.primary)

        view = View()
        view.add_item(�������_button)
        view.add_item(���_button)
        view.add_item(���_button)
        view.add_item(������_button)

        await ctx.send("�������� �������:", view=view)

    @commands.Cog.listener()
    async def on_button_click(self, interaction: discord.Interaction):
        if interaction.custom_id == "�������":
            def check(m):
                return m.author == interaction.user and m.channel == interaction.channel

            await interaction.send("������� ���������� ��������� ��� ��������:")

            try:
                msg = await self.bot.wait_for('message', timeout=60.0, check=check)
                ���������� = int(msg.content)
                await interaction.channel.purge(limit=���������� + 1)
                await interaction.send(f'������� {����������} ���������.')
            except ValueError:
                await interaction.send("������������ ���������� ���������.")
            except asyncio.TimeoutError:
                await interaction.send("����� �������� �������.")

        elif interaction.custom_id == "���":
            def check(m):
                return m.author == interaction.user and m.channel == interaction.channel

            await interaction.send("������� ������������ ��� ���� � ������� (� ������� '������������#������������� �������'):")

            try:
                msg = await self.bot.wait_for('message', timeout=60.0, check=check)
                member_name, member_discriminator, ������� = msg.content.split(' ', 2)
                member = discord.utils.get(interaction.guild.members, name=member_name, discriminator=member_discriminator)
                await member.kick(reason=�������)
                await interaction.send(f'�������� {member.mention} ��� ������.')
            except ValueError:
                await interaction.send("������������ ������ �����.")
            except asyncio.TimeoutError:
                await interaction.send("����� �������� �������.")
            except AttributeError:
                await interaction.send("�������� �� ������.")

        elif interaction.custom_id == "���":
            def check(m):
                return m.author == interaction.user and m.channel == interaction.channel

            await interaction.send("������� ������������ ��� ���� � ������� (� ������� '������������#������������� �������'):")

            try:
                msg = await self.bot.wait_for('message', timeout=60.0, check=check)
                member_name, member_discriminator, ������� = msg.content.split(' ', 2)
                member = discord.utils.get(interaction.guild.members, name=member_name, discriminator=member_discriminator)
                await member.ban(reason=�������)
                await interaction.send(f'�������� {member.mention} ��� �������.')
            except ValueError:
                await interaction.send("������������ ������ �����.")
            except asyncio.TimeoutError:
                await interaction.send("����� �������� �������.")
            except AttributeError:
                await interaction.send("�������� �� ������.")

        elif interaction.custom_id == "������":
            def check(m):
                return m.author == interaction.user and m.channel == interaction.channel

            await interaction.send("������� ������������ ��� ������� (� ������� '������������#�������������'):")

            try:
                msg = await self.bot.wait_for('message', timeout=60.0, check=check)
                ������������ = msg.content
                banned_users = await interaction.guild.bans()
                member_name, member_discriminator = ������������.split('#')

                for ban_entry in banned_users:
                    user = ban_entry.user

                    if (user.name, user.discriminator) == (member_name, member_discriminator):
                        await interaction.guild.unban(user)
                        await interaction.send(f'������������ {user.mention} ��� ��������.')
                        return

                await interaction.send("������������ �� ������ � ������ �����.")
            except ValueError:
                await interaction.send("������������ ������ �����.")
            except asyncio.TimeoutError:
                await interaction.send("����� �������� �������.")







async def setup(bot):
    await bot.add_cog(MyCog(bot))
