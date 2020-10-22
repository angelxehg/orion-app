# Orion Chat API

API Antigua de la aplicación [Tomatoe Chat](https://github.com/angelxehg/tomatoe-chat), antes llamada Orion Chat.

- [Configurar PyCharm](./docs/pycharm.md)
- [Diagramas](./docs/diagrams)
- [Open API 3.0](./docs/api/spec.yaml)

## Objetivos

Desarrollar una aplicación de mensajería instantánea con herramientas para mejorar la eficiencia de la comunicación entre alumnos y profesores, en un periodo de 3 meses.

- [X]  Completar documentación ISO 29110
- [X]  Crear plataforma Backend
- [X]  Crear interface de usuario
- [X]  Desplegar aplicación

## Instalación local

Para instalar de manera local ejecute los siguientes comandos:

- Crear entorno virtual `python -m virtualenv .venv/orion/`
- Activar entorno virtual `source .venv/orion/bin/activate`
- Instalar paquetes `pip install -r config/requirements/dev.txt`

Se requiere configurar la base de datos y un super usuario antes de iniciar el servidor

- Migrar estructura base de datos `python manage.py migrate` (se usará SQLite por defecto)
- Crear super usuario `python manage.py createsuperuser`
- Iniciar servidor `python manage.py runserver`
- Ejecutar pruebas `python manage.py test`

## Instalación en Heroku

Para instalar en Heroku ejecute los siguientes comandos:

- Crear aplicación en Heroku `heroku create`

Se deben especificar las variables `SECRET_KEY`, `HOST` y `DEBUG` para que pueda funcionar el servidor

- Generar clave secreta `python keygen.py`
- Configurar clave secreta `heroku config:set SECRET_KEY=[SECRET_KEY]`
- Configurar depuración `heroku config:set DEBUG=FALSE` o `heroku config:set DEBUG=TRUE`
- Configurar host `heroku config:set HOST=[HOST]`
- Configurar production settings `heroku config:set DJANGO_SETTINGS_MODULE=orion_ecs.production`

Se requiere configurar la base de datos y un super usuario antes de iniciar el servidor

- Desactivar CollectStatic `heroku config:set DISABLE_COLLECTSTATIC=1` (solo se requiere la primera vez)
- Migrar estructura base de datos `heroku run python manage.py migrate`
- Correr CollectStatic `heroku run 'bower install --config.interactive=false;grunt prep;python manage.py collectstatic --noinput'`
- Reactivar CollectStatic `heroku config:unset DISABLE_COLLECTSTATIC`
