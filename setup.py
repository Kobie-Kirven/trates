import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name='ttsim',
    version='1.0',
    packages=['src'],
    # entry_points = {
    #     "console_scripts": ['ttsimp = src.ttsim:main']
    #     },
    scripts=['./lib/ttsim'],
    author='Kobie Kirven',
    description='TTSIM',
    install_requires=[
        'setuptools',
        'biopython'
    ],
    python_requires='>=3.5'
)