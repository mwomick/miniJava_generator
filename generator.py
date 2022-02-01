from random import randint

import randutil

literals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'true', 'false']
binop = ['>', '<', '==', '>=', '<=', '!=', '&&', '||', '+', '-', '*', '/']
unop = ['-', '!']
operators = ['>', '<', '==', '>=', '<=', '!=', '&&', '||', '+', '-', '*', '/', '!']


def makeProgram():
    # // P comment is for my personal testing purposes
    program = '// P\n'
    program += randClassDeclaration()
    return program


def randClassDeclaration():
    text = f'class {randIdentifier()} {{\n'

    declarationNum = randint(0, 20)
    for _ in range(declarationNum):
        fieldOrMethod = randint(0, 1)
        if fieldOrMethod == 0:
            text += makeFieldDeclaration(indentation=1)
        else:
            text += makeMethodDeclaration(indentation=1)
        text += '\n'
    text += '\n}'


def makeFieldDeclaration(indentation: int = 0):
    field = ''
    if indentation:
        field += '  ' * indentation
    field += f'{randVisibility()}{randAccess()}{randType()} {randIdentifier()};\n'
    return field


def makeMethodDeclaration(indentation: int = 0):
    method = ""
    if indentation:
        method += '  ' * indentation

    method += randVisibility()
    method += randAccess()
    method += randTypeOrVoid() + ' '
    method += randIdentifier()

    method += f'({randParameterList()}) '

    # {Statement*}
    method += '{\n'

    if indentation:
        method += '  ' * indentation

    statementNum = randint(0, 20)
    for _ in range(statementNum):
        method += makeStatement()
    
    method += '}\n'
    return method


def randReference():
    '''Returns a random reference of format id | this | Reference . id'''
    e = randint(0, 2)
    if e == 0:
        return randIdentifier()
    elif e == 1:
        return 'this'
    else:
        return f'{randReference()}.{randIdentifier()}'


def makeStatement():
    # TODO: support more statements
    e = randint(0, 2)
    if e == 0:
        return "\n{\n" + makeStatement() + "\n}\n"
    if e == 1:
        return randType() + " " + randIdentifier() + "="+makeExpression()+";\n"
    if e == 2:
        return randReference() + "=" + makeExpression() + ";\n"


def makeExpression():
    e = randint(0, 5)

    if e == 0:
        return randReference()
    elif e == 1:
        return randReference() + "[" + makeExpression()+"]"
    elif e == 2:
        return "(" + makeExpression() + ")"
    elif e == 3:
        return randLiteral()
    elif e == 4:
        return randUnop() + makeExpression()
    elif e == 5:
        return makeExpression() + randBinop() + makeExpression()


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


def randTypeOrVoid():
    # 5 choices of Type + void
    r = randint(0, 5)
    if r == 0:
        return 'void'
    else:
        return randType()


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
    '''Returns 0 or more parameters'''
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