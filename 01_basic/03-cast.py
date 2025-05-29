def printHeader(title):
    print("-"*25)
    print("»",title)
    print("-"*25)


printHeader("str to int")
print(type(int("5")))

printHeader("any to str")
print(type(str(5)))
print(type(str(5.5)))
print(type(str(True)))
print(type(str(None)))

printHeader("str to float")
print(type(float("10e5")))

printHeader("any to bool")
print(type(bool(5)),5, bool(5), sep="\t|\t")
print(type(bool(0)),0, bool(0), sep="\t|\t")
print(type(bool("")),'""', bool(""), sep="\t|\t")
print(type(bool(" ")),'" "',bool(" "), sep="\t|\t")
print(type(bool("False")),"False", bool("False"), sep="\t|\t")
print(type(bool("True")), "True", bool("True"), sep="\t|\t")

