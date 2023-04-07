#!/usr/bin/env python3
def clear():
    from os import system, name
    if name =="nt":
        _=system("cls")
    else:
        _=system("clear")
def introduction():
    import time
    clear()
    print(color.RED+'''
             #   # ##### #     #      ####
             #   # #     #     #     #    #
             ##### ###   #     #     #    #
             #   # #     #     #     #    #
             #   # ##### ##### #####  ####
 '''+color.END)
    time.sleep(1)
    clear()
    print(color.GREEN+'''
                   #    #     #  #####
                  # #   # #   #  #    #
                 # # #  #   # #  #    #
                #     # #     #  ##### 
 '''+color.END)
    time.sleep(0.6)
    clear()
    print(color.RED+'''
 #  #  #  ###### #       #####   ####   #     #  ######
 #  #  #  #      #      #       #    #  # # # #  #
 #  #  #  ###    #      #       #    #  #  #  #  ####
 #  #  #  #      #      #       #    #  #     #  #
 ## ##   ######  #####  #####   ####   #     #  ######
 '''+color.END)
    time.sleep(1)
    clear()
    print(color.GREEN+"Welcome to Ryan's", color.RED+"Tic-Tac-Toe!"+color.END, color.GREEN+"GLHF!\n"+color.END) #Greeting Message
def comp_strat(grid_string):
    if grid_string[17]=="5":
        return "5"
    elif grid_string[1]==grid_string[5] and grid_string[9]=="3":  #1
        return "3"
    elif grid_string[9]==grid_string[1] and grid_string[5]=="2": #1
        return "2"
    elif grid_string[9]==grid_string[5] and grid_string[1]=="1": #1
        return "1"
    elif grid_string[13]==grid_string[17] and grid_string[21]=="6": #2
        return "6"
    elif grid_string[21]==grid_string[17] and grid_string[13]=="4": #2
        return "4"
    elif grid_string[25]==grid_string[29] and grid_string[33]=="9": #3
        return "9"
    elif grid_string[33]==grid_string[25] and grid_string[29]=="8": #3
        return "8"
    elif grid_string[33]==grid_string[29] and grid_string[25]=="7": #3
        return "7"
    elif grid_string[1]==grid_string[13] and grid_string[25]=="7": #4
        return "7"
    elif grid_string[25]==grid_string[1] and grid_string[13]=="4": #4
        return "4"
    elif grid_string[25]==grid_string[13] and grid_string[1]=="1": #4
        return"1"
    elif grid_string[5]==grid_string[17] and grid_string[29]=="8": #5
        return "8"
    elif grid_string[29]==grid_string[17] and grid_string[5]=="2": #5
        return "2"
    elif grid_string[9]==grid_string[21] and grid_string[33]=="9": #6
        return "9"
    elif grid_string[33]==grid_string[9] and grid_string[21]=="6": #6
        return "6"
    elif grid_string[33]==grid_string[21] and grid_string[9]=="3": #6
        return "3"
    elif grid_string[1]==grid_string[17] and grid_string[33]=="9": #7
        return "9"
    elif grid_string[33]==grid_string[17] and grid_string[1]=="1": #7
        return "1"
    elif grid_string[9]==grid_string[17] and grid_string[25]=="7": #8
        return "7"
    elif grid_string[25]==grid_string[17] and grid_string[9]=="3": #8
        return "3"
class color: #Attempting to add some flare to the game
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

