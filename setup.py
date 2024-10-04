from setuptools import setup, Extension
import pybind11

#python3.12 setup.py build_ext --inplace

ext_modules = [
    Extension(
        "euler_solver",
        ["euler_solver.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++"
    )
]

setup(
    name="euler_solver",
    version='0.1',
    ext_modules=ext_modules,
    install_requires=['pybind11'],
    zip_safe=False
)
