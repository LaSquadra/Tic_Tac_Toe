#!/usr/bin/env python3
import game_functions as GF
from color_module import Color
from time import sleep


def create_players(number_of_players: int) -> tuple[GF.Player, GF.Player]:
    """
    Create the players for the current game.
    :param number_of_players: Number of human players
    :return: tuple[GF.Player, GF.Player]
    """
    if number_of_players == 1:
        player_1 = GF.Player(input("Who dares challenge the Computer Overlord? "), "X")
        player_2 = GF.Player("Computer Overlord", "O")
    else:
        player_1 = GF.Player(input("Who is player 1? "), "X")
        player_2 = GF.Player(input("Who is player 2? "), "O")
    return player_1, player_2


def setup_game() -> tuple[int, int | None, GF.Player, GF.Player]:
    """
    Gather the settings and players for a game.
    :return: tuple[int, int | None, GF.Player, GF.Player]
    """
    GF.introduction()
    number_of_players = GF.get_player_count()
    difficulty = GF.select_difficulty() if number_of_players == 1 else None
    player_1, player_2 = create_players(number_of_players)

    GF.clear()
    print(f"{player_1.name} will be {Color.RED+player_1.symbol+Color.END}'s and "
          f"{player_2.name} will be {Color.RED+player_2.symbol+Color.END}'s.")
    return number_of_players, difficulty, player_1, player_2


def current_player(turn: int, player_1: GF.Player, player_2: GF.Player) -> GF.Player:
    """
    Determine whose turn it is.
    :param turn: The current turn number
    :param player_1: The first player
    :param player_2: The second player
    :return: GF.Player
    """
    if turn % 2 == 1:
        return player_1
    return player_2


def get_player_move(board: list[str], player: GF.Player, player_1: GF.Player,
                    number_of_players: int, difficulty: int | None) -> str:
    """
    Get the next move from either a human player or the computer.
    :param board: The current tic-tac-toe board
    :param player: The current player
    :param player_1: The human player in single-player mode
    :param number_of_players: Number of human players
    :param difficulty: Computer difficulty, if applicable
    :return: str
    """
    if number_of_players == 1 and player.name == "Computer Overlord":
        print("It is the Computer Overlord's turn.")
        sleep(1.0)
        return GF.comp_strat(board, player.symbol, player_1.symbol, difficulty or 2)

    print(f"It is {player.name}'s turn:")
    return GF.turn_input()


def get_valid_move(board: list[str], player: GF.Player, player_1: GF.Player,
                   number_of_players: int, difficulty: int | None) -> str:
    """
    Keep asking for a move until it is currently available.
    :param board: The current tic-tac-toe board
    :param player: The current player
    :param player_1: The human player in single-player mode
    :param number_of_players: Number of human players
    :param difficulty: Computer difficulty, if applicable
    :return: str
    """
    player_input = get_player_move(board, player, player_1, number_of_players, difficulty)
    GF.clear()

    while player_input not in GF.available_moves(board):
        print(GF.render_board(board))
        print(f"\nYou cannot select {player_input}. "
              "Please choose one of the numbered boxes from the board.")
        player_input = get_player_move(board, player, player_1, number_of_players, difficulty)
        GF.clear()

    return player_input


def play_game(number_of_players: int, difficulty: int | None,
              player_1: GF.Player, player_2: GF.Player) -> None:
    """
    Play one full game of tic-tac-toe.
    :param number_of_players: Number of human players
    :param difficulty: Computer difficulty, if applicable
    :param player_1: The first player
    :param player_2: The second player
    :return: None
    """
    board = GF.create_board()

    for turn in range(1, 10):
        print('\r'+GF.render_board(board))
        player = current_player(turn, player_1, player_2)
        player_input = get_valid_move(board, player, player_1, number_of_players, difficulty)
        board[int(player_input) - 1] = player.symbol

        winner = GF.check_win_condition(turn, board, player)
        if winner:
            print(winner)
            break
        sleep(1)

    print('\n'+GF.render_board(board))


def prompt_play_again() -> bool:
    """
    Ask whether the user wants another game.
    :return: bool
    """
    play_again = input(Color.RED+'''
    Press ANY KEY if you would like to play again
                       /OR/
                press ENTER to end.
                        '''+Color.END)
    return bool(play_again)


def main() -> None:
    """
    Run games until the user chooses to stop.
    :return: None
    """
    while True:
        number_of_players, difficulty, player_1, player_2 = setup_game()
        play_game(number_of_players, difficulty, player_1, player_2)
        if not prompt_play_again():
            break


if __name__ == "__main__":
    main()
