import os
import json
from livereload import Server
from datetime import datetime
from cam.utils.format import format

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

def get_current_time() -> str:
    '''
    Return the current time format like "Month Date, Year - Hours:minutes:seconds"
    '''
    return datetime.now().strftime("%B %d, %Y - %H:%M:%S")

def serve(root_path: str, watch_path: str, host: str ='localhost', port: int = 8000):
    '''
    Start live watch server for frontend devlopment.
    '''
    server = Server()
    # Watch the directory for changes
    server.watch(watch_path, delay=1)

    # Start the server on port 8000
    try:
        print(format(f'''
            Watching for file changes...
            Performing system checks...

            System check identified no issues.
            {get_current_time()}
            Starting cam development server at http://{host}:{port}
            Quit the server with CONTROL-C.
            '''))
        server.serve(root=root_path,  host=host, port=port)
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

    try:
        app_type: str = camconfig['type']
    except Exception as error:
        return 'type key is not found in camconfig.json'

    # Validate camconfig.json data for running frontend devlopment server.
    if app_type.lower() == 'js-app':
        # Get host from camconfig.json and validate it.
        try:
            HOST: str = camconfig['host']
        except Exception as error:
            return 'host key is not found in camconfig.json'
        if not isinstance(HOST, str):
            return f'Invalid host ({HOST}) in camconfig.json'
        if HOST != '' and len(HOST) != 6 and len(HOST) != 9 and len(HOST) != 13:
            return f'Invalid host ({HOST}) in camconfig.json'

        # Get port from camconfig.json and validate it.
        try:
            PORT: int = camconfig['port']
        except Exception as error:
            return 'port key is not found in camconfig.json'
        if not isinstance(PORT, int):
            return f'Invalid port ({PORT}) in camconfig.json'
        if len(str(PORT)) < 4:
            return f'Invalid PORT ({PORT}) in camconfig.json'
            
        # Get path from camconfig.json and validate it.
        try:
            PATH: dict = camconfig['path']
        except Exception as error:
            return 'path key is not found in camconfig.json'
        if not isinstance(PATH, dict):
            return 'Invalid path config in camconfig.json'

        # Get root and watch path from camconfig.json and validate its.
        try:
            root_path = PATH['root']
            watch_path = PATH['watch']
        except Exception as error:
            return 'root and watch key are not found in camconfig.json'

        serve(root_path=root_path, watch_path=watch_path, host=HOST, port=PORT)
    else:
        return 'value of type key is invalid in camconfig.json'
