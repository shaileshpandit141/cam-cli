from sys import argv


def get_commans() -> tuple[str, str | None , list[str]]:
    commands: list[str] = argv
    absolute_path: str = commands[0]
    command_name: str | None = None
    command_options: list[str] = []
    try:
        command_name = commands[1]
        command_options = commands[2:]
    except IndexError as error:
        pass

    return (absolute_path, command_name, command_options)
