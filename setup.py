from setuptools import setup, find_packages

setup(
    name='transistor-fm',
    version='0.1.0',
    packages=find_packages(),
    description='A Python client for the Transistor.fm API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Josh Griffiths',
    author_email='josh@hakuna.co.uk',
    url='https://github.com/yourusername/my_package',
    install_requires=['requests']
)