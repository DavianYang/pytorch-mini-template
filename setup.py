import os
from setuptools import find_packages, setup

def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content

def get_requirements(filename='requirements.txt'):
    path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(path, filename), 'r') as f:
        requires = [line.os.replace('\n', '') for line in f.readlines()]
    return requires


if __name__ == "__main__":
    setup(
        name='template',
        version='0.1',
        description='Write Description',
        author='DavianYang',
        auther_email='kothantyarzarhein@gmail.com',
        keywords='deep learning',
        url='https://github.com/DavianYang/mini-template',
        packages=find_packages(exclude=('cfg', 'tools', 'test')),
        license='MIT License',
        setup_requires=['numpy'],
        tests_requires=['pytest'],
        install_requires=get_requirements()
    )