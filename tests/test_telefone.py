from exercicios.telefone import Telefone


def test_telefone_init():
    assert Telefone() is not None


def test_ligar():
    telefone = Telefone()
    assert 'ligar para 2345678' == \
           telefone.ligar(2345678)
