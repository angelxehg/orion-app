# PyCharm configuration

Here are some examples of PyCharm Run Configuration

## Run Server

** Note: Change `HOST`, `DEBUG`, `SECRET_KEY` and `SDK_HOME`

```xml
<component name="ProjectRunConfigurationManager">
  <configuration default="false" name="Run Server" type="PythonConfigurationType" factoryName="Python">
    <module name="orion-ecs-cmd" />
    <option name="INTERPRETER_OPTIONS" value="" />
    <option name="PARENT_ENVS" value="true" />
    <envs>
      <env name="PYTHONUNBUFFERED" value="1" />
      <env name="HOST" value="127.0.0.1" />
      <env name="DEBUG" value="TRUE" />
      <env name="SECRET_KEY" value="EXAMPLE_KEY" />
    </envs>
    <option name="SDK_HOME" value="C:\Users\angel\Proyectos\orion-ecs-cmd\.venv\orion\Scripts\python.exe" />
    <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$" />
    <option name="IS_MODULE_SDK" value="false" />
    <option name="ADD_CONTENT_ROOTS" value="true" />
    <option name="ADD_SOURCE_ROOTS" value="true" />
    <option name="SCRIPT_NAME" value="manage.py" />
    <option name="PARAMETERS" value="runserver" />
    <option name="SHOW_COMMAND_LINE" value="false" />
    <option name="EMULATE_TERMINAL" value="false" />
    <option name="MODULE_MODE" value="false" />
    <option name="REDIRECT_INPUT" value="false" />
    <option name="INPUT_FILE" value="" />
    <method v="2" />
  </configuration>
</component>
```

## Run Migrations

** Note: Change `HOST`, `DEBUG`, `SECRET_KEY` and `SDK_HOME`

```xml
<component name="ProjectRunConfigurationManager">
  <configuration default="false" name="Run Migrations" type="PythonConfigurationType" factoryName="Python">
    <module name="orion-ecs-cmd" />
    <option name="INTERPRETER_OPTIONS" value="" />
    <option name="PARENT_ENVS" value="true" />
    <envs>
      <env name="PYTHONUNBUFFERED" value="1" />
      <env name="HOST" value="127.0.0.1" />
      <env name="DEBUG" value="TRUE" />
      <env name="SECRET_KEY" value="EXAMPLE_KEY" />
    </envs>
    <option name="SDK_HOME" value="C:\Users\angel\Proyectos\orion-ecs-cmd\.venv\orion\Scripts\python.exe" />
    <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$" />
    <option name="IS_MODULE_SDK" value="false" />
    <option name="ADD_CONTENT_ROOTS" value="true" />
    <option name="ADD_SOURCE_ROOTS" value="true" />
    <option name="SCRIPT_NAME" value="manage.py" />
    <option name="PARAMETERS" value="migrate" />
    <option name="SHOW_COMMAND_LINE" value="false" />
    <option name="EMULATE_TERMINAL" value="false" />
    <option name="MODULE_MODE" value="false" />
    <option name="REDIRECT_INPUT" value="false" />
    <option name="INPUT_FILE" value="" />
    <method v="2" />
  </configuration>
</component>
```

## Run Tests

** Note: Change `HOST`, `DEBUG`, `SECRET_KEY` and `SDK_HOME`

```xml
<component name="ProjectRunConfigurationManager">
  <configuration default="false" name="Run Tests" type="PythonConfigurationType" factoryName="Python">
    <module name="orion-ecs-cmd" />
    <option name="INTERPRETER_OPTIONS" value="" />
    <option name="PARENT_ENVS" value="true" />
    <envs>
      <env name="PYTHONUNBUFFERED" value="1" />
      <env name="HOST" value="127.0.0.1" />
      <env name="DEBUG" value="TRUE" />
      <env name="SECRET_KEY" value="EXAMPLE_KEY" />
    </envs>
    <option name="SDK_HOME" value="C:\Users\angel\Proyectos\orion-ecs-cmd\.venv\orion\Scripts\python.exe" />
    <option name="WORKING_DIRECTORY" value="$PROJECT_DIR$" />
    <option name="IS_MODULE_SDK" value="false" />
    <option name="ADD_CONTENT_ROOTS" value="true" />
    <option name="ADD_SOURCE_ROOTS" value="true" />
    <option name="SCRIPT_NAME" value="manage.py" />
    <option name="PARAMETERS" value="test" />
    <option name="SHOW_COMMAND_LINE" value="false" />
    <option name="EMULATE_TERMINAL" value="false" />
    <option name="MODULE_MODE" value="false" />
    <option name="REDIRECT_INPUT" value="false" />
    <option name="INPUT_FILE" value="" />
    <method v="2" />
  </configuration>
</component>
```

