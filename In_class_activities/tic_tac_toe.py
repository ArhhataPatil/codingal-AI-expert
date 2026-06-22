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

def player_move(board, player_symbol):
     move=-1
     while move not in range(1,9) or board[move-1].isdigit():
          try:
               move=int(input("Tnter yiur number (1-9):"))
               if move not in range (1,10) or not board[move-1].isdigit():
                    print("Invalid move. Please try again.")
          except:
               print("Invalid input. Please enter a number between 1 and 9.")
     board[move-1]=player_symbol

def Ai_move(board, ai_symbol,player_symbol):
     for i in range (9):
          if board[i].isdigit():
               board_copy=board.copy()
               board_copy[i]=player_symbol
               if check_win(board_copy, player_symbol):
                      board[i]=ai_symbol
                      return
     for i in range(9):
          if board[i].isdigit():
               board_copy=board.copy()
               board_copy[i]=ai_symbol
               if check_win(board_copy, ai_symbol):
                    board[i]=ai_symbol
                    return
     possible_moves=[i for i in range(9) if board[i].isdigit()]
     move=random.choice(possible_moves)
     board[move]=ai_symbol

def check_win(board, symbol):
     win_conditions=[
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
]
         for condition in win_conditions:
            if board[condition[0]] == board[condition[1]] == board[condition[2]]==symbol:
                    return True
        return False
                 


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
            if turn=='player':
                player_move(board, player_s)
                if check_win(board, player_s):
                    display(board)
                    print(f"Congratulations {player_n}! You win!")
                    game_on=False
                else:
                    if check_full(board):
                        display(board)
                        print("It's a tie!")
                    else:
                        turn='AI'

                else:
                    ai_move(board,ai_symbol, player_symbol)
                    if check_win(board, ai_symbol):
                        display(board)
                        print(f"Sorry {player_n}, the AI wins!")
                        game_on=False
                else:
            
        

if __name__=="__main__":
    ttt()

