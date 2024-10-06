from setuptools import setup, find_packages

setup(
    name="mycliapp",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "cam=cam.main:main",  # CLI command
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI app with math and string utilities using sys module",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mycliapp",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
