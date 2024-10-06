import os


class CreateApp:
    def __init__(self, app_name: str, structure: dict) -> None:
        # Validation for for each argument.
        assert isinstance(app_name, str), ':: app_name arg is only string datatype supported.'
        assert isinstance(structure, dict), ':: structue arg is only dict datatype supported.'

        self.app_name = app_name
        self.structure = { app_name: structure}

    def  create(self)-> None:
        # Consider the . directiroy to create a file tree.
        self.__create_structure('.', self.structure)

    def __create_structure(self, base_path: str, structure: dict) -> None:
        for name, content_or_subtree in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content_or_subtree, dict):
                # Create directory
                os.makedirs(path, exist_ok=True)
                print(f"Created directory: {path}")
                # Recursively create the structure within the directory
                self.__create_structure(path, content_or_subtree)
            else:
                # Create file and write content
                with open(path, "w") as file:
                    if content_or_subtree is None:
                        file.write('')
                    else:
                        file.write(content_or_subtree)
                print(f"Created file: {path} with content")

    def run(self):
        pass

    def git_init(self):
        pass
