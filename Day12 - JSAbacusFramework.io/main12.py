class MyObj(object):
    data = {}


def main():
    f = open("realInput.txt")
    for line in f:
        count = 0
        currentNumber = ""
        isNegative = False
        for ch in line:
            if ch is '-':
                isNegative = True
            elif ch.isdigit():
                currentNumber += ch
            elif currentNumber.isdigit():
                if isNegative:
                    count -= int(currentNumber)
                else:
                    count += int(currentNumber)
                currentNumber = ""
                isNegative = False
            else:
                isNegative = False

        print("{0}, {1}".format(count, line.strip()))

if __name__ == "__main__":
    main()
