# Proyecto Docker Compose: Agenda de Contactos 

Aplicación web distribuida en microservicios contenerizados utilizando **Docker Compose**, diseñada para demostrar el ciclo de vida, la orquestación, las redes virtuales, la persistencia y la interacción entre capas de un sistema web completo.

---

## Asignación de Roles

| Rol | Responsabilidad Principal | Entregable Clave |
| :--- | :--- | :--- |
| **Ingeniero DevOps / Infraestructura** | Orquestación general, redes virtuales, variables de entorno y persistencia. | `docker-compose.yml`, `.env`, redes y volúmenes |
| **Administrador de Bases de Datos (DBA)** | Modelo relacional, script DDL/DML y credenciales. | `database/database.sql` |
| **Ingeniero Backend** | API REST, lógica de negocio y conexión a la base de datos. | `backend/app.py`, `backend/Dockerfile` |
| **Ingeniero Frontend** | Interfaz web interactiva y consumo asíncrono de la API. | `frontend/index.html`, `frontend/Dockerfile` |

---

## 📂 Estructura del Directorio

```
c:\Users\Erick\Downloads\Docker_project\
├── .env                          # Variables de entorno activas
├── .env.example                  # Plantilla de variables de entorno
├── docker-compose.yml            # Archivo principal de orquestación Docker
├── README.md                     # Documentación técnica
├── database/
│   └── database.sql             # Script SQL de creación y datos de prueba
├── backend/
│   ├── app.py                   # API REST en Flask con reintentos y os.getenv
│   ├── Dockerfile               # Imagen Docker para el backend
│   ├── requirements.txt         # Dependencias estándar para pip
│   └── pyproject.toml           # Especificación moderna PEP 621
└── frontend/
    ├── Dockerfile               # Imagen Docker para Nginx
    └── index.html               # Interfaz de usuario interactiva
```

---

## Guía de Ejecución

### 1. Iniciar Docker Desktop
Asegúrate de que la aplicación **Docker Desktop** esté abierta y ejecutándose en tu sistema.

### 2. Abrir Terminal en la Carpeta del Proyecto
Abre tu consola y navega a la carpeta:
```bash
cd [ruta_de_tu_proyecto]
```

### 3. Construir y Levantar los Contenedores
Descarga imágenes, compilar el frontend y backend, y arrancar todos los servicios:
```bash
docker-compose up --build -d
```

### 4. Verificar el Estado de los Contenedores
Comprueba que los 3 servicios estén arriba (`Up`):
```bash
docker-compose ps
```
Deberás ver los tres contenedores:
- `agenda_db` (MySQL 8.0, estado `healthy`)
- `agenda_backend` (Flask en puerto 5000)
- `agenda_frontend` (Nginx en puerto 8080)

---

## Pruebas
### Navegador Web
1. Abre tu navegador e ingresa a:  
   **`http://localhost:8080`**
2. Ingresa un nuevo contacto en el formulario y haz clic en **Guardar Contacto**. Comprueba que aparece en la tabla al instante.
3. Utiliza el buscador en tiempo real para filtrar por nombre o departamento.
4. Puedes hacer clic en **Eliminar** para probar el endpoint `DELETE`.

### Probar la API Backend Directamente
- **Comprobación de Salud:**
  ```bash
  curl http://localhost:5000/api/health
  ```
  *Respuesta esperada:* `{"database":"conectada","host":"db-backend","status":"OK"}`

- **Consultar Contactos:**
  ```bash
  curl http://localhost:5000/api/contactos
  ```

### Probar la Persistencia de Datos
1. Detén los contenedores:
   ```bash
   docker-compose down
   ```
2. Vuelve a levantarlos:
   ```bash
   docker-compose up -d
   ```
3. Recarga `http://localhost:8080` en tu navegador:  
   *Los contactos nuevos que agregaste siguen intactos gracias al volumen `db_data`.*

---

## 🛑 Detener el Proyecto
Para detener y retirar los contenedores preservando los datos:
```bash
docker-compose down
```
*(Si en algún momento deseas eliminar también la base de datos para empezar de cero, puedes agregar el flag `-v`: `docker-compose down -v`).*
