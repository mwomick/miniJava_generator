from random import randint

import randutil

literals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'true', 'false']
binop = ['>', '<', '==', '>=', '<=', '!=', '&&', '||', '+', '-', '*', '/']
unop = ['-', '!']
operators = ['>', '<', '==', '>=', '<=', '!=', '&&', '||', '+', '-', '*', '/', '!']

MAX_REFERENCE_LEVEL = 4
MAX_NESTED_LEVEL = 5

def makeProgram():
    # // P comment is for my personal testing purposes
    program = '// P\n'
    program += makeClassDeclaration()
    return program


def makeClassDeclaration():
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
    return text


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
        method += makeStatement(indentation+1)
    
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
        return f'{randIdentifier()}[]'


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


def randArgumentList(level: int | None = None):
    '''Returns 0 or more arguments'''
    numOfArguments = randint(0, 8) if level > 0 else 0
    if numOfArguments == 0:
        return ''
    
    args = randExpression(level=level-1)
    for _ in range(1, numOfArguments+1):
        args += ', '
        args += randExpression(level=level-1)
    
    return args


def randReference(level: int | None = None):
    '''Returns a random reference of format id | this | Reference . id'''
    e = randint(0, 2) if level > 0 else randint(0, 1)
    if e == 0:
        return randIdentifier()
    elif e == 1:
        return 'this'
    else:
        return f'{randReference(level=level - 1 if level else MAX_REFERENCE_LEVEL)}.{randIdentifier()}'


def makeStatement(indentation: int = 0, level: int | None = None):
    '''Returns a statement'''
    if level is None:
        level = MAX_NESTED_LEVEL
    e = randint(0, 7) if level > 0 else randutil.randCase(0, 7, [1, 2, 3, 6, 7])

    statement = '  ' * indentation
    if e == 0:
        statement += '{\n'
        if level > 0:
            statement += makeStatement(indentation+1)
        statement += '  ' * indentation + '}\n'
        return statement

    if e == 1:
        statement += f'{randType()} {randIdentifier()} = {randExpression(level=level-1)};\n'
        return statement
    if e == 2:
        statement += f'{randReference(level=level-1)} = {randExpression(level=level-1)};\n'
        return statement
    if e == 3:
        statement += f'{randReference(level=level-1)} [{randExpression(level=level-1)}] = {randExpression(level=level-1)};\n'
        return statement
    if e == 4:
        statement += f'{randReference(level=level-1)}({randArgumentList(level=level-1)});\n'
        return statement
    if e == 5:
        hasExpresion = randint(0, 1) if level > 0 else 0
        if hasExpresion == 0:
            return 'return;\n'
        statement += f'return {randExpression(level=level-1)};\n'
        return statement
    if e == 6:
        statement += f'if ({randExpression(level=level-1)})\n'
        statement += makeStatement(level=level-1)

        hasElse = randint(0, 1)
        if hasElse == 0:
            return statement
        
        statement += '  ' * indentation + 'else\n'
        statement += makeStatement(level=level-1)
        return statement
    if e == 7:
        statement += f'while ({randExpression(level=level-1)})\n'
        statement += makeStatement(level=level-1)
        return statement


def randExpression(level: int | None = None):
    '''Returns an expression'''
    if level is None:
        level = MAX_NESTED_LEVEL

    e = randint(0, 7) if level > 0 else randutil.randCase(0, 7, [1, 3, 4, 5])

    if e == 0:
        return randReference(level=level-1)
    if e == 1:
        return randReference(level=level-1) + "[" + randExpression(level=level-1) + "]"
    if e == 2:
        return f'{randReference(level=level-1)}({randArgumentList(level=level-1)})'
    if e == 3:
        return randUnop() + randExpression(level=level-1)
    if e == 4:
        return randExpression(level=level-1) + randBinop() + randExpression(level=level-1)
    if e == 5:
        return f'({randExpression(level=level-1)})'
    if e == 6:
        return randLiteral()
    if e == 7:
        expression = 'new '

        r = randint(0, 2) if level != 0 else 0
        if r == 0:
            expression += f'{randIdentifier()}()'
        elif r == 1:
            expression += f'int[{randExpression(level=level-1)}]'
        else:
            expression += f'{randIdentifier()}[{randExpression(level=level-1)}]'
        return expression


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

