def time_format(sec: int, _format: int = 0, _sort: int = 0, _round: int = 2):
    _hours = 0
    _minute = 0
    _sec = sec

    if sec > 3599:
        _hours += sec // 3600
        _sec = sec % 3600

    if sec > 59:
        _minute += sec // 60
        _sec = sec % 60

    _sec = round(_sec, _round)

    if _sort:
        _hours = str(_hours) + " h "
        _minute = str(_minute) + " m "
        _sec = str(_sec) + " s"

    if _format:
        if _sec and _minute == "0 m ":
            return _sec

        elif _minute and _hours == "0 h ":
            return _minute, _sec

    return _hours, _minute, _sec


def size_format(byte: int, _round: int = 1) -> tuple[int | float, str]:
    kb = 1024
    mb = 1048576
    gb = 1073741824
    tb = 1099511627776
    size = 0
    byte = int(byte)

    if byte < kb:
        return byte, "B"

    elif kb <= byte < mb:
        size, unit = (byte / kb), "KB"

    elif mb <= byte < gb:
        size, unit = (byte / mb), "MB"

    elif gb <= byte < tb:
        size, unit = (byte / gb), "GB"

    elif tb <= byte:
        size, unit = (byte / tb), "TB"

    _size = round(float(size), _round)

    return _size, unit


def direction(windDir: str) -> str:
    windDirLen = len(windDir)
    if windDirLen > 3 or not windDir:
        return "Unknown"

    windDir = windDir.lower()
    newWindDir = ""

    allDir: dict = {
        "e": "east",
        "w": "west",
        "n": "north",
        "s": "south",
    }

    first = True

    for oneWindDir in windDir:
        if oneWindDir in allDir:
            extractedDir = allDir[oneWindDir]

            if first:
                extractedDir = extractedDir.title()
                first = False

            newWindDir += extractedDir

            if windDirLen == 3:
                newWindDir += "-"
                windDirLen = None

        else:
            return "Unknown"

    return newWindDir


if __name__ == "__main__":
    print(direction("NNE"))
    print(time_format(int(input(">>> "))))
