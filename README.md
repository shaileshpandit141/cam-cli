# cam (core app manager) cli

cam (core app manager) cli is a command-line tool for creating boilerplate code for various types of applications including vanilla JavaScript frontend web apps, Python modules, Flask apps, etc.

### Installation
[You can install cam cli using pip and pip3:](https://pypi.org/project/cam-cli-tool/)

  ```shell
  pip3 install cam-cli-tool
  ```
  **If you are on Windows OS you need to do this**

  - If pip gives you a `WARNING` like this during installation:
  ```shell
  WARNING: The script cam.exe is installed in `C:\Users\Welcome\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz0n4kfra0p8\LocalCache\local-packages\Python310\Scripts` which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  ```

  - Then you need to add the installation PATH of cam.exe to the Windows user environment variables. The PATH is displayed during installation. If you don't add it, Windows will display an error like this:
  ```text
  'cam' is not recognized as an internal or external command,
  operable program or batch file.
  ```

  **Copy the Path from the Warning Message**

  The path you need to add to your PATH environment variable is

  - **Add the Directory to PATH manually**
  1. Open the Start menu, search for `Environment Variables` and select `Edit the system environment variables`.

  2. In the `System Properties` window, click on `Environment Variables`.

  3. In the `Environment Variables` window, find the `Path` variable under `User variables` (for your user) and select it. Then, click `Edit`.

  4. Click `New` and paste the path:
  ```shell
  C:\Users\Welcome\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz0n4kfra0p8\LocalCache\local-packages\Python310\Scripts
  ```
  5. Click `OK` to save the changes and close all the dialog boxes.

  6. Restart Command Prompt
  After updating the PATH, close any open Command Prompt windows and open a new one. Then try running:
  ```shell
  cam
  ```

  *This should now work without issues.*

  - **You can also add an environment variable directly from the Command Prompt**

  1. Open Command Prompt as Administrator
  Search for "Command Prompt" in the Start menu, right-click it, and select Run as administrator.

  2. Add the Directory to the PATH

  Use the following command to add the directory to your PATH temporarily (for the current session):
  ```shell
  set PATH=%PATH%;C:\Users\Welcome\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz0n4kfra0p8\LocalCache\local-packages\Python310\Scripts
  ```
  Change the demo path to match the path displayed in the warning message

  To add it permanently (so it persists across sessions), use this command:
  ```shell
  setx PATH "%PATH%;C:\Users\Welcome\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz0n4kfra0p8\LocalCache\local-packages\Python310\Scripts"
  ```
  Change the demo path to match the path displayed in the warning message

  3. Restart Command Prompt
  After running the command, close the Command Prompt and open a new one to ensure the new PATH is recognized.

  4. Verify the Command
  Now, you should be able to run:
  ```shell
  cam
  ```

  *This should now work without issues.*

### Command list
  - cam create-js-app .
  - cam create-py-module .
  - cam create-flask-app .
  - cam create-js-app <app_name>
  - cam create-py-module <app_name>
  - cam create-flask-app <app_name>
  - cam run

  **note:** . means create app in current directory.

### Usage

Once installed, you can use the following commands to create different types of applications:

### Create a Vanilla JavaScript Frontend Web App
**Command**
```shell
cam create-js-app <app_name>
```
**Navigate to <app_name> directory**
```bash
cam run
```
It will start the development server.

**Directory tree**
```
app_name/
│
├── assets/
│   ├── icons/
|   |   └── favicon.svg
|   └── images/
|
├── meta/
│   ├── config_script.js
│   └── config_styles.css
|
├── src/
│   ├── index.js
│   └── other_js_files
|
├── styles/
│   ├── styles.css
│   └── other_css_files
|
├── .gitignore
├── index.html
├── LICENSE.txt
└── README.md
```

### Create a Python Module
**Command**
```shell
cam create-py-module <module_name>
```
**Navigate to <app_name> directory**
```bash
cam run
```
It will run the Python module for testing.

**Directory tree**
```
module_name/
│
├── docs/
|   └── index.md
|
├── module_name/
│   ├── utils/
|   |   └── __init__.py
│   ├── __init__.py
│   └── main.py
|
├── tests/
│   └── test.py
|
├── config.py
├── .gitignore
├── LICENSE.txt
├── README.md
└── requirements.txt
```

### Create a Flask App
**Command**
```shell
cam create-flask-app <app_name>
```
**Navigate to <app_name> directory**
```bash
cam run
```
It will start the Flask development server.

**Directory tree**
```
flask_app_name/
│
├── docs/
|   └── index.md
|
├── src/
│   ├── __init__.py
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   ├── static/
│   │   ├── css/
│   │   |    └── style.css
|   |   ├── images/
|   |   ├── icons/
|   |   └── js/
|   |       └── script.html
│   ├── templates/
│   │   ├── base.html
│   │   └── home.html
│   └── utils/
│       └── helper_functions.py
│
├── tests/
│   └── test.py
│
├── config.py
├── .gitignore
├── LICENSE.txt
├── README.md
├── run.py
└── requirements.txt
```

### Contributing
Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Author
If you have any questions or need assistance with this project, please contact `Shailesh` at `shaileshpandit141@gmail.com`.

Thank you for using `cam` cli.
