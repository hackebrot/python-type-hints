import typing


class Person:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name


Team = typing.List[Person]


def hello_team(team: Team) -> str:
    return "\n".join(f"Hello {person.name}!" for person in team)


if __name__ == "__main__":

    team = [
        Person("Audrey"),
        Person("Danny"),
        Person("Michael"),
        Person("Raphael"),
    ]

    print(hello_team(team))
