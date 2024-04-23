class Calculadora:
    
    @staticmethod
    def media( a, b):
        if not isinstance(a, int) or not isinstance (b, int):
            raise TypeError("Or argumentos devem ser números inteiros")

        return (a+b)/2
    