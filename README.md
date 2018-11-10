![Rubick Logo](https://i.imgur.com/JcJOzXA.png)

# Rubick Build tool
> Rubick es una linea de comando que nos permite utilizar scaffolds para generar la estructura base de cualquier tipo de proyecto.

# Scaffold
> Un scaffold (andamios) es una plantilla que contiene la estructura del proyecto y una serie de indicaciones las cuales seran utilizadas por Rubick para crear de manera dinamica el proyecto.
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
Requerimientos:
* docker
```sh
docker pull devlusaja/rubick
docker run -it devlusaja/rubick
```

# Licencia
MIT

**Free Software, Hell Yeah!**