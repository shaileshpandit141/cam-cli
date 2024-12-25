from cam_cli_tool.command import get_commans
from cam_cli_tool.create_app import CreateApp
from cam_cli_tool.run import run
from cam_cli_tool.utils import format
from cam_cli_tool.app_tree import js_tree, py_module_tree


def controller():

    absolute_path, command_name, command_options = get_commans()

    if command_name is None:
        return format("""
            :: cam  <- command

            cam command Required at list one argument.

            List of supported argument are:

            :: create-js-app    <- for creating javascript application.
            :: create-py-module    <- for creating python module.
            :: create-flask-app    <- for creating flask application.

            Example:
            create an app with specific app name.
            :: cam create-js-app <app_name>
            :: cam create-py-module <module_name>
            :: cam create-flask-app <app_name>

            create an app with in the current directiory.
            :: cam create-js-app .
            :: cam create-py-module .
            :: cam create-flask-app .
        """)

    # Command validation and handle the JavaScript app.
    if command_name.lower() == "create-js-app":
        if len(command_options) <=0:
            return format("""
                :: cam create-js-app    <- command

                cam create-js-app command required an app_name or . for current directory.

                Example:
                create an app with specific app name.
                :: cam create-js-app <app_name>

                create an app with in the current directiory.
                :: cam create-js-app .
            """)

        # Perform creation of javascript app.
        app_name = command_options[0]
        try:
            js_app = CreateApp(app_name, js_tree())
        except AssertionError as error:
            return error
        response = js_app.create()
        return response

    # Command validation and handle the python module.
    if command_name.lower() == "create-py-module":
        if len(command_options) <=0:
            return format("""
                :: cam create-py-module    <- command

                cam create-py-module command required an app_name or . for current directory.

                Example:
                create an app with specific app name.
                :: cam create-py-module <module_name>

                create an app with in the current directiory.
                :: cam create-py-module .
            """)

        # Perform creation of javascript app.
        module_name = command_options[0]
        try:
            js_app = CreateApp(module_name, py_module_tree())
        except AssertionError as error:
            return error
        response = js_app.create()
        return response

    elif command_name.lower() == "create-py-module":
        if len(command_options) <=0:
            return format("""
                :: cam create-py-module    <- command

                cam create-py-module command required an module_name or . for current directory.

                Example:
                :: cam create-py-module .    <- create an app with in the current directiory.
                :: cam create-py-module <module_name>    <- create an app with specific module name.
            """)

        # Perform creation of javascript app.
        print("py module created.")

    elif command_name.lower() == 'run' or command_name.lower() == 'start':
        response = run()
        return response
    else:
        return "Invalid command"
