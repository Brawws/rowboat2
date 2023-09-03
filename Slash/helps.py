import discord
from discord.ext import commands

@commands.hybrid_command()
async def helps(interaction: discord.Interaction):
    embed = discord.Embed(title="Welcome To Row Boat's Help Page")
    embed.add_field(name="Slash Commands",
                    value="helps - Shows the help page \nhello - Returns hello to you \nrowboat - Try it ;)",
                    inline=False)
    embed.add_field(name="$ Commands",
                    value="libre - Shows Epic Games Free game(s).",
                    inline=False)
    await interaction.interaction.response.send_message(embed=embed)

async def setup(bot):
    bot.add_command(helps)
