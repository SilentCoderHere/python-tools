from inspect import getfullargspec, isclass
from io import StringIO
from typing import Callable


def inspectFunction(__func__: Callable) -> dict:
    """
    Extract details about a function.

    Returns a dict with:
      - name: function name
      - args: list of arguments
      - default: dict of default arguments (if any)
      - varargs: variable arguments (*args)
      - varkw: keyword arguments (**kwargs)
      - annotation: type annotations
    """
    allData: dict = {}
    allData["name"] = __func__.__name__

    fullargs = getfullargspec(__func__)

    argument = fullargs.args
    allData["args"] = argument

    defaultValue = fullargs.defaults
    if defaultValue:
        defaultLen = len(defaultValue)
        defaultArgs = fullargs.args[::-1][:defaultLen][::-1]
        defaultDict = {}

        for key, value in zip(defaultArgs, defaultValue):
            defaultDict[key] = value

        allData["default"] = defaultDict

    if fullargs.varargs:
        allData["varargs"] = fullargs.varargs
    if fullargs.varkw:
        allData["varkw"] = fullargs.varkw

    allData["annotation"] = fullargs.annotations
    return allData


def buildDoc(__func__: Callable, read: bool = False) -> str:
    """
    Build a documentation string for a function.

    If read=True, generates a human-readable version.
    Otherwise, generates a template with placeholders.
    """
    __doc__ = StringIO()
    write = __doc__.write
    index = 1

    detail = inspectFunction(__func__)

    if read:
        write("Function name: ")

    write(detail["name"])

    if not read:
        write(": __description__")

    write("\n\nArgument:\n")
    for args in detail["args"]:
        __type = detail["annotation"].get(args, "Unknown")

        if isclass(__type):
            __type = __type.__name__

        extra = ""
        if "default" in detail and args in detail["default"]:
            default = detail["default"][args]
            __type = f"{__type}, optional"
            extra = f" Default is {default!r}."

        write(
            f"   {args} ({__type}): {' __summary__.' if not read else f'parameter {index}.'}{extra}\n"
        )

        index += 1

    returnType = detail["annotation"].get("return", "<unknown>")

    if returnType != "<unknown>":
        if isclass(returnType):
            returnType = returnType.__name__

        write(f"\nReturns: {returnType if read else ''}")
        if not read:
            write(f"\n   {returnType}: __summary__.")

    return __doc__.getvalue()


if __name__ == "__main__":

    def testFunc(a: int, b: str = "Hi") -> str:
        return b * a

    print(inspectFunction(testFunc))
    print(buildDoc(testFunc, read=True))
