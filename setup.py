from setuptools import setup, find_packages
from powerline_date import version

setup(
    name='powerline_date',
    author='Colin Wood',
    author_email='',
    install_requires=[

    ],
    url='',
    download_url='',
    long_description=open('README.mkd').read(),
    version=version,
    include_package_data=True,
    packages=find_packages(),
    description='',
    tests_require=[
        'nose',
    ],
    keywords=[],
)
