from setuptools import setup, find_packages

requirements = []
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="ceac_tracker",
    packages=find_packages(),
    install_requires=requirements,
)
