from cam.utils.format import format

def camconfig_json() -> str:
    return format('''
        {
            "type": "js-app",
            "host": "localhost",
            "port": 800,
            "path": {
                "root": ".",
                "watch": "."
            }
        }

        ''')

def index_html() -> str:
    return format('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">

            <!-- Linked favicon. -->
            <link rel="shortcut icon" href="./assets/icons/favicon.svg" type="image/x-icon">

            <!-- Default document title. -->
            <title>cam cli</title>

            <!-- Linked stylesheet files. -->
            <link rel="stylesheet" href="./styles/index.css">
            <link rel="stylesheet" href="./styles/app.css">
        </head>
        <body>
            <div id="root">
                <!-- The main content will be written here. -->
            </div>

            <!-- Linked JavaScript files. -->
            <script type="module" src="./src/app.js"></script>
        </body>
        </html>

        ''')

def favicon_svg() -> str:
    return format('''
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 630 630">
        <rect width="630" height="630" fill="#f7df1e"/>
        <path d="m423.2 492.19c12.69 20.72 29.2 35.95 58.4 35.95 24.53 0 40.2-12.26 40.2-29.2 0-20.3-16.1-27.49-43.1-39.3l-14.8-6.35c-42.72-18.2-71.1-41-71.1-89.2 0-44.4 33.83-78.2 86.7-78.2 37.64 0 64.7 13.1 84.2 47.4l-46.1 29.6c-10.15-18.2-21.1-25.37-38.1-25.37-17.34 0-28.33 11-28.33 25.37 0 17.76 11 24.95 36.4 35.95l14.8 6.34c50.3 21.57 78.7 43.56 78.7 93 0 53.3-41.87 82.5-98.1 82.5-54.98 0-90.5-26.2-107.88-60.54zm-209.13 5.13c9.3 16.5 17.76 30.45 38.1 30.45 19.45 0 31.72-7.61 31.72-37.2v-201.3h59.2v202.1c0 61.3-35.94 89.2-88.4 89.2-47.4 0-74.85-24.53-88.81-54.075z"/>
        </svg>

        ''')

def index_css() -> str:
    return format('''
        /* Remove all margins, paddings, and borders */
        *,
        *::before,
        *::after {
            margin: 0;
            padding: 0;
            border: 0;
            box-sizing: border-box;
            vertical-align: baseline;
        }

        /* Set a base font size */
        html {
            /* 16px by default */
            font-size: 100%;
            line-height: 1.5;
            scrollbar-width: thin;
            scroll-behavior: smooth;
        }

        /* Remove list styles */
        ul,
        ol {
            list-style: none;
        }

        /* Remove default fieldset styling */
        fieldset {
            border: 0;
            padding: 0;
            margin: 0;
        }

        /* Remove table spacing */
        table {
            border-collapse: collapse;
            border-spacing: 0;
        }

        /* Reset form elements */
        input,
        button,
        textarea,
        select {
            font-family: inherit;
            font-size: inherit;
            color: inherit;
            background: none;
            border: none;
            outline: none;
            padding: 0;
            margin: 0;
            appearance: none;
            -webkit-appearance: none;
            user-select: none;
        }

        /* Normalize link appearance */
        a {
            text-decoration: none;
            color: default;
            cursor: default;
            user-select: none;
        }

        /* Reset media elements */
        img,
        video,
        audio {
            display: block;
            max-width: 100%;
            height: auto;
            user-select: none;
        }

        /* Reset blockquote styling */
        blockquote {
            margin: 0;
            padding: 0;
        }

        /* Clear floats */
        .clearfix::after {
            content: "";
            display: table;
            clear: both;
        }

        /* Force smooth scrolling */
        html {
            scroll-behavior: smooth;
            overflow: hidden;
            overflow-y: auto;
        }

        /* Reset strong and b to have normal font weight */
        strong,
        b {
            font-weight: normal;
        }

        form {
            user-select: none;
        }

        /* body  */
        body {
            font-family: Arial, Helvetica, sans-serif;
            font-size: 1rem;
            width: 100%;
            overflow: hidden;
            overflow-y: auto;
            text-rendering: optimizeLegibility;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        #root {
            width: 100%;
            height: fit-content;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        ''')

def app_css() -> str:
    return format('''
        /* #root styles for app */
        #root {
            padding-inline: 24px;
            min-height: 100vh;
        }
        /* app initial test styles */
        .app {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            user-select: none;
        }

        /* Circle logo styles */
        .logo {
            aspect-ratio: 1/1;
            width: 100%;
            max-width: 350px;
            background-color: #cccccc;
            border-radius: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            letter-spacing: 0.04em;
            animation: scaleUpDown 2s infinite;
        }

        /* Keyframes for scale up and down */
        @keyframes scaleUpDown {
            0% {
                transform: scale(.8);
            }
    
            50% {
                transform: scale(1);
            }
    
            100% {
                transform: scale(.8);
            }
        }

        h1 {
            padding-block: 16px;
            letter-spacing: 0.04em;
            text-align: center;
            max-width: 550px;
        }

        p {
            letter-spacing: 0.04em;
            line-height: 1.5;
            text-align: center;
            width: 100%;
            max-width: 450px;
        }

        /* Button styles */
        .button {
            background-color: #cccccc;
            margin-block: 16px;
            height: 40px;
            padding-inline: 16px;
            border-radius: 999rem;
            font-size: 16px;
            font-weight: 600;
            letter-spacing: 0.04em;
            text-transform: capitalize;
            transition: background-color 300ms ease-in-out;
        }

        .button:hover {
            background-color: #bbbbbb;
        }

        ''')

def app_js() -> str:
    return format('''
        const root = document.getElementById('root')

        document.addEventListener('DOMContentLoaded', () => {
          root.insertAdjacentHTML("beforeend", (() => (
            `
            <div class="app">
              <div class="logo">00</div>
              <h1>Welcome to cam cli</h1>
              <p>
                This boilerplate includes all the necessary setup to build a frontend web app using vanilla JavaScript.      </p>
              </p>
              <button class="button">increment</button>
            </div>
            `
          ))())

          root.querySelector('.button').addEventListener('click', () => {
            const logo = root.querySelector('.logo')
            let initialNum = parseInt(logo.innerHTML)
            logo.innerHTML = initialNum < 9 ? `0${initialNum + 1}` : initialNum + 1
          })
        })

        ''')
