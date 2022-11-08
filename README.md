# Project Movies DB
 
 El proyecto se trata de crear una base de datos, la cual va a estar formada por una serie de tablas que de manera inicial van a pasar por un proceso de "limpieza" en Python.
 
 Las tablas mencionadas se tratan de parte de la información de una tienda de alquiler de películas o coloquilmente videoclub.
 
 ## 1. Proceso de limpieza en Python.
 
 Se realiza la importación de los csv desde la carpeta data a Python conviertiéndolos en data frames. Los archivos importados son los csv actor, category, film, inventory, language, old_HDD y rental. Dichos archivos como se indica anteriormente son limpiados de manera superflua ya que el formato de los archivos en general es consistente y está igualada. Únicamente se borran los nulos, se comprueba si existe algún duplicado, se concatenan los nombre y apellidos de los actores para unificar en la misma columa el nombre y se separan la fecha y la hora en las columnas que aparecen unidas.
 
 ## 2. Creación de la base de datos.
 
 Toda vez se ha realizado la limpieza de los archivos se procede a cargar los mismos a SQL a través de python, formándose una libreria en SQL denominada cinema. 
 En dicha librería hay que establecer las relaciones entre las columnas, que tras su obserbación y estudio se modifica la de old_HDD dejando únicmante las columnas que nos interesan de la misma.
 
 Se realiza el diagrama ERD cambiado los tipos de datos a los correctos, estableciendo las relaciones y las serán las Primary Keys y las Foreing Key, quedando el diagrama de la siguiente manera:

![Diagrama%20ERR.png](attachment:Diagrama%20ERR.png)

 
 Al establecerse todas las relaciones, se sincroniza el modelo con la base de datos, quedando así la base de datos guardada de menera correcta.
 
 ## 3. Comprobación del correcto funcionamiento de la base de datos.
 
 Para verificar si se ha creado correctamente la base de datos y las relaciones entre todas las tablas indicadas, se tiran 10 querys:
 
##### - ¿Cuáles son los 10 películas de la categoría Classics con contengan un Behind the Scenes?

![query0.png](attachment:query0.png)

##### - Los 7 actores con más películas en inglés de la categoría Children.

![query1.png](attachment:query1.png)

##### - ¿Cuales son las 15 películas con mayor número de actores que intervienen?

![query2.png](attachment:query2.png)

##### - Si una película tiene un ratio de alquiler mayor de 2.5 se considera popular, es es menor, impopular.

![query3.png](attachment:query3.png)

##### - Películas en mandarín

Sale una lista vacía porque no hay películas en Mandarín.

##### - ¿Cuáles son los 5 actores con más películas de duración superior a 80 minutos?

![query4.png](attachment:query4.png)

##### - ¿Cuáles son las películas de acción de una duración inferior a 100 minutos?

![query5.png](attachment:query5.png)

##### - Actores que han salido en películas con clasificación 'G'.

![query6.png](attachment:query6.png)

##### -Las 20 películas en la que solo aparece un actor con menor duración.

![query7.png](attachment:query7.png)

##### - Determinar cuántas películas existen por cada categoría.

![query8.png](attachment:query8.png)


 
 
