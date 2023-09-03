import os
import discord
from dotenv import load_dotenv
from Commands import libre
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f'{bot.user} is now online.')
    try:
        await bot.load_extension("Slash Commands.hello")
        await bot.add_cog(libre.Free(bot))
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} commands')
    except Exception as e:
        print(e)

#Bot Slash Commands
@bot.tree.command(name="rowboat")
async def rowboat(interaction: discord.Interaction):
    await interaction.response.send_message("*Row, row, row your boat\n"
                   "Gently down the stream\n"
                   "Merrily, merrily, merrily, merrily\n"
                   "Life is but a dream*")

@bot.tree.command(name="help")
async def helps(interaction: discord.Interaction):
    embed = discord.Embed(title="Welcome To Row Boat's Help Page")
    embed.add_field(name="Slash Commands", value="help - Shows the help page \nhello - Returns hello to you \nrowboat - Try it ;)", inline=False)
    embed.add_field(name="$ Commands",
                    value="libre - Shows Epic Games Free game(s).",
                    inline=False)
    await interaction.response.send_message(embed=embed)

bot.run(TOKEN)