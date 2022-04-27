def es_par(a, b):
    if a % 2 == 0 and b % 3== 0:
        return True
    else:
        return False


def test_positive():
    result = es_par(2, 4)
    assert result,"EL numero no es par " #si falla se imprime el msj en pantalla("msj")


def test_negative():
    result = es_par(3, 9)
    assert not result

def test_prueba():
    result = es_par(15, 12)
    assert not result  #no es verdadero (assert not)

