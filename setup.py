from setuptools import setup, find_packages

setup(
    name='bullish',
    version='1.0',
    description='Stock market simulation',
    url='https://github.com/J-Obog/bullish-marketsim',
    author='JObog',
    author_email='jobogbaimhe@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests'])
)