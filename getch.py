from io import StringIO
from sys import stdin
from termios import TCSADRAIN, tcgetattr, tcsetattr
from tty import setraw


def getString(number: int = 1) -> str:
    if number > 10 or number < 1:
        raise ValueError

    fileno = stdin.fileno()

    oldSettings = tcgetattr(fileno)
    try:
        setraw(fileno)
        string = stdin.read(number)
    finally:
        tcsetattr(fileno, TCSADRAIN, oldSettings)

    return string


def getChar() -> str:
    return getString(1)


def getInput(prompt: str = ""):
    stream = StringIO()
    print(prompt, end="", flush=True)

    while True:
        char = getChar()
        if char == "\r":
            stream.seek(0)
            print()
            return stream.read()

        stream.write(char)
        print(char, end="", flush=True)


def getPassword(prompt: str = "", char="*"):
    if len(char) > 1:
        raise ValueError

    stream = StringIO()
    print(prompt, end="", flush=True)

    while True:
        string = getChar()
        if string == "\r":
            stream.seek(0)
            print()
            return stream.read()

        stream.write(string)
        print(char, end="", flush=True)


if __name__ == "__main__":
    word = getPassword("Password: ")
    print(word)
