class Ussuario:
    def __init__(self, username, senha):
        self._username = username
        self._senha = senha

    def setUsername(self, username):
        self._username = username

    def setSenha(self, senha):
        self._senha = senha

    def getUsername(self):
        return self._username

    def getSenha(self):
        return self._senha

    def _confereSenha(self, senha):
        if senha == self._senha:
            return True
        else:
            return False
