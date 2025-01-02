import os

from ezcord import discord

from bot.utils.Logging import Color, log


class Stats:
    loaded_commands = 0
    loaded_events = 0
    loaded_tasks = 0

def bot_info(bot: discord.Bot):
    bot_name = "GalaxyStatus"
    bot_id = str(bot.application_id)
    loaded_commands = str(Stats.loaded_commands)
    loaded_tasks = str(Stats.loaded_tasks)
    loaded_events = str(Stats.loaded_events)
    ping = str(round(bot.latency * 1000)) + "ms"

    max_len = max(len(bot_name), len(bot_id), len(loaded_commands), len(loaded_tasks), len(loaded_events), len(ping))

    print()
    print(
        Color.LIGHT_GRAY + f"╭{'─' * (max_len + 2)}┬{'─' * (max_len + 2)}┬{'─' * (max_len + 2)}┬{'─' * (max_len + 2)}┬{'─' * (max_len + 2)}┬{'─' * (max_len + 2)}╮")
    print(
        Color.LIGHT_GRAY + f"│ {'Bot':>{max_len}} │ {'ID':>{max_len}} │ {'Commands':>{max_len}} │ {'Tasks':>{max_len}} │ {'Events':>{max_len}} │ {'Ping':>{max_len}} │")
    print(
        Color.LIGHT_GRAY + f"│{'─' * (max_len + 2)}┼{'─' * (max_len + 2)}┼{'─' * (max_len + 2)}┼{'─' * (max_len + 2)}┼{'─' * (max_len + 2)}┼{'─' * (max_len + 2)}┼")
    print(
        f"│ {Color.LIGHT_GREEN}{bot_name:>{max_len}} {Color.LIGHT_GRAY}│ {Color.LIGHT_BLUE}{bot_id:>{max_len}} {Color.LIGHT_GRAY}│ {Color.LIGHT_PINK}{loaded_commands:>{max_len}} {Color.LIGHT_GRAY}│ {Color.YELLOW}{loaded_tasks:>{max_len}} {Color.LIGHT_GRAY}│ {Color.PINK}{loaded_events:>{max_len}} {Color.LIGHT_GRAY}│ {Color.ORANGE}{ping:>{max_len}} {Color.LIGHT_GRAY}│")
    print(
        Color.LIGHT_GRAY + f"╰{'─' * (max_len + 2)}┴{'─' * (max_len + 2)}┴{'─' * (max_len + 2)}┴{'─' * (max_len + 2)}┴{'─' * (max_len + 2)}┴{'─' * (max_len + 2)}╯")
    print()

def extension_loader(bot: discord.Bot):
    """
    Load all extensions (commands, events) for the provided bot.
    """
    for path in ["events", "commands", "tasks"]:
        for filename in os.listdir(path):
            if "#" in filename:
                if path == "commands":
                    log("warn", f"Skipping command {filename.replace("#", "")} because it is disabled.")
                elif path == "events":
                    log("warn", f"Skipping event {filename.replace("#", "")} because it is disabled.")
                elif path == "tasks":
                    log("warn", f"Skipping task {filename.replace("#", "")} because it is disabled.")
                continue
            if filename.endswith(".py"):
                if path == "events":
                    bot.load_extension(path + "." + filename[:-3])
                    Stats.loaded_events += 1
                elif path == "commands":
                    bot.load_extension(path + "." + filename[:-3])
                    Stats.loaded_commands += 1
                elif path == "tasks":
                    bot.load_extension(path + "." + filename[:-3])
                    Stats.loaded_tasks += 1
    log("success", "All extensions loaded successfully.")