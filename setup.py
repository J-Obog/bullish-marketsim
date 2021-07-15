from setuptools import setup, find_packages

setup(
    name='marketsim',
    version='1.0',
    description='Stock market simulation',
    url='https://github.com/J-Obog/market-simulator',
    author='JObog',
    author_email='jobogbaimhe@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests'])
)