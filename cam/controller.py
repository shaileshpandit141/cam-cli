from sys import argv
from cam.command.commad import get_commans
from cam.create_app.create_app import CreateApp
from cam.app_tree.java_script_tree import java_script_tree


def controller():

    absolute_path, command_name, command_options = get_commans()

    if command_name is None:
        return "Invalid command name. did you mean xyz"

    # Command validation.
    if command_name.lower() == "create-js-app":
        if len(command_options) <=0:
            return "Oop's app_name can not be empty enter . or other valid name."

        # Perform your actions.
        app_name = command_options[0]
        try:
            js_app = CreateApp(app_name, java_script_tree())
        except AssertionError as error:
            return error
        print(':: JavaScript App creating...')
        js_app.create()
        print(':: JavaScript App created successful.')

    elif command_name.lower() == "create-py-module":
        if len(command_options) <=0:
            return "Oop's app_name can not be empty enter . or other valid name."
        print("py module created.")
    else:
        return "Invalid command"
