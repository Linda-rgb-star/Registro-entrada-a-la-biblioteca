from modelo.conexion import obtener_conexion


class UsuarioModel:

    # 1️⃣ Registrar usuario (sin huella aún)
    @staticmethod
    def guardar_usuario(nombre, correo, telefono, identificacion):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO usuarios 
        (nombre, correo, telefono, identificacion, huella_registrada)
        VALUES (%s, %s, %s, %s, %s)
        """

        valores = (nombre, correo, telefono, identificacion, 0)  # 0 = no tiene huella

        cursor.execute(sql, valores)
        conexion.commit()

        cursor.close()
        conexion.close()


    # 2️⃣ Simular registro de huella
    @staticmethod
    def registrar_huella(identificacion):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE usuarios
        SET huella_registrada = 1
        WHERE identificacion = %s
        """

        cursor.execute(sql, (identificacion,))
        conexion.commit()

        cursor.close()
        conexion.close()


    # 3️⃣ Verificar si ya tiene huella
    @staticmethod
    def tiene_huella(identificacion):
        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)

        sql = """
        SELECT huella_registrada 
        FROM usuarios 
        WHERE identificacion = %s
        """

        cursor.execute(sql, (identificacion,))
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado:
            return resultado["huella_registrada"]
        return None