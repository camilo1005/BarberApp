from bd import obtener_conexion


def insertar_corte(nombrecorte, tiposombras, freestyles, cejas, barba, marcado, patilla, diacita, horacita):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO cortes (nombrecorte, tiposombra, freestyles, cejas, barba, marcado,patilla,diacita,horacita) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s)",
                       (nombrecorte, tiposombras, freestyles, cejas, barba, marcado, patilla, diacita, horacita))
    conexion.commit()
    conexion.close()


def obtener_corte():
    conexion = obtener_conexion()
    cortes = []
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT cortes.codigocorte as codigocorte, cortes.nombrecorte as nombrecorte  , cortes.tiposombra as tiposombra,cortes.freestyles as freestyles , cortes.cejas as cejas ,cortes.barba as barba, cortes.marcado as marcado,cortes.patilla as patilla,cortes.diacita as diacita,cortes.horacita as horacita  FROM BarberApp.cortes")
        cortes = cursor.fetchall()
    conexion.close()
    return cortes


def eliminar_corte(codigocorte):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "DELETE FROM cortes USING cortes WHERE cortes.codigocorte=%s", (codigocorte))
    conexion.commit()
    conexion.close()


def obtener_corte_por_id(codigocorte):
    conexion = obtener_conexion()
    cortes = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT  cortes.codigocorte as codigocorte, cortes.nombrecorte as nombrecorte  , cortes.tiposombra as tiposombra,cortes.freestyles as freestyles , cortes.cejas as cejas ,cortes.barba as barba, cortes.marcado as marcado,cortes.patilla as patilla,cortes.diacita as diacita,cortes.horacita as horacita  FROM BarberApp.cortes WHERE codigocorte=%s", (codigocorte,))
        cortes = cursor.fetchone()
        print("hola")
        for corte in cortes:
            print(corte)
    conexion.close()
    return cortes


def actualizar_corte(nombrecorte, tiposombra, freestyles, cejas, barba, marcado, patilla, diacita, horacita, codigocortes):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE cortes SET nombrecorte=%s, tiposombra=%s, freestyles=%s, cejas=%s, barba=%s, marcado=%s,patilla=%s,diacita=%s,horacita=%s WHERE codigocorte=%s",
                       (nombrecorte, tiposombra, freestyles, cejas, barba, marcado, patilla, diacita, horacita, codigocortes))
    conexion.commit()
    conexion.close()
