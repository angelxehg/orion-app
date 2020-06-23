# Orion ECS CMD

Orion Effective Communications System Command Module

## Objetivos

Desarrollar una aplicación de mensajería instantánea con herramientas para mejorar la eficiencia de la comunicación entre alumnos y profesores, en un periodo de 3 meses.

- [ ]  Completar documentación ISO 29110
- [ ]  Crear plataforma Backend
- [ ]  Crear interface de usuario
- [ ]  Desplegar aplicación

## Operación

Para crear un entorno virtual `python -m virtualenv ~/.envs/base-env/`

Para activar el entorno virtual `. ~/.envs/base-env/bin/activate.fish`

Para instalar los paquetes usar `pip install -r requirements.txt`

Para migrar las bases de datos usar `python manage.py migrate`

Para crear super usuario usar `python manage.py createsuperuser`

Para iniciar el servidor Django usar `python manage.py runserver` o `python manage.py runserver 0.0.0.0:8000`
