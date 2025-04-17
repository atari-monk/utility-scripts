from setuptools import setup, find_packages

setup(
    name="utility-scripts",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "info=core.info.cli:main",
            "time=core.timestamp_cli:main",
            "taog=core.task_log.cli:main",
            "shme=core.scheme.cli:main"
        ],
    },
    python_requires=">=3.7",
)