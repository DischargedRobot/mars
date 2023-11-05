from cup import Cup
import cube

while True:
    step = int(input('Ващи действия?\n'))
    if step == 1:
        print(Cup().cast())