from modelo.conexion import obtener_conexion

class UsuarioModel:

    @staticmethod
    def tiene_huella(identificacion):
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute(
            "SELECT huella_registrada FROM usuarios WHERE identificacion = %s",
            (identificacion,)
        )

        usuario = cursor.fetchone()

        cursor.close()
        conexion.close()

        if usuario:
            return usuario["huella_registrada"]
        return None


    @staticmethod
    def liberar_locker(identificacion):
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute(
            "SELECT id, huella_registrada FROM usuarios WHERE identificacion = %s",
            (identificacion,)
        )

        usuario = cursor.fetchone()

        if not usuario:
            return "Usuario no encontrado"

        if usuario["huella_registrada"] == 0:
            return "Huella no registrada"

        cursor.execute(
            "UPDATE lockers SET disponible = 1, usuario_id = NULL WHERE usuario_id = %s",
            (usuario["id"],)
        )

        conexion.commit()

        cursor.close()
        conexion.close()

        return "Locker liberado correctamente"