from cam_cli_tool.utils import mit_license
from .templates import (
    camconfig_json,
    index_html,
    favicon_svg,
    index_css,
    app_css,
    app_js,
)

def js_tree() -> dict:
    return (
        {
            "assets": {
                "images": {},
                "icons": {
                    "favicon.svg": favicon_svg()
                }
            },
            "styles": {
                "app.css": app_css(),
                "index.css": index_css()
            },
            "src": {
                "app.js": app_js(),
                "utils.js": None
            },
            "camconfig.json": camconfig_json(),
            "index.html": index_html(),
            "README.md": None,
            "LICENSE.txt": mit_license()
        }
    )
