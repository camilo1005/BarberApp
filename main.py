from flask import Flask, render_template, request, redirect
import controlador_cortes
import controladores_barbero
import controlador_cliente
import controlador_administradores

app = Flask(__name__)


#home

@app.route('/')
def home():
    return render_template('home.html')

#desarrolladores
@app.route('/desarrolladores')
def desarrolladores():
    return render_template('desarrolladores.html')

#corte

@app.route('/agregar_corte')
def formulario_agregar_corte():
    return render_template("agregar_corte.html")


@app.route('/guardar_corte', methods=['POST'])
def guardar_corte():
    nombrecorte = request.form["nombrecorte"]
    tiposombra = request.form["tiposombra"]
    freestyles = request.form["freestyles"]
    cejas = request.form["cejas"]
    barba = request.form["barba"]
    marcado = request.form["marcado"]
    patilla = request.form["patilla"]
    diacita = request.form["diacita"]
    horacita = request.form["horacita"]
    controlador_cortes.insertar_corte(
        nombrecorte, tiposombra, freestyles, cejas, barba, marcado, patilla, diacita, horacita)
    return redirect("/cortes")


@app.route("/")
@app.route("/cortes")
def cortes():
    cortes = controlador_cortes.obtener_corte()
    return render_template("cortes.html", cortes=cortes)


@app.route('/eliminar_corte', methods=['POST'])
def eliminar_corte():
    controlador_cortes.eliminar_corte(request.form["codigocorte"])
    return redirect("/cortes")


@app.route("/formulario_editar_corte/<int:codigocorte>")
def editar_corte(codigocorte):
    print("entro a pintar el formulario")
    corte = controlador_cortes.obtener_corte_por_id(codigocorte)
    return render_template("editar_corte.html", corte=corte)


@app.route('/actualizar_corte', methods=['POST'])
def actualizar_corte():
    codigocorte = request.form["codigocorte"]
    nombrecorte = request.form["nombrecorte"]
    tiposombra = request.form["tiposombra"]
    freestyles = request.form["freestyles"]
    cejas = request.form["cejas"]
    barba = request.form["barba"]
    marcado = request.form["marcado"]
    patilla = request.form["patilla"]
    diacita = request.form["diacita"]
    horacita = request.form["horacita"]
    controlador_cortes.actualizar_corte(
        nombrecorte, tiposombra, freestyles, cejas, barba, marcado, patilla, diacita, horacita, codigocorte)
    return redirect("/cortes")

# barbero


@app.route('/agregar_barbero')
def formulario_agregar_barbero():
    return render_template("agregar_barbero.html")


@app.route('/guardar_barbero', methods=['POST'])
def guardar_barbero():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    descripcion = request.form["descripcion"]
    controladores_barbero.insertar_el_barbero(nombre, apellido, descripcion)
    return redirect("/barberos")


@app.route('/')
@app.route('/barberos')
def barberos():
    barberos = controladores_barbero.obtener_el_barbero()
    return render_template("barbero.html", barberos=barberos)


@app.route('/eliminar_barbero', methods=['POST'])
def eliminar_barbero():
    controladores_barbero.eliminar_el_barbero(request.form["codigobarbero"])
    return redirect("/barberos")


@app.route('/formulario_editar_barbero/<int:codigobarbero>')
def editar_barbero(codigobarbero):
    barbero = controladores_barbero.obtener_el_corte_del_barbero_por_id(
        codigobarbero)
    return render_template("editar_barbero.html", barbero=barbero)


@app.route('/actializar_barbero', methods=['POST'])
def actualizar_barbero():
    codigobarbero = request.form["codigobarbero"]
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    descripcion = request.form["descripcion"]
    controladores_barbero.actualizar_el_barbero(
        nombre, apellido, descripcion, codigobarbero)
    return redirect("/barberos")

# cliente


@app.route('/agregar_cliente')
def formulario_agregar_cliente():
    return render_template('agregar_cliente.html')


@app.route('/guardar_clientes', methods=['POST'])
def guardar_cliente():
    cedula = request.form['cedula']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    fechanacimiento = request.form['fechanacimiento']
    telefono = request.form['telefono']
    controlador_cliente.agregar_clientes(
        nombre, apellido, fechanacimiento, telefono, cedula)
    return redirect('/clientes')


@app.route('/')
@app.route('/clientes')
def clientes():
    clientes = controlador_cliente.obtener_cliente()
    return render_template('clientes.html', clientes=clientes)


@app.route('/eliminar_cliente', methods=['POST'])
def eliminar_cliente():
    controlador_cliente.eliminar_cliente(request.form['codigocliente'])
    return redirect('/clientes')


@app.route('/formulario_editar_cliente/<int:codigocliente>')
def editar_cliente(codigocliente):
    cliente = controlador_cliente.obtener_cliente_por_id(codigocliente)
    return render_template('editar_cliente.html', cliente=cliente)


@app.route('/actualizar_cliente', methods=['POST'])
def actualizar_cliente():
    codigocliente = request.form['codigocliente']
    cedula = request.form['cedula']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    fechanacimiento = request.form['fechanacimiento']
    telefono = request.form['telefono']
    controlador_cliente.actualizar_cliente(
        nombre, apellido, fechanacimiento, telefono, cedula, codigocliente)
    return redirect('/clientes')

#administradores

@app.route('/agregar_administrador')
def formulario_agregar_administrador():
    return render_template("agregar_administrador.html")


@app.route('/guardar_administrador', methods=['POST'])
def guardar_administrador():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    telefono = request.form["telefono"]
    correo = request.form["correo"]
    contrasena = request.form["contrasena"]
    
    controlador_administradores.insertar_administrador(
        nombre, apellido, telefono, correo, contrasena)
    return redirect("/administradores")


@app.route("/")
@app.route("/administradores")
def administradores():
    administradores = controlador_administradores.obtener_administrador()
    return render_template("administradores.html", administradores=administradores)


@app.route('/eliminar_administrador', methods=['POST'])
def eliminar_administrador():
    controlador_administradores.eliminar_administrador(request.form["codigoadministrador"])
    return redirect("/administradores")


@app.route("/formulario_editar_administrador/<int:codigoadministrador>")
def editar_administrador(codigoadministrador):
    administrador = controlador_administradores.obtener_administrador_por_id(codigoadministrador)
    return render_template("editar_administrador.html", administrador=administrador)


@app.route('/actualizar_administrador', methods=['POST'])
def actualizar_administrador():
    codigoadministrador = request.form["codigoadministrador"]
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    telefono = request.form["telefono"]
    correo = request.form["correo"]
    contrasena = request.form["contrasena"]
    
    controlador_administradores.actualizar_administrador(
        nombre, apellido, telefono, correo, contrasena, codigoadministrador)
    return redirect("/administradores")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
