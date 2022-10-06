def gnomeSort(sort_list, n, key):
    """

    :param sort_list: the list that needs to be sorted
    :param n: the lenght of the list
    :param key: the number of the element to be sorted on
    :return:
    """
    if key != 22:
        # used for sorting integer "numbers"
        index = 0
        while index < n:
            if index == 0:
                index = index + 1
            if int(sort_list[index][key]) >= int(sort_list[index - 1][key]):
                index = index + 1
            else:
                sort_list[index], sort_list[index - 1] = sort_list[index - 1], sort_list[index]
                index = index - 1
    if key == 22:
        # used for sorting float "numbers"
        index = 0
        while index < n:
            if index == 0:
                index = index + 1
            if float(sort_list[index][2]) >= float(sort_list[index - 1][2]):
                index = index + 1
            else:
                sort_list[index], sort_list[index - 1] = sort_list[index - 1], sort_list[index]
                index = index - 1

    return sort_list


def filter(l, fct):
    tempArray = []
    for e in l:
        if fct(e) == True:
            tempArray.append(e)
    return tempArray
