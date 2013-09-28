import unittest
from math import sqrt
from triangle import detect_triangle
class MyTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(detect_triangle(-7,3,5),-1)
    def test_2(self):
        self.assertEqual(detect_triangle(1,-3,3),-1)
    def test_3(self):
        self.assertEqual(detect_triangle(1,1,-4),-1)
    def test_4(self):
        self.assertEqual(detect_triangle(-1,-2,-4),-1)
    def test_5(self):
        self.assertEqual(detect_triangle(2,5,10**39),-1)
    def test_6(self):
        self.assertEqual(detect_triangle(8* 10**39,200,440),-1)
    def test_7(self):
        self.assertEqual(detect_triangle(8* 10**39,10**40 ,440),-1)
    def test_8(self):
        self.assertEqual(detect_triangle(8* 10**39,8* 10**39,8* 10**39),-1)
    def test_9(self):    
        self.assertEqual(detect_triangle(4,1,2),0)
    def test_10(self): 
        self.assertEqual(detect_triangle(1,2,4),0)
    def test_11(self): 
        self.assertEqual(detect_triangle(1,4,2),0)
    def test_12(self): 
        self.assertEqual(detect_triangle(2,2,2),1)
    def test_13(self): 
        self.assertEqual(detect_triangle(2,2,3),4)
    def test_14(self): 
        self.assertEqual(detect_triangle(3,4,5),3)
    def test_15(self): 
        self.assertEqual(detect_triangle(3,5,6),5)
    def main():
        unittest.main()
if __name__ == '__main__':
    unittest.main()     
