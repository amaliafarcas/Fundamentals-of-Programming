

class expense:
    def __init__(self, date, price, etype):
        """
        Constructor for expense class
        :param date: expense date
        :param price: expense price
        :param etype: expense type
        :return: the dictionary
        """
        if int(date) < 1:
            raise ValueError("Invalid apartment number")
        if etype not in ['water', 'groceries', 'gas', 'heating', 'other', 'phone']:
            raise ValueError("Invalid expense")
        if int(price) < 0:
            raise ValueError("Invalid amount of money")
        self._date = date
        self._price = price
        self._etype = etype

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_value):
        self._date = new_value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_value):
        self._price = new_value

    @property
    def etype(self):
        return self._etype

    @etype.setter
    def etype(self, new_value):
        self._etype = new_value

    def __str__(self):
        return "day:" + str(self.date) + "    price:" + str(self.price) + "    type:" + str(self.etype)
