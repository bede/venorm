import re
import sys

from setuptools import setup


__version__ = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        open('venorm/__init__.py').read()).group(1)


if sys.version_info[0] < 3:
      sys.exit('Venorm requires Python >= 3.5')


CLASSIFIERS = ['Environment :: Console',
               'Environment :: MacOS X',
               'Intended Audience :: Science/Research',
               'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
               'Natural Language :: English',
               'Operating System :: POSIX :: Linux',
               'Operating System :: MacOS :: MacOS X',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: 3.6',
               'Topic :: Scientific/Engineering :: Bio-Informatics']


setup(name='venorm',
      version=__version__,
      description='Coverage optimised de novo assembly of viral populations',
      url='https://github.com/bede/venorm',
      author='Bede Constantinides',
      author_email='bedeabc@gmail.com',
      license='LICENSE',
      packages=['venorm'],
      zip_safe=True,
      include_package_data=True,
      install_requires=['argh==0.26.2',
                        'biopython==1.70',
                        'khmer==2.1.1',
                        'numpy==1.22.0',
                        'pandas==0.20.3',
                        'plotly==2.0.14',
                        'requests==2.18.4'],
      entry_points = {'console_scripts':['venorm=venorm.venorm:cli']})
