from random import randint

UC_CONS = "QWRTYPSDFGHJKLZXCVBNM"
LC_CONS = "qwrtypsdfghjklzxcvbnm"
UC_VOW = "AEIOU"
LC_VOW = "aeiou"

def randIdentifier():
    # TODO: Does not currently include digits
    identifier = ""
    for i in range(0, randint(1, 10)):
        case = randint(0, 5)
        if i%2 == 0:
            e = randint(0, 20)
            if(case < 1):
                identifier = identifier + UC_CONS[e:e+1]
            else:
                identifier = identifier + LC_CONS[e:e+1]
        else:
            e = randint(0, 4)
            if(case < 1):
                identifier = identifier + UC_VOW[e:e+1]
            else:
                identifier = identifier + LC_VOW[e:e+1]
    return identifier


def makeProgram():
    program = "class " + randIdentifier() + " { \n"
    for i in range(0, randint(0, 10)):
        fieldOrMethod = randint(0, 1)
        if(fieldOrMethod):
            # field
            program = program + makeField()
        else:
            # method
            pass
    program = program + "}"
    return program


def makeType():
    e = randint(0, 4)
    if(e == 0):
        return " int"
    elif(e == 1):
        return " boolean"
    elif(e == 2):
        return " " + randIdentifier()
    elif(e == 3):
        return " " + randIdentifier() + "[]"
    elif(e == 4):
        return " int[]"


def makeField():
    field = ""
    visibility = randint(0, 2)
    access = randint(0, 1)

    if(visibility == 0):
        pass
    elif(visibility == 1):
        field = field + " public"
    elif(visibility == 2):
        field = field + " private"

    if(access == 0):
        pass
    else:
        field = field + " static"

    field = field + makeType()
    field = field + " " + randIdentifier() + ";\n"  
    return field  


print(makeProgram())