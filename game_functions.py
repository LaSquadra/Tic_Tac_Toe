from color_module import Color
from time import sleep
from dataclasses import dataclass
from random import choice, random


WINNING_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]

HARD_MODE_MISTAKE_CHANCE = 0.15


@dataclass
class Player:
    """
    This is the Player object that will be used within the tic-tac-toe game
    """
    name: str
    symbol: str


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
    while True:
        value = input(message)
        try:
            if isinstance(options[0], int):
                value = int(value)
            if value in options:
                return value
            raise ValueError
        except ValueError:
            print(f"You need to select one of the following: {options}")


def get_player_count() -> int:
    message = "Select number of players: (1-2) "
    options = [1, 2]
    return validate_input(message, options)


def select_difficulty() -> int:
    message = "Select a difficulty level: (1-3) "
    options = [1, 2, 3]
    return validate_input(message, options)


def turn_input() -> str:
    message = "Where would you like to play? "
    options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return validate_input(message, options)


def create_board() -> list[str]:
    """
    Create a fresh tic-tac-toe board.
    :return: list[str]
    """
    return [str(position) for position in range(1, 10)]


def render_board(board: list[str]) -> str:
    """
    Build the printable tic-tac-toe board from the current board state.
    :param board: The current tic-tac-toe board
    :return: str
    """
    return (f"_{board[0]}_|_{board[1]}_|_{board[2]}_\n"
            f"_{board[3]}_|_{board[4]}_|_{board[5]}_\n"
            f" {board[6]} | {board[7]} | {board[8]} ")


def available_moves(board: list[str]) -> list[str]:
    """
    Find all unplayed spaces on the board.
    :param board: The current tic-tac-toe board
    :return: list[str]
    """
    return [space for space in board if space not in ("X", "O")]


def get_winner_symbol(board: list[str]) -> str | None:
    """
    Return the winning symbol if a player has won.
    :param board: The current tic-tac-toe board
    :return: str | None
    """
    for first, second, third in WINNING_COMBINATIONS:
        if board[first] == board[second] == board[third] and board[first] in ("X", "O"):
            return board[first]
    return None


def is_draw(board: list[str]) -> bool:
    """
    Return whether the game has ended without a winner.
    :param board: The current tic-tac-toe board
    :return: bool
    """
    return get_winner_symbol(board) is None and not available_moves(board)


def find_winning_move(board: list[str], symbol: str) -> str | None:
    """
    Find a move that completes a winning line for the given symbol.
    :param board: The current tic-tac-toe board
    :param symbol: The symbol to check
    :return: str | None
    """
    for combo in WINNING_COMBINATIONS:
        values = [board[index] for index in combo]
        if values.count(symbol) == 2:
            for index in combo:
                if board[index] not in ("X", "O"):
                    return board[index]
    return None


def medium_computer_move(board: list[str], computer_symbol: str = "O", player_symbol: str = "X") -> str:
    """
    Choose a solid move that can win, block, or take a strong square.
    :param board: The current tic-tac-toe board
    :param computer_symbol: The computer player's symbol
    :param player_symbol: The human player's symbol
    :return: str
    """
    winning_move = find_winning_move(board, computer_symbol)
    if winning_move:
        return winning_move

    blocking_move = find_winning_move(board, player_symbol)
    if blocking_move:
        return blocking_move

    for move in ("5", "1", "3", "7", "9"):
        if move in board:
            return move

    return choice(available_moves(board))


def score_board(board: list[str], computer_symbol: str, player_symbol: str, depth: int) -> int | None:
    """
    Score a finished board from the computer's perspective.
    :param board: The current tic-tac-toe board
    :param computer_symbol: The computer player's symbol
    :param player_symbol: The human player's symbol
    :param depth: The current minimax depth
    :return: int | None
    """
    winner = get_winner_symbol(board)
    if winner == computer_symbol:
        return 10 - depth
    if winner == player_symbol:
        return depth - 10
    if is_draw(board):
        return 0
    return None


