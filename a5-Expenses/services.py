from src.domain.domain import expense
import random


class functions:
    def __init__(self):
        self.elist = ['water', 'groceries', 'gas', 'heating', 'other', 'phone']
        self._expense_list = []
        self._listoflists = []
        self.test_add()

    def generate_expense(self, n):
        for i in range(n):
            d = random.randint(1, 31)
            p = random.randint(1, 200)
            t = random.choice(self.elist)
            self._expense_list.append(expense(d, p, t))

    def new_list(self):
        self._listoflists.append(self._expense_list.copy())

    def add(self, date, price, etype):
        """
        adds a new expense to the list
        :param date: the date of the expense read from the console
        :param price: the price of the expense read from the console
        :param etype: the type of the expense read from the console
        :return:
        """
        if int(date) < int(1) or int(date) > int(30):
            raise ValueError
        elif int(price) < 1:
            raise ValueError
        elif etype not in self.elist:
            raise ValueError
        else:
            self._expense_list.append(expense(date, price, etype))
        return True

    def test_add(self):
        """
        tests the correctness of the add function
        :return:
        """
        self.new_list()
        self.add(5, 5, 'gas')
        m = self._expense_list[len(self._expense_list) - 1]
        assert get_price(m) == 5 and get_date(m) == 5 and get_etype(m) == 'gas'
        self.undo()

    def sort_expense_list(self):
        """
        Sort list of expenses ascending by day
        :return: Sorted copy of the original list
        """
        return sorted(self._expense_list, key=get_date, reverse=False)

    def filter(self):
        print("Enter minimum price: ")
        p = input()
        k = len(self._expense_list)
        i = 0
        while i < len(self._expense_list):
            if get_price(self._expense_list[i]) <= int(p):
                self._expense_list.pop(i)
                i -= 1
            i += 1
        if k == len(self._expense_list):
            raise ValueError("No expense to be removed")

    def undo(self):
        n = len(self._listoflists)
        if n == 0:
            raise ValueError("Can not undo. Reached initial list")
        self._expense_list.clear()
        for exp in self._listoflists[n - 1]:
            self._expense_list.append(exp)
        self._listoflists.pop()


def get_date(e):
    return e.date


def get_price(e):
    return e.price


def get_etype(e):
    return e.etype
