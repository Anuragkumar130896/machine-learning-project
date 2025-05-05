from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    Returns a list of required packages listed in the given file.
    '''
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]  # Removes \n and empty lines

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Anurag Kumar',
    author_email='anu130896@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
