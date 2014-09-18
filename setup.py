from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = "clojure-py",
    ext_modules = cythonize('clojure/lang/*.pyx'),
)