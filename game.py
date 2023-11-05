from cup import Cup
from table import Table

table_game = Table()

while True:
    step = int(input('Ващи действия?\n1) Бросить кубики\n2) Посмотреть количество кубиков\n'))
    if step == 1:
        table_game.put_aside()
        print(f'Количество людей = {table_game.hand.list_cup.count("человек")}\nКоличество куриц = {table_game.hand.list_cup.count("курица")}\n'
              f'Количество коров = {table_game.hand.list_cup.count("корова")}\nКоличество лазеров смерти = {table_game.hand.list_cup.count("лазер")}\n'
              f'Количество танков = {table_game.table.count("танк")}')

        
