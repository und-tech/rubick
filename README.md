![Rubick Logo](https://i.imgur.com/JcJOzXA.png)

# Rubick Build tool
> Rubick es una herramienta versatil que nos permite utilizar scaffolds para generar la estructura base de cualquier tipo de proyecto.

# Scaffold
> Un scaffold (andamios) es una plantilla que contiene la estructura del proyecto y una serie de indicaciones (lenguaje ubicuo) las cuales seran utilizadas por Rubick para crear de manera dinamica el proyecto.
Rubick cuenta con scaffolds genericos almacenados en el repositorio https://github.com/und-tech/rubick-scaffolds, pero lo genial es que tambien puedes crear tus propios scaffolds y pasarlos a Rubick.

# Instalación:
Rubick ofrece 3 formas para instalarlo

#### 1. PIP
Requerimientos:
* python3
* git
```sh
pip install rubick
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

# Lenguaje Ubicuo
Cualquier scaffold que se desee pasar a Rubick debera incluir un archivo .scaffold en el cual se ingresaran las instrucciones para Rubick
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

# Licencia
MIT

**Free Software, Hell Yeah!**