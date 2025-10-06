def add1():
    """This function adds 1 + 1 and prints the result."""
    result = 1 + 1
    print(result)

def add2(x, y):
    result = x + y
    print(result)

def add3(x: int, y: int):
    result = x + y
    return result

def add4():
    result = 1 + 1
    return result

def printLogo():
    logo = """  _      ____   _____  _____ 
| |    / __ \ / ____|/ ____|
| |   | |  | | (___ | |     
| |   | |  | |\___ \| |     
| |___| |__| |____) | |____ 
|______\____/|_____/ \_____|"""
    print(logo)

# add2(1, 1)
# variable = (add3(1, 1))
# tipo_variable = type(variable)
#
# print(tipo_variable, "Hola", "adios", "punto")


printLogo()