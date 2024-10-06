def flask_app_tree():
    return (
        {
            "flask_app_name": {
                "docs": {
                    "index.md": "Index documentation content"
                },
                "src": {
                    "__init__.py": "",
                    "views.py": "Views content",
                    "models.py": "Models content",
                    "forms.py": "Forms content",
                    "static": {
                        "css": {
                            "style.css": "/* CSS content */"
                        },
                        "images": {},
                        "icons": {},
                        "js": {
                            "script.html": "<!-- JavaScript content -->"
                        }
                    },
                    "templates": {
                        "base.html": "<!-- Base template content -->",
                        "home.html": "<!-- Home template content -->"
                    },
                    "utils": {
                        "helper_functions.py": "# Helper functions"
                    }
                },
                "tests": {
                    "test.py": "# Test cases"
                },
                "config.py": "# Configuration file",
                ".gitignore": "# Ignore file",
                "LICENSE.txt": "License content",
                "README.md": "README content",
                "run.py": "# Run script",
                "requirements.txt": "# Requirements file"
            }
        }
    )
