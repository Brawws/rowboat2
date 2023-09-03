import discord
import asyncio
from Plugins import timeconvert
from epicstore_api import EpicGamesStoreAPI
from discord.ext import commands

class Free(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def libre(self, ctx):
        buttons = [u"\u25C0", u"\u25B6"]  # BBW BW FW FFW
        api = EpicGamesStoreAPI(locale='en-US', country='PH')
        free = api.get_free_games()
        total = free['data']['Catalog']['searchStore']['paging']['total']
        file = discord.File("img/epic-games.png")
        pages = []
        self.bot.get_page = []
        current = 0

        for i in range(total):
            pages.append(i)

        for game in range(total):
            price = free['data']['Catalog']['searchStore']['elements'][game]['price']['totalPrice']['discountPrice']
            end_dates = free['data']['Catalog']['searchStore']['elements'][game]['price']['lineOffers'][0][
                'appliedRules']
            offer_type = ""
            if price == 0 and end_dates:
                end_date = \
                free['data']['Catalog']['searchStore']['elements'][game]['price']['lineOffers'][0]['appliedRules'][0][
                    'endDate']
                localtime = timeconvert.convert(end_date)

                if free['data']['Catalog']['searchStore']['elements'][game]['offerType'] == "BASE_GAME":
                    offer_type = "Base Game"
                elif free['data']['Catalog']['searchStore']['elements'][game]['offerType'] == "DLC":
                    offer_type = "DLC"

                pages[game] = discord.Embed(title=free['data']['Catalog']['searchStore']['elements'][game]['title'],
                                            description="*" + free['data']['Catalog']['searchStore']['elements'][game][
                                                'description'] + "*")
                pages[game].set_thumbnail(url="attachment://epic-games.png")
                pages[game].set_footer(text=f"Requested By: {ctx.author}", icon_url=ctx.author.avatar)
                pages[game].add_field(name="Type", value=offer_type, inline=False)
                pages[game].add_field(name="Original Price", value=
                free['data']['Catalog']['searchStore']['elements'][game]['price']['totalPrice']['fmtPrice'][
                    'originalPrice'], inline=False)
                pages[game].add_field(name="End Date", value=localtime, inline=False)
                pages[game].set_image(
                    url=free['data']['Catalog']['searchStore']['elements'][game]['keyImages'][0]['url'])
                self.bot.get_page.append(pages[game])
            elif price != 0 and not end_dates:
                continue

        msg = await ctx.send(file=file, embed=self.bot.get_page[current])

        for button in buttons:
            await msg.add_reaction(button)

        def check(reaction, user):
            return user == ctx.author and reaction.emoji in buttons

        while True:
            try:
                previous_page = current
                reaction, user = await self.bot.wait_for("reaction_add", timeout=30, check=check)

                if reaction.emoji == u"\u25C0" and current >= 1:
                    current -= 1
                    await msg.remove_reaction(reaction, user)
                elif reaction.emoji == u"\u25C0" and current == 0:
                    current = len(self.bot.get_page) - 1
                    await msg.remove_reaction(reaction, user)
                elif reaction.emoji == u"\u25B6" and current != len(self.bot.get_page) - 1:
                    current += 1
                    await msg.remove_reaction(reaction, user)
                elif reaction.emoji == u"\u25B6" and current == len(self.bot.get_page) - 1:
                    current = 0
                    await msg.remove_reaction(reaction, user)

                if current != previous_page:
                    await msg.edit(embed=self.bot.get_page[current])

            except asyncio.TimeoutError:
                await msg.clear_reactions()
                break