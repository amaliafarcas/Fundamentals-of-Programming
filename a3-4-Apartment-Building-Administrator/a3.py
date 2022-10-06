def create_apartment(ap_nr, etype, price):
    """
    Creates the dictionary
    :param ap_nr: number of apartment
    :param etype: expense type
    :param price: expense price
    :return: the dictionary
    """
    if int(ap_nr) < 1:
        raise ValueError("Invalid apartment number")
    if etype not in ['water', 'heating', 'electricity', 'gas', 'other']:
        raise ValueError("Invalid expense")
    if int(price) < 0:
        raise ValueError("Invalid amount of money")
    return {'ap_nr': ap_nr, 'etype': etype, 'price': price}


def get_ap_nr(expense):
    """
    gets apartment number
    :param expense:
    :return: apartment number
    """
    return int(expense['ap_nr'])


def get_etype(expense):
    """
    gets expense type
    :param expense:
    :return: expense type
    """
    return expense['etype']


def get_price(expense):
    """
    gets expense price
    :param expense:
    :return: expense price
    """
    return int(expense['price'])


def generate_ap():
    """
    generates a list of apartments with their expense and price
    :return: expense
    """
    return [create_apartment(1, 'gas', 25), create_apartment(12, 'electricity', 14), create_apartment(8, 'other', 65),
            create_apartment(20, 'water', 89), create_apartment(17, 'heating', 70), create_apartment(7, 'gas', 25),
            create_apartment(20, 'electricity', 74), create_apartment(12, 'other', 65), create_apartment(2, 'gas', 50),
            create_apartment(18, 'heating', 70), create_apartment(1, 'other', 25), create_apartment(11, 'heating', 24)]


def split_command_params(user_command):
    """
    Split the user's command into the command word and a parameters string
    :param user_command: Command input by the user
    :return: A tuple of (<command word>, <command params>) in lowercase
    """
    user_command = user_command.strip()
    tokens = user_command.split(maxsplit=1)
    if len(tokens) > 0:
        command_word = tokens[0].lower()
    command_params = None
    if 1 < len(tokens) <= 5:
        command_params = tokens[1].lower()
    return command_word, command_params


def test_split_command_params():
    assert split_command_params('list all') == ('list', 'all')
    assert split_command_params('list > 5') == ('list', '> 5')
    assert split_command_params('list = 5') == ('list', '= 5')
    assert split_command_params('remove 1') == ('remove', '1')
    assert split_command_params('remove 1 to 15') == ('remove', '1 to 15')
    assert split_command_params('replace 1 gas with 15') == ('replace', '1 gas with 15')


test_split_command_params()


def add_ap(expense_list, expense):
    """
    Verifies if the apartment and the expense already exists and returns the message "Expense already exists"
    if it already exists
    :param expense_list:
    :param expense: *introduced by the user*
    :return:
    """
    for exp in expense_list:
        if get_ap_nr(expense) == get_ap_nr(exp) and get_etype(expense) == get_etype(exp):
            raise ValueError
    expense_list.append(expense)
    return True


def add_ap_command(expense_list, command_params):
    """
    Adds the expense to the list (if it does not exist)
    :param expense_list:
    :param command_params:
    :return:
    """
    expense_tokens = command_params.split(";")
    for tokens in expense_tokens:
        try:
            ap_nr, etype, price = tokens.split(' ')
            expense = create_apartment(ap_nr.strip(), etype.strip(), int(price.strip()))
            add_ap(expense_list, expense)

        except ValueError:
            print("Invalid command")


def k_ap_nr(expense):
    """
    gets the key for the sorting function
    :param expense:
    :return:
    """
    return int(get_ap_nr(expense))


def replace_command(expense_list, command_params):
    """
    replaces an existing expense with one introduced by the user
    :param expense_list:
    :param command_params:
    :return: the updated expense_list
    """
    expense_tokens = command_params.split(";")
    for tokens in expense_tokens:
        try:
            ap_nr, etype, com, new_price = tokens.split(' ')
            for i in range(len(expense_list)):
                if get_ap_nr(expense_list[i]) == int(ap_nr) and get_etype(expense_list[i]) == etype:
                    expense_list[i]['price'] = int(new_price)
                    return expense_list

        except ValueError:
            print("Invalid command")


