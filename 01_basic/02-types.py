def printHeader(title):
    print("-"*25)
    print("»",title)
    print("-"*25)

## Int
printHeader("Int")
print(type(5))
print(type(-10))
print(type(156545131515153151351351531))

## Float
printHeader("Float")
print(type(1.0))
print(type(-0.5))
print(type(0.0))
print(type(1e-3))

## String
printHeader("String")
print(type("abc"))
print(type('xyz'))
print(type("1"))
print(type("10e3"))

## Boolean
printHeader("Boolean")
print(type(True))
print(type(False))
print(type(5>3))

## NoneType
printHeader("NoneType")
print(type(None))

