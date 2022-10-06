from random import randint, choice
from exception import PlaneException
import unittest


class MoveComputer:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer
        self._moves = list()
        self._last = -1
        self._list_x = list()

    def move(self):
        """
        the move of the computer (computer remembers every move)
        if first move -> computer moves randomly
        if second move -> computer checks the outcome of the last move
                                    if X -> moves in randomly NEAR the last move
                                    if O or C -> computer moves randomly
        if third or more -> computer checks the outcome of the last move
                                    if X -> moves in randomly NEAR the last move
                                    if C -> computer moves randomly
                                    if O -> computer checks the list of Xs (any move that resulted into an X)
                                            and makes the next move accordingly
                                            (checks if there is a 'C' in the proximity or if the proximity is all full)
        :return: the row and the column of the move
        """
        nr_moves = len(self._moves)
        last_x = 0
        if nr_moves == 0:
            square = self.move_random()
            row = square[0]
            col = square[1]
            self._moves.append([row, col])
            self._player.move(row, col)
        elif nr_moves == 1:
            last_move = self._moves[nr_moves - 1]
            row = last_move[0]
            col = last_move[1]
            if self._player._data[row][col] == 'O' or self._player._data[row][col] == 'C':
                #print("OorC")
                square = self.move_random()
                row = square[0]
                col = square[1]
                self._moves.append([row, col])
                self._player.move(row, col)
            else:
                self._last = nr_moves - 1
                self._list_x.append(self._last)
                last_x = self._moves[self._last]
                #print("elseOorC")
                if self.verify_cabin(row, col):
                    square = self.move_random()
                else:
                    square = self.choose_square(row, col)
                row = square[0]
                col = square[1]
                self._moves.append([square[0], square[1]])
                self._player.move(square[0], square[1])
        else:
            last_move = self._moves[nr_moves - 1]
            row = last_move[0]
            col = last_move[1]

            if self._player._data[row][col] == 'O':
                #print("O")
                #print(self._last)
                if self._last != -1:
                    last_x = self._moves[self._last]
                    if self.is_last_x_full(last_x[0], last_x[1]):
                        last_x = self._moves[self._last - 1]

                    #print(last_x)
                    if self.verify_cabin(last_x[0], last_x[1]):
                        square = self.move_random()
                    else:
                        square = self.choose_square(last_x[0], last_x[1])
                    empty_list = self._player.empty_squares()
                    i = 0
                    k = 0
                    while i == 0:
                        for sq in empty_list:
                            if int(sq[0]) == int(square[0]) and int(sq[1]) == int(square[1]):
                                i = 1
                        if i == 0:
                            k += 1
                            square = self.choose_square(last_x[0], last_x[1])
                        if k == 9:
                            square = self.move_random()
                            #print("OX-else-random")
                            break
                    #print(square)
                else:
                    square = self.move_random()
                #print(square)
                row = square[0]
                col = square[1]
                self._moves.append([square[0], square[1]])
                self._player.move(square[0], square[1])

            elif self._player._data[row][col] == 'X':
                #print("X")
                self._last = nr_moves - 1
                #print(self._last)
                last_x = self._moves[self._last]
                if self.verify_cabin(row, col):
                    square = self.move_random()
                else:
                    square = self.choose_square(row, col)
                empty_list = self._player.empty_squares()
                i = 0
                k = 0
                #print(square)
                while i == 0:
                    for sq in empty_list:
                        if int(sq[0]) == int(square[0]) and int(sq[1]) == int(square[1]):
                            i = 1
                    if i == 0:
                        k += 1

                        square = self.choose_square(row, col)
                        #print(square)
                    if k == 9:
                        square = self.move_random()
                        #print("OX-else-random")
                        break
                #print(square)
                row = square[0]
                col = square[1]
                self._moves.append([square[0], square[1]])
                self._player.move(square[0], square[1])

            else:
                #print("else-random")
                square = self.move_random()
                row = square[0]
                col = square[1]
                self._moves.append([row, col])
                self._player.move(row, col)
        return row, col

    def is_last_x_full(self, row, col):
        if self._player._data[row][col + 1] == ' ' or self._player._data[row][col - 1] == ' ' \
                or self._player._data[row - 1][col - 1] == ' ' \
                or self._player._data[row - 1][col] == ' ' or self._player._data[row - 1][col + 1] == ' ' \
                or self._player._data[row + 1][col - 1] == ' ' or self._player._data[row + 1][col] == ' ' \
                or self._player._data[row + 1][col + 1] == ' ':
            return False
        else:
            return True

    def choose_square(self, row, col):
        """
        chooses a cell in the proximity of the last X
        :param row: the row of the last X
        :param col: the column of the last X
        :return: the row and the column of the next move to be made
        """
        #print("choose", row, col)
        if 0 < row < 9:
            row_list = (row - 1, row, row + 1)
            row = choice(row_list)
        elif row == 0:
            row_list = (row, row + 1)
            row = choice(row_list)
        elif row == 9:
            row_list = (row - 1, row)
            row = choice(row_list)

        if 0 < col < 9:
            col_list = (col - 1, col, col + 1)
            col = choice(col_list)
        elif col == 0:
            col_list = (col, col + 1)
            col = choice(col_list)
        elif col == 9:
            col_list = (col - 1, col)
            col = choice(col_list)
        #print("choosefin", row, col)
        return [row, col]

    def move_random(self):
        """
        chooses randomly a square from the list of empty squares
        :return:
        """
        empty_list = self._player.empty_squares()
        square = choice(empty_list)
        return square

    def verify_cabin(self, row, col):
        """
        verifies whether an X is near a C or not
        (to make sure the X we are about to make a move near is not from an already crushed plane)
        :param row: the row
        :param col: the col
        :return: True/False
        """
        i = 0
        if row > 1 and row < 8:
            if col == 0:
                if self._player._data[row - 2][col] == 'C' or self._player._data[row - 2][col + 1] == 'C' \
                        or self._player._data[row - 2][col + 2] == 'C' \
                        or self._player._data[row - 1][col] == 'C' or self._player._data[row - 1][col + 1] == 'C' \
                        or self._player._data[row - 1][col + 2] == 'C' \
                        or self._player._data[row][col] == 'C' or self._player._data[row][col + 1] == 'C' \
                        or self._player._data[row][col + 2] == 'C' \
                        or self._player._data[row + 1][col] == 'C' or self._player._data[row + 1][col + 1] == 'C' \
                        or self._player._data[row + 1][col + 2] == 'C' \
                        or self._player._data[row + 2][col] == 'C' or self._player._data[row + 2][col + 1] == 'C' \
                        or self._player._data[row + 2][col + 2] == 'C':
                    i = 1
            elif col == 9:
                if self._player._data[row - 2][col - 2] == 'C' or self._player._data[row - 2][col - 1] == 'C' \
                        or self._player._data[row - 2][col] == 'C' \
                        or self._player._data[row - 1][col - 2] == 'C' or self._player._data[row - 1][col - 1] == 'C' \
                        or self._player._data[row - 1][col] == 'C' \
                        or self._player._data[row][col - 2] == 'C' or self._player._data[row][col - 1] == 'C' \
                        or self._player._data[row][col] == 'C' \
                        or self._player._data[row + 1][col - 2] == 'C' or self._player._data[row + 1][col - 1] == 'C' \
                        or self._player._data[row + 1][col] == 'C' \
                        or self._player._data[row + 2][col - 2] == 'C' or self._player._data[row + 2][col - 1] == 'C' \
                        or self._player._data[row + 2][col] == 'C':
                    i = 1
            elif col == 1:
                if self._player._data[row - 2][col - 2] == 'C' or self._player._data[row - 2][col - 1] == 'C' \
                        or self._player._data[row - 2][col] == 'C' or self._player._data[row - 2][col + 1] == 'C' \
                        or self._player._data[row - 1][col - 2] == 'C' or self._player._data[row - 1][col - 1] == 'C' \
                        or self._player._data[row - 1][col] == 'C' or self._player._data[row - 1][col + 1] == 'C' \
                        or self._player._data[row][col - 2] == 'C' or self._player._data[row][col - 1] == 'C' \
                        or self._player._data[row][col] == 'C' or self._player._data[row][col + 1] == 'C' \
                        or self._player._data[row + 1][col - 2] == 'C' or self._player._data[row + 1][col - 1] == 'C' \
                        or self._player._data[row + 1][col] == 'C' or self._player._data[row + 1][col + 1] == 'C' \
                        or self._player._data[row + 2][col - 2] == 'C' or self._player._data[row + 2][col - 1] == 'C' \
                        or self._player._data[row + 2][col] == 'C' or self._player._data[row + 2][col + 1] == 'C':
                    i = 1
            elif col == 8:
                if self._player._data[row - 2][col - 2] == 'C' or self._player._data[row - 2][col - 1] == 'C' \
                        or self._player._data[row - 2][col] == 'C' or self._player._data[row - 2][col + 1] == 'C' \
                        or self._player._data[row - 1][col - 2] == 'C' or self._player._data[row - 1][col - 1] == 'C' \
                        or self._player._data[row - 1][col] == 'C' or self._player._data[row - 1][col + 1] == 'C' \
                        or self._player._data[row][col - 2] == 'C' or self._player._data[row][col - 1] == 'C' \
                        or self._player._data[row][col] == 'C' or self._player._data[row][col + 1] == 'C' \
                        or self._player._data[row + 1][col - 2] == 'C' or self._player._data[row + 1][col - 1] == 'C' \
                        or self._player._data[row + 1][col] == 'C' or self._player._data[row + 1][col + 1] == 'C' \
                        or self._player._data[row + 2][col - 2] == 'C' or self._player._data[row + 2][col - 1] == 'C' \
                        or self._player._data[row + 2][col] == 'C' or self._player._data[row + 2][col + 1] == 'C':
                    i = 1
            else:
                if self._player._data[row - 2][col - 2] == 'C' or self._player._data[row - 2][col - 1] == 'C' \
                        or self._player._data[row - 2][col] == 'C' or self._player._data[row - 2][col + 1] == 'C' \
                        or self._player._data[row - 2][col + 2] == 'C' \
                        or self._player._data[row - 1][col - 2] == 'C' or self._player._data[row - 1][col - 1] == 'C' \
                        or self._player._data[row - 1][col] == 'C' or self._player._data[row - 1][col + 1] == 'C' \
                        or self._player._data[row - 1][col + 2] == 'C' \
                        or self._player._data[row][col - 2] == 'C' or self._player._data[row][col - 1] == 'C' \
                        or self._player._data[row][col] == 'C' or self._player._data[row][col + 1] == 'C' \
                        or self._player._data[row][col + 2] == 'C' \
                        or self._player._data[row + 1][col - 2] == 'C' or self._player._data[row + 1][col - 1] == 'C' \
                        or self._player._data[row + 1][col] == 'C' or self._player._data[row + 1][col + 1] == 'C' \
                        or self._player._data[row + 1][col + 2] == 'C' \
                        or self._player._data[row + 2][col - 2] == 'C' or self._player._data[row + 2][col - 1] == 'C' \
                        or self._player._data[row + 2][col] == 'C' or self._player._data[row + 2][col + 1] == 'C' \
                        or self._player._data[row + 2][col + 2] == 'C':
                    i = 1
        elif row == 0:
            if col == 0:
                if self._player._data[row + 2][col + 2] == 'C':
                    i = 1
            elif col == 9:
                if self._player._data[row - 2][col - 2] == 'C':
                    i = 1
            elif col == 1:
                if self._player._data[row][col - 1] == 'C' or self._player._data[row][col + 2] == 'C' \
                        or self._player._data[row][col] == 'C' or self._player._data[row][col + 1] == 'C' \
                        or self._player._data[row + 1][col - 1] == 'C' or self._player._data[row + 1][col + 2] == 'C' \
                        or self._player._data[row + 1][col] == 'C' or self._player._data[row + 1][col + 1] == 'C' \
                        or self._player._data[row + 2][col - 1] == 'C' or self._player._data[row + 2][col + 2] == 'C' \
                        or self._player._data[row + 2][col] == 'C' or self._player._data[row + 2][col + 1] == 'C':
                    i = 1
            elif col == 8:
                if self._player._data[row][col - 2] == 'C' or self._player._data[row][col - 1] == 'C' \
                        or self._player._data[row][col] == 'C' or self._player._data[row][col + 1] == 'C' \
                        or self._player._data[row + 1][col - 2] == 'C' or self._player._data[row + 1][col - 1] == 'C' \
                        or self._player._data[row + 1][col] == 'C' or self._player._data[row + 1][col + 1] == 'C' \
                        or self._player._data[row + 2][col - 2] == 'C' or self._player._data[row + 2][col - 1] == 'C' \
                        or self._player._data[row + 2][col] == 'C' or self._player._data[row + 2][col + 1] == 'C':
                    i = 1
            else:
                if self._player._data[row][col - 2] == 'C' or self._player._data[row][col - 1] == 'C' \
                        or self._player._data[row][col] == 'C' or self._player._data[row][col + 1] == 'C' \
                        or self._player._data[row][col + 2] == 'C' \
                        or self._player._data[row + 1][col - 2] == 'C' or self._player._data[row + 1][col - 1] == 'C' \
                        or self._player._data[row + 1][col] == 'C' or self._player._data[row + 1][col + 1] == 'C' \
                        or self._player._data[row + 1][col + 2] == 'C' \
                        or self._player._data[row + 2][col - 2] == 'C' or self._player._data[row + 2][col - 1] == 'C' \
                        or self._player._data[row + 2][col] == 'C' or self._player._data[row + 2][col + 1] == 'C' \
                        or self._player._data[row + 2][col + 2] == 'C':
                    i = 1
        elif row == 1:
            if col == 0:
                if self._player._data[row][col + 2] == 'C':
                    i = 1
            elif col == 9:
                if self._player._data[row][col - 2] == 'C':
                    i = 1
            elif col == 1:
                if self._player._data[row - 1][col - 1] == 'C' \
                        or self._player._data[row - 1][col] == 'C' or self._player._data[row - 1][col + 1] == 'C' \
                        or self._player._data[row - 1][col + 2] == 'C' \
                        or self._player._data[row][col - 1] == 'C' \
                        or self._player._data[row][col] == 'C' or self._player._data[row][col + 1] == 'C' \
                        or self._player._data[row][col + 2] == 'C' \
                        or self._player._data[row + 1][col - 1] == 'C' \
                        or self._player._data[row + 1][col] == 'C' or self._player._data[row + 1][col + 1] == 'C' \
                        or self._player._data[row + 1][col + 2] == 'C' \
                        or self._player._data[row + 2][col - 1] == 'C' \
                        or self._player._data[row + 2][col] == 'C' or self._player._data[row + 2][col + 1] == 'C' \
                        or self._player._data[row + 2][col + 2] == 'C':
                    i = 1
            elif col == 8:
                if self._player._data[row - 1][col - 2] == 'C' or self._player._data[row - 1][col - 1] == 'C' \
                        or self._player._data[row - 1][col] == 'C' or self._player._data[row - 1][col + 1] == 'C' \
                        or self._player._data[row][col - 2] == 'C' or self._player._data[row][col - 1] == 'C' \
                        or self._player._data[row][col] == 'C' or self._player._data[row][col + 1] == 'C' \
                        or self._player._data[row + 1][col - 2] == 'C' or self._player._data[row + 1][col - 1] == 'C' \
                        or self._player._data[row + 1][col] == 'C' or self._player._data[row + 1][col + 1] == 'C' \
                        or self._player._data[row + 2][col - 2] == 'C' or self._player._data[row + 2][col - 1] == 'C' \
                        or self._player._data[row + 2][col] == 'C' or self._player._data[row + 2][col + 1] == 'C':
                    i = 1
            else:
                if self._player._data[row - 1][col - 2] == 'C' or self._player._data[row - 1][col - 1] == 'C' \
                        or self._player._data[row - 1][col] == 'C' or self._player._data[row - 1][col + 1] == 'C' \
                        or self._player._data[row - 1][col + 2] == 'C' \
                        or self._player._data[row][col - 2] == 'C' or self._player._data[row][col - 1] == 'C' \
                        or self._player._data[row][col] == 'C' or self._player._data[row][col + 1] == 'C' \
                        or self._player._data[row][col + 2] == 'C' \
                        or self._player._data[row + 1][col - 2] == 'C' or self._player._data[row + 1][col - 1] == 'C' \
                        or self._player._data[row + 1][col] == 'C' or self._player._data[row + 1][col + 1] == 'C' \
                        or self._player._data[row + 1][col + 2] == 'C' \
                        or self._player._data[row + 2][col - 2] == 'C' or self._player._data[row + 2][col - 1] == 'C' \
                        or self._player._data[row + 2][col] == 'C' or self._player._data[row + 2][col + 1] == 'C' \
                        or self._player._data[row + 2][col + 2] == 'C':
                    i = 1

        elif row == 8:
            if col == 0:
                if self._player._data[row][col + 2] == 'C' or self._player._data[row][col + 1] == 'C':
                    i = 1
            elif col == 9:
                if self._player._data[row][col - 2] == 'C' or self._player._data[row][col - 1] == 'C':
                    i = 1
            elif col == 1:
                if self._player._data[row - 2][col - 1] == 'C' \
                        or self._player._data[row - 2][col] == 'C' or self._player._data[row - 2][col + 1] == 'C' \
                        or self._player._data[row - 2][col + 2] == 'C' \
                        or self._player._data[row - 1][col - 1] == 'C' \
                        or self._player._data[row - 1][col] == 'C' or self._player._data[row - 1][col + 1] == 'C' \
                        or self._player._data[row - 1][col + 2] == 'C' \
                        or self._player._data[row][col - 1] == 'C' \
                        or self._player._data[row][col] == 'C' or self._player._data[row][col + 1] == 'C' \
                        or self._player._data[row][col + 2] == 'C' \
                        or self._player._data[row + 1][col - 1] == 'C' \
                        or self._player._data[row + 1][col] == 'C' or self._player._data[row + 1][col + 1] == 'C' \
                        or self._player._data[row + 1][col + 2] == 'C':
                    i = 1
            elif col == 8:
                if self._player._data[row - 2][col - 2] == 'C' or self._player._data[row - 2][col - 1] == 'C' \
                        or self._player._data[row - 2][col] == 'C' or self._player._data[row - 2][col + 1] == 'C' \
                        or self._player._data[row - 1][col - 2] == 'C' or self._player._data[row - 1][col - 1] == 'C' \
                        or self._player._data[row - 1][col] == 'C' or self._player._data[row - 1][col + 1] == 'C' \
                        or self._player._data[row][col - 2] == 'C' or self._player._data[row][col - 1] == 'C' \
                        or self._player._data[row][col] == 'C' or self._player._data[row][col + 1] == 'C' \
                        or self._player._data[row + 1][col - 2] == 'C' or self._player._data[row + 1][col - 1] == 'C' \
                        or self._player._data[row + 1][col] == 'C' or self._player._data[row + 1][col + 1] == 'C':
                    i = 1
            else:
                if self._player._data[row - 2][col - 2] == 'C' or self._player._data[row - 2][col - 1] == 'C' \
                        or self._player._data[row - 2][col] == 'C' or self._player._data[row - 2][col + 1] == 'C' \
                        or self._player._data[row - 2][col + 2] == 'C' \
                        or self._player._data[row - 1][col - 2] == 'C' or self._player._data[row - 1][col - 1] == 'C' \
                        or self._player._data[row - 1][col] == 'C' or self._player._data[row - 1][col + 1] == 'C' \
                        or self._player._data[row - 1][col + 2] == 'C' \
                        or self._player._data[row][col - 2] == 'C' or self._player._data[row][col - 1] == 'C' \
                        or self._player._data[row][col] == 'C' or self._player._data[row][col + 1] == 'C' \
                        or self._player._data[row][col + 2] == 'C' \
                        or self._player._data[row + 1][col - 2] == 'C' or self._player._data[row + 1][col - 1] == 'C' \
                        or self._player._data[row + 1][col] == 'C' or self._player._data[row + 1][col + 1] == 'C' \
                        or self._player._data[row + 1][col + 2] == 'C':
                    i = 1
        elif row == 9:
            if col == 0:
                if self._player._data[row - 1][col + 2] == 'C':
                    i = 1
            elif col == 9:
                if self._player._data[row - 1][col - 2] == 'C':
                    i = 1
            elif col == 1:
                if self._player._data[row - 2][col - 1] == 'C' \
                        or self._player._data[row - 2][col] == 'C' or self._player._data[row - 2][col + 1] == 'C' \
                        or self._player._data[row - 2][col + 2] == 'C' \
                        or self._player._data[row - 1][col - 1] == 'C' \
                        or self._player._data[row - 1][col] == 'C' or self._player._data[row - 1][col + 1] == 'C' \
                        or self._player._data[row - 1][col + 2] == 'C' \
                        or self._player._data[row][col - 1] == 'C' \
                        or self._player._data[row][col] == 'C' or self._player._data[row][col + 1] == 'C' \
                        or self._player._data[row][col + 2] == 'C':
                    i = 1
            elif col == 8:
                if self._player._data[row - 2][col - 2] == 'C' or self._player._data[row - 2][col - 1] == 'C' \
                        or self._player._data[row - 2][col] == 'C' or self._player._data[row - 2][col + 1] == 'C' \
                        or self._player._data[row - 1][col - 2] == 'C' or self._player._data[row - 1][col - 1] == 'C' \
                        or self._player._data[row - 1][col] == 'C' or self._player._data[row - 1][col + 1] == 'C' \
                        or self._player._data[row][col - 2] == 'C' or self._player._data[row][col - 1] == 'C' \
                        or self._player._data[row][col] == 'C' or self._player._data[row][col + 1] == 'C':
                    i = 1
            else:
                if self._player._data[row - 2][col - 2] == 'C' or self._player._data[row - 2][col - 1] == 'C' \
                        or self._player._data[row - 2][col] == 'C' or self._player._data[row - 2][col + 1] == 'C' \
                        or self._player._data[row - 2][col + 2] == 'C' \
                        or self._player._data[row - 1][col - 2] == 'C' or self._player._data[row - 1][col - 1] == 'C' \
                        or self._player._data[row - 1][col] == 'C' or self._player._data[row - 1][col + 1] == 'C' \
                        or self._player._data[row - 1][col + 2] == 'C' \
                        or self._player._data[row][col - 2] == 'C' or self._player._data[row][col - 1] == 'C' \
                        or self._player._data[row][col] == 'C' or self._player._data[row][col + 1] == 'C' \
                        or self._player._data[row][col + 2] == 'C':
                    i = 1

        if i == 1:
            return True
        else:
            return False

    def set_plane(self):
        """
        sets a plane randomly
        :return:
        """
        coord_list = ['N', 'E', 'S', 'V']
        orientation = choice(coord_list)
        row = randint(1, 9)
        col = randint(1, 9)
        try:
            self._computer.set_plane(row, col, orientation)
        except PlaneException as ve:
            raise ve


