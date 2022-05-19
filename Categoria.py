class Categoria():
    def __init__(self, nome, cod_categoria):
        self._nome = nome
        self._cod_categoria =  cod_categoria

    def setNome(self, nome):
        self._nome = nome

    def getNome(self):
        return self._nome

    def getCOD(self):
        return self._cod_categoria