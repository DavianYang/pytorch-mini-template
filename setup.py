import io
import os
import re
from setuptools import find_packages, setup

def read(*names, **kwargs):
    path = os.path.dirname(__file__)
    with io.open(
        os.path.join(path, *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as f:
        return f.read()

def get_requirements(filename='requirements.txt'):
    here = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(here, filename), 'r') as f:
        requires = [line.replace('\n', '') for line in f.readlines()]
    return requires

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

readme = read("README.md")

if __name__ == "__main__":
    setup(
        name='template',
        version=find_version("package", "__init__.py"),
        description='Write Description',
        author='DavianYang',
        auther_email='kothantyarzarhein@gmail.com',
        keywords='deep learning',
        url='https://github.com/DavianYang/mini-template',
        packages=find_packages(
            exclude=(
                'cfg', 
                'tools', 
                'tests',
                'tests.*'
            )
        ),
        license='MIT License',
        python_requires=">=3.6.0",
        setup_requires=['pytest-runner', 'cython', 'numpy'],
        tests_requires=['pytest'],
        install_requires=get_requirements(),
        zip_safe=True
    )