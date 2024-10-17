from setuptools import find_packages, setup
from typing import List

hypen_e_dot =  '-e .'
def get_requirements(file_path:str)-> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","")for req in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    
    return requirements

setup(
    name = 'car_price',
    version='0.0.1',
    author='Vinay',
    author_email='kumarvinay0011.vk@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)