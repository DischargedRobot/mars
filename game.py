from cup import Cup
from table import Table

while True:
    step = int(input('Ващи действия?\n1) Бросить кубики\n2) Посмотреть количество кубиков\n'))
    if step == 1:
        table_game = Table()
        table_game.put_aside()
        print(f'Количество людей = {table_game.hand.count("человек")}\nКоличество куриц = {table_game.hand.count("курица")}\n'
              f'Количество коров = {table_game.hand.count("корова")}\nКоличество лазеров смерти = {table_game.hand.count("лазер")}\n'
              f'Количество танков = {table_game.table.count("танк")}')

        
