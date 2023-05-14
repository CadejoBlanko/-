from setuptools import setup, find_namespace_packages

setup(
    name = 'Sorter',
    version = '0.1',
    description = 'Sorts files in a folder',
    author = 'Oleksandr Martyniuk',
    author_emeil = 'sasha.martynuk.1@gmail.com',
    url = '',
    license = 'MIT',
    packages = find_namespace_packages(),  
    include_package_data = True,
    entry_points = {'console_scripts': ['clean-folder=clean_folder.clean:folder_creation']}
    )