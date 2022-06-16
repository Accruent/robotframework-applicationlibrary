#!/usr/bin/env python3

import version

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("docs/README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='robotframework-applicationlibrary',
      version=version.VERSION,
      description='Robot Framework framework for mobile and desktop testing.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/Accruent/robotframework-applicationlibrary',
      maintainer='Brandon Wolfe, Neil Howell, Matt Bozek, Pinky Majhi',
      maintainer_email='robosquad@accruent.com',
      license='GPL-3.0',
      keywords='Robot Framework robot-framework selenium appium winappdriver appium robotframework'
               'desktop windows zoomba python robotframework-library appium-windows appiumlibrary'
               'appium-mobile mobile applicationlibrary application app lib',
      platforms='any',
      install_requires=requirements,
      extras_require={
        'testing': [
          'Appium-Python-Client',
          'mock'
        ]
      },
      classifiers="""
        Development Status :: 5 - Production/Stable
        Operating System :: OS Independent
        Programming Language :: Python :: 3
        Topic :: Software Development :: Testing
        Framework :: Robot Framework :: Library
        """.strip().splitlines(),
      package_dir={'': 'src'},
      packages=['ApplicationLibrary', 'ApplicationLibrary/Helpers']
      )
