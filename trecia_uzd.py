# 12. nustatyti ar duota simbolių eilutė yra palindromas
# Parašykite funkciją X su dokumentaciniais testais
# Ištestuokite funkciją
# Paverskite dokumentacinius testus unittest'ais
# Parašykite funkcijai X unittest'us

import doctest, unittest, pdb

def isPalindrome(s):

    """
    >>> isPalindrome("00 00")
    'Yes'
    >>> isPalindrome("00 001")
    'No'
    >>> isPalindrome(15)
    'Not a string'
    """    
    if (not isinstance(s, str)):
        return "Not a string"
    elif s == s[::-1]:
        return "Yes"
    else:
        return "No"
    # return s == s[::-1]
 
s = "00 001"
ans = isPalindrome(s)
 
print("First: '" + s + "'") 

    
s2 = "00 00"   

print("Second: '" + s2 + "'")
    

 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    
# Turn into unit tests code:    
    
# import unittest
# import doctest
# import trecia_uzd

# def load_tests(loader, tests, ignore):
    # tests.addTests(doctest.DocTestSuite(trecia_uzd))
    # return tests
    
# if __name__ == '__main__':
    # unittest.main()