input_list = [1, 2, 3, 4, 5]


def recursion_print_list(input_list, target_index = None):
    list_end = len(input_list) - 1
    target_index = 0 if target_index is None else target_index
    print(input_list[target_index])
    if target_index == list_end:
        return
    else:
        recursion_print_list(input_list, target_index + 1)

recursion_print_list(input_list)
