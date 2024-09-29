from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads the given requirements.txt file
    and returns a list of dependencies.
    '''
    requirements = []
    with open(file_path) as file_obj:
        # Read each line from requirements.txt
        requirements = file_obj.readlines()
        # Remove newline characters and clean each line
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove '-e .' if present (used for local editable installation)
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

# Setup configuration for packaging
setup(
    name='mlproject',
    version='0.0.1',
    author='nsn',
    author_email='nishantsharmaneupane345@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Corrected typo
)
