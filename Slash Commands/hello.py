from discord.ext import commands

@commands.hybrid_command()
async def hello(ctx):
    user = ctx
    await ctx.send(f"Hello {ctx.author.display_name}! I'm Rowboat.")

async def setup(bot):
    bot.add_command(hello)