# last_strlen["str", "char"] = len("char") = 4

def last_strlen(str):
    lst = [len(x) for x in str]
    return lst[-1]


if __name__ == "__main__":
    str = input().strip().split(" ")

    strlen = last_strlen(str)
    print(strlen)
