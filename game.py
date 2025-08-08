# game.py
from inspect import ismethod

from gameparts import Board

# Вот новая функция.
def main():
    game = Board()
    game.display()
    row = int(input('Введите номер строки: '))
    column = int(input('Введите номер столбца: '))
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()

# А вот вызов этой функции.
if __name__ == '__main__':
    main() 