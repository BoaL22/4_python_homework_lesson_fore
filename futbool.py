    # Задача FOOTBALL необязательная. Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

    # За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

    # Формат ввода следующий:
    # В первой строке указано целое число nn — количество завершенных игр.
    # После этого идет nn строк, в которых записаны результаты игры в следующем формате:
    # Первая команда - Забито первой командой; Вторая команда - Забито второй командой

    # Вывод программы необходимо оформить следующим образом:
    # Команда: Всего игр, Побед, Ничьих, Поражений, Всего очков

    # Конкретный пример ввода-вывода приведён ниже.

    # Порядок вывода команд произвольный.

    # Sample Input:

    # 3
    # Спартак;9;Зенит;10
    # Локомотив;12;Зенит;3
    # Спартак;8;Локомотив;15
    # Sample Output:

    # Спартак:2 0 0 2 0
    # Зенит:2 1 0 1 3
    # Локомотив:2 2 0 0 6


def name_team(number_game, teams):
    team_input = input(f' Кто играл в {number_game} игре? \n Зенит, Спартак или Локомотив?\n ')
    if team_input.lower() in teams:
        team_1 = team_input
        return team_1
    else:
        print('Введите название команды правильно! ')
        name_team(number_game, teams)


zenit = {'games': 0,'win': 0, 'draw': 0, 'loss': 0}
spartak = {'games': 0,'win': 0, 'draw': 0, 'loss': 0}
lokomotiv = {'games': 0,'win': 0, 'draw': 0, 'loss': 0}

teams = {'зенит': zenit, 'спартак': spartak, 'локомотив': lokomotiv}

number_games_1 = int(input(' Сколько игр было? '))
number_game = 1
while number_game <= number_games_1:
    team_1 = name_team(number_game, teams)
    team_1 = team_1.lower()
    teams[team_1]['games'] += 1

    team_2 = name_team(number_game, teams)
    team_2 = team_2.lower()
    teams[team_2]['games'] += 1

    goal_team_1 = int(input(f'Сколько голов забил {team_1}? '))
    goal_team_2 = int(input(f'Сколько голов забил {team_2}? '))

    if goal_team_1 == goal_team_2:
        teams[team_1]['draw'] += 1
        teams[team_2]['draw'] += 1

    elif goal_team_1 > goal_team_2:
        teams[team_1]['win'] += 1
        teams[team_2]['loss'] += 1

    elif goal_team_1 < goal_team_2:
        teams[team_1]['loss'] += 1
        teams[team_2]['win'] += 1

    number_game += 1

score_zenit = sum(zenit.values())
score_spartak = sum(spartak.values())
score_lokomotiv = sum(lokomotiv.values())

print(f'Зенит: {zenit["games"]} {zenit["win"]} {zenit["draw"]} {zenit["loss"]} {score_zenit}')
print(f'Спартак: {spartak["games"]} {spartak["win"]} {spartak["draw"]} {spartak["loss"]} {score_spartak}')
print(f'Локомотив: {lokomotiv["games"]} {lokomotiv["win"]} {lokomotiv["draw"]} {lokomotiv["loss"]} {score_lokomotiv}')