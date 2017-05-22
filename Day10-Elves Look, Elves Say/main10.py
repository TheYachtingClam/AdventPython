def look_and_say(input):
    output = ''
    latest_char = ''
    char_count = 0
    for ch in input:
        if ch is not latest_char and char_count is 0:
            latest_char = ch
            char_count = 1
        elif ch is not latest_char:
            output += str(char_count) + latest_char
            latest_char = ch
            char_count = 1
        else:
            char_count += 1
    return output + str(char_count) + latest_char


def main():
    f = open("realInput.txt")

    cycleTimes = f.readline().strip()
    startValue = f.readline().strip()

    for idx in range(0, int(cycleTimes)):
        print("{0}\n".format(startValue))
        startValue = look_and_say(startValue)

    print("{0}\ncycleTimes = {1} len={2}".format(startValue, cycleTimes, len(startValue)))


if __name__ == "__main__":
    main()
