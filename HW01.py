"""
this is a Triangle classification function which has three sides: a, b, and c.
Written by Qi Zhao 
"""

import unittest as ut 


class TestHWO1(ut.TestCase):
    #Test cases class with extended test cases.
    def test_classify_triangle_case_1(self):
        self.assertEqual(classify_triangle(1,3,2.5), "scalene")
        self.assertEqual(classify_triangle(3,1,2.5), "scalene")
        self.assertEqual(classify_triangle(3,4,5), "right")
        self.assertEqual(classify_triangle(4,3,5), "right")
        self.assertEqual(classify_triangle(4,4,5), "isosceles")
        self.assertEqual(classify_triangle(4,5,4), "isosceles")        
        self.assertEqual(classify_triangle(4,4,4), "equilateral")
    
    def test_classify_triangle_case_2(self):
        self.assertEqual(classify_triangle(-4,-4,-4), "Wrong Input, Not a Triangle")
        self.assertEqual(classify_triangle(-3,-5,-4), "Wrong Input, Not a Triangle")
        self.assertEqual(classify_triangle(-3,-4,-4), "Wrong Input, Not a Triangle")
        self.assertEqual(classify_triangle(-2,-5,-4), "Wrong Input, Not a Triangle")
        self.assertEqual(classify_triangle(0,0,0), "Wrong Input, Not a Triangle")


def classify_triangle(a, b, c):
    #the a,b,c represents the three sides of a triangle.
    sorted_sides = [a,b,c]
    sorted_sides.sort()
    for side in sorted_sides:
        if side < 0:
            return "Wrong Input, Not a Triangle"
    a, b, c = sorted_sides[0], sorted_sides[1], sorted_sides[2]
    if a*a + b*b == c*c:
        return "right"
    if a == b or b == c:
        if a == c:
            return "equilateral"
        else:
            return "isosceles"
    else:
        return "scalene"

if __name__ == '__main__':
    ut.main(exit=False, verbosity=2)