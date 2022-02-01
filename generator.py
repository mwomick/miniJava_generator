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


def randVisibility():
    '''Returns an optional visibility keywords with trailing space'''
    r = randint(0, 2)
    return ['public ', 'private ', ''][r]


def randAccess():
    '''Returns an optional 'static' keyword with trailing space'''
    r = randint(0, 1)
    return 'static ' if r == 0 else ''


def randTypeOrVoid():
    '''Returns a Type or void keyword'''
    # 5 choices of Type + void
    r = randint(0, 5)
    if r == 0:
        return 'void'
    else:
        return randType()


def randType():
    '''Returns a Type'''
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
    for _ in range(1, numOfParameters+1):
        parameters += ', '
        parameters += f'{randType()} {randIdentifier()}'
    
    return parameters


def randArgumentList():
    '''Returns 0 or more arguments'''
    numOfArguments = randint(0, 8)
    if numOfArguments == 0:
        return ''
    
    args = randExpression()
    for _ in range(1, numOfArguments+1):
        args += ', '
        args += randExpression()
    
    return args


def randReference():
    '''Returns a random reference of format id | this | Reference . id'''
    e = randint(0, 2)
    if e == 0:
        return randIdentifier()
    elif e == 1:
        return 'this'
    else:
        return f'{randReference()}.{randIdentifier()}'


def makeStatement(indentation: int = 0):
    e = randint(0, 7)

    statement = '  ' * indentation
    if e == 0:
        statement += '{\n'
        statement += makeStatement(indentation+1)
        statement += '  ' * indentation + '}\n'
        return statement

    if e == 1:
        statement += f'{randType()} {randIdentifier()} = {randExpression()};\n'
        return statement
    if e == 2:
        statement += f'{randReference()} = {randExpression()};\n'
        return statement
    if e == 3:
        statement += f'{randReference()} [{randExpression()}] = {randExpression()};\n'
        return statement
    if e == 4:
        statement += f'{randReference()}({randArgumentList()});\n'
        return statement
    if e == 5:
        hasExpresion = randint(0, 1)
        if hasExpresion == 0:
            return 'return;\n'
        statement += f'return {randExpression()};\n'
        return statement
    if e == 6:
        statement += f'if ({randExpression()})\n'
        statement += makeStatement()

        hasElse = randint(0, 1)
        if hasElse == 0:
            return statement
        
        statement += '  ' * indentation + 'else\n'
        statement += makeStatement()
        return statement
    if e == 7:
        statement += f'while ({randExpression()})\n'
        statement += makeStatement()
        return statement


def randExpression():
    e = randint(0, 5)

    if e == 0:
        return randReference()
    elif e == 1:
        return randReference() + "[" + randExpression()+"]"
    elif e == 2:
        return "(" + randExpression() + ")"
    elif e == 3:
        return randLiteral()
    elif e == 4:
        return randUnop() + randExpression()
    elif e == 5:
        return randExpression() + randBinop() + randExpression()


def randLiteral():
    '''Returns a num or a boolean value'''
    r = randint(0, len(literals) - 1)
    return literals[r]


def randIdentifier():
    '''Returns an identifier'''
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
    '''Returns an operator'''
    r = randint(0, len(operators) - 1)
    return operators[r]


def randBinop():
    '''Returns an binary operator'''
    r = randint(0, len(binop) - 1)
    return binop[r]


def randUnop():
    '''Returns an unary operator'''
    r = randint(0, len(unop) - 1)
    return unop[r]

