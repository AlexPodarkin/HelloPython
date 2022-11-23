
def What_day_off():
    day_of_week = int(input('введите число(день недели): '))
    if day_of_week == 1 or day_of_week == 2 or day_of_week == 3 or day_of_week == 4 or day_of_week == 5:
        print('будний день :(')
    elif day_of_week == 6 or day_of_week == 7:
        print('Ура! ВЫХОНОЙ :)')
    else:
        print('некорректный ввод!')


def truth_test():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)


def coordinate_check():
    x = int(input('введите координату x: '))
    y = int(input('введите координату y: '))
    if x > 0 and y > 0:
        print('точка находится в 1 четверти! ')
    elif x < 0 and y > 0:
        print('точка находится в 2 четверти! ')
    elif x < 0 and y < 0:
        print('точка находится в 3 четверти! ')
    else:
        print('точка находится в 4 четверти! ')

def quarter_check():
    quarter = int(input('введите номер четверти: '))
    if quarter == 1:
        print('диапазон х=0 +∞, y=0 +∞')
    elif quarter == 2:
        print('диапазон х=0 -∞, y=0 +∞')
    elif quarter == 3:
        print('диапазон х=0 -∞, y=0 -∞')
    else:
        print('диапазон х=0 +∞, y=0-∞')


def distance_between_points():
    x1 = float(input('введите координату x1: '))
    y1 = float(input('введите координату y1: '))
    x2 = float(input('введите координату x2: '))
    y2 = float(input('введите координату y2: '))
    result = ((x2-x1)**2 + (y2-y1)**2)**0.5         # также короньможно извлеч с помощю метода math.sqrt()
    result = round(result, 3)                       # округление до 3 знаков
    print(f'Расстояние между точками в пространстве = {result}')

What_day_off()
truth_test()
coordinate_check()
quarter_check()
distance_between_points()  # сделал методами для вашего удобства.


