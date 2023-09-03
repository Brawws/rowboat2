import discord
import asyncio
from PIL import Image, ImageFont, ImageDraw
from discord.ext import commands

@commands.hybrid_command()
async def meme(interaction: discord.Interaction, text: str):
    img = Image.open("img/testpic.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 24)

    draw.text((0, 150), text, (0, 0, 0), font=font)
    img.save("img/writepic.png")
    loop = asyncio.get_event_loop()

    await loop.run_in_executor(None, meme, img)
    await interaction.interaction.response.send_message(file=discord.File("img/writepic.png"))

async def setup(bot):
    bot.add_command(meme)
