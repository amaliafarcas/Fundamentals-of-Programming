import texttable
from exception import PlaneException
from validator import ValidatePlane
import unittest


class ComputerBoard:
    def __init__(self, width, height):
        self._cols = width
        self._rows = height
        # 0 is default value
        self._data = [[0] * self._cols for i in range(self._rows)]
        self._cabin_list_computer = list()
        self._plane_list_computer = list()
        self._planes_crushed = list()
        self._val = ValidatePlane()

    def set_plane(self, row, col, orientation):
        """
        sets a plane by memorising the cells that contain the plane
        :param row:
        :param col:
        :param orientation:
        :return:
        """
        aux = [row, col]
        if aux in self._cabin_list_computer:
            raise PlaneException("Different planes can not have the same cabin")
        try:
            aux_plane_list = self._val.validate_plane(row, col, orientation, self._plane_list_computer)
            for c in aux_plane_list:
                self._plane_list_computer.append(c)
            self._cabin_list_computer.append([row, col - 1])
        except PlaneException as ve:
            raise ve

    def show_planes(self):
        """
        used for helping in the process of creating the game in order to verify whether or not the planes are
        set correctly
        :return:
        """
        planes = self._plane_list_computer
        for p in planes:
            i = int(p[0])
            j = int(p[1])
            self._data[i][j] = 'p'

    def move(self, x, y):
        """
        Makes a move on the board
        O - air
        X - plane
        C - cabin
        :param x: Row
        :param y: Column
        """
        if len(self._planes_crushed) == 3:
            raise PlaneException("Game Over!")

        if not (0 <= x < self._rows and 0 <= y < self._cols):
            raise PlaneException("Not a valid cell!")

        if self._data[x][y] != 0:
            raise PlaneException("Cell already taken!")

        p = [x, y]
        if p in self._plane_list_computer:
            self._data[x][y] = 'X'
        elif p in self._cabin_list_computer:
            self._planes_crushed.append(p)
            #self.crush_plane(p)
            self._data[x][y] = 'C'
        else:
            self._data[x][y] = 'O'

    def crush_plane(self, p):
        """
        previously used to crush a plane if the cabin was attacked
        (not used anymore for it would make the game too simple)
        :param p: the cabin crushed
        :return:
        """
        i = 0
        k = 0
        for c in self._cabin_list_computer:
            if p == c:
                k = i
            i += 1

        for i in range(9*k, 9*(k+1)):
            x = self._plane_list_computer[i][0]
            y = self._plane_list_computer[i][1]
            self._data[x][y] = 'X'

    def empty_squares(self):
        """
        Return a list of all non-played squares
        :return:
        """
        result = []
        for i in range(self._rows):
            for j in range(self._cols):
                if self._data[i][j] == 0:
                    result.append((i, j))
        # Removes the (0,0), which is the first element in the list
        result.pop(0)
        return result

    def __str__(self):
        t = texttable.Texttable()

        # Horizontal header
        header_row = ['/']
        for i in range(self._cols):
            header_row.append(1 + i)
        t.header(header_row)

        for i in range(self._rows):
            row = self._data[i]
            # Initialize vertical header
            display_row = [chr(65 + i)]

            for j in range(self._cols):
                val = self._data[i][j]
                if val == 0:
                    display_row.append(' ')
                else:
                    display_row.append(val)

            t.add_row(display_row)
        return t.draw()


