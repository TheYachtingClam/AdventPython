def next_password(last_password):
    pass


def straight_rule(password):
    last_char = ' '
    series_length = 0
    for ch in password:
        if series_length is 3:
            break

        if ord(last_char) + 1 is ord(ch):
            last_char = ch
            series_length += 1
        else:
            last_char = ch
            series_length = 1

    if series_length is 3:
        return True

    return False


def mistaken_rule(password):
    if 'i' in password:
        return False
    if 'o' in password:
        return False
    if 'l' in password:
        return False
    return True


def non_overlapping_rule(password):
    last_char = ' '
    number_of_pairs = 0
    for ch in password:
        if number_of_pairs >= 2:
            break
        if last_char is ch:
            number_of_pairs += 1
            last_char = ' '
        else:
            last_char = ch

    if number_of_pairs >= 2:
        return True

    return False


def check_rules(password):
    if not straight_rule(password):
        return False
    if not mistaken_rule(password):
        return False
    if not non_overlapping_rule(password):
        return False
    return True


def main():
    f = open("testInput.txt")

    print(str(check_rules("ghjaabcc")))
    for line in f:
        print(next_password(line))


if __name__ == "__main__":
    main()
