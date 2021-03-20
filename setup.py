import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TTSIM", # Replace with your own username
    version="0.0.1",
    author="Kobie Kirven",
    author_email="kjkirven@presby.edu",
    description="Transporter Termini SIMulation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kobie-Kirven/TTSIM",
    project_urls={
        "Bug Tracker": "https://github.com/Kobie-Kirven/TTSIM/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)