# Descripción
Se provee una aplicación encargada de crear viajes dados un origen, un destino y una fecha
de partida, a partir de eventos de vuelos obtenidos de un servicio externo.

## Implementación
La solución implementada sigue un enfoque DDD, agrupando la lógica en
diferentes capas: 
- `domain` que comprende la lógica de negocio. 
- `infrastructure` implementa la lógica de acceso a los recursos externos.
- `application` donde se encuentran los casos de uso. Para este ejercicio, se implementa
solo la creación de viajes.

En una capa separada (`interfaces`) se integra la lógica de las capas 
anteriores en una API que expone un endpoint para la creación de vuelos
según los siguientes parámetros: una ciudad de origen, una ciudad de destino y
una fecha de partida.  

## Requerimientos
Para ejecutar la solución es necesario:
 - Docker
 - docker-compose

# Cómo ejecutar la solución
Ejecutar el siguiente comando desde el directorio raíz del proyecto:

`docker-compose -f docker/docker-compose.yml up --build`

---
**NOTE**: Para la ejecución es necesario configurar un archivo `.env` dentro de la 
carpeta `configuration`.
Se provee un `.env.template` a modo de ejemplo.

---

Una vez ejecutado, el servicio estará escuchando en el puerto 9090.

### Configuración
El servicio puede configurarse a través de variables de entorno definidas
en un archivo `.env`.

| Variable | Descripción | Tipo |
|---|---|---|
| EXTERNAL_API_RETRIES | Número máximo de reintentos para el acceso a una API externa | int |
| EXTERNAL_API_TIMEOUT | Tiempo máximo de espera para recibir una respuesta de la API externa (en segundos). | float |
| EXTERNAL_API_URL | URL de la API externa | string |
| FILTER_CONFIG | Configuración de [filtros](#filtros) | string(*) |

(*) La configuración de filtros se debe definir como una lista de diccionarios en formato JSON.

#### Filtros
Se definen filtros para los distintos criterios de búsqueda de viajes:
- **Máximo número de conexiones** (key: "max_connections_filter"): Filtra los viajes
que tengan un número de conexiones mayor a la configurada.
- **Duración de vuelo máxima** (key: "max_duration_filter"): Filtra los viajes con una
duración mayor al valor configurado, expresado en horas.
- **Duración máxima de escala** (key: "max_stopover_filter"): Filtra los viajes con
escalas de duración mayor al valor, configurado en horas.

## Cómo ejecutar la suite de test
Para ejecutar la suite de tests, desde el directorio raíz ejecutar:

`docker-compose -f docker/docker-compose.test.yml up --build`