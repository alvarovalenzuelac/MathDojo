import unittest,numpy

class MathDojo:
    def __init__(self) -> None:
        self.result = 0

    def add(self,num,*nums):
        """
        try:
            int(num)
            for i in nums:
                int(i)
            map(init,nums)
        except ValueError:
            print("solo se aceptan numeros")
            return self
            """
        self.result += num
        for i in nums:
            self.result += i
        return self
    
    def substract(self,num, *nums):
        """
        try:
            int(num)
            for i in nums:
                int(i)
        except ValueError:
            print("solo se aceptan numeros")
            return self
            """
        self.result -= num
        for i in nums:
            self.result -= i
        return self
    
    def desviacion_estandar(self,num, *nums):
        lista_numeros = [num]
        for i in nums:
            lista_numeros.append(i)
        promedio = sum(lista_numeros) / len(lista_numeros)
        sumatoria = 0
        for j in lista_numeros:
            sumatoria += (j - promedio)**2
        self.result = (sumatoria / len(lista_numeros))**0.5
        return self

"""
print(MathDojo().desviacion_estandar(15,75,9).result)
print(numpy.std([15,75,9]))
"""

class math_dojo_tests(unittest.TestCase):
        def setUp(self):
        # agrega las tareas setUp 
            print("running setUp")
        
        def test_substract_recibe_numeros(self):
            """
            #para validar si ignora la operacion cuando enviamos alguna letra, debe tener un try en la funcion de la clase
            md = MathDojo().add(5)
            resultado_esperado = 10
            resultado_test = md.substract(1,2,"hola").add(5,"hola").add(5).substract("chao").result
            self.assertEqual(resultado_esperado,resultado_test)
            """
            with self.assertRaises(TypeError):
                md = MathDojo()
                self.assertRaises(md.substract(1,2,"hola"))
        
        def test_add_recibe_numeros(self):
            with self.assertRaises(TypeError):
                self.assertRaises(MathDojo().add(5,"hola"))
        
        def test_add(self):
            resultado_test = MathDojo().add(12).add(8,10).result
            resultado_esperado = 30
            self.assertEqual(resultado_test,resultado_esperado)
            
        def test_substract(self):
            resultado_esperado = -50   
            resultado_test = MathDojo().substract(12).substract(8,10).substract(20).result
            self.assertEqual(resultado_test,resultado_esperado)
        
        def test_cero(self):
            self.assertEqual(0,MathDojo().result)
        
        def test_desviacion_recibe_numeros(self):
            with self.assertRaises(TypeError):
                self.assertRaises(MathDojo().desviacion_estandar(5,"hola"))
        
        def tearDown(self):
        # agrega las tareas tearDown 
            print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main() # esto ejecuta nuestras pruebas