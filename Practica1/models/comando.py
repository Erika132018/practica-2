class Comando:
    def __init__(self):
        self.__comando = ''

    @property
    def comando(self):
        return self.__comando

    @comando.setter
    def comando(self, value):
        self.__comando = value

    def serializable(self):
        return {
            "comando": self.__comando
        }

    @staticmethod
    def deserializar(data):
        comando = Comando()
        comando.comando = data["comando"]
        return comando

    def __str__(self):
        return f"Comando: {self.__comando}"


        