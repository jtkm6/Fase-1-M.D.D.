#Proyecto Fase #1 - Minería De Datos
- - - -

>Para la primera fase se requiere que se haga todo el pre-procesamiento de los datos, esto incluye, limpieza,
reducción y transformación de datos.

>En algunas menciones hay pocas apariciones de TEG y no proporcionan datos útiles para la mineria, por lo
que se limitará la minería a las siguientes menciones:
> - Aplicaciones en Internet
> - Base de Datos
> - Inteligencia Artificial
> - Sistemas de Información
> - Tecnologías de Comunicación y Redes de Computadoras

## Estructura del Repositorio
- - - -

* [App.py] - Es el script que toma el archivo en bruto de los datos en un .txt y lo prosesa.
* [In/] - Es la carpeta donde esta el archivo de entrada.
* [Out/] - Es la carpeta donde el script coloca los archivos resultantes.
* [PythonData/] - Es la carpeta que contiene el "virtual environment" de `Python 3.5`.

## Ejecucion del Programa
- - - -

Para la ejecución del programa basta con colocar el archivo `Datos_Proyecto.txt` dentro de la carpeta [In/], luego debemos abrir una terminal y cargar el "virtual environment" de `Python 3.5`.

```bash
Mineria De Datos>PythonData\Scripts\activate.bat

(PYTHON~1) Mineria De Datos>python App.py
Registros procesados: 213
Registros ignorados: 35

```

Esto será suficiente para obtener en la carpeta [Out/] los datos ya procesados en los respectivos archivos `Datos_Proyecto.csv` el cual contiene la información filtrada y con formato `.csv` y el archivo `Datos_Proyecto_Stemmer.csv` el cual contiene la información filtrada y con los datos reducidos mediante el método de stemming.

## ¿Que hace el script?
- - - -

### Transformación de los datos
Al ser el formato muy similar a un archivo `.csv` se realizan los cambios necesarios en el mismo para obtener un archivo `.csv` con el formato correcto. De esta manera, va a poder ser visualizado de manera correcta en cualquier herramienta de análisis de datos (como weka).

Se hace uso de las operaciones de manejo de string en python para generar los cambios necesarios, entre los cuales están, por ejemplo, el cambio de las comillas simples a comillas dobles, borrado de saltos de línea innecesarios. De esta forma hacemos que los datos se lean de manera correcta en él `.csv`.

Luego se continúan haciendo las modificaciones que se precisan para que la base de datos se establezca de manera correcta. Además, se llevan todas las palabras a minúsculas esto tendrá como consecuencia un buen estudio sobre los datos de manera posterior.

### Limpieza de los datos
Posterior al filtrado de los datos y el descarte de las menciones que no son requeridas, notamos que hay trabajos especiales de grado a los que le faltan las palabras claves, entonces para solventar este inconveniente utilizamos la moda de las palabras claves que ya tienen los trabajos especiales de grado de la misma mención que si tienen las palabras claves y de esta forma rellenamos los datos faltantes.

De igual forma el script evalúa mediante gramática la estructura de cada entrada en la tabla, descartando las que no tienen un formato coherente y no es recuperable.

### Reduccion de datos
El algoritmo más común para stemming es el algoritmo de Porter. Existen además métodos basados en análisis lexicográfico y otros algoritmos similares (KSTEM, stemming con cuerpo, métodos lingüísticos...).

Para fines de este proyecto se utilizo la implementacion del algoritmo de Porter para el lenguaje español, esta implementacion la conseguimos de [pyStemmer]

## Autores
- - - -
**Nombre:** Efrain Diaz  
**C.I.:** 24.888.992  
**E-Mail:** uriel.eudp@gmail.com

**Nombre:** Jorge Khabazze  
**C.I.:** 23.692.079  
**E-Mail:** jtkm6jk@gmail.com

   [App.py]: <./App.py>
   [In/]: <./In/>
   [Out/]: <./Out/>
   [PythonData/]: <./PythonData/>
   [pyStemmer]: <https://github.com/snowballstem/pystemmer>