from setuptools import setup, find_packages

setup(
    name="git-quickinit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyGithub",
    ],
    entry_points={
        "console_scripts": [
            "git-quickinit=git_quickinit.cli:main",
        ],
    },
    include_package_data=True,
)
