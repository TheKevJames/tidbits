import os

import setuptools


PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(PACKAGE_ROOT, 'README.rst')) as f:
    README = f.read()

with open(os.path.join(PACKAGE_ROOT, 'requirements.txt')) as f:
    REQUIREMENTS = [r.strip() for r in f.readlines()]


setuptools.setup(
    name='tidbits',
    version='0.4.1',
    description='Useful Python Tidbits',
    long_description=README,
    packages=setuptools.find_packages(exclude=('tests',)),
    install_requires=REQUIREMENTS,
    extras_require={
        'gcloud': ['python-json-logger >= 0.1.0, < 1.0.0'],
        'sentry': ['raven >= 5.0.0, < 7.0.0'],
    },
    author='Kevin James',
    author_email='KevinJames@thekev.in',
    url='https://github.com/TheKevJames/tidbits',
    project_urls={
        'Changelog': 'https://github.com/TheKevJames/tidbits/releases',
    },
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
)