class PlayerBoard:
    def __init__(self, width, height):
        self._cols = width
        self._rows = height
        # 0 is default value
        self._data = [[0] * self._cols for i in range(self._rows)]
        self._cabin_list_player = list()
        self._plane_list_player = list()
        self._planes_crushed = list()
        self._val = ValidatePlane()

    def set_plane(self, row, col, orientation):
        """
        sets a plane by memorising the cells that contain the plane
        :param row:
        :param col:
        :param orientation:
        :return:
        """
        aux = [row, col]
        if aux in self._cabin_list_player:
            raise PlaneException("Different planes can not have the same cabin")

        try:
            aux_plane_list = self._val.validate_plane(row, col, orientation, self._plane_list_player)
            for c in aux_plane_list:
                self._plane_list_player.append(c)
            self._cabin_list_player.append([row, col-1])
        except PlaneException as ve:
            raise ve

    def show_planes(self):
        """
        used for helping in the process of creating the game in order to verify whether or not the planes are
        set correctly
        :return:
        """
        planes = self._plane_list_player
        for p in planes:
            i = int(p[0])
            j = int(p[1])
            self._data[i][j] = 'p'

        print(self._cabin_list_player)

    def move(self, x, y):
        """
        Makes a move on the board
        O - air
        X - plane
        C - cabin
        :param x: Row
        :param y: Column
        """
        if len(self._planes_crushed) == 3:
            raise PlaneException("Game Over!")

        if not (0 <= x < self._rows and 0 <= y < self._cols):
            raise PlaneException("Not a valid cell!")

        if self._data[x][y] != 0:
            raise PlaneException("Cell already taken!")

        p = [x, y]
        if p in self._plane_list_player:
            self._data[x][y] = 'X'
        elif p in self._cabin_list_player:
            self._planes_crushed.append(p)
            #self.crush_plane(p)
            self._data[x][y] = 'C'
        else:
            self._data[x][y] = 'O'

    def empty_squares(self):
        """
        Return a list of all non-played squares (without (0,0))
        :return:
        """
        result = []
        for i in range(self._rows):
            for j in range(self._cols):
                if self._data[i][j] == 0:
                    result.append((i, j))
        # Removes the (0,0), which is the first element in the list
        result.pop(0)
        return result

    def crush_plane(self, p):
        """
        previously used to crush a plane if the cabin was attacked
        (not used anymore for it would make the game too simple)
        :param p: the cabin crushed
        :return:
        """
        i = 0
        k = 0
        for c in self._cabin_list_player:
            if p == c:
                k = i
            i += 1

        for i in range(9*k, 9*(k+1)):
            x = self._plane_list_player[i][0]
            y = self._plane_list_player[i][1]
            self._data[x][y] = 'X'

    def __str__(self):
        t = texttable.Texttable()

        # Horizontal header
        header_row = ['/']
        for i in range(self._cols):
            header_row.append(1 + i)
        t.header(header_row)

        for i in range(self._rows):
            row = self._data[i]
            # Initialize vertical header
            display_row = [chr(65 + i)]

            for j in range(self._cols):
                val = self._data[i][j]
                if val == 0:
                    display_row.append(' ')
                else:
                    display_row.append(val)

            t.add_row(display_row)
        return t.draw()


class ComputerBoardTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testComputerBoardTest(self):
        board = ComputerBoard(10, 10)

        #set plane

        board.set_plane(2, 3, 'N')
        self.assertEqual(len(board._cabin_list_computer), 1)
        self.assertEqual(len(board._plane_list_computer), 9)

        #move

        board.move(2, 2)
        board.move(5, 7)
        board.move(2, 3)
        self.assertEqual(board._data[2][2], 'C')
        self.assertEqual(board._data[5][7], 'O')
        self.assertEqual(board._data[2][3], 'X')
        self.assertEqual(len(board._planes_crushed), 1)

        #empty_squares

        empty = board.empty_squares()
        self.assertEqual(len(empty), 96)


class PlayerBoardTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testPlayerBoardTest(self):
        board = PlayerBoard(10, 10)

        #set plane

        board.set_plane(2, 3, 'N')
        self.assertEqual(len(board._cabin_list_player), 1)
        self.assertEqual(len(board._plane_list_player), 9)

        #move

        board.move(2, 2)
        board.move(5, 7)
        board.move(2, 3)
        self.assertEqual(board._data[2][2], 'C')
        self.assertEqual(board._data[5][7], 'O')
        self.assertEqual(board._data[2][3], 'X')
        self.assertEqual(len(board._planes_crushed), 1)
