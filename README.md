# Project Movies DB
 
 El proyecto se trata de crear una base de datos, la cual va a estar formada por una serie de tablas que de manera inicial van a pasar por un proceso de "limpieza" en Python.
 
 Las tablas mencionadas se tratan de parte de la información de una tienda de alquiler de películas o coloquilmente videoclub.
 
 ## 1. Proceso de limpieza en Python.
 
 Se realiza la importación de los csv desde la carpeta data a Python conviertiéndolos en data frames. Los archivos importados son los csv actor, category, film, inventory, language, old_HDD y rental. Dichos archivos como se indica anteriormente son limpiados de manera superflua ya que el formato de los archivos en general es consistente y está igualada. Únicamente se borran los nulos, se comprueba si existe algún duplicado, se concatenan los nombre y apellidos de los actores para unificar en la misma columa el nombre y se separan la fecha y la hora en las columnas que aparecen unidas.
 
 ## 2. Creación de la base de datos.
 
 Toda vez se ha realizado la limpieza de los archivos se procede a cargar los mismos a SQL a través de python, formándose una libreria en SQL denominada cinema. 
 En dicha librería hay que establecer las relaciones entre las columnas, que tras su obserbación y estudio se modifica la de old_HDD dejando únicmante las columnas que nos interesan de la misma.
 
 Se realiza el diagrama ERD cambiado los tipos de datos a los correctos, estableciendo las relaciones y las serán las Primary Keys y las Foreing Key, quedando el diagrama de la siguiente manera:
 

![image](https://user-images.githubusercontent.com/113057530/200517840-8ec4d57e-2d48-47fc-a661-d617e37aa98b.png)

 
 Al establecerse todas las relaciones, se sincroniza el modelo con la base de datos, quedando así la base de datos guardada de menera correcta.
 
 

## 3. Comprobación del correcto funcionamiento de la base de datos.
 
 Para verificar si se ha creado correctamente la base de datos y las relaciones entre todas las tablas indicadas, se tiran 10 querys:
 
##### - ¿Cuáles son los 10 películas de la categoría Classics con contengan un Behind the Scenes?

![image](https://user-images.githubusercontent.com/113057530/200517710-e4eace84-61ab-4cbf-86ed-60e5614c2e85.png)


##### - Los 7 actores con más películas en inglés de la categoría Children.


![image](https://user-images.githubusercontent.com/113057530/200517945-df89530e-c956-47a4-8270-5f784be41aea.png)


##### - ¿Cuales son las 15 películas con mayor número de actores que intervienen?

![image](https://user-images.githubusercontent.com/113057530/200518004-ba78fbac-88a3-4473-bdb5-d9c2b2fa8500.png)


##### - Si una película tiene un ratio de alquiler mayor de 2.5 se considera popular, es es menor, impopular.

![image](https://user-images.githubusercontent.com/113057530/200518058-21ea9fde-b7c7-4b6a-93a4-7021d1d0c28b.png)


##### - Películas en mandarín

Sale una lista vacía porque no hay películas en Mandarín.



##### - ¿Cuáles son los 5 actores con más películas de duración superior a 80 minutos?

![image](https://user-images.githubusercontent.com/113057530/200518129-69546fb7-6c82-4845-894f-e3ba96c4edda.png)


##### - ¿Cuáles son las películas de acción de una duración inferior a 100 minutos?

![image](https://user-images.githubusercontent.com/113057530/200518189-bc6fddf0-bda0-465b-ad96-96934baf068a.png)


##### - Actores que han salido en películas con clasificación 'G'.

![image](https://user-images.githubusercontent.com/113057530/200518234-691de021-0b2d-404b-8d10-30636f98f2d9.png)

##### -Las 20 películas en la que solo aparece un actor con menor duración.

![image](https://user-images.githubusercontent.com/113057530/200518283-d7cdd687-8f29-4391-b371-e60cd5aa7e57.png)

##### - Determinar cuántas películas existen por cada categoría.

![image](https://user-images.githubusercontent.com/113057530/200518334-46d68384-cdda-4737-9e97-55704639de7a.png)

