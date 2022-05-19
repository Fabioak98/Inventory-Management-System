class Product:

    def __init__(self, cod_produto: int, nome: str, quantidade: int):
        self.__cod_produto = cod_produto
        self.__nome = nome
        self.__quantidade = quantidade

    def getQnt(self):
        return self.__quantidade

    def getName(self):
        return self.__nome

    def getCOD(self):
        return self.__cod_produto

    def setQnt(self,valor):
        self.__quantidade = valor

    def setNOme(self,nome):
        self.__nome: nome

