import os
import datetime
import inspect


class Color:
    """
    A class to store color codes for the terminal.
    """
    RED = '\033[91m'
    LIGHT_RED = '\033[31m'
    GREEN = '\033[92m'
    LIGHT_GREEN = '\033[32m'
    YELLOW = '\033[93m'
    LIGHT_YELLOW = '\033[33m'
    ORANGE = '\033[33m'
    LIGHT_ORANGE = '\033[33m'
    BLUE = '\033[94m'
    LIGHT_BLUE = '\033[34m'
    PURPLE = '\033[95m'
    LIGHT_PURPLE = '\033[35m'
    CYAN = '\033[96m'
    LIGHT_CYAN = '\033[36m'
    PINK = '\033[95m'
    LIGHT_PINK = '\033[35m'
    GRAY = '\033[90m'
    LIGHT_GRAY = '\033[37m'
    RESET = '\033[0m'


def clear():
    """
    Clear the console.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def banner():
    """
    Print the bot's banner.
    """
    print(Color.LIGHT_BLUE + r"""
   ______      __                 _____ __        __            
  / ____/___ _/ /___ __  ____  __/ ___// /_____ _/ /___  _______
 / / __/ __ `/ / __ `/ |/_/ / / /\__ \/ __/ __ `/ __/ / / / ___/
/ /_/ / /_/ / / /_/ />  </ /_/ /___/ / /_/ /_/ / /_/ /_/ (__  ) 
\____/\__,_/_/\__,_/_/|_|\__, //____/\__/\__,_/\__/\__,_/____/  
                        /____/                                  
""" + Color.RESET)


def log(type: str, args: str):
    """
    Debugging function that prints the current time and the provided argument.
    """

    caller_frame = inspect.stack()[1]
    caller_file_name = os.path.basename(caller_frame.filename).replace('.py', '')

    type_color = {
        "error": Color.RED,
        "warn": Color.YELLOW,
        "info": Color.BLUE,
        "success": Color.GREEN
    }.get(type, Color.RESET)

    type = f"{type_color}{caller_file_name:^18}{Color.RESET}"


    time = datetime.datetime.now().strftime("%H:%M:%S")

    print(
        f'{Color.GRAY}[{Color.YELLOW}{type}{Color.GRAY}] {Color.GRAY}({Color.LIGHT_GRAY}{time}{Color.GRAY}) {Color.RESET}{args}')