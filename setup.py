from setuptools import setup, find_packages

setup(
    name='powerline_date',
    author='Colin Wood',
    author_email='cwood06@gmail.com',
    install_requires=[
        'python-dateutil',
    ],
    url='https://github.com/cwood/powerlin-date',
    download_url='https://github.com/cwood/powerline-date',
    long_description=open('README.mkd').read(),
    version="0.0.1",
    include_package_data=True,
    packages=find_packages(),
    description='A powerline date segment replacement',
    tests_require=[
        'nose',
    ],
    keywords=[],
)
