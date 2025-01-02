import json
import os

from bot.utils.Logging import log


def load_json():
    with open('utils/data/knowledge_dropdown.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_word_combinations(type: str):
    """
    Get the word combinations from the settings file.
    """
    with open("utils/data/word_combinations.json", "r") as file:
        settings = json.load(file)
        return settings.get(type, [])


def get_bot_settings(key: str):
    """
    Get the value of the provided key from the bot's settings.
    """

    if os.path.exists("utils/data/settings_debug.json"):
        # Open the file
        with open("utils/data/settings_debug.json", "r") as file:
            settings = json.load(file)
            if key in settings:
                return settings[key]
            else:
                log("error", f"Key {key} not found in settings_debug.json")
                return None
    else:
        with open("utils/data/settings_operational.json", "r") as file:
            settings = json.load(file)
            if key in settings:
                return settings[key]
            else:
                log("error", f"Key {key} not found in settings_operational.json")
                return None