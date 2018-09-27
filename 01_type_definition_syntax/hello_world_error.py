def hello1(name: str) -> str:
    return f"Hello {name}!"


def hello2(name: str) -> str:
    return 1234


if __name__ == "__main__":
    print(hello1(1234))
    print(hello2("world"))
