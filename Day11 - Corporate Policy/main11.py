def next_password(last_password):
    pass


def straight_rule(password):
    pass


def mistaken_rule(password):
    pass


def non_overlapping_rule(password):
    pass


def main():
    f = open("testInput.txt")

    for line in f:
        print(next_password(line))


if __name__ == "__main__":
    main()
