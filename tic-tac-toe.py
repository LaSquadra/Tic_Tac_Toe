#!/usr/bin/env python3
import game_functions as GF
from color_module import Color
from time import sleep
from random import randint


def main():
    # intro and variable assignment
    GF.introduction()
    number_of_players = GF.get_player_count()
    # single-player player assignment
    if number_of_players == 1:
        difficulty = GF.select_difficulty()
        player_1 = GF.Player("Who dares challenge the Computer Overlord? ", "X")
        player_2 = GF.Player("Computer Overlord", "O")
    # two-player player assignment
    else:
        player_1 = GF.Player("Who is player 1? ", "X")
        player_2 = GF.Player("Who is player 2? ", "O")
    GF.clear()
    print(f"{player_1.name} will be {Color.RED+player_1.symbol+Color.END}'s and "
          f"{player_2.name} will be {Color.RED+player_2.symbol+Color.END}'s.")
    grid_string = "_1_|_2_|_3_\n_4_|_5_|_6_\n 7 | 8 | 9 "  # initial grid

    # Start of application:
    for i in range(1, 10):
        if i < 10:
            turn = i
            print('\r'+grid_string)
            # Determining turns and player_variables
            if turn % 2 == 1:
                player = player_1
                print(f"It is {player.name}'s turn:")
                player_input = GF.turn_input()
            elif number_of_players == 1:   # creating option for single player mode
                player = player_2
                print("It is the Computer Overloard's turn.")
                sleep(1.0)
                if difficulty == 1:
                    player_input = str(randint(1, 9))
                    while str(player_input) not in grid_string:
                        player_input = str(randint(1, 9))
                elif difficulty == 2:
                    player_input = GF.comp_strat(grid_string)
            else:
                player = player_2
                print(f"It is {player}'s turn:")
                player_input = GF.turn_input()
            GF.clear()

            # Creating controls to prevent previously selected boxes from being used again
            while player_input not in ("1", "2", "3", "4", "5", "6", "7", "8", "9") or player_input not in grid_string:
                print(grid_string)
                if turn % 2 == 0:
                    comp_move = randint(1, 9)
                    player_input = str(comp_move)
                else:    
                    print(f"\nYou cannot select {player_input}. "
                          "Please choose one of the numbered boxes from the board.")
                    player_input = input("Where would you like to play? ")
                GF.clear()
            else:
                grid_string = grid_string.replace(str(player_input), player.symbol)
                winner = GF.check_win_condition(i, grid_string, player)
                if winner:
                    print(winner)
                    break
                sleep(1)
            i += 1

    # End of application:
    print('\n'+grid_string)
    play_again = input(Color.RED+'''
    Press ANY KEY if you would like to play again
                       /OR/
                press ENTER to end. 
                        ''')
    if play_again:
        main()
    else:
        exit(0)


if __name__ == "__main__":
    main()
