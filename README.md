# Orion ECS CMD

Orion Effective Communications System Command Module. Powers [Orion Chat](https://github.com/angelxehg/orion-chat-app).

[![CircleCI](https://circleci.com/gh/angelxehg/orion-ecs-cmd.svg?style=shield)](https://circleci.com/gh/angelxehg/orion-ecs-cmd)

## Objetivos

Desarrollar una aplicación de mensajería instantánea con herramientas para mejorar la eficiencia de la comunicación entre alumnos y profesores, en un periodo de 3 meses.

- [ ]  Completar documentación ISO 29110
- [ ]  Crear plataforma Backend
- [ ]  Crear interface de usuario
- [ ]  Desplegar aplicación

## Instalación local

Para instalar de manera local ejecute los siguientes comandos:

- Crear entorno virtual `python -m virtualenv .venv/orion/`
- Activar entorno virtual `source .venv/orion/bin/activate`
- Instalar paquetes `pip install -r config/requirements/dev.txt`

### Configurar e iniciar servidor

Se requiere configurar la base de datos y un super usuario antes de iniciar el servidor

- Migrar estructura base de datos `python manage.py migrate` (se usará SQLite por defecto)
- Crear super usuario `python manage.py createsuperuser`
- Iniciar servidor `python manage.py runserver`
- Ejecutar pruebas `python manage.py test`

## Instalación en Heroku

Para instalar en Heroku ejecute los siguientes comandos:

- Crear aplicación en Heroku `heroku create`

### Variables de entorno

Se deben especificar las variables `SECRET_KEY`, `HOST` y `DEBUG` para que pueda funcionar el servidor

- Generar clave secreta `python keygen.py`
- Configurar clave secreta `heroku config:set SECRET_KEY=[SECRET_KEY]`
- Configurar depuración `heroku config:set DEBUG=FALSE` o `heroku config:set DEBUG=TRUE`
- Configurar host `heroku config:set HOST=[HOST]`
- Configurar production settings `heroku config:set DJANGO_SETTINGS_MODULE=orion_ecs.production`

### Configurar e iniciar servidor

Se requiere configurar la base de datos y un super usuario antes de iniciar el servidor

- Desactivar CollectStatic `heroku config:set DISABLE_COLLECTSTATIC=1` (solo se requiere la primera vez)
- Migrar estructura base de datos `heroku run python manage.py migrate`
- Correr CollectStatic `heroku run 'bower install --config.interactive=false;grunt prep;python manage.py collectstatic --noinput'`
- Reactivar CollectStatic `heroku config:unset DISABLE_COLLECTSTATIC`
