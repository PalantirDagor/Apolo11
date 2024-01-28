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
│    ├── Simulator         # Carpeta con la logica para iniciar el proyecto.
│    │   ├── __init__.py
│    │   └── simulator.py
│    ├── dashboard         # Carpeta con la logica con los resultados de la ejecución.
│    │   ├── __init__.py
│    │   └── process.py
│    ├── model             # Carpeta con la logica del modelo de generación de logica del negocio.
│    │   ├── __init__.py
│    │   ├── file.py
│    │   ├── message.py
│    │   └── report.py
│    └── utilities         # Carpeta con los utilitarios que sirven de manera global al poryecto.
│        ├── __init__.py
│        ├── control_messages.py
│        ├── files.py
│        └── generic.py
└── tests                  # Carpeta con la logica para realizar pruebas automatizadas al proyecto.
    ├── __init__.py
    ├── inicilizar.py
    └── test_e.py          
```


## Ejecución del proyecto

Para ejecutar el proyecto se requiere ubicar la carpeta con los script en el directorio de su preferencia, se debe de iniciar una consola de comandos del sistema operativo huesped, dentro de la carpeta "apolo11" y utilizar el siguiente comando para correr los script de simulacion y reporte

### Comando de Simulacion:

En la consola de comando se ingresará:
```
python app.py -start simulation
```

Este comando da inicio a la ejecución de la simulacion de datos, que por defecto correra por 20 segundos, este funcionamiento por defecto podra ser nodificado a gusto por quien lo inicie segun su necesidad tanto aumentando la cantidad de tiempo o disminuyendolo con el siguiente comando:
```
python app.py -start simulation -sc 15
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