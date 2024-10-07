from os import system, path, makedirs
import json
from livereload import Server
from tornado.autoreload import watch
from cam.utils.format import format

class CreateApp:
    def __init__(self, app_name: str, structure: dict) -> None:
        # Validation for for each argument.
        assert isinstance(app_name, str), ':: app_name arg is only string datatype supported.'
        assert isinstance(structure, dict), ':: structue arg is only dict datatype supported.'

        self.app_name = app_name
        self.structure = { app_name: structure}

    def  create(self)-> str:
        '''
        Create the app tree with default content.
        '''
        # Consider the . directiroy to create a file tree.
        if self.__is_file_exist(f'camconfig.json') or self.__is_file_exist(self.app_name):
            return 'This app is exist. try with an other name'
        else:
            print('JavaScript app is creating...\n')
            self.__create_structure('.', self.structure)
            print('\nJavaScript App created successful.\n')
            if self.app_name == '.':
                return format(f'''
                    start the development server by uing cam commands like
                    
                    :: cam run    <- command
                    :: cam start    <- command
                    ''')
            return format(f'''
                start the development server by uing cam commands like
                
                :: cd {self.app_name}    <- navigate to created app
                
                :: cam run    <- command
                :: cam start    <- command
                ''')

    def __is_file_exist(self, file_name: str) -> bool:
        '''
        Check the app is all ready exist or not.
        '''
        return path.exists(file_name)

    def __create_structure(self, base_path: str, structure: dict) -> None:
        for name, content_or_subtree in structure.items():
            absolute_path = path.join(base_path, name)
            if isinstance(content_or_subtree, dict):
                # Create directory
                makedirs(absolute_path, exist_ok=True)
                print(f'Created directory: {absolute_path}')
                # Recursively create the structure within the directory
                self.__create_structure(absolute_path, content_or_subtree)
            else:
                # Create file and write content
                with open(absolute_path, 'w') as file:
                    if content_or_subtree is None:
                        file.write('')
                    else:
                        file.write(content_or_subtree)
                print(f'Created file: {absolute_path} with content')

    def git_init(self):
        pass