def main():
   #intro and variable assignment
    introduction() 
    import time
    from random import randint
    number_of_players=input("Select number of players: (1-2) ") #initializing single vs two player mode
    
    while str(number_of_players) not in "12": #sanitizing player number selection input
        number_of_players=input("Please select either '1' or '2': ")
    if int(number_of_players)==1: #single-player player assignment
        difficulty=input("Select a difficulty level: (1-2) ") #creating dificulty levels
        while str(difficulty) not in "12": #sanitizing difficulty selection input
            difficulty=input("Please select either '1' or '2': ")
        player_1=input("Who dares challenge the Computer Overlord? ")
        player_2="Computer Overlord"
    else: #two-player player assignment
        player_1=input("Who is player 1? ")
        player_2=input("Who is player 2? ")
    clear()
    player_1_symbol="X"
    player_2_symbol="O"
    print(f"{player_1} will be {color.RED+player_1_symbol+color.END}'s and {player_2} will be {color.RED+player_2_symbol+color.END}'s.")
    grid_string="_1_|_2_|_3_\n_4_|_5_|_6_\n 7 | 8 | 9 "  #initial grid
   #Start of application:
    for i in range(1,10):
        if i<10:
            turn=i
            print('\r'+grid_string,end='')
            print()
           #Determining turns and player_variables 
            if turn%2==1:    
                player=player_1
                print(f"It is {player}'s turn:")
                player_symbol=player_1_symbol
                player_input=input("Where would you like to play? ")
            elif int(number_of_players)==1:   #creating option for single player mode
                player=player_2
                print("It is the Computer Overloard's turn.")
                time.sleep(1.0)
                player_symbol=player_2_symbol
                if difficulty=="1":
                    player_input=str(randint(1,9))
                    while str(player_input) not in grid_string:
                        player_input=str(randint(1,9))
                elif difficulty=="2":
                    player_input=comp_strat(grid_string)
            else:
                player=player_2
                print(f"It is {player}'s turn:")
                player_symbol=player_2_symbol
                player_input=input("Where would you like to play? ")
            clear()
           #Creating controls to prevent previously selected boxes from being used again
            while player_input not in ("1","2","3","4","5","6","7","8","9") or player_input not in grid_string:
                print(grid_string)
                if turn%2==0:
                    comp_move=randint(1,9)
                    player_input=str(comp_move)
                else:    
                    print(f"\nYou cannot select {player_input}. Please choose one of the numbered boxes from the board.")
                    player_input=input("Where would you like to play? ")
                clear()
            else:
                grid_string=grid_string.replace(str(player_input),player_symbol)         
           #Creating Win Conditions:    
            #Grid index locations---> 1=1, 2=5, 3=9, 4=13, 5=17, 6=21, 7=25, 8=29, 9=33
            if grid_string[1]==player_symbol and grid_string[5]==player_symbol and grid_string[9]==player_symbol:      # top row win
                print(f"Taking the W right across the top, {color.RED+player+color.END} pulled it out in the end.")
                break
            elif grid_string[13]==player_symbol and grid_string[17]==player_symbol and grid_string[21]==player_symbol: # middle row win
                print(f"{color.RED+player+color.END} snatched the victory strait through the middle.  How embarassing.")
                break
            elif grid_string[25]==player_symbol and grid_string[29]==player_symbol and grid_string[33]==player_symbol: # bottom row win
                print(f"Clutching the W with a sweep across the bottom!  {color.RED+player+color.END} wins!")
                break
            elif grid_string[1]==player_symbol and grid_string[13]==player_symbol and grid_string[25]==player_symbol:  # left colum win
                print(f"Holding firm to that left colum to secure the win, {color.BLUE+player+color.END} takes it!")
                break
            elif grid_string[5]==player_symbol and grid_string[17]==player_symbol and grid_string[29]==player_symbol:  # middle colum win
                print(f"Taking the W right down the middle: {color.BLUE+player+color.END}")
                break
            elif grid_string[9]==player_symbol and grid_string[21]==player_symbol and grid_string[33]==player_symbol:  # right colum win
                print(f"End of the line for you.  {color.BLUE+player+color.END} just took the far right colum!")
                break
            elif grid_string[1]==player_symbol and grid_string[17]==player_symbol and grid_string[33]==player_symbol:  # \ win
                print(f"Dang, I bet you didn't even see that coming!  {color.GREEN+player+color.END} just took your down like a bishop taking a pawn!")
                break
            elif grid_string[9]==player_symbol and grid_string[17]==player_symbol and grid_string[25]==player_symbol:  # / win
                print(f"That is it, {color.GREEN+player+color.END} emerged victorious with a nice slash across the board.")
                break
            elif i==9:
                print("A draw?")
                print("\nYou are either pretty good or really bad.  I just really don't want to watch you struggle through that again.")
                time.sleep(1)
           #finishing "if i<10:" <--added for visual compression formatting
            i+=1
   #End of application: 
    print('\n'+grid_string)
    play_again=input(color.RED+'''
    Press ANY KEY if you would like to play again
                       /OR/
                press CTR+C to end. 
                        ''')
    if play_again=="y" or "Y":
        main()
if __name__=="__main__":
    main()
