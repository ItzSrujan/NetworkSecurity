from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:  ## process each line
                requirements = line.strip()
                ## ignore empty lines and -e.
                if requirements and requirements != "-e .":
                    requirement_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Srujan Pote",
    author_email="srujanpote16@zohomail.in",
    packages=find_packages(),
    install_requires=get_requirements()
)