# game.py
from gameparts import Board


from gameparts.exceptions import FieldIndexError

# Вот новая функция.
def main():
    game = Board()
    game.display()
    row = int(input('Введите номер строки: '))
    if row < 0 or row >= game.field_size:
        raise FieldIndexError('Введенное значение за границами игрового поля!')
    column = int(input('Введите номер столбца: '))
    if column < 0 or column >= game.field_size:
        raise FieldIndexError('Введенное значение за границами игрового поля!')
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()

# А вот вызов этой функции.
if __name__ == '__main__':
    main() 