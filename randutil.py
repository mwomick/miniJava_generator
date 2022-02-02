from random import randint, choice
import string


def randDigit():
    r = randint(0, len(string.digits) - 1)
    return string.digits[r]


def randUppercase():
    r = randint(0, len(string.ascii_uppercase) - 1)
    return string.ascii_uppercase[r]


def randLowercase():
    r = randint(0, len(string.ascii_lowercase) - 1)
    return string.ascii_lowercase[r]


def randLetter():
    r = randint(0, len(string.ascii_letters) - 1)
    return string.ascii_letters[r]


def randCase(start, end, exclude=[]):
    return choice([i for i in range(start, end) if i not in exclude])

