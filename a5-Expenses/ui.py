from src.services.services import functions


class ui:

    def __init__(self):
        self.elist = ['water', 'groceries', 'gas', 'heating', 'other', 'phone']
        self._func = functions()

    def main_menu(self):
        print("1. Add an expense.")
        print("2. Display the list of expenses.")
        print("3. Filter the list so that it contains only expenses above a certain value.")
        print("4. Undo the last operation that modified program data.")
        print("5. Exit")

    def _generate_expense(self):
        n = int(10)
        self._func.generate_expense(int(n))

    def _print_expenses(self):
        k = 0
        expenses = self._func.sort_expense_list()
        for e in expenses:
            k = 1
            print(str(e))
        if k == 0:
            print("Expense list is empty")

    def add_exp_command(self):
        """
        Reads the parameters and calls the add function
        :return:
        """
        print("need to write date, price and type")
        print("Input date: ")
        d = input()
        while int(d) < int(1) or int(d) > int(30):
            print("Enter date 1-30")
            print("Input date: ")
            d = input()

        print("Input price: ")
        p = input()

        while int(p) < 1:
            print("Enter price >0")
            print("Input price: ")
            p = input()

        print("Input type: ")
        t = input()

        while t not in self.elist:
            print("Expense not in list.")
            print("The list: water, groceries, gas, heating, other, phone")
            print("Input type: ")
            t = input()

        try:
            self._func.add(int(d), int(p), t)
            print("Successfully added")
        except ValueError as ve:
            print(str(ve))

    def filter_ui(self):

        try:
            self._func.filter()
            print("Successfully deleted ")
        except ValueError as ve:
            print(str(ve))

    def undo_ui(self):

        try:
            self._func.undo()
            print("Successfully undid")
        except ValueError as ve:
            print(str(ve))

    def start(self):

        self._generate_expense()
        while True:
            try:
                self.main_menu()
                print("Insert option: ")
                option = input()
                if option == '1':
                    self._func.new_list()
                    self.add_exp_command()
                if option == '2':
                    self._print_expenses()
                if option == '3':
                    self._func.new_list()
                    self.filter_ui()
                if option == '4':
                    self.undo_ui()
                if option == '5':
                    return False
                if int(option) < 1 or int(option) > 5:
                    print("Invalid option")
            except ValueError as ve:
                print(str(ve))


console = ui()

console.start()
