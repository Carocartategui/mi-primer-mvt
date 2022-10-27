# Nuestro Primer MVT Django - CoderHouse Python

## Proyecto Final

Comision: 44065
Profesor: German Martinez
Tutor: Esteban Acevedo

Grupo Conformado por:
- Carolina Cartategui
- Claudio Ruhlmann
- Christian Porcel de Peralta

El ejemplo de MVT contiene codigo de:

- Modelos
- Vistas
- Templates

## Chequear que este instalado Python

Para comenzar primero tienen que asegurarse que tienen instalado, python.

En windows tiene que abrir una terminal cmd o powershell.

```PS
PS C:\> python --version
Python 3.X.X 
```

En Linux/Mac tiene que abrir una terminal bash

```bash
$ python --version
Python 3.X.X 
```

Si les aparece la versión todo OK pueden seguir. Caso contrario descarguen python desde este [link](https://www.python.org/downloads/).

## Instalar django

En una terminal cmd o powershell desde windows:

```PS
C:\> pip install django
```

Linux/Mac:

```bash
$ pip install django
```

Si no arrojo errores esto es suficiente para poder correr el projecto.

## Clonar el projecto con git

Windows:

```PS
C:\> git clone https://github.com/Carocartategui/mi-primer-mvt
```

Linux/Mac:
```bash
$ git clone https://github.com/Carocartategui/mi-primer-mvt
```

## Correr el Servidor

Los siguinetes comandos son analogos en Mac/Linux/Windows:

```bash
cd mi-primer-mvt
python manage.py migrate
```
La consola mostrara las migraciones de la base de datos que se realizaron.

Luego arrancamos el servidor web

```bash
python manage.py runserver
```
Listo ya tienes corriendo el servidor web.

Ahora has click en el siguiente link para ver el ejemplo corriendo: 

[http://localhost:8000/](http://localhost:8000/)
