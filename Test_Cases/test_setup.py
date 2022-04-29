import pytest

def resultado(prueba):
  if prueba == 7:
       return True
  else:
       return False



class TestSuite:
    @classmethod
    def setup_class(cls):
        print("SE EJECUTA UNA SOLA VEZ AL INICIO")

    def setup_method(self):
        print("INICIO TEST CASE")       #SE EJECUTA ANTES DE CADA TEST CASE

    @pytest.mark.false
    def test_first(self):
        prueba = 5
        assert prueba,"SUERTE LA PROXIMA"

    @pytest.mark.false
    def test_second(self):
        prueba = 3
        assert not prueba,"SUERTE LA PROXIMA"

    @pytest.mark.true          # @PYTEST.MARK MARCADORES, ETIQUETAMOS LOS TEST
    def test_third(self):
        prueba = 7
        assert prueba,"BIEN HECHO"

    def do_something(self):
        pass

    def teardown_method(selfs):
        print("FINALIZA TEST CASE")     #SE EJECUTA AL FINAL DE CADA TEST CASE

    @classmethod
    def teardown_class(cls):
        print("FINALIZAN TODOS LOS TEST CASES")     #SE EJECUTA UNA SOLA VEZ AL FINAL