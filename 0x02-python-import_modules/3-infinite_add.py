#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    result = 0

    for i in range(1, len(argv)):
        numbers = int(argv[i])
        result += numbers
    print(result)
