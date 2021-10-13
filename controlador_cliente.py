from bd import obtener_conexion


def agregar_clientes(nombre, apellido, fechanacimiento, telefono, cedula):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('INSERT INTO cliente(cedula, nombre, apellido, fechanacimiento, telefono) VALUES (%s,%s,%s,%s,%s)',
                       (cedula, nombre, apellido, fechanacimiento, telefono))
    conexion.commit()
    conexion.close()


def obtener_cliente():
    conexion = obtener_conexion()
    clientes = []
    with conexion.cursor() as cursor:
        cursor.execute('SELECT cliente.codigocliente as codigocliente, cliente.cedula as cedula, cliente.nombre as nombre, cliente.apellido as apellido, cliente.fechanacimiento as fechanacimiento, cliente.telefono as telefono FROM barberapp.cliente')
        clientes = cursor.fetchall()
        conexion.close()
        return clientes


def eliminar_cliente(codigocliente):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            'DELETE FROM  cliente USING cliente WHERE cliente.codigocliente = %s', (codigocliente))
    conexion.commit()
    conexion.close()


def actualizar_cliente(nombre, apellido, fechanacimiento, telefono, cedula, codigoclinte):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('UPDATE cliente SET nombre = %s, apellido =  %s, fechanacimiento =  %s, telefono = %s, cedula = %s WHERE codigocliente = %s',
                       (nombre, apellido, fechanacimiento, telefono, cedula, codigoclinte))
    conexion.commit()
    conexion.close()

# funcion que permite ver los datos de un cliente cuando este se va a editar


def obtener_cliente_por_id(codigocliente):
    conexion = obtener_conexion()
    clientes = None
    with conexion.cursor() as cursor:
        cursor.execute('SELECT cliente.codigocliente as codigocliente, cliente.cedula as cedula, cliente.nombre as nombre, cliente.apellido as apellido, cliente.fechanacimiento as fechanacimiento, cliente.telefono as telefono FROM barberapp.cliente WHERE codigocliente = %s', (codigocliente,))
        clientes = cursor.fetchone()
    conexion.close()
    return clientes
