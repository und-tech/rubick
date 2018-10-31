![Rubick Logo](http://freevector.co/wp-content/uploads/2010/07/24941-magician-hat-with-facial-hair1.png)
# Rubick

##### ¿Qué es?
Es una linea de comando que utiliza plantillas (scaffolds) para generar una estructura base.

##### ¿Dónde se encuentran los scaffolds?
Las plantillas estan almacenadas en el repositorio https://github.com/und-tech/rubick-scaffolds, la estructura de estas plantillas cumple con la arquitectura propuesta para nuestros proyectos.

##### ¿Qué tipos de proyectos puedo crear?

* APIrest (python, netCore, nodeJS)
* Crones o Schedules (python)

# Requerimientos

* python3
* supertools
* git

# Instalación:

~~~~
$ pip install rubick
~~~~

También puedes instalar directamente desde el repositorio

~~~~
$ git clone https://github.com/und-tech/rubick
$ cd rubick
$ make install-developer
$ rubick
~~~~

[![asciicast](https://asciinema.org/a/ArNF5eyZkVdojLwq78Kvjd15g.png)](https://asciinema.org/a/ArNF5eyZkVdojLwq78Kvjd15g)

# Creación de un proyecto

Este comando creara la estructura de un proyecto Rest basado en python

~~~~
$ rubick api:create
~~~~

[![asciicast](https://asciinema.org/a/sJKZVCFcMZed30s7XNduDdSE4.png)](https://asciinema.org/a/sJKZVCFcMZed30s7XNduDdSE4)


# Actualización de Scaffolds

Si los templates son modificados podemos usar este comando para actualizar nuestra copia local

~~~~
$ rubick scaffolds:update
~~~~

Para ver más comandos:

~~~~
$ rubick
~~~~
