from setuptools import setup, find_packages

setup(
    name="treimage",
    author="Brandon Rozek",
    description="Copy an image out of trebuchets.",
    version="0.8",
    packages=find_packages(),
    install_requires=['Pillow~=7.1.2']
)