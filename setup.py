from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), 'r') as f:
    long_description = f.read()

setup(
    name='Gen-make',
    version='1.0.0',
    description='A script generate basic Makefile',
    author='Pravin Raghul',
    author_email='pravinraghul@gmail.com',
    url='https://github.com/Ideas100/Gen-make',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    classifiers= [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8'
    ],
    packages=['gen_make'],
    entry_points={
        'console_scripts': ['gen-make = gen_make.script:main'],
    }
)
