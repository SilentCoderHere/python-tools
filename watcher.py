from os import get_terminal_size, path
from subprocess import PIPE, run
from sys import argv
from time import perf_counter, sleep


def getFile() -> str:
    if argv[1::]:
        return argv[1]

    else:
        print("usage: python run_file.py __filename__")
        quit()


def getmtime(filename: str) -> float:
    return path.getmtime(filename)


def intro() -> None:
    total = get_terminal_size().columns
    line = ("—" * total) * 2

    print(f"{line}\nChange Detected In File [RUNNING]\n{line}\n")


def timer(func):
    def wrapper(*args, **kwargs) -> None:
        start = perf_counter()
        func(*args, **kwargs)
        print(f"\nThis Process Takes {(perf_counter() - start):.2f} Seconds")

    return wrapper


@timer
def runFile(filename: str) -> None:
    process = run(f"python3 {filename}", stderr=PIPE, shell=True)

    if process.returncode:
        error = process.stderr.decode()
        print(error)


def watcher(filename: str) -> None:
    timeForWait = 3
    lastModified = getmtime(filename)
    print("Watching .....")

    while True:
        lastmt = getmtime(filename)
        if lastModified != lastmt:
            sleep(timeForWait)

            if lastmt != getmtime(filename):
                continue

            intro()
            try:
                runFile(filename)  # Running File

            except KeyboardInterrupt:
                ...
            print("\nWatching .....")

            try:
                lastModified = getmtime(filename)
            except FileNotFoundError:
                continue

        else:
            try:
                sleep(0.5)
            except KeyboardInterrupt:
                print()
                quit()


if __name__ == "__main__":
    filename = getFile()

    if not path.exists(filename):
        print("File Not Found!")

    elif filename.split(".")[-1] == "py":
        watcher(filename)

    else:
        print("Only Python File Supported!")
