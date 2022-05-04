from re import S


def print_rangoli(size):
    s = (2 * size - 1) + (2 * size - 2)

    for i in range(1, size+1):
        row = ""

        for c in range(1, (2*i)):
            if c < ((2*i)/2)+1:
                character = 97+size-c
            else:
                character = character + 1

            if row != "":
                row = row + "-" + chr(character)
            else:
                row = chr(character)

        print(row.center(s, '-'))

    for i in range(size-1, 0, -1):
        row = ""
        for c in range(1, (2*i)):
            if c < ((2*i)/2)+1:
                character = 97+size-c
            else:
                character = character + 1

            if row != "":
                row = row + "-" + chr(character)
            else:
                row = chr(character)

        print(row.center(s, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
