from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cam-cli-tool",
    version="0.2.4",
    author="shailesh",
    author_email="shaileshpandit141@gmail.com.com",
    description=("""
        cam CLI is a command-line tool for creating boilerplate code for various types of applications
        including vanilla JavaScript frontend web app, Python module, Flask app and etc.
    """),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shaileshpandit141/cam-cli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "livereload>=2.5"
    ],
    entry_points={
        "console_scripts": [
            "cam=cam.main:main",  # cam CLI command.
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
