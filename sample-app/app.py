"""Sample app for the Git fundamentals lab."""


def greet(name: str, shout: bool = False) -> str:
    message = f"Hello, {name}!"
    return message.upper() if shout else message


if __name__ == "__main__":
    import sys

    args = [a for a in sys.argv[1:] if a != "--shout"]
    shout = "--shout" in sys.argv[1:]
    who = args[0] if args else "world"
    print(greet(who, shout=shout))
