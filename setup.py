from setuptools import setup,find_packages

setup(
    name='ismrmrdviewer',
    version='0.2.1',
    packages=find_packages(),
    license='LICENSE.txt',
    author='Kristoffer Langeland Knudsen',
    author_email='kristofferlknudsen@gradientsoftware.net',
    description='Simple tool for viewing ISMRMRD data.',
    entry_points={'gui_scripts' : [ 'ismrmrdviewer=ismrmrdviewer.__main__:main']},
    install_requires=[
        'cycler>=0.12.1',
        'h5py>=3.10',
        'ismrmrd>=1.6.1',
        'kiwisolver>=1.4.4',
        'matplotlib>=3.8',
        'numpy>=1.26',
        'pyparsing>=3.1',
        'PySide6>=6.7',
        'python-dateutil>=2.9',
        'six>=1.16'
    ],
    python_requires='>=3.13'
)
