import unittest
from calc import calc_me

class CalcTest(unittest.TestCase):
    def test_add(self):
        "Сложение"
        self.assertEqual(calc_me(1, 2,"+"), 3)

    def test_sub(self):
        "Вычитание"
        self.assertEqual(calc_me(4, 2,"-"), 2)
        
    def test_mul(self):
        "Умножение"
        self.assertEqual(calc_me(12345679, 8,"*"), 98765432)
        
    def test_div(self):
        "Деление"
        self.assertEqual(calc_me(111111111, 9,"/"), 12345679)

    def test_oper_expo1(self):
        "возведение в степень"
        self.assertEqual(calc_me(4, 2,"^"), 16)

    def test_oper_expo2(self):
        "возведение в степень.2"
        self.assertEqual(calc_me(3, 2,"**"), 9)

    def test_div_neg(self):
        """Негативный, деление на ноль"""
        self.assertEqual(calc_me(12, 0,"/"), 'ERROR: Divide by zero!')

    def test_symbol_neg1(self):
        """Негативный, использование символов1"""
        self.assertEqual(calc_me(12.2, 2,"/"), 'ERROR: now it is does not supported')

    def test_symbol_neg2(self):
        """Негативный, использование символов2"""
        self.assertEqual(calc_me(8, 1.5,"*"), 'ERROR: now it is does not supported')

    def test_oper_none1(self):
        """Негативный, нет переменной1"""
        self.assertEqual(calc_me(None, 2,"+"), 'ERROR: send me Number1')

    def test_oper_none2(self):
        """Негативный, нет переменной2"""
        self.assertEqual(calc_me(2, None,"-"), 'ERROR: send me Number2')



if __name__ == '__main__':
    unittest.main(verbosity=2)