from setuptools import setup, find_packages

setup(
    name="pushoverkit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "pushoverkit=pushoverkit.cli.main:main"
        ]
    },
)