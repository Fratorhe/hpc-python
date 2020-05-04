from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(
     ext_modules=cythonize(["heat.py","heat_cython.pyx"])
)
