import ezcord
from ezcord import discord


class ExampleCommand(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def do_something(self, ctx: ezcord.EzContext):
        return ctx.info("Task IncidentCommandCog has been created successfully.")

def setup(bot):
    bot.add_cog(ExampleCommand(bot))