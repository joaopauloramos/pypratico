from exercicios.palidromo import eh_palidromo


def test_palidromo_vazio():
    assert eh_palidromo('')


def test_palidromo_caracter():
    assert eh_palidromo('a')

def test_nao_eh_palidromo():
    assert not eh_palidromo('ab')


