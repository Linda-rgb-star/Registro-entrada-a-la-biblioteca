from flask import render_template, request, redirect, url_for
from modelo.casilleroModel import UsuarioModel


class CasilleroController:

    # Página principal
    @staticmethod
    def inicio():
        return render_template("index.html")


    # Mostrar formulario de registro
    @staticmethod
    def mostrar_registro():
        return render_template("registro.html")


    # Guardar datos del usuario
    @staticmethod
    def guardar_usuario():
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        identificacion = request.form["identificacion"]

        # Guardamos usuario con huella = 0
        UsuarioModel.guardar_usuario(nombre, correo, telefono, identificacion)

        # Redirigimos a página de registro de huella
        return redirect(url_for("registro_huella", identificacion=identificacion))


    # Mostrar página de huella
    @staticmethod
    def mostrar_registro_huella(identificacion):
        return render_template("registro_huella.html", identificacion=identificacion)


    # Guardar huella (simulación)
    @staticmethod
    def guardar_huella():
        identificacion = request.form["identificacion"]

        UsuarioModel.registrar_huella(identificacion)

        return redirect(url_for("inicio"))