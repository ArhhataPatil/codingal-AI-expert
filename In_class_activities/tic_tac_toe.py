import random
from colorama import init, Fore, Style
init (autoreset=True)

def player_choice():
    symbol=''
    while symbol not in ['X','O']:
        symbol=input(f"{Fore.CYAN}Choose your symbol (X or O): "+ Style.RESET_ALL).upper()
        if symbol=="X":
            return ('X', 'O')
        else:
            return ('O', 'X')
def display(board):
            print()
            def colored(cell):
                if cell=='X':
                    return Fore.RED + cell + Fore.RESET
                elif cell=='O':
                    return Fore.BLUE + cell + Fore.RESET
                else:
                    return Fore.YELLOW + cell + Fore.RESET
            print(f"{colored(board[0])} | {colored(board[1])} | {colored(board[2])}")
            print("--+---+--")
            print(f"{colored(board[3])} | {colored(board[4])} | {colored(board[5])}")
            print("--+---+--")
            print(f"{colored(board[6])} | {colored(board[7])} | {colored(board[8])}")
            

def ttt():
    print(f"Welcome to Tic Tac Toe!")
    player_n=input("Enter your name! "+ Style.RESET_ALL)
    while True:
        board= ['1','2','3','4','5','6','7','8','9']
        player_s, AI_s=player_choice()
        turn='player'
        game_on=True

        while game_on:
            display(board)
            break
        break

if __name__=="__main__":
    ttt()

