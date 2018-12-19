# Ant
> Es una herramienta OpenSource escrita en Python que nos permite utilizar scaffolds para generar la estructura base de cualquier tipo de proyecto sin importar el lenguaje de programación o el tamaño del proyecto.

# Scaffold
> Un scaffold (andamios) es una plantilla que contiene la estructura del proyecto y una serie de indicaciones (especificación) las cuales serán utilizadas por Ant para crear de manera dinámica el proyecto. Ant cuenta con scaffolds genericos almacenados en el repositorio [https://github.com/und-tech/ant-scaffolds](https://github.com/und-tech/ant-scaffolds), pero lo genial es que también puedes crear tus propios scaffolds para que Ant los utilice.

# Instalación
Ant ofrece 3 formas para instalarlo

#### 1. PIP
Requerimientos:
* python3
* pip3
* git
```sh
pip3 install ant-cli
ant
```

#### 2. Clonar el repositorio
Requerimientos:
* python3
* pip3
* supertools
* git

```sh
git clone https://github.com/und-tech/ant
cd ant
make install-from-source
ant
```

![ant-install](https://i.imgur.com/RZBUoc7.gif)

#### 3. Docker
[Click para ir al repositorio de la imagen de Docker](https://hub.docker.com/r/undcomercio/ant/)

Requerimientos:
* docker
```sh
docker pull undcomercio/ant
docker run -it undcomercio/ant
```

# Especificación
Se apuesta por utilizar una especificación o lenguaje que será interpretado por Ant al momento de crear un proyecto.
Esta especificación nos da la libertad de poder crear diferentes tipos de scaffolds sin la necesidad de hacer cambios en Ant. 
Todo scaffold debe incluir un archivo .scaffold en el cual se ingresaran las instrucciones para Ant
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

# Ejemplos

#### A) En una instalación con PIP3 o desde el origen

##### 1. Listando todos los comandos, opciones y argumentos
![ant](https://i.imgur.com/Q8kDmCE.png)

##### 2. Listando todos scaffolds
![ant-scaffold-list](https://i.imgur.com/HAU6FYW.png)

##### 3. Personalizando la lista de scaffolds
![ant-scaffold-list](https://i.imgur.com/7eT5Zrs.png)

##### 4. Utilizando un scaffold
![ant-scaffold-assemble](https://i.imgur.com/7FvSlPd.gif)

#### B) Con la imagen de Docker

##### 1. Utilizando un scaffold
![docker-ant-scaffold-assemble](https://i.imgur.com/EKu4agc.gif)
 

# Licencia
MIT

**Free Software, Hell Yeah!**