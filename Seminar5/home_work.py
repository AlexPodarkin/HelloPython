from random import randint

def task_1():
    text = 'Любви, надежды, тихой славы\
            Недолго нежил нас обман,\
            Исчезли юные забавы,\
            Как сон, как утренний туман;'
    result = list(filter(lambda i: 'а' not in i and 'б' not in i and 'в' not in i, text.split()))
    print(f'Результат выборки:  {result}')


def task_2():
    print('          ============xxx============')
    print('Игра с конфетами, человек против человека.')
    print('          ============xxx============')
    candy = 220             # количество конфет
    max_candy_round = 28    # за один ход можно забрать не более чем 28 конфет
    count = randint(1, 2)   # для рандомного определения того кто ходит первым
    print(f'Колво конфет:{candy}, за один ход можно забрать не более чем {max_candy_round} конфет')
    print('          ============xxx============')
    print(f'Итак!  монета брошена первым ходит {count} игрок!')
    print('          ============xxx============')
    while candy >= 0:
        if count == 1:
            print(f'       оставшееся количество конфет =', candy)
            a = int(input('1 Игрок введите кол-во конфет которое хотите забрать =>'))
            if a > max_candy_round:
                print('ИГРОК 1 играет не по правилам!!!') 
            candy -= a
            count = 2
            if candy <= 0:
                break
        else:
            print(f'       оставшееся количество конфет =', candy)
            b = int(input('2 Игрок введите кол-во конфет которое хотите забрать =>'))
            if b > max_candy_round:
                print('ИГРОК 2 играет не по правилам!!!') 
            candy -= b
            count = 1
            if candy <= 0:
                break

    if count == 2:
        print('1 ИГРОК WIIIN !!!')
    else:
        print('2 ИГРОК WIIIN !!!')


def task_3():
    initial_string = 'ggggfsssyyyyYYYYYffdfdsoooooooooooooo'
    print(initial_string)
    print('Изначальный размер строки:', len(initial_string))
    compression = ''
    count = 1
    for i in range(1, len(initial_string)):
        if initial_string[i] == initial_string[i - 1]:
            count += 1
        else :
            compression += str(count) + initial_string[i - 1]
            count = 1
    print(compression)
    print('Размер после сжатия:', len(compression))

#task_1()
task_2()
#task_3()
# что бы всегда побеждать в игре надо сначала взять 23 конфеты первому кто пойдет
# а затем добирать конфеты противника до 28шт, после этого на предпоследнем
# ходу останется 29конфет и противник не сможет добрать 1 конфету. Конфеты наши ;)
