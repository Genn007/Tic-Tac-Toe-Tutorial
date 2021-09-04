#  Учебная игра в крестики-нолики.
#  Код адаптирован из примера на GitHub xo.py

def draw_board(board):
    print ("  0 1 2")
    for i in range(3):
        print (i, board[0+i*3], board[1+i*3], board[2+i*3], )
    return

def init_board():
    b = list()
    for i in range(1,10):
        b.append('-')
    return b

def get_move(token,board, info):
    valid = False
    while not valid:
        answer = input("Ваш ход " + token + "? ")
        str_move = answer.split()
        if not(str_move[0] in "012" and str_move[1] in "012"):
            print("Некорректный ввод." + info)
        else:
            move = int(str_move[0])*3 + int(str_move[1])
#            print(move)
            if (str(board[move]) not in "XO"):
                board[move] = token
                valid = True
            else:
                print(" Эта клетка занята")
    return

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    winner = "-"
    for e in win_coord:
        if board[e[0]] == board[e[1]] == board[e[2]]:
            winner = board[e[0]]
            break
    if winner in "XO":
        return winner
    else:
        return False

def game(board):
    counter = 0
    win = False
    info = "\n Введите две цифры [0..2] через пробел: первая цифра - ряд, вторая - место в ряду  "
    while not win:
        draw_board(board)
        print(info)
        if counter % 2 == 0:
            get_move("X", board, info)
        else:
            get_move("O", board, info)
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)



board = init_board()
game(board)
