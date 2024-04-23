import pytest
from TDD.testes.Calculadora import Calculadora

def test_media():
    result = Calculadora.media(2, 4)
    assert result == 3

def test_media_com_float():
    with pytest.raises(TypeError):
        Calculadora.media(2.5, 4)
