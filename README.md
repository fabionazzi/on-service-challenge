# Descripción



## Cómo ejecutar la solución
Para ejecutr la solución, primero se debe crear la imagen ejecutando desde el 
directorio raíz del proyecto:

`docker-compose -f docker/docker-compose.yml build`

Con la imagen creada, ejecutar:

`docker-compose -f docker/docker-compose.yml up`

Una vez ejecutado, estará escuchando en el puerto 9090.

## Cómo ejecutar la suite de test
Para ejecutr la suite de tests, desde el directorio raíz ejecutar:

`docker-compose -f docker/docker-compose.test.yml build`

Con la imagen creada, ejecutar:

`docker-compose -f docker/docker-compose.test.yml up`