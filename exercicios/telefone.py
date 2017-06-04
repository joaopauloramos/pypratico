class RediscarExcecao(Exception):
    pass


class Telefone:
    def __init__(self):
        self.numero_anterior = None

    def ligar(self, numero):
        self.numero_anterior = numero
        return f'ligar para {numero}'

    def rediscar(self):
        if self.numero_anterior == None:
            raise RediscarExcecao

        return self.ligar(self.numero_anterior)
