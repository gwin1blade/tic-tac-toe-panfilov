# крестики - нолики итоговое практическое задания B5.6 FPW 180 Панфилов
def play():
    print("Правила игры крестики - нолики")
    print("Ввод символов производиться по координатам X и Y")
    print("Удачи kekw")

def playing_field():  # рамка игрового поля
    print(f"   0  1  2")
    print(f"   _  _  _")
    for i in range(3):
        print(f"{i} | {board[i][0]} {board[i][1]} {board[i][2]}")


# playing_field()


def user_move():  # ввод пользователя
    print()
    while True:
        move = input("Ваш ход:").split()

        if len(move) != 2:
            print("Ошибка, введите две координаты:")
            continue

        x, y = move

        if not (x.isdigit()) or not (y.isdigit()):
            print("Ошибка, введите два числа:")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Ход неверный, попробуйте снова:")
            continue

        if board[x][y] != " ":
            print("Клетка занята, попробуйте снова:")
            continue

        return x, y


# user_move()

def win_(): # Проверка победных комбинаций
    win_comb =(((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for i in win_comb:
        symbols = []
        for j in i:
            symbols.append(board[j[0]][j[1]])
        if symbols == ["X", "X", "X"]:
            print("Победа крестиков")
            return True
        if symbols == ["0", "0", "0"]:
            print("Победа ноликов")
            return True
    return False
play()
board = [[" "] * 3 for i in range(3)]  # игровое поле

move_num = 0

while True: # ходы
    move_num += 1

    playing_field()

    if move_num % 2 == 1:
        print("Ход крестиков")
    else:
        print("Ход ноликов")

    x, y = user_move()

    if move_num % 2 == 1:
        board[x][y] = "X"
    else:
        board[x][y] = "0"

    if win_():
        break

    if move_num == 9:
        print("Ничья")
        break



