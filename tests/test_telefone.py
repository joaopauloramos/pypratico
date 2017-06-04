import pytest
from exercicios.telefone import Telefone, RediscarExcecao


def test_telefone_init():
    assert Telefone() is not None

NUMEROS_VALIDOS = ['8754432', 2345678, '2345678']

@pytest.mark.parametrize('numero', NUMEROS_VALIDOS)
def test_ligar(numero):
    telefone = Telefone()
    assert 'ligar para ' + str(numero) == \
           telefone.ligar(numero)

@pytest.mark.parametrize('numero', NUMEROS_VALIDOS)
def test_rediscar(numero):
    telefone = Telefone()
    telefone.ligar(numero)
    assert 'ligar para ' + str(numero) \
           == telefone.rediscar()

def test_rediscar_excecao():
    """Certifica que tentar rediscar antes de fazer uma ligação lança excecção"""
    telefone = Telefone()
    try:
        telefone.rediscar()
    except RediscarExcecao:
        pass # Deu certo
    else:
        pytest.fail('Rediscar deveria ser lancado excecao')
