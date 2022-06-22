# 12. nustatyti ar duota simbolių eilutė yra palindromas
# Parašykite funkciją X su dokumentaciniais testais
# Ištestuokite funkciją
# Paverskite dokumentacinius testus unittest'ais
# Parašykite funkcijai X unittest'us


import unittest
import doctest
import trecia_uzd

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(trecia_uzd))
    return tests
    
if __name__ == '__main__':
    unittest.main()