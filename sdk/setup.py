from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="rc522-sdk",
    version='0.0.1',
    description='rc522-sdk v0.0.1',
    ext_modules=cythonize(["spi.py", "rc522.py", "util.py", "reader.py"], ),
)
