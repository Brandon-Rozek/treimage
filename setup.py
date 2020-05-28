from setuptools import setup, find_packages

setup(
    name="treimage",
    description="Copy an image out of trebuchets.",
    version="0.1",
    packages=find_packages(),
    install_requires=['Pillow~=7.1.2']
)