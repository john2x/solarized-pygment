#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='solarized-pygment',
    version='0.1',
    description='Pygments version of the solarized theme.',
    keywords='pygments style solarized',
    #license='BSD',
    author='John Louis Del Rosario',
    author_email='john2x@gmail.com',

    url='https://github.com/john2x/solarized-pygment',

    py_modules=['solarized'],
    install_requires=['pygments >= 1.4'],

    entry_points='''[pygments.styles]
                    solarized=solarized:SolarizedStyle''',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        #'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
