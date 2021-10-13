from bd import obtener_conexion


def insertar_administrador(nombre, apellido, telefono, correo, contrasena):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO administradores (nombre, apellido, telefono, correo, contrasena) VALUES (%s,%s,%s,%s,%s)",
                       (nombre, apellido, telefono, correo, contrasena))
    conexion.commit()
    conexion.close()


def obtener_administrador():
    conexion = obtener_conexion()
    cortes = []
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT administradores.codigoadministrador as codigoadministrador, administradores.nombre as nombre  , administradores.apellido as apellido, administradores.telefono as telefono , administradores.correo as correo , administradores.contrasena as contrasena  FROM BarberApp.administradores")
        cortes = cursor.fetchall()
    conexion.close()
    return cortes


def eliminar_administrador(codigoadministrador):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "DELETE FROM administradores USING administradores WHERE administradores.codigoadministrador=%s", (codigoadministrador))
    conexion.commit()
    conexion.close()


def obtener_administrador_por_id(codigoadministrador):
    conexion = obtener_conexion()
    administradores = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT  administradores.codigoadministrador as codigoadministrador, administradores.nombre as nombre  , administradores.apellido as apellido,administradores.telefono as telefono , administradores.correo as correo FROM BarberApp.administradores WHERE codigoadministrador=%s", (codigoadministrador))
        administradores = cursor.fetchone()
    conexion.close()
    return administradores


def actualizar_administrador(nombre, apellido, telefono, correo, contrasena, codigoadministrador):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE administradores SET nombre=%s, apellido=%s, telefono=%s, correo=%s, contrasena=%s WHERE codigoadministrador=%s",
                       (nombre, apellido, telefono, correo, contrasena, codigoadministrador))
    conexion.commit()
    conexion.close()
