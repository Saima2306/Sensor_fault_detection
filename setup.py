from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This is a function which returns the list of requirements
    """
    requirements_list:List[str]=[]

    """
    Write a code to read requirement.txt file and obtain in requirements_list 
    """
    
    file1 = open("requirements.txt","r")
    file2 = file1.read()
    requirements_list = file2.split() 
    print(type(requirements_list))
    return requirements_list
setup(
    name = "sensor",
    version = "0.0.1",
    author = "Saima",
    author_email="saimai@iitbhilai.ac.in",
    packages=find_packages(),
    install_requires = get_requirements()

)