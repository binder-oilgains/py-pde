from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'py-pde',
  packages = find_packages(),
  version = '0.2.1',
  license='MIT',
  description = 'Python package for solving partial differential equations',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'David Zwicker',
  author_email = 'david.zwicker@ds.mpg.de',
  url = 'https://github.com/zwicker-group/py-pde',
  download_url = 'https://github.com/zwicker-group/py-pde/archive/v0.2.1.tar.gz',
  keywords = ['pdes', 'partial-differential-equations', 'dynamical-systems'],
  python_requires='>=3.6',
  install_requires=['matplotlib',
                    'numpy',
                    'numba',
                    'scipy',
                    'sympy'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)