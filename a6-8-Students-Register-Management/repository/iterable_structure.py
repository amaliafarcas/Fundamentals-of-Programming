import unittest


class IterableStructure:
    def __init__(self):
        self.list = []
        self.index = -1

    def __iter__(self):

        "iterator for the class"
        return iter(self.list)

    def __next__(self):

        "getter for the next item from the list"
        if self.index > len(self.list) - 1:
            raise StopIteration
        else:
            self.index += 1
        return self.data[self.index]

    def __len__(self):
        "for the lenght"
        return len(self.list)

    def __setitem__(self, index, val):
        "the setter for an item"
        self.list[index] = val

    def __getitem__(self, index):
        "we get here the item"
        return self.list[index]

    def append(self, x):
        self.list.append(x)

    def __delitem__(self, index):
        "here is the delete function"
        del self.list[index]


class IterableStructureTest(unittest.TestCase):
    def setup(self):
        """
            Runs before any of the tests
        Used to set up the class so that tests can be run

        :return: None
        """
        unittest.TestCase.setUp(self)

    def test_elem(self):
        self.__data = IterableStructure()
        # test len and append
        self.assertEqual(len(self.__data), 0)
        self.__data.append(['test0', 'test1'])
        self.__data.append(['test2', 'test3'])
        self.assertEqual(len(self.__data), 2)

        temp = []
        for i in range(0, len(self.__data)):
            temp.append(self.__data[i])

        self.assertEqual(temp[0][0], 'test0')
        self.assertEqual(temp[0][1], 'test1')
        self.assertEqual(temp[1][0], 'test2')
        self.assertEqual(temp[1][1], 'test3')

        # test next
        self.index = 0
        self.assertEqual(self.__data.__next__(), ['test2', 'test3'])

        # test setitem
        self.__data.__setitem__(0, ['t0', 't1'])
        self.assertEqual(temp[0], ['t0', 't1'])

        # test getitem
        self.assertEqual(self.__data.__getitem__(0), ['t0', 't1'])
        self.assertEqual(self.__data.__getitem__(1), ['test2', 'test3'])

        # test delete
        self.assertEqual(len(self.__data), 2)
        self.__data.__delitem__(1)
        self.assertEqual(len(self.__data), 1)

    def tearDown(self):
        """
        Runs after all the tests have completed
        Used to close the test environment (clase files, DB connections, deallocate memory)
        :return:
        """

        unittest.TestCase.tearDown(self)

#$ coverage run -m unittest discover