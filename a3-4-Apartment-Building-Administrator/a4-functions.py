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


def new_list(expense_list, listoflists):
    """
    memorises every change of the initial list
    :param expense_list:
    :param listoflists:
    :return:
    """
    listoflists.append(expense_list.copy())


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


def k_tap_pr(expense):
    """
        gets the key for the sorting function
        :param expense:
        :return:
    """
    return int(get_tprice(expense))


def k_etype(expense):
    """
        gets the key for the sorting function
        :param expense:
        :return:
    """
    return get_etype(expense)


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

max
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


test_get_sign()


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


test_get_lvalue()


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


def create_totexp(tap_nr, tprice):
    """
    creates a dictionary(ap) that memorises the apartment and the total price
    :param tap_nr:
    :param tprice:
    :return:
    """
    if int(tap_nr) < 1:
        raise ValueError("Invalid apartment number")
    if int(tprice) < 0:
        raise ValueError("Invalid amount of money")
    return {'tap_nr': tap_nr, 'tprice': tprice}


def get_tap_nr(expense):
    """
    gets apartment number for the dictionary(ap) with the total price
    :param expense:
    :return:
    """
    return int(expense['tap_nr'])


def get_tprice(expense):
    """
    gets the total price
    :param expense:
    :return:
    """
    return int(expense['tprice'])


def add_tap(tap_list, expense):
    """
    adds apartments/expenses and their total (expense) price to the dictionary
    :param tap_list:
    :param expense:
    :return:
    """
    tap_list.append(expense)
    return True


def add_tap_command(tap_list, i, a):
    """
    creates the 'expense' (ap nr, total) and calls function add_tap
    :param tap_list:
    :param i:
    :param a:
    :return:
    """
    try:
        expense = create_totexp(i, a)
        add_tap(tap_list, expense)
    except ValueError:
        print("invalid")


def sum_tap(s, a):
    """
    sums up all the expenses for each apartment
    :param s:
    :param a:
    :return:
    """
    s = int(s + a)
    return s


def sort_ap(expense_list):
    """
    sorts in ascending order (with respect to the price) the dictionary(ap) with the total expense price
    :param expense_list:
    :return:
    """
    tap_list = []
    sort_expenses = sorted(expense_list, key=k_ap_nr)
    aux = int(1)
    s = int(0)
    for expense in sort_expenses:
        if get_ap_nr(expense) == aux:
            a = get_price(expense)
            s = sum_tap(s, a)
        else:
            add_tap_command(tap_list, aux, s)
            aux = get_ap_nr(expense)
            s = int(get_price(expense))
    add_tap_command(tap_list, aux, s)
    return tap_list


def create_tottype(etype, tprice):
    """
    creates a dictionary(exp) that memorises the expense and the total price
    :param etype:
    :param tprice:
    :return:
    """
    if int(tprice) < 0:
        raise ValueError("Invalid amount of money")
    return {'etype': etype, 'tprice': tprice}


def add_taptype_command(tap_list, i, a):
    """
    adds expenses and their total price to the dictionary(exp)
    :param tap_list:
    :param i:
    :param a:
    :return:
    """
    try:
        expense = create_tottype(i, a)
        add_tap(tap_list, expense)
    except ValueError:
        print("invalid")


def sum_tetype(s, a):
    """
    sums up all the expenses for each type
    :param s:
    :param a:
    :return:
    """
    s = int(s + a)
    return s


def sort_etype(expense_list):
    """
    sorts in ascending order (with respect to the price) the dictionary(exp) with the total expense price
    :param expense_list:
    :return:
    """
    tap_list = []
    sort_expenses = sorted(expense_list, key=k_etype)
    aux = 'electricity'
    s = int(0)
    for expense in sort_expenses:
        if get_etype(expense) == aux:
            a = get_price(expense)
            s = sum_tap(s, a)
        else:
            add_taptype_command(tap_list, aux, s)
            aux = get_etype(expense)
            s = int(get_price(expense))
    add_taptype_command(tap_list, aux, s)
    return tap_list


def filter_exp(expense_list, command_params):
    """
    removes the expenses that do not match the parameter introduced by the user
    :param expense_list:
    :param command_params:
    :return:
    """
    token = command_params.strip()
    k = 0
    adj = []
    for expense in expense_list:
        if get_etype(expense) != token:
            adj.append(expense)
            k = 1
    for x in adj:
        expense_list.remove(x)
    if k == 0:
        print("No expense to be removed")


def filter_sum(expense_list, command_params):
    """
    removes apartments with the total sum bigger than the one introduced by the user
    :param expense_list:
    :param command_params:
    :return:
    """
    token = command_params.strip()
    tap_list = sort_ap(expense_list)
    for expense in tap_list:
        if get_tprice(expense) >= int(token):
            exp = get_tap_nr(expense)
            remove_ap(expense_list, exp)
            k = 1
    if k == 0:
        print("No expense to be removed")


def filter_command(expense_list, command_params):
    """
    the commands fot the word 'filter'
    :param expense_list:
    :param command_params:
    :return:
    """
    token = command_params.strip()
    if token in ['water', 'heating', 'electricity', 'gas', 'other']:
        filter_exp(expense_list, command_params)
    else:
        filter_sum(expense_list, command_params)


def undo_command_run(expense_list, listoflists):
    """

    :param expense_list:
    :param listoflists:
    :return:
    """
    n = len(listoflists)
    if n == 0:
        raise ValueError("Can not undo. Reached initial list")
    expense_list.clear()
    for exp in listoflists[n-1]:
        expense_list.append(exp)
    listoflists.pop()
