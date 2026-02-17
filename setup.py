from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    try: 
        requirements_list = []
        with open("requirements.txt", "r") as file:

            lines = file.readlines()
            for line in lines:
                requirement = line.strip()

                if requirement and requirement != "-e .":
                    requirements_list.append(requirement)

        print(f"Requirements found: {requirements_list}")
        return requirements_list

    except Exception as e:
        print(f"Error occurred while reading requirements: {e}")
        return []
    
setup(
    name="Atlas",
    version="0.0.1",
    author="Abhinav Gupta",
    author_email="abhinav.gupta.dev05@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)