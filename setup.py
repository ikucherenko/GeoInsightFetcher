from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='GeoInsightFetcher',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points={
        'console_scripts':
            ['GeoInsightFetcher = app.madgicx_geo:main']
        },
    test_suite='app.test_madgicx_geo'
)

install_requires = [
    'requests==2.21.0',
    'mock==2.0.0'
]
