from cam.app_tree.templates.javascript_template import (
    camconfig_json,
    index_html,
    favicon_svg,
    index_css,
    app_css,
    app_js
    
)

def javascript_tree() -> dict:
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
            "README.md": None
        }
    )
