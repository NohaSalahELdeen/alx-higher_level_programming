#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    defined_names = dir(hidden_4)
    for i in defined_names:
        if not i.startswith("__"):
            print(i)
