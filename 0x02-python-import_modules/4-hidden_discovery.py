#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for _name in dir(hidden_4):
        if _name[1] == '_':
            continue
        else:
            print(_name)