def minimax(board: list[str], computer_symbol: str, player_symbol: str, is_computer_turn: bool, depth: int = 0) -> int:
    """
    Recursively score the best outcome available from the current board.
    :param board: The current tic-tac-toe board
    :param computer_symbol: The computer player's symbol
    :param player_symbol: The human player's symbol
    :param is_computer_turn: Whether the computer is choosing this move
    :param depth: The current search depth
    :return: int
    """
    score = score_board(board, computer_symbol, player_symbol, depth)
    if score is not None:
        return score

    if is_computer_turn:
        best_score = -100
        symbol = computer_symbol
    else:
        best_score = 100
        symbol = player_symbol

    for move in available_moves(board):
        move_index = int(move) - 1
        board[move_index] = symbol
        move_score = minimax(board, computer_symbol, player_symbol, not is_computer_turn, depth + 1)
        board[move_index] = move

        if is_computer_turn:
            best_score = max(best_score, move_score)
        else:
            best_score = min(best_score, move_score)

    return best_score


def rank_computer_moves(board: list[str], computer_symbol: str, player_symbol: str) -> tuple[list[str], list[str]]:
    """
    Split available moves into best moves and weaker-but-legal moves.
    :param board: The current tic-tac-toe board
    :param computer_symbol: The computer player's symbol
    :param player_symbol: The human player's symbol
    :return: tuple[list[str], list[str]]
    """
    scored_moves = []

    for move in available_moves(board):
        move_index = int(move) - 1
        board[move_index] = computer_symbol
        move_score = minimax(board, computer_symbol, player_symbol, False)
        board[move_index] = move
        scored_moves.append((move, move_score))

    best_score = max(score for _, score in scored_moves)
    best_moves = [move for move, score in scored_moves if score == best_score]
    weaker_moves = [move for move, score in scored_moves if score < best_score]

    return best_moves, weaker_moves


def choose_preferred_move(moves: list[str]) -> str:
    """
    Choose from moves using a stable tic-tac-toe preference order.
    :param moves: Legal moves to choose from
    :return: str
    """
    preferred_moves = ("5", "1", "3", "7", "9", "2", "4", "6", "8")
    for move in preferred_moves:
        if move in moves:
            return move
    return moves[0]


def imperfect_hard_computer_move(board: list[str], computer_symbol: str = "O", player_symbol: str = "X") -> str:
    """
    Usually choose the minimax move, but occasionally choose a weaker legal move.
    :param board: The current tic-tac-toe board
    :param computer_symbol: The computer player's symbol
    :param player_symbol: The human player's symbol
    :return: str
    """
    best_moves, weaker_moves = rank_computer_moves(board, computer_symbol, player_symbol)
    if weaker_moves and random() < HARD_MODE_MISTAKE_CHANCE:
        return choice(weaker_moves)
    return choose_preferred_move(best_moves)


def comp_strat(board: list[str], computer_symbol: str = "O", player_symbol: str = "X",
               difficulty: int = 2) -> str:
    """
    Choose a computer move for the requested difficulty.
    :param board: The current tic-tac-toe board
    :param computer_symbol: The computer player's symbol
    :param player_symbol: The human player's symbol
    :param difficulty: The selected computer difficulty
    :return: str
    """
    if difficulty == 1:
        return choice(available_moves(board))
    if difficulty == 3:
        return imperfect_hard_computer_move(board, computer_symbol, player_symbol)
    return medium_computer_move(board, computer_symbol, player_symbol)


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


def check_win_condition(turn: int, board: list[str], player: Player) -> str | None:
    """
    Checking Win Conditions
    :param turn: the turn number of the current game
    :param board: The current tic-tac-toe board
    :param player: The Player object
    """
    if get_winner_symbol(board) == player.symbol:
        return f"{Color.GREEN + player.name + Color.END} wins!"
    if turn == 9:
        return ("A draw?\nYou are either pretty good or really bad.  "
                "I don't want to watch you struggle through that again either way.")
    return None
