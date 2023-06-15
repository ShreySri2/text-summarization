from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    this function is for getting all the depenendcies from the requirements.txt 
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements






setup(
    name='YourPackageName',
    version='1.0.0',
    author='Shrey Srivastava',
    author_email='shrey2502@gmail.com',
    description='model with interface to get dimensions of products on amazon',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)