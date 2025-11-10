## Descripción
# Usa la red bridge de Docker para comunicar dos contenedores.
# El primero actúa como servidor (por ejemplo, el Echo del sprint 3),
# y el segundo como cliente que se conecta al contenedor servidor.
# Se observa cómo Docker asigna IPs internas y maneja puertos.

# Ejemplo de comandos a ejecutar en terminal:
# docker network create red_prueba
# docker run -dit --name servidor --network red_prueba python:3 bash
# docker exec -it servidor python3 -m http.server 8000
# docker run -it --rm --network red_prueba curlimages/curl curl http://servidor:8000
