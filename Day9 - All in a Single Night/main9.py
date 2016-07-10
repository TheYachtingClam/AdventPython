def create_permutation(number_list):
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
    f = open("realInput.txt")
    distanceData = {}
    unique_list = []
    for line in f:
        split_line = line.split()
        from_city = split_line[0]
        to_city = split_line[2]
        if from_city not in unique_list:
            unique_list.append(from_city)

        if to_city not in unique_list:
            unique_list.append(to_city)

        distance = int(split_line[4])
        distanceData[(from_city, to_city)] = distance

    final_val = create_permutation(unique_list)
    shortestTrip = []
    shortestDistance = 0

    for trip in final_val:
        tripLength = 0
        from_city = ''
        to_city = ''
        for leg in trip:
            if from_city == '' and to_city == '':
                to_city = leg
                continue
            else:
                from_city = to_city
                to_city = leg

            if (from_city, to_city) in distanceData:
                tripLength += distanceData[(from_city, to_city)]
            else:
                tripLength += distanceData[(to_city, from_city)]

        if tripLength > shortestDistance:
            shortestTrip = trip
            shortestDistance = tripLength

    print("shortest trip is {0} miles, {1}".format(shortestDistance, str(shortestTrip)))


if __name__ == "__main__":
    main()