def test_replace_command():
    test_list = [create_apartment(1, 'gas', 25), create_apartment(12, 'electricity', 14),
                 create_apartment(2, 'gas', 78), create_apartment(22, 'electricity', 7),
                 create_apartment(5, 'gas', 69), create_apartment(17, 'electricity', 85)]
    test_list = replace_command(test_list, '1 gas with 11')
    test_list = replace_command(test_list, '12 electricity 1')
    test_list = replace_command(test_list, '2 gas 96')
    test_list = replace_command(test_list, '22 electricity 5')
    test_list = replace_command(test_list, '5 gas 96')
    test_list = replace_command(test_list, '17 electricity 5')
    assert get_price(test_list[0]) == 11
    assert get_price(test_list[1]) == 1
    assert get_price(test_list[2]) == 96
    assert get_price(test_list[3]) == 5
    assert get_price(test_list[4]) == 96
    assert get_price(test_list[5]) == 5


#test_replace_command()


def get_sign(command_params):
    """
    Memorises the sign introduced by the user
    :param command_params:
    :return: the sign
    """
    tokens = command_params.split(' ')
    for token in tokens:
        if token in ['=', '<', '>']:
            sign = token

    return sign


def test_get_sign():
    assert get_sign('< 15') == '<'
    assert get_sign('= 14') == '='
    assert get_sign('> 89') == '>'


#test_get_sign()


def get_lvalue(command_params):
    """
    memorises the value introduced by the user
    :param command_params:
    :return: the value of a list command
    """
    tokens = command_params.split(' ')
    for token in tokens:
        if token not in ['=', '<', '>']:
            lvalue = token

    return lvalue


def test_get_lvalue():
    assert get_lvalue('< 15') == '15'
    assert get_lvalue('= 14') == '14'
    assert get_lvalue('> 89') == '89'


#test_get_value()


def remove_ap(expense_list, exp):
    """
    finds the expense that needs to be removed, memorises it in a list,
    and deletes it from the initial list
    :param expense_list:
    :param exp:
    :return:
    """
    adj = []
    for expense in expense_list:
        if get_ap_nr(expense) == int(exp):
            adj.append(expense)
    for x in adj:
        expense_list.remove(x)
    return True


def remove_ap_command(expense_list, command_params):
    """
    matches the parameters introduced by the user to the ones existing in the list and calls the function remove
    :param expense_list:
    :param command_params:
    :return:
    """
    expense_tokens = command_params.split(";")
    for tokens in expense_tokens:
        try:
            exp = tokens.strip()
            remove_ap(expense_list, exp)
        except ValueError:
            print("Could not remove apartment")
    return True


def remove_exp_command(expense_list, command_params):
    """
        matches the parameters introduced by the user to the ones existing in the list and calls the function remove
        :param expense_list:
        :param command_params:
        :return:
    """
    expense_tokens = command_params.split(";")
    for tokens in expense_tokens:
        try:
            exp = tokens.strip()
            remove_exp(expense_list, exp)
        except ValueError:
            print("Could not remove expenses")
    return True


def remove_exp(expense_list, exp):
    """
    finds the expense that needs to be removed, memorises it in a list,
    and deletes it from the initial list
    :param expense_list:
    :param exp:
    :return:
    """
    adj = []
    for expense in expense_list:
        if get_etype(expense) == exp:
            adj.append(expense)
    for x in adj:
        expense_list.remove(x)
    return True


#ui-functions


def expense_equal(expense_list, command_params):
    """
    sums up the expense prices for each apartment, compares to the sum introduced by the user and prints
    if the condition is met
    :param expense_list:
    :param command_params:
    :return:
    """
    lvalue = get_lvalue(command_params)
    k = 0
    for i in range(1, 31):
        sum_exp = int(0)
        for expense in expense_list:
            if int(get_ap_nr(expense)) == int(i):
                sum_exp = int(sum_exp + get_price(expense))
        if int(sum_exp) == int(lvalue):
            print(i)
            k = 1
    if k == 0:
        print("No such apartment")


