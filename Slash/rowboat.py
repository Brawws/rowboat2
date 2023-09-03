import discord
from discord.ext import commands

@commands.hybrid_command()
async def rowboat(interaction: discord.Interaction):
    await interaction.interaction.response.send_message("*Row, row, row your boat\n"
                   "Gently down the stream\n"
                   "Merrily, merrily, merrily, merrily\n"
                   "Life is but a dream*")

async def setup(bot):
    bot.add_command(rowboat)