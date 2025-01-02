import discord
import ezcord
from utils.Bot import extension_loader
from utils.ConfigManager import get_bot_settings
from utils.Logging import clear, banner

# Initializes the bot
bot = ezcord.Bot(intents=discord.Intents.all())

if __name__ == "__main__":
    # Clears the terminal
    clear()

    # Prints the banner
    banner()

    # Loads the extensions
    extension_loader(bot)

    # Runs the bot
    bot.run(get_bot_settings('token'))