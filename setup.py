from setuptools import setup, find_packages
from pathlib import Path

# Read README.md as long_description
this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text(encoding="utf-8")

setup(
    name="pushoverkit",
    version="0.1.0",
    author="Trần Ngọc Minh Hiếu",
    author_email="tnmhieu@gmail.com",
    description="A powerful and Pythonic wrapper for the Pushover API with CLI support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tranngocminhhieu/pushoverkit",
    packages=find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points={
        "console_scripts": [
            "pushoverkit=pushoverkit.cli.main:main"
        ]
    },
)