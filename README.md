![Rubick Logo](https://i.imgur.com/JcJOzXA.png)

# Rubick Build tool
> Es una herramienta OpenSource escrita en Python que nos permite utilizar scaffolds para generar la estructura base de cualquier tipo de proyecto sin importar el lenguaje de programación o el tamaño del proyecto.

# Scaffold
> Un scaffold (andamios) es una plantilla que contiene la estructura del proyecto y una serie de indicaciones (especificación) las cuales serán utilizadas por Rubick para crear de manera dinámica el proyecto. Rubick cuenta con scaffolds genericos almacenados en el repositorio [https://github.com/und-tech/rubick-scaffolds](https://github.com/und-tech/rubick-scaffolds), pero lo genial es que también puedes crear tus propios scaffolds para que Rubick los utilice.

# Instalación:
Rubick ofrece 3 formas para instalarlo

#### 1. PIP
Requerimientos:
* python3
* git
```sh
pip3 install rubick
rubick
```

#### 2. Clonar el repositorio
Requerimientos:
* python3
* supertools
* git

```sh
git clone https://github.com/und-tech/rubick
cd rubick
make install-developer
rubick
```

[![asciicast](https://asciinema.org/a/ArNF5eyZkVdojLwq78Kvjd15g.png)](https://asciinema.org/a/ArNF5eyZkVdojLwq78Kvjd15g)

#### 3. Docker
[Click para ir al repositorio de la imagen de Docker](https://hub.docker.com/r/devlusaja/rubick/)

Requerimientos:
* docker
```sh
docker pull devlusaja/rubick
docker run -it devlusaja/rubick
```

# Especificación
Se apuesta por utilizar una especificación o lenguaje que será interpretado por Rubick al momento de crear un proyecto.
Esta especificación nos da la libertad de poder crear diferentes tipos de scaffolds sin la necesidad de hacer cambios en Rubick 
Todo scaffold debe incluir un archivo .scaffold en el cual se ingresaran las instrucciones para Rubick
```yaml
scaffold:
  author: 'Developer'
  name: 'APIrest'
  description: 'API escrita en el lenguaje python utilizando una arquitectura hexagonal.'
  save_prompts: 'prompts.json'
  prompts:
    -
      name: 'package'
      description: 'Ingresa el nombre del paquete principal'
      default: 'context'
    -
      name: 'api_version'
      description: 'Ingresa la versión para tu api'
      default: 'v1'
    -
      name: 'container_port'
      description: 'Ingresa el puerto para la aplicación'
      default: '8080'
  replace_names:
    -
      search: '+package+'
      use_prompt: 'package'
```

# Caracteristicas

- [x] Creación de proyectos.
- [ ] Filtros de búsqueda en el comando scaffolds:list.
- [ ] Soporte para la opción --scaffolds en la imagen de docker.
- [ ] Comando para la validación de la sintaxis de un scaffold.
- [ ] Especificación para la generación de código dentro de un proyecto.

# Licencia
MIT

**Free Software, Hell Yeah!**