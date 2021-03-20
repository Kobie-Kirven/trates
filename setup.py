import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# setuptools.setup(
#     name="ttsim", # Replace with your own username
#     version="0.0.1",
#     author="Kobie Kirven",
#     author_email="kjkirven@presby.edu",
#     description="Transporter Termini SIMulation",
#     long_description=long_description,
#     scripts=['./lib/ttsim.sh'],
#     long_description_content_type="text/markdown",
#     url="https://github.com/Kobie-Kirven/TTSIM",
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     package_dir={"": "src"},
#     packages=setuptools.find_packages(where="src"),
#     python_requires=">=3.6",
# )

import setuptools
setuptools.setup(
    name='ttsim',
    version='1.0',
    scripts=['./lib/ttsim.sh'],
    author='Kobie Kirven',
    description='TTSIM',
    packages=['src'],
    install_requires=[
        'setuptools',
    ],
    python_requires='>=3.5'
)