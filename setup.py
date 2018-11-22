import os.path
from setuptools import setup, find_packages

package_dir = os.path.abspath(os.path.dirname(__file__))
setup(
    name = "rubick",
    version = "0.0.4",
    author = "Orbis Venture S.A.C",
    author_email = "oscar.sanchez@orbis.com.pe",
    description = "Es una herramienta OpenSource escrita en Python que nos permite "
                  "utilizar scaffolds para generar la estructura base de cualquier tipo de "
                  "proyecto sin importar el lenguaje de programación o el tamaño del proyecto",
    package_data={'': ['config.yaml']},
    packages = find_packages(),
    include_package_data=True,
    install_requires = ["click==6.7",
                        "Jinja2==2.10",
                        "GitPython==2.1.11",
                        "PyYAML==3.12",
                        "terminaltables==3.1.0"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts = ['bin/rubick'],
)
