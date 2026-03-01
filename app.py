from flask import Flask, render_template, request, redirect, url_for
from modelo.casilleroModel import UsuarioModel

app = Flask(
    __name__,
    template_folder="vista/templates",
    static_folder="vista/static"
)

# ----------------------------
# Página principal
# ----------------------------
@app.route("/")
def inicio():
    return render_template("index.html")


# ----------------------------
# Mostrar formulario de registro
# ----------------------------
@app.route("/registro")
def registro():
    return render_template("registro.html")


# ----------------------------
# Guardar usuario (huella = 0)
# ----------------------------
@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    telefono = request.form["telefono"]
    identificacion = request.form["identificacion"]

    # Guardamos usuario sin huella
    UsuarioModel.guardar_usuario(nombre, correo, telefono, identificacion)

    # Redirigimos a la página de huella
    return redirect(url_for("registro_huella", identificacion=identificacion))


# ----------------------------
# Mostrar página de registro de huella
# ----------------------------
@app.route("/registro_huella/<identificacion>")
def registro_huella(identificacion):
    return render_template("registro_huella.html", identificacion=identificacion)


# ----------------------------
# Guardar huella (simulación)
# ----------------------------
@app.route("/guardar_huella", methods=["POST"])
def guardar_huella():
    identificacion = request.form["identificacion"]

    # Actualizamos huella_registrada = 1
    UsuarioModel.registrar_huella(identificacion)

    return redirect(url_for("inicio"))


# ----------------------------
# Página obtener locker
# ----------------------------
@app.route("/obtener")
def obtener():
    return render_template("obtener.html")


# ----------------------------
# Página liberar locker
# ----------------------------
@app.route("/liberar")
def liberar():
    return render_template("liberar.html")


# ----------------------------
# Ejecutar servidor
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)