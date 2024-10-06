import os

# Function to create directories and files
def create_structure(base_path: str, structure: dict):
    for name, content_or_subtree in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content_or_subtree, dict):
            # Create directory
            os.makedirs(path, exist_ok=True)
            # Recursively create the structure within the directory
            create_structure(path, content_or_subtree)
        else:
            # Create file and write content
            with open(path, 'w') as file:
                file.write(content_or_subtree)
