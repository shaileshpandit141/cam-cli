from textwrap import dedent

def format(sting_code: str) -> str:
    return dedent(sting_code).strip("\n")