def expense_smaller(expense_list, command_params):
    """
    sums up the expense prices for each apartment, compares to the sum introduced by the user and prints
    if the condition is met
    :param expense_list:
    :param command_params:
    :return:
    """
    lvalue = get_lvalue(command_params)
    k = 0
    for i in range(1, 31):
        sum_exp = int(0)
        for expense in expense_list:
            if int(get_ap_nr(expense)) == int(i):
                sum_exp = int(sum_exp + get_price(expense))
        if int(sum_exp) < int(lvalue) and int(sum_exp) > 0:
            print(i, " ", sum_exp)
            k = 1
    if k == 0:
        print("No such apartment")


def expense_bigger(expense_list, command_params):
    """
    sums up the expense prices for each apartment, compares to the sum introduced by the user and prints
    if the condition is met
    :param expense_list:
    :param command_params:
    :return:
    """
    lvalue = get_lvalue(command_params)
    k = 0
    for i in range(1, 31):
        sum_exp = int(0)
        for expense in expense_list:
            if int(get_ap_nr(expense)) == int(i):
                sum_exp = int(sum_exp + get_price(expense))
        if int(sum_exp) > int(lvalue):
            print(i, " ", sum_exp)
            k = 1
    if k == 0:
        print("No such apartment")


def list_commands(expense_list, command_params):
    """
    the command for the command word 'list'
    :param expense_list:
    :param command_params:
    :return:
    """
    tokens = command_params.split(' ')
    if len(tokens) == 1:
        for token in tokens:
            try:
                if token == 'all':
                    show_allexpenses(expense_list)
                elif 30 >= int(token) >= 1:
                    show_apexpenses(expense_list, command_params)
                else:
                    print("Apartment does not exist")
            except ValueError:
                print("Invalid command")
    elif len(tokens) == 2:
        sign = get_sign(command_params)
        if sign == '=':
            expense_equal(expense_list, command_params)
        elif sign == '>':
            expense_bigger(expense_list, command_params)
        elif sign == '<':
            expense_smaller(expense_list, command_params)
        else:
            print("Invalid command")

    else:
        print("Invalid command")


def remove_commands(expense_list, command_params):
    """
    the commands for the command word 'remove'
    :param expense_list:
    :param command_params:
    :return:
    """
    tokens = command_params.split(' ')
    if len(tokens) == 1:
        for token in tokens:
            token.strip()
            try:
                if token in ['water', 'heating', 'electricity', 'gas', 'other']:
                    remove_exp_command(expense_list, command_params)
                elif 30 >= int(token) >= 1:
                    remove_ap_command(expense_list, command_params)
                elif int(token) > 30:
                    print("Apartment does not exist")
            except ValueError:
                print("Invalid command")
    elif len(tokens) == 3:
        tokens = command_params.split(";")
        for token in tokens:
            try:
                ap1, a, ap2 = token.split(" ")
                ap1 = int(ap1)
                ap2 = int(ap2)
                for i in range(ap1, ap2+1):
                    exp = i
                    remove_ap(expense_list, exp)
            except ValueError:
                print("Invalid option")
    else:
        print("Invalid option")


def show_allexpenses(expense_list):
    """
    sorts the expense list and prints all apartments with their expense type and price
    :param expense_list:
    :return:
    """
    sort_expenses = sorted(expense_list, key=k_ap_nr)
    for expense in sort_expenses:
        print(str(get_ap_nr(expense)), str(get_etype(expense)), str(get_price(expense)))


def show_apexpenses(expense_list, command_params):
    """
    in the sorted list, matches the parameter introduced by the user and prints the expenses and the prices
    for the 'called' apartment
    :param expense_list:
    :param command_params:
    :return:
    """
    sort_expenses = sorted(expense_list, key=k_ap_nr)
    tokens = command_params.split(' ')
    k = 0
    for expense in sort_expenses:
        for token in tokens:
            if get_ap_nr(expense) == int(token):
                print(str(get_ap_nr(expense)), str(get_etype(expense)), str(get_price(expense)))
                k = 1
    if k == 0:
        print("No expenses")


def start_command():
    expense_list = generate_ap()

    while True:
        command = input("Command: ")
        command_word, command_params = split_command_params(command)
        print(command_word, command_params)
        if command_word == 'add':
            add_ap_command(expense_list, command_params)
        elif command_word == 'replace':
            expense_list = replace_command(expense_list, command_params)
        elif command_word == 'remove':
            remove_commands(expense_list, command_params)
        elif command_word == 'list':
            list_commands(expense_list, command_params)
        elif command_word == 'exit':
            return
        else:
            print("Invalid command")


start_command()
