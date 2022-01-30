from setuptools import setup, find_packages

setup(
    name="axe",
    version="1.0",
    author="Krish Matta",
    author_email="self@krishxmatta.dev",
    packages=find_packages(),
    install_requires=[
        "click",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "axe = axe.cli:cli"
        ],
    },
)
