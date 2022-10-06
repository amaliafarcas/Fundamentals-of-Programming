from a4-functions import get_lvalue, get_ap_nr, get_price, get_sign, remove_ap_command, sort_etype, \
    remove_exp_command, remove_ap, k_ap_nr, get_etype, sort_ap, get_tap_nr, \
    get_tprice, k_tap_pr


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
            print(i, " ", sum_exp)
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


def display_sum(expense_list, command_params):
    """
    prints the total amount for the expenses having type
    :param expense_list:
    :param command_params:
    :return:
    """
    token = command_params.strip()
    s = int(0)
    for expense in expense_list:
        if get_etype(expense) == str(token):
            s = s + int(get_price(expense))
    print(s)


def max_exp_ap(expense_list, command_params):
    """
    prints the maximum amount per each expense type for apartment
    :param expense_list:
    :param command_params:
    :return:
    """
    token = command_params.strip()
    maxim_v = int(0)
    maxime_list = []
    for expense in expense_list:
        if get_ap_nr(expense) == int(token):
            if get_price(expense) > maxim_v:
                maxim_v = get_price(expense)
                maxime_list = []
                maxime_list.append(get_etype(expense))
            elif get_price(expense) == maxim_v:
                maxime_list.append(get_etype(expense))
    print(maxim_v, maxime_list)


def sort_command(expense_list, command_params):
    """
    the command for the command word 'sort'
    :param expense_list:
    :param command_params:
    :return:
    """
    token = command_params.strip()
    if token == 'apartment':
        list_sortap(expense_list)
    elif token == 'type':
        list_sortetype(expense_list)
    else:
        print("Invalid command")


def list_sortap(expense_list):
    """
    display the list of apartments sorted ascending by total amount of expenses
    :param expense_list:
    :return:
    """
    tap_list = sort_ap(expense_list)
    sort_tap_list = sorted(tap_list, key=k_tap_pr)
    for exp in sort_tap_list:
        print(str(get_tap_nr(exp)), str(get_tprice(exp)))


def list_sortetype(expense_list):
    """
    displays the total amount of expenses for each type, sorted ascending by amount of money
    :param expense_list:
    :return:
    """
    tap_list = sort_etype(expense_list)
    sort_etype_list = sorted(tap_list, key=k_tap_pr)
    for exp in sort_etype_list:
        print(str(get_etype(exp)), str(get_tprice(exp)))
