# Este sprint ejecuta un contenedor con un servidor web Nginx.
# El parámetro -d lo ejecuta en segundo plano (detached) y -p 8080:80 expone el puerto 80 del contenedor al 8080 del host.
# Podés abrir el navegador y entrar a http://localhost:8080 para ver la página por defecto de Nginx.

# Comando a ejecutar en la terminal:
# docker run -d --name web -p 8080:80 nginx
