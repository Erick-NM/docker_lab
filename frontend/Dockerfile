FROM nginx:alpine

# Copiar el archivo HTML estático al directorio raíz de Nginx
COPY index.html /usr/share/nginx/html/index.html

# Exponer el puerto 80 dentro del contenedor
EXPOSE 80

# Iniciar servidor Nginx en primer plano
CMD ["nginx", "-g", "daemon off;"]
