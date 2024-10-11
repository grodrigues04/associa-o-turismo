class Usuario():
    def __init__(self, login, senha) -> None:
        self.__login = login
        self.__senha = senha


class Jogador(Usuario):
    def __init__(self,login,senha, descrição=None) -> None:
        super().__init__(login, senha)
        self.__jogos_jogador = []

    def adiciona_jogo(self,jogo):
        self.__jogos_jogador.append(jogo)

    def remove_jogo(self,jogo):
        self.__jogos_jogador.remove(jogo)

class Desenvolvedor(Usuario):
    def __init__(self) -> None:
        super().__init__()
        self.__biblioteca_dev = [] #bibliteca dev é a lista de jogos que o desenvolvedor criou

class Jogo():
    def __init__(self) -> None:
        self.__autor = Desenvolvedor


jogador_um = Jogador("login@1","123", "sou um cara legal")



