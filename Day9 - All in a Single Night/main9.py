def create_permutation(number_list):
    print(str(number_list))
    list_to_return = []
    if len(number_list) == 2:
        list_to_return = [list([number_list[0], number_list[1]]), list([number_list[1], number_list[0]])]
        return list_to_return

    for idx, val in enumerate(number_list):
        sub_list = []
        sub_list.extend(number_list[:idx])
        sub_list.extend(number_list[idx + 1:])
        new_list = create_permutation(sub_list)
        for tempList in new_list:
            list_to_add = [val]
            list_to_add.extend(tempList)
            list_to_return.append(list_to_add)
    return list_to_return


def main():
    print "just ran main"
    final_val = create_permutation([0, 1, 2, 3, 4, 5])
    print(str(final_val))
    print("amount of lists = {0}".format(len(final_val)))


if __name__ == "__main__":
    main()