class MovePlayer:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def set_plane(self, square, orientation):
        """
        sets a plane
        :param square: the cabin of the plane
        :param orientation: the orientation of the plane
        :return:
        """
        row = ord(square[0]) - 65
        col = int(square[1:])
        self._player.set_plane(row, col, orientation)

    def move(self, square):
        """
        where the player wants to attack computer's board
        :param square: the square player wants to attack
        :return:
        """
        # Turn square into coordinates
        try:
            row = ord(square[0]) - 65
            col = int(square[1:])
            self._computer.move(row, col - 1)
        except PlaneException as ve:
            raise ve

"""

class MoveTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testMoveTest(self):
        cmove = MoveComputer(start.player, start.computer)
        cmove._player = start.player
        cmove._computer = start.computer

        pmove = MovePlayer(start.player, start.computer)
        pmove._player = start.player
        pmove._computer = start.computer

        #set plane

        cmove.set_plane()
        pmove.set_plane('B3', 'N')

        self.assertEqual(len(pmove._player._plane_list_player), 1)
        self.assertEqual(len(cmove._computer._plane_list_computer), 1)

        cmove._moves = {[2, 2]}
        cmove._list_x = {[2, 2]}

        self.assertEqual(cmove.verify_cabin(5, 5), False)
        cmove.move()

        square = cmove._computer._plane_list_computer[0]
        col = square[0]
        row = square[1]
        if col == 9:
            square = chr(65 + row) + chr(49) + chr(48)
        else:
            square = chr(65 + row) + chr(49 + col)
        pmove.move(square)

        self.assertEqual(pmove._player._data[col][row], 'X')

        square = cmove._computer._cabin_list_computer[0]
        col = square[0]
        row = square[1]
        if col == 9:
            square = chr(65 + row) + chr(49) + chr(48)
        else:
            square = chr(65 + row) + chr(49 + col)
        pmove.move(square)

        self.assertEqual(pmove._player._data[col][row], 'C')

        empty = cmove._computer.empty_squares()

        square = empty[5]
        col = square[0]
        row = square[1]
        if col == 9:
            square = chr(65 + row) + chr(49) + chr(48)
        else:
            square = chr(65 + row) + chr(49 + col)
        pmove.move(square)

        self.assertEqual(pmove._player._data[col][row], 'O')

"""