# Apolo11
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Apollo_11_insignia.png/800px-Apollo_11_insignia.png" alt="apolo 11" border="0"/>



**Apolo11** es un programa diseñado con el objetivo de aprender y practicar el lenguaje **Python** dentro del esquema del bootcamp **Coding Up My Future**. Este proyecto se enfoca en proporcionar una base sólida de conocimientos teóricos y prácticos para los integrantes del grupo **16** del curso ya mencionado. Los objetivos a cumplir son:

- Medir la comprensión profunda de los conceptos fundamentales y avanzados
obtenidos en el Bootcamp y la capacidad para aplicarlos en situaciones 
prácticas.
- Evaluar la habilidad para abordar problemas y desafíos de diversa complejidad, 
desde tareas fundamentales hasta proyectos de alto nivel, de manera efectiva y 
con un enfoque estratégico.
- Formar a los participantes para alcanzar un nivel avanzado de maestría en 
Python y que pueden liderar proyectos, tomar decisiones críticas y contribuir 
de manera significativa en esta área más adelante.
- Fomentar un ambiente de aprendizaje en el que los participantes puedan 
demostrar su capacidad, conocimiento y experiencia de manera rigurosa y 
desafiante.

## Tabla de contenido

- [Estructura del proyecto](#estructura-del-proyecto)
- [Proceso de instalación del proyecto](#proceso-de-instalación-del-proyecto)
- [Ejecución del proyecto](#ejecución-del-proyecto)
- [Desarrolladores](#desarrolladores)
- [Licencia](#licencia)

## Estructura del proyecto

El material del proyecto estará disponible en las siguientes carpetas: 


```linux
.
├── README.md              # Leame
├── main.py                # Archivo principal de ejecución
├── poetry.lock            # registro de las dependencias usadas en el proyecto
├── pyproject.toml         # Requisitos del sistema de compilación
├── documents              # Carpeta con el archivo del reto.
│   └── 002.problema.pdf
├── files                  # Carpeta con los archivos generados por la app 
│   └── algún-archivo
├── settings                # Carpeta con los archivos de configuración del proyecto.
│   ├── configuration_file.yaml
│   └── message.yaml
├── src                    # Carpeta contenedora de las carpetas que estructuran el proyecto.
│    ├── simulator         # Carpeta con la logica para iniciar el proyecto.
│    │   ├── __init__.py
│    │   └── simulator.py
│    ├── dashboard         # Carpeta con la logica con los resultados de la ejecución.
│    │   ├── __init__.py
│    │   └── process.py
│    └── utilities         # Carpeta con los utilitarios que sirven de manera global al poryecto.
│        ├── __init__.py
|        ├── config.py  
│        ├── control_messages.py
│        ├── files.py
│        └── generic.py
└── tests                  # Carpeta con la logica para realizar pruebas automatizadas al proyecto.
    ├── __init__.py
    ├── dashboard.py
    └── simulator.py 
    └── utilities.py          
```


## Proceso de instalación del proyecto

Primero debemos descarga este repositorio, para esto abriremos una consola de comandos en la ruta o carpeta que deseemos, ingresando el siguiente comando:
```
git clone https://github.com/PalantirDagor/Apolo11.git
```
Luego podemos ingresar a la carpeta que creo el proceso de nombre "Apolo11" de manera manual, ó sobre la misma consola ya abierta ingresamos el comando: 
```
cd Apolo11
```
Y usando cualquiera de estas dos formas estaremos dentro de la carpeta de la aplicación a la cual debemos realizar un proceso de preparación para su correcta ejecución, y estos son los pasos:

### Instalación de entorno virtual
Este paso es muy importante para poder ejecutar todo dentro de condiciones de software adecuadas para la aplicación, instalar con el siguiente comando:
```
python -m venv env
```
Este proceso nos instalará una carpeta con nombre "env" y dentro de esta estarán los scripts que contendran la información necesaria para el entorno virtual.
Luego se debe ingresar a esta carpeta ya sea de manera manual o por consola de comando hasta llegar a la carpeta scripts, si se hace a traves de comandos en la consola, usar:
```
cd env/Scripts
```
Ó para la plataforma Windows
```
cd env\Scripts
```
Una ves dentro de esta carpeta "Scripts" ingresar el comando:
```
Activate.ps1
```
Si no se ejecuta y genera error como este:
```
activate.ps1 : El término 'activate.ps1' no se reconoce como nombre de un cmdlet, función, archivo de script o programa ejecutable. Compruebe si escribió correctamente el nombre o, si incluyó una ruta de acceso, compruebe 
que dicha ruta es correcta e inténtelo de nuevo.
```
Utilizar el siguiente comando:
```
.\Activate.ps1
```
Si el error es uno como este:
```
Activate.ps1 : No se puede cargar el archivo c:\...\Apolo11\env\Scripts\Activate.ps1 porque la ejecución    
de scripts está deshabilitada en este sistema.
```
Utilizar el siguiente comando que habilitará el uso de scripts en su maquina:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Si todo funciona correctamete debe instalar Poetry para el manejo de las librerias y la constucción correcta de la aplicación ya que este ha sido hecho utilizando esta herramienta.

### Instalación de poetry
En una consola de comandos nueva debe de descargar Poetry con el siguiente comando para Windows:
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
Luego ya instalado Poetry, verificar con el comando:
```
poetry --version
```
El cual indicará la version instalada y confirmará al mostrar la versión de esta manera:
```
Poetry (version x.x.x)
```
Indicando que la herramienta ya se esta ejecutando. Si muestra el siguiente mensaje de error:
```
poetry : El término 'poetry' no se reconoce como nombre de un cmdlet, función, archivo de script o programa
ejecutable.
```
Se debe de  ingresar la ruta donde quedo instalado Poetry "...\AppData\Roaming\Python\Scripts" en las variables de entorno.

### Instalación de poetry en el entorno virtual
Luego con el entorno virtual activado, se debe de ingresar el siguiente comando para iniciar la instalación de Poetry dentro del entorno:
```
python -m poetry
```
Ya instalada la herramienta, utilizar el comando:
```
poetry install
```
Este comando instalara todas las librerias y dependencias de la aplicación que haran que todo funcione correctamente y que queden guardadas en el entorno virutal para su ejecución, ya en este paso se debe de iniciar los pasos para su ejecución en el punto siguiente.


## Ejecución del proyecto

Para ejecutar el proyecto se requiere ubicar la carpeta con los script en el directorio de su preferencia, se debe de iniciar una consola de comandos del sistema operativo huesped, dentro de la carpeta "apolo11" y utilizar el siguiente comando para correr los script de simulacion y reporte

### Comando de Simulacion:

En la consola de comando se ingresará:
```
python main.py -start simulation
```

Este comando da inicio a la ejecución de la simulacion de datos, que por defecto correra por 20 segundos, este funcionamiento por defecto podra ser nodificado a gusto por quien lo inicie segun su necesidad tanto aumentando la cantidad de tiempo o disminuyendolo con el siguiente comando:
```
python main.py -start simulation -sc 15
```

### Comando Generacion de Reporte:

Para la generacion del reporte, este es el comando
```
python app.py -start report -nr nombre_reporte
```
Donde "-nr" indica a la aplicación el nombre que tendra el archivo con los datos generados en la evaluación y reporte del proceso surtido en la simulación.

### Comando para ejecucion de pruebas:

Para la generacion de pruebas de covertura, este es el comando
```
python -m pytest --cov
```

## Desarrolladores 

El Poryecto es creado y presentado por: **Jorge Alberto Molina Zapata**, **Elvis Alexis Betancur López** y **Duber Alexander Galvis Giraldo**

## Licencia

El contenido de este poryecto se proporciona bajo la Licencia **MIT**. Consulta el archivo de licencia almacenado en esta repositorio para mas información.