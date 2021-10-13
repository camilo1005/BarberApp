from bd import obtener_conexion


def insertar_el_barbero(nombre, apellido, descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO barbero (nombre,apellido,descripcion) VALUES(%s,%s,%s)",
                       (nombre, apellido, descripcion))
    conexion.commit()
    conexion.close()


def obtener_el_barbero():
    conexion = obtener_conexion()
    barberos = []
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT barbero.codigobarbero as codigobarbero, barbero.nombre as nombre,barbero.apellido as apellido, barbero.descripcion as descripcion FROM barberapp.barbero")
        barberos = cursor.fetchall()
    conexion.close()
    return barberos


def eliminar_el_barbero(codigobarbero):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "DELETE FROM barbero USING barbero WHERE barbero.codigobarbero=%s ", (codigobarbero))
    conexion.commit()
    conexion.commit()


def obtener_el_corte_del_barbero_por_id(codigobarbero):
    conexion = obtener_conexion()
    barberos = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT barbero.codigobarbero as codigobarbero, barbero.nombre as nombre,barbero.apellido as apellido, barbero.descripcion as descripcion FROM barberapp.barbero WHERE codigobarbero=%s ", (codigobarbero))

        barberos = cursor.fetchone()
    conexion.close()
    return barberos


def actualizar_el_barbero(nombre, apellido, descripcion, codigobarbero):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE barbero SET nombre=%s,apellido=%s,descripcion=%s WHERE codigobarbero=%s",
                       (nombre, apellido, descripcion, codigobarbero))
    conexion.commit()
    conexion.close()
