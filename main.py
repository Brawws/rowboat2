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
        await bot.load_extension("Slash.hello")
        await bot.load_extension("Slash.helps")
        await bot.load_extension("Slash.rowboat")
        await bot.load_extension("Slash.meme")
        await bot.add_cog(libre.Free(bot))
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} commands')
    except Exception as e:
        print(e)

bot.run(TOKEN)
