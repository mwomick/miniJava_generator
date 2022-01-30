from random import randint

UC_CONS = "QWRTYPSDFGHJKLZXCVBNM"
LC_CONS = "qwrtypsdfghjklzxcvbnm"
UC_VOW = "AEIOU"
LC_VOW = "aeiou"
DIGIT = "1234567890"
LITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'true', 'false']
BINOPS = ['*', '-', '+', '/', '>', '<', '<=', '>=', '==', '&&', '||']
UNOPS = ['!', '-']

def randIdentifier():
    identifier = ""
    for i in range(0, randint(1, 10)):
        case = randint(0, 5)
        if i > 0:
            e = randint(0, 9)
            if(randint(0,5) == 0):
                identifier += DIGIT[e:e+1]
        if i%2 == 0:
            e = randint(0, 20)
            if(case < 1):
                identifier += UC_CONS[e:e+1]
            else:
                identifier += LC_CONS[e:e+1]
        else:
            e = randint(0, 4)
            if(case < 1):
                identifier += UC_VOW[e:e+1]
            else:
                identifier += LC_VOW[e:e+1]
    return identifier


def makeProgram():
    program = "class " + randIdentifier() + " { \n"
    for i in range(0, randint(0, 10)):
        fieldOrMethod = randint(0, 1)
        if(fieldOrMethod):
            # field
            program += makeField()
        else:
            # method
            program += makeMethod()
    program += "\n}"
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
        field += " public"
    elif(visibility == 2):
        field += " private"

    if(access == 0):
        pass
    else:
        field += " static"

    field += makeType()
    field += " " + randIdentifier() + ";\n"  
    return field  


def makeReference():
    e = randint(0, 2)

    if(e == 0):
        return " " + randIdentifier()
    elif(e == 1):
        return " this"
    else:
        return makeReference() + "." +randIdentifier()


def makeStatement():
    e = randint(0, 2)
    if e == 0:
        return "\n{\n" + makeStatement() + "\n}\n"
    if e == 1:
        return makeType() + " " + randIdentifier() +"="+makeExpression()+";\n"
    if e == 2:
        return makeReference() + "=" + makeExpression() + ";\n"


def makeExpression():
    e = randint(0, 5)

    if(e == 0):
        return makeReference()
    elif(e == 1):
        return makeReference() +"[" +makeExpression()+"]"
    elif(e == 2):
        return "(" + makeExpression() +")"
    elif(e == 3):
        return LITS[randint(0,11)]
    elif(e == 4):
        return UNOPS[randint(0,1)] + makeExpression()
    elif(e == 5):
        return makeExpression() + BINOPS[randint(0, 10)] + makeExpression()

def makeMethod():
    method = ""
    visibility = randint(0, 2)
    access = randint(0, 1)
    typ = randint(0, 1)

    if(visibility == 0):
        pass
    elif(visibility == 1):
        method += " public"
    elif(visibility == 2):
        method += " private"

    if(access == 0):
        pass
    else:
        method += " static"

    if(typ == 0):
        method += " void"
    else:
        method += " " + makeType()

    method += " " + randIdentifier() +"(){\n"
    method += makeStatement()
    method += "\n}"
    return method


print(makeProgram())