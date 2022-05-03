# Given an integer, , print the following values for each integer  from  to :

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binaryv

hexa_digit = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',

}


def convertDecimalToOct(n, oct=[]):
    if n == 0:
        oct_number = "".join(str(v) for v in oct[::-1])
        oct.clear()
        return oct_number
    else:
        reminder = n % 8
        oct.append(reminder)
        dividend = int(n / 8)
        return convertDecimalToOct(dividend, oct=oct)


def convertDecimalToHexadecimal(n, oct=[]):
    if n == 0:
        oct_number = "".join(str(v) for v in oct[::-1])
        oct.clear()
        return oct_number
    else:
        reminder = n % 16
        oct.append(hexa_digit[reminder])
        dividend = int(n / 16)
        return convertDecimalToHexadecimal(dividend, oct=oct)


def convertDecimalToBinary(n, oct=[]):

    if n == 0:
        oct_number = "".join(str(v) for v in oct[::-1])
        oct.clear()
        return oct_number
    else:
        reminder = n % 2
        oct.append(reminder)
        dividend = int(n / 2)
        return convertDecimalToBinary(dividend, oct=oct)


def print_formatted(number):
    list = []
    for i in range(1, number+1):
        l = [str(i), convertDecimalToOct(i), convertDecimalToHexadecimal(
            i), convertDecimalToBinary(i)]
        list.append(l.copy())
        l.clear()

    l4 = len(str(list[number-1][3]))

    for i in list:
        print(i[0].rjust(l4), i[1].rjust(l4),
              i[2].rjust(l4), i[3].rjust(l4),)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
