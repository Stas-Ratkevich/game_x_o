def start_game(game):
    player_1 = input("Игрок-1 выберите символ (х или о): ")         # Игрок-1 выбирает символ.
    if player_1 in set("хx"):                                       # Игрок-2 получает противоположный символ.
        player_2 = "o"                                              # (используется set чтобы отличать русские
    else:                                                           # и английские символы).
        player_2 = "x"
    if player_1 in set("xoхо") and player_2 in set("xoхо"):         # Проверяется правильность введения символов.
        game(player_1, player_2)                                    # Если все правильно начинается игра!
    else:
        print("Выбраны недопустимые для игры символы!")             # Предупреждение, что выбраны неверные символы.


def winner(game_list):                                              # Функция провекрки выигрышной комбинации.
    if game_list[1][1] == game_list[1][2] == game_list[1][3] != "-" or game_list[1][1] == game_list[2][1] == game_list[3][1] != "-":
        print(f"Игра окончена!\nПОБЕДИЛИ - {game_list[1][1]}")
        return True
    elif game_list[2][1] == game_list[2][2] == game_list[2][3] != "-" or game_list[1][2] == game_list[2][2] == game_list[3][2] != "-":
        print(f"Игра окончена!\nПОБЕДИЛИ - {game_list[2][2]}")
        return True
    elif game_list[3][1] == game_list[3][2] == game_list[3][3] != "-" or game_list[1][3] == game_list[2][3] == game_list[3][3] != "-":
        print(f"Игра окончена!\nПОБЕДИЛИ - {game_list[3][3]}")
        return True
    elif game_list[1][1] == game_list[2][2] == game_list[3][3] != "-" or game_list[3][1] == game_list[2][2] == game_list[1][3] != "-":
        print(f"Игра окончена!\nПОБЕДИЛИ - {game_list[2][2]}")
        return True
    else:
        return False


def game(player_1, player_2):                                       # Функция, описывающая ход игры.
    count = 1                                                       # Cчетчик количества ходов, их не больше 5.
    while count < 6:                                                # Цикл игры.
        item_1 = list(input(f"\nИгрок-1 введите координаты - {player_1}: "))      # Игрок-1 вводит координаты символа.
        game_list[int(item_1[0])][int(item_1[2])] = player_1        # На поле по указанным координатам меняется символ.
        if count < 5:                                               # На 5 ходу на поле остается только 1 место,
            item_2 = list(input(f"Игрок-2 введите координаты - {player_2}: "))    # запрос у второго игрока не нужен.
            game_list[int(item_2[0])][int(item_2[2])] = player_2
        print(f"""{"".center(57,"-")}     
#   1   2   3
1   {game_list[1][1]}   {game_list[1][2]}   {game_list[1][3]}            Ход {count}
2   {game_list[2][1]}   {game_list[2][2]}   {game_list[2][3]}            Игрок-1 играет {player_1}
3   {game_list[3][1]}   {game_list[3][2]}   {game_list[3][3]}            Игрок-2 играет {player_2}
{"".center(57,"-")}""")                                             # На поле ставятся отметки по указанным координатам.
        if winner(game_list):                                       # Проверяется наличие на поле выигрышной комбинации.
            count = 6                                               # Если комбинация есть цикл завершается.
        elif not winner(game_list) and count == 5:                  # Если на 5 ходу выигрыша нет, тогда - ничья.
            print("Игра окончена\nНИЧЬЯ")
        count += 1


game_list = [['#', 1, 2, 3],
             [1, '-', '-', '-'],
             [2, '-', '-', '-'],
             [3, '-', '-', '-']]
print(f"""{"ПРАВИЛА".center(57,"*")}\n                              
1. Выберите символ для игры (второму игроку назначется
противоположный автоматически.)
2. Укажите через пробел строку поля, а затем столбец поля,
на пересечении которых хотите поставить свой символ.
2. Побеждает тот игрок, который первым выстроит в линию 3
одинаковых символа.\n
{"ИГРОВОЕ ПОЛЕ".center(57,"*")}\n  
#   1   2   3
1   {game_list[1][1]}   {game_list[1][2]}   {game_list[1][3]}            (Информация о номере хода)
2   {game_list[2][1]}   {game_list[2][2]}   {game_list[2][3]}            (Символ, выбранный Игроком-1)
3   {game_list[3][1]}   {game_list[3][2]}   {game_list[3][3]}            (Символ, выбранный Игроком-1)\n
{"ИГРА".center(57,"*")}\n""")
start_game(game)
