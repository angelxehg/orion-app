# Orion ECS CMD

Orion Effective Communications System Command Module

## Objetivos

Desarrollar una aplicación de mensajería instantánea con herramientas para mejorar la eficiencia de la comunicación entre alumnos y profesores, en un periodo de 3 meses.

- [ ]  Completar documentación ISO 29110
- [ ]  Crear plataforma Backend
- [ ]  Crear interface de usuario
- [ ]  Desplegar aplicación

## Commands

Crear entorno virtual `python -m virtualenv .env/orion/`

Activar entorno virtual `source .env/orion/bin/activate.fish`

Instalar paquetes `pip install -r requirements.txt`

Migrar estructura base de datos `python manage.py migrate`

Crear super usuario `python manage.py createsuperuser`

Iniciar servidor `python manage.py runserver`
