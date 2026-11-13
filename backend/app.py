import os
import time
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
CORS(app)

# ========================================================
# CONFIGURACIÓN MEDIANTE VARIABLES DE ENTORNO (DEVOPS)
# ========================================================
DB_HOST = os.getenv("DB_HOST", "db-backend")
DB_USER = os.getenv("DB_USER", "admin_directorio")
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin_directorio_pass")
DB_NAME = os.getenv("DB_NAME", "directorio_empresa")
DB_PORT = int(os.getenv("DB_PORT", 3306))


def conectar_bd(reintentos=6, espera=3):
    """
    Establece conexión a la base de datos MySQL con reintentos
    para tolerar el tiempo de inicialización de MySQL en Docker.
    """
    for i in range(reintentos):
        try:
            conexion = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME,
                port=DB_PORT
            )
            if conexion.is_connected():
                return conexion
        except Error as e:
            print(f"[BD] Esperando conexión a MySQL ({i + 1}/{reintentos})... {e}")
            if i < reintentos - 1:
                time.sleep(espera)
    raise Exception("No se pudo conectar a la base de datos MySQL tras múltiples intentos.")


# ========================================================
# ENDPOINTS DE LA API REST (BACKEND)
# ========================================================

@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint de salud para verificar estado de la API y de la BD."""
    try:
        conn = conectar_bd(reintentos=1)
        conn.close()
        return jsonify({
            "status": "OK",
            "database": "conectada",
            "host": DB_HOST,
            "database_name": DB_NAME
        }), 200
    except Exception as e:
        return jsonify({
            "status": "DEGRADED",
            "error": str(e)
        }), 500


@app.route('/api/contactos', methods=['GET'])
def obtener_contactos():
    """Obtiene todos los contactos registrados en la base de datos."""
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre, telefono, departamento FROM contactos ORDER BY id ASC")
        datos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return jsonify(datos), 200
    except Exception as e:
        return jsonify({"error": f"Error al consultar contactos: {str(e)}"}), 500


@app.route('/api/contactos', methods=['POST'])
def guardar_contacto():
    """Registra un nuevo contacto en la base de datos."""
    try:
        nuevo_contacto = request.get_json(force=True)
        if not nuevo_contacto:
            return jsonify({"error": "Cuerpo de solicitud vacío o formato no válido"}), 400

        nombre = nuevo_contacto.get('nombre', '').strip()
        telefono = nuevo_contacto.get('telefono', '').strip()
        departamento = nuevo_contacto.get('departamento', '').strip()

        if not nombre or not telefono or not departamento:
            return jsonify({
                "error": "Todos los campos (nombre, teléfono, departamento) son obligatorios."
            }), 400

        conexion = conectar_bd()
        cursor = conexion.cursor()
        consulta = "INSERT INTO contactos (nombre, telefono, departamento) VALUES (%s, %s, %s)"
        cursor.execute(consulta, (nombre, telefono, departamento))
        conexion.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        conexion.close()

        return jsonify({
            "mensaje": "Contacto guardado exitosamente",
            "id": nuevo_id
        }), 201
    except Exception as e:
        return jsonify({"error": f"Error al guardar contacto: {str(e)}"}), 500


@app.route('/api/contactos/<int:contacto_id>', methods=['DELETE'])
def eliminar_contacto(contacto_id):
    """Elimina un contacto por su ID."""
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM contactos WHERE id = %s", (contacto_id,))
        conexion.commit()
        filas_afectadas = cursor.rowcount
        cursor.close()
        conexion.close()

        if filas_afectadas == 0:
            return jsonify({"error": f"Contacto con ID {contacto_id} no encontrado"}), 404

        return jsonify({"mensaje": f"Contacto {contacto_id} eliminado exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": f"Error al eliminar contacto: {str(e)}"}), 500


if __name__ == '__main__':
    puerto = int(os.getenv("PORT", 5000))
    print(f"[*] Iniciando Backend en 0.0.0.0:{puerto} (DB_HOST={DB_HOST})...")
    app.run(host='0.0.0.0', port=puerto, debug=False)
