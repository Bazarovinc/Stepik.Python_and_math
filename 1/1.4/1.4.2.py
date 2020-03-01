def sum2(a, b):
    if (type(a) is not type(1) and type(a) is not type(1.0)) and (type(b) is type(1) or type(b) is type(1.0)):
        return ("1st argument is not a number")
    elif (type(b) is not type(1) and type(b) is not type(1.0)) and (type(a) is type(1) or type(a) is type(1.0)):
        return ("2nd argument is not a number")
    elif (type(a) is not type(1) and type(a) is not type(1.0)) and (type(b) is not type(1) and type(a) is not type(1.0)):
        return ("all arguments are not a numbers")
    else:
        return (str(a + b))

print(sum2(8567.4, 484827323.92))