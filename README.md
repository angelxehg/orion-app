# Orion ECS CMD

Orion Effective Communications System Command Module

## Objetivos

Desarrollar una aplicación de mensajería instantánea con herramientas para mejorar la eficiencia de la comunicación entre alumnos y profesores, en un periodo de 3 meses.

- [ ]  Completar documentación ISO 29110
- [ ]  Crear plataforma Backend
- [ ]  Crear interface de usuario
- [ ]  Desplegar aplicación

## Commands

Crear entorno virtual `python -m virtualenv .venv/orion/`

Activar entorno virtual `source .venv/orion/bin/activate.fish`

Instalar paquetes `pip install -r requirements.txt`

Migrar estructura base de datos `python manage.py migrate`

Crear super usuario `python manage.py createsuperuser`

Iniciar servidor `python manage.py runserver`

## Deploy (Heroku)

Generar clave secreta `python keygen.py`

Configurar clave secreta `heroku config:set SECRET_KEY=[SECRET_KEY]`

Configurar depuración `heroku config:set DEBUG=FALSE` o `heroku config:set DEBUG=TRUE`

Configurar host `heroku config:set HOST=[HOST]`

Desactivar CollectStatic `heroku config:set DISABLE_COLLECTSTATIC=1`

Migrar estructura base de datos `heroku run python manage.py migrate`

Correr CollectStatic `heroku run 'bower install --config.interactive=false;grunt prep;python manage.py collectstatic --noinput'`

Reactivar CollectStatic `heroku config:unset DISABLE_COLLECTSTATIC`
