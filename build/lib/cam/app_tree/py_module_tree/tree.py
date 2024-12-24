from cam.utils import mit_license

def py_module_tree() -> dict:
    return (
        {
            "module_name": {
                "__init__.py": None,
                "main.py": None,
                "utils.py": None
            },
            "tests": {
                "__init__.py": None,
                "main.py": None,
                "utils.py": None
            },
            "camconfig.json": None,
            "setup.py": None,
            "README.md": None,
            "LICENSE.txt": mit_license(),
            ".gitignore": None
        }
    )
