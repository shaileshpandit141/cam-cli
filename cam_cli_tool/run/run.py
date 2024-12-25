import os
import json
from livereload import Server  # type: ignore
from datetime import datetime
from cam_cli_tool.utils import format

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
        print('Error: The file `camconfig.json` was not found.')
    except json.JSONDecodeError:
        print('Error: The file `camconfig.json` contains invalid JSON.')

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
            except Exception:
                print('Enter a 4 digit port number.')

def run():
    # Check if the configuration file exists
    if not os.path.exists('camconfig.json'):
        return 'camconfig.json file does not exist.'

    # Read and validate the configuration
    camconfig = read_json()
    if not validate_camconfig_structure(camconfig):
        return 'Invalid camconfig.json'

    app_type = camconfig.get('type', '').lower()  # type: ignore
    if app_type == 'js-app':
        result = validate_and_serve_js_app(camconfig)
        return result if result else None
    else:
        return 'value of type key is invalid in camconfig.json'


def validate_camconfig_structure(camconfig):
    if camconfig is None:
        print('Please configure the camconfig.json file.')
        return False
    if not isinstance(camconfig, dict):
        print('camconfig.json must be a dictionary.')
        return False
    return True


def validate_and_serve_js_app(camconfig):
    # Validate and get host
    HOST = camconfig.get('host')
    if not validate_host(HOST):
        return f'Invalid host ({HOST}) in camconfig.json'

    # Validate and get port
    PORT = camconfig.get('port')
    if not validate_port(PORT):
        return f'Invalid port ({PORT}) in camconfig.json'

    # Validate and get path
    PATH = camconfig.get('path')
    if not validate_path(PATH):
        return 'Invalid path config in camconfig.json'

    # Validate root and watch paths
    root_path = PATH.get('root')
    watch_path = PATH.get('watch')
    if not root_path or not watch_path:
        return 'root and watch keys are not found in camconfig.json'

    # Start the server
    serve(root_path=root_path, watch_path=watch_path, host=HOST, port=PORT)
    return None


def validate_host(host):
    return isinstance(host, str) and (len(host) in {6, 9, 13} or host == '')


def validate_port(port):
    return isinstance(port, int) and len(str(port)) >= 4


def validate_path(path):
    return isinstance(path, dict) and 'root' in path and 'watch' in path
