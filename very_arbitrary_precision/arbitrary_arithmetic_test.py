import unittest
from arbitrary_arithmetic import add, _rippleCarry, _prependZeroes

class ArbitraryArithmeticTest(unittest.TestCase):

  def testAddIntegers(self):
    self.assertEqual(add([], []), [])
    self.assertEqual(add([1], []), [1])
    self.assertEqual(add([], [1]), [1])
    self.assertEqual(add([1],[1]), [2])
    self.assertEqual(add([1,2,3],[1]), [1,2,4])
    self.assertEqual(add([1],[1,2,3]), [1,2,4])
    self.assertEqual(add([1,2,3],[1,2,3]), [2,4,6])
    self.assertEqual(add([9,9,9],[9,9,9]), [1,9,9,8])
    self.assertEqual(add([243,53,9],[42,0,18]), [2,9,0,5,7])
    self.assertEqual(add([100],[1]), [1,0,1])

  def testRippleCarry(self):
    self.assertEqual(_rippleCarry([1, 11]),(0, [2, 1])) 
    self.assertEqual(_rippleCarry([0]), (0, [0])) 
    self.assertEqual(_rippleCarry([1,2]), (0, [1,2])) 
    self.assertEqual(_rippleCarry([42,2]), (4, [2,2])) 
    self.assertEqual(_rippleCarry([2,342]), (3, [6,2])) 
    self.assertEqual(_rippleCarry([1, 2,53342]), (53, [4,6,2])) 
    self.assertEqual(_rippleCarry([642,2]), (64, [2,2])) 
    self.assertEqual(_rippleCarry([100]), (10, [0])) 

  def testPrependZeroes(self):
    self.assertEqual(_prependZeroes([1], 5), [0,0,0,0,0,1])
    self.assertEqual(_prependZeroes([1,2], 1), [0,1,2])
    self.assertEqual(_prependZeroes([1,2], 0), [1,2])
    self.assertEqual(_prependZeroes([], 1), [0])

  def testPrependZeroesIgnoresNegative(self):
    self.assertEqual(_prependZeroes([1,2], -1), [1,2])

if __name__ == '__main__':
    unittest.main()