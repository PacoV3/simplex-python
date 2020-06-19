# Simplex en Python

Proyecto Simplex de Minimizar y Maximizar y Simplex de 2 fases de Minimizar y Maximizar.

## Pre-requisitos

Para este proyecto necesitamos [python](https://www.python.org) (en este caso use la versión 3.8.2), el manejador de paquetes [pip](https://pip.pypa.io/en/stable/) (que ya viene con las instalación de python) y el controlador de versiones [git](https://git-scm.com).

## Instalación

Primero es necesario clonar el repositorio, crear nuestro entorno virtual y allí instalar los requerimientos.

Clonar el repositorio

```cmd
git clone https://github.com/PacoV3/simplex_python.git
```

Entrar al proyecto

```cmd
cd simplex_python
```

Crear el entorno virtual

```cmd
python -m venv venv
```

Activar el entorno en Windows

```cmd
venv\Scripts\activate.bat
```

Activar el entorno en Linux

```bash
source venv/bin/activate
```

Instalar los requerimientos

```cmd
pip install -r requirements.txt
```

## Uso

Para trabajar con el proyecto necesitamos abrir el excel que anexo y llenar en orden las variables y restricciones junto con la función objetivo.

Una vez llenados los datos solo es necesario ejecutar el proyecto desde la consola, con python.

```cmd
python read_excel.py
```
En el archivo simplex_examples.py hay otras formas de trabajar con la clase, solo es cuestión de querer trabajarlo con Excel o no.

##### Hecho por Francisco - 6to ISCE
