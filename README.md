# Tercera Pre Entrega - Gimena Sozzi
# Planoteca

Planoteca es una plataforma creada con el objetivo de establecer un mercado virtual para arquitectos, en el cual puedan publicar sus proyectos de construcción y diseño, y los clientes puedan navegar por ellos para encontrar aquellos que satisfagan sus necesidades. Este proyecto está desarrollado utilizando el framework Django.
## Funcionalidades implementadas

Hasta el momento, se han implementado las siguientes funciones:

- crear_proyecto: Permite crear un proyecto en la base de datos.
- buscar_proyecto: Permite buscar un proyecto en la base de datos.

## Dependencias

Para instalar las dependencias de Planoteca, es recomendable utilizar un entorno virtual (Virtualenv) y luego instalarlas utilizando el archivo requirements.txt. Aquí te dejamos los pasos a seguir:

1. Crear un entorno virtual y activarlo.

2. Instalar las dependencias desde el archivo requirements.txt:

`pip install -r requirements.txt`

## Ejecución

Después de instalar las dependencias, es necesario inicializar la base de datos. Para ello, es necesario ejecutar los siguientes comandos:

1. Aplicar las migraciones para crear la base de datos sqlite:

`python manage.py migrate`

Una vez realizados estos pasos, ya puedes iniciar el servidor de desarrollo de Django con el siguiente comando:

`python manage.py runserver`

## Contribuyentes

- Gimena Sozzi

¡Espero que te sea útil este archivo README.md!
