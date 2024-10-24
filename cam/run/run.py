import os
import json
from livereload import Server

def read_json() -> dict | None:
    '''
    Reads a JSON file and converts it to a Python native data type (dictionary or list).

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        data (dict or list): Python native data type containing the JSON content.
    '''
    try:
        with open('camconfig.json', 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f'Error: The file `camconfig.json` was not found.')
    except json.JSONDecodeError:
        print(f'Error: The file `camconfig.json` contains invalid JSON.')

def serve(root_path: str, watch_path: str, port: int = 8000, host: str ='localhost'):
    '''
    Start live watch server for frontend devlopment.
    '''
    server = Server()
    # Watch the directory for changes
    server.watch(watch_path, delay=1)

    # Start the server on port 8000
    try:
        server.serve(root=root_path, port=port, host=host)
    except OSError as error:
        print(error)
        print('If you want to run it from any other port then please enter that')
        new_port = input(':: ')
        if len(new_port) == 4:
            try:
                new_port = int(new_port)
                server.serve(root=root_path, port=new_port, host=host)
            except Exception as error:
                print('Enter a 4 digit port number.')

def run():
    if not (os.path.exists('camconfig.json')):
        return 'camconfig.json file is not exist.'

    camconfig = read_json()

    if camconfig is None:
        return 'Please configure the camconfig.js file.'
    if not isinstance(camconfig, dict):
        return 'Invalid camconfig.json'
    if 'type' not in camconfig:
        return 'type key is not configure in camconfig.json file.'

    app_type: str = camconfig['type']
    
    # Handle fronend.
    if app_type.lower() == 'js-app':
        if 'path' not in camconfig:
            return 'path key is not find in the camconfig.json'

        path:str  = camconfig['path']

        if not isinstance(path, dict):
            return 'Invalid path config in camconfig.json'
        if 'root' not in path and 'watch' not in path:
            return 'camconfig.json is not configure path key properly.'

        root_path = path['root']
        watch_path = path['watch']

        serve(root_path=root_path, watch_path=watch_path)
    else:
        return 'value of type key is invalid in camconfig.json'