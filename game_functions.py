from color_module import Color
from time import sleep
from dataclasses import dataclass
import questionary


@dataclass
class Player:
    """
    This is the Player object that will be used within the tic-tac-toe game
    """
    def __init__(self, message, symbol):
        if message == "Computer Overlord":
            self.name = message
        else:
            self.name: str = input(message)
        self.symbol: str = symbol


def clear():
    from os import system, name
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def validate_input(message: str, options: list[int | str]) -> int | str:
    """
    :param options: What the value can be
    :param message: The message to prompt the user for input
    :return: str  The user's response (as a string)
    """
    value = input(message)
    try:
        if isinstance(options[0], int):
            value = int(value)
        if value in options:
            return value
        else:
            raise ValueError
    except ValueError:
        print(f"You need to select one of the following: {options}")
        validate_input(message, options)


def get_player_count() -> int:
    message = "Select number of players: (1-2) "
    options = [1, 2]
    return validate_input(message, options)


def select_difficulty() -> int:
    message = "Select a difficulty level: (1-2) "
    options = [1, 2]
    return validate_input(message, options)


def turn_input() -> str:
    message = "Where would you like to play? "
    options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return validate_input(message, options)


def comp_strat(grid: str) -> str:
    """
    This function creates the logic for the computer opponent.
    **Currently only used when the player sets the difficulty to 2**
    TODO: Can this be updated/augmented with and actual AI agent to play against?
    :param grid: The string representation of the grid (tic-tac-toe board)
    :return: str
    """

    if grid[17] == "5":
        return "5"
    elif grid[1] == grid[5] and grid[9] == "3":  # 1
        return "3"
    elif grid[9] == grid[1] and grid[5] == "2":  # 1
        return "2"
    elif grid[9] == grid[5] and grid[1] == "1":  # 1
        return "1"
    elif grid[13] == grid[17] and grid[21] == "6":  # 2
        return "6"
    elif grid[21] == grid[17] and grid[13] == "4":  # 2
        return "4"
    elif grid[25] == grid[29] and grid[33] == "9":  # 3
        return "9"
    elif grid[33] == grid[25] and grid[29] == "8":  # 3
        return "8"
    elif grid[33] == grid[29] and grid[25] == "7":  # 3
        return "7"
    elif grid[1] == grid[13] and grid[25] == "7":  # 4
        return "7"
    elif grid[25] == grid[1] and grid[13] == "4":  # 4
        return "4"
    elif grid[25] == grid[13] and grid[1] == "1":  # 4
        return "1"
    elif grid[5] == grid[17] and grid[29] == "8":  # 5
        return "8"
    elif grid[29] == grid[17] and grid[5] == "2":  # 5
        return "2"
    elif grid[9] == grid[21] and grid[33] == "9":  # 6
        return "9"
    elif grid[33] == grid[9] and grid[21] == "6":  # 6
        return "6"
    elif grid[33] == grid[21] and grid[9] == "3":  # 6
        return "3"
    elif grid[1] == grid[17] and grid[33] == "9":  # 7
        return "9"
    elif grid[33] == grid[17] and grid[1] == "1":  # 7
        return "1"
    elif grid[9] == grid[17] and grid[25] == "7":  # 8
        return "7"
    elif grid[25] == grid[17] and grid[9] == "3":  # 8
        return "3"


def introduction():
    """
    This simply displays a fun greeting for the player(s) prior to starting the game.
    :return: None
    """
    clear()
    print(Color.RED+'''
             #   # ##### #     #      ####
             #   # #     #     #     #    #
             ##### ###   #     #     #    #
             #   # #     #     #     #    #
             #   # ##### ##### #####  ####
 '''+Color.END)
    sleep(1)
    clear()
    print(Color.GREEN+'''
                   #     #     #  #####
                  # #    # #   #  #    #
                 # # #   #   # #  #    #
                #     #  #     #  ##### 
 '''+Color.END)
    sleep(0.6)
    clear()
    print(Color.RED+'''
 #  #  #  ###### #       #####   ####   #     #  ######
 #  #  #  #      #      #       #    #  # # # #  #
 #  #  #  ###    #      #       #    #  #  #  #  ####
 #  #  #  #      #      #       #    #  #     #  #
  ## ##   ######  #####  #####   ####   #     #  ######
 '''+Color.END)
    sleep(1)
    clear()

    # Greeting Message
    print(Color.GREEN+"Welcome to Ryan's", Color.RED+"Tic-Tac-Toe!"+Color.END, Color.GREEN+"GLHF!\n"+Color.END)


def check_win_condition(turn: int, grid: str, player: Player) -> str:
    """
    Checking Win Conditions
    :param turn: the turn number of the current game
    :param grid: The string representation of the grid (tic-tac-toe board)
    :param player: The Player object
    """
    # Grid index locations---> 1=1, 2=5, 3=9, 4=13, 5=17, 6=21, 7=25, 8=29, 9=33
    ps = player.symbol
    # Condition 1:
    if grid[1] == ps and grid[5] == ps and grid[9] == ps:  # top row win
        return (f"Taking the W right across the top, "
                f"{Color.RED + player.name + Color.END} pulled it out in the end.")
    # Condition 2:
    elif grid[13] == ps and grid[17] == ps and grid[21] == ps:  # middle row win
        return (f"{Color.RED + player.name + Color.END} "
                f"snatched the victory strait through the middle.  How embarrassing.")
    # Condition 3:
    elif grid[25] == ps and grid[29] == ps and grid[33] == ps:  # bottom row win
        return (f"Clutching the W with a sweep across the bottom!  "
                f"{Color.RED + player.name + Color.END} wins!")
    # Condition 4:
    elif grid[1] == ps and grid[13] == ps and grid[25] == ps:  # left colum win
        return (f"Holding firm to that left colum to secure the win, "
                f"{Color.BLUE + player.name + Color.END} takes it!")
    # Condition 5:
    elif grid[5] == ps and grid[17] == ps and grid[29] == ps:  # middle colum win
        return (f"Taking the W right down the middle: "
                f"{Color.BLUE + player.name + Color.END}")
    # Condition 6:
    elif grid[9] == ps and grid[21] == ps and grid[33] == ps:  # right colum win
        return (f"End of the line for you.  "
                f"{Color.BLUE + player.name + Color.END} just took the far right colum!")
    # Condition 7:
    elif grid[1] == ps and grid[17] == ps and grid[33] == ps:  # \ win
        return (f"Dang, I bet you didn't even see that coming!  "
                f"{Color.GREEN + player.name + Color.END} just took your down like a bishop taking a pawn!")
    # Condition 8:
    elif grid[9] == ps and grid[17] == ps and grid[25] == ps:  # / win
        return (f"That is it, {Color.GREEN + player.name + Color.END} "
                f"emerged victorious with a nice slash across the board.")
    # Condition 9: This condition is the DRAW outcome where no user wins.
    elif turn == 9:
        return ("A draw?\nYou are either pretty good or really bad.  "
                "I don't want to watch you struggle through that again either way.")
