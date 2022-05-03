# HackerRank.com presents "Pythonist 2".

def convert(c):
    ascii_c = ord(c)
    if ascii_c >= 97 and ascii_c <= 122:
        return chr(ascii_c - 32)
    elif ascii_c >= 65 and ascii_c <= 90:
        return chr(ascii_c + 32)
    else:
        return c


def swap_case(s):
    result = ""
    for c in s:
        result = f"{result}{convert(c)}"
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
