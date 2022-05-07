def merge_the_tools(string, k):
    for word in [string[i:i+k] for i in range(0, len(string), k)]:
        result = ""
        for c in word:
            if c not in result:
                result = f"{result}{c}"
        print(result)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
