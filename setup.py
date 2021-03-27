import setuptools
import sys
from pathlib import Path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


CURRENT_DIR = Path(__file__).parent
sys.path.insert(0, str(CURRENT_DIR))


setuptools.setup(
    name="trates",
    version="1.0",
    packages=["src", "src/trates"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "trates-prepare=src.__main__:prepare",
            "trates-rmsd=src.__main__:rmsd"
        ],
    },
    author="Kobie Kirven",
    description="TTSIM",
    install_requires=["setuptools", "biopython"],
    python_requires=">=3.5",
)
