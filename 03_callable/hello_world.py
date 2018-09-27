import typing


def hello(name: str) -> str:
    return f"Hello {name}!"


def guten_tag(name: str) -> str:
    return f"Guten Tag {name}!"


def greeting(formatter: typing.Callable[[str], str], name: str) -> str:
    return formatter(name)


if __name__ == "__main__":
    print(greeting(hello, "world"))
    print(greeting(guten_tag, "Welt"))
