import pytest
from unitest.unitest import calcular_quadrado, calcular_retangulo, calcular_triangulo
from utils.utils import ler_csv

def test_calcular_quadrado():
    lado = 3
    resultado_esperado = 9

    resultado_obtido = calcular_quadrado(lado)

    assert resultado_esperado == resultado_obtido


def test_calcular_retangulo():
    base = 5
    altura = 7
    resultado_esperado = 35

    resultado_obtido = calcular_retangulo(base, altura)

    assert resultado_esperado == resultado_obtido


def test_calcular_triangulo():
    base = 8
    altura = 12
    resultado_esperado = 48

    resultado_obtido = calcular_triangulo(base, altura)

    assert resultado_esperado == resultado_obtido


@pytest.mark.parametrize('lado, resultado_esperado',
                         [
                             (5, 25),
                             (4, 16),
                             (9, 81),
                             (6, 36),
                             (7, 49)
                         ]
                         )

def test_calcular_quadrado_lista(lado, resultado_esperado):

    resultado_obtido = calcular_quadrado(lado)

    assert resultado_esperado == resultado_obtido


@pytest.mark.parametrize('base, altura, resultado_esperado',
                            ler_csv('./fixtures/massa_triangulo.csv')
                         )

def test_calcular_triangulo_csv(base, altura, resultado_esperado):

    resultado_obtido = calcular_triangulo(float(base), float(altura))

    assert float(resultado_esperado) == resultado_obtido