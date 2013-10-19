import unittest
from input import main
from sys import argv
import re
import itertools

def ArrayTest():
    a = main.__doc__
    array =[]
    b =  a.split('\n')
    for i in b:
        if(b[0] == ''):
            del b[0]
        t = len(b) -1
        while t != 0:
            if(b[t] == ''):
                del b[t]
            t = t-1
    k = len(b)-1
    index =0
    check =0
    while index != k:
        number = re.findall(r'\d+', '%s' %(b[index]))
        number = map(int,number)
        array.append(number)
        index = index +1
    leng = len(array)
    i = 0
    test = []
    while(i<len(array)):
        j = 0
        num = []
        while(j< len(array[i])-1):
              num.append((array[i][j]))
              num.append((array[i][j] + array[i][j+1])/2)
              num.append(array[i][j+1])
              j = j+2
        test.append(num)
        i = i+1
    j = 1
    mang = []
    mang.append(test[0])
    result = test[0]
    while j < len(test):
        mang.append(test[j])
        j = j+1
    testCase = list(itertools.product(*mang))
    arrlen  = len(testCase)
    return testCase
class TestSequense(unittest.TestCase):
    pass

def test_generator(a):
    def test(self):
        self.assertEqual(main(a),"test")
    return test
if __name__ == '__main__':
    testCase = ArrayTest()
    i=0
    for param in testCase:
        name = 'testName'+str(i)
        test = test_generator(param)
        setattr(TestSequense, name, test)
        i = i+1
    unittest.main()
