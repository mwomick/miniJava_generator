from random import randint

import randutil

literals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'true', 'false']
binop = ['>', '<', '==', '>=', '<=', '!=', '&&', '||', '+', '-', '*', '/']
unop = ['-', '!']
operators = ['>', '<', '==', '>=', '<=', '!=', '&&', '||', '+', '-', '*', '/', '!']


def makeProgram():
    # // P comment is for my personal testing purposes
    program = '// P\n'
    program += "class " + randIdentifier() + " { \n"
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
    if e == 0:
        return " int"
    elif e == 1:
        return " boolean"
    elif e == 2:
        return " " + randIdentifier()
    elif e == 3:
        return " " + randIdentifier() + "[]"
    elif e == 4:
        return " int[]"


def makeField():
    field = ""
    visibility = randint(0, 2)
    access = randint(0, 1)

    if visibility == 0 :
        pass
    elif visibility == 1:
        field += " public"
    elif visibility == 2:
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
        return makeReference() + "." + randIdentifier()


def makeStatement():
    e = randint(0, 2)
    if e == 0:
        return "\n{\n" + makeStatement() + "\n}\n"
    if e == 1:
        return makeType() + " " + randIdentifier() + "="+makeExpression()+";\n"
    if e == 2:
        return makeReference() + "=" + makeExpression() + ";\n"


def makeExpression():
    e = randint(0, 5)

    if e == 0:
        return makeReference()
    elif e == 1:
        return makeReference() + "[" + makeExpression()+"]"
    elif e == 2:
        return "(" + makeExpression() + ")"
    elif e == 3:
        return randLiteral()
    elif e == 4:
        return randUnop() + makeExpression()
    elif e == 5:
        return makeExpression() + randBinop() + makeExpression()


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

    if access == 0:
        pass
    else:
        method += " static"

    if typ == 0:
        method += " void"
    else:
        method += " " + makeType()

    method += " " + randIdentifier() + "(){\n"
    method += makeStatement()
    method += "\n}"
    return method


def randLiteral():
    r = randint(0, len(literals) - 1)
    return literals[r]


def randIdentifier():
    length = randint(1, 10)

    identifier = randutil.randLetter()

    for _ in range(1, length):
        case = randint(0, 3)
        if case == 0:
            identifier += randutil.randUppercase()
        elif case == 1:
            identifier += randutil.randLowercase()
        elif case == 2:
            identifier += randutil.randDigit()
        elif case == 3:
            identifier += '_' # underscore

    return identifier


def randOperator():
    r = randint(0, len(operators) - 1)
    return operators[r]


def randBinop():
    r = randint(0, len(binop) - 1)
    return binop[r]


def randUnop():
    r = randint(0, len(unop) - 1)
    return unop[r]


def randVisibility():
    r = randint(0, 2)
    return ['public ', 'private ', ''][r]


def randAccess():
    r = randint(0, 1)
    return 'static ' if r == 0 else ''


def randType():
    # 5 choices
    # int | boolean | id | int[] | id[] 
    r = randint(0, 4)
    if r == 0:
        return 'int'
    if r == 1:
        return 'boolean'
    if r == 2:
        return randIdentifier()
    if r == 3:
        return 'int[]'
    if r == 4:
        return f'{randIdentifier}[]'


def randParameterList():
    numOfParameters = randint(0, 8)
    if numOfParameters == 0:
        return ''

    parameters = f'{randType()} {randIdentifier()}'
    for _ in range(1, numOfParameters):
        parameters += ', '
        parameters += f'{randType()} {randIdentifier()}'
    
    return parameters


def randArgumentList():
    pass