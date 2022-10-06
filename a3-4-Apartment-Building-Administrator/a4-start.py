from a4-functions import generate_ap, split_command_params, add_ap_command, \
    replace_command, filter_command, undo_command_run, new_list
from a4-ui import remove_commands, list_commands,  display_sum, max_exp_ap, \
    sort_command


def start_command():
    expense_list = generate_ap()
    listoflists = []
    while True:
        try:
            command = input("Command: ")
            command_word, command_params = split_command_params(command)
            print(command_word, command_params)
            if command_word == 'add':
                new_list(expense_list, listoflists)
                add_ap_command(expense_list, command_params)
            elif command_word == 'replace':
                new_list(expense_list, listoflists)
                expense_list = replace_command(expense_list, command_params)
            elif command_word == 'remove':
                new_list(expense_list, listoflists)
                remove_commands(expense_list, command_params)
            elif command_word == 'list':
                list_commands(expense_list, command_params)
            elif command_word == 'sum':
                display_sum(expense_list, command_params)
            elif command_word == 'max':
                max_exp_ap(expense_list, command_params)
            elif command_word == 'sort':
                sort_command(expense_list, command_params)
            elif command_word == 'filter':
                new_list(expense_list, listoflists)
                filter_command(expense_list, command_params)
            elif command_word == 'undo':
                undo_command_run(expense_list, listoflists)
            elif command_word == 'exit':
                return
            else:
                print("Invalid command")
        except ValueError as ve:
            print(str(ve))


start_command()
