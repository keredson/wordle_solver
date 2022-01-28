import unittest
from wordle_solver import WordleSolver


class TestWordleSolver(unittest.TestCase):

  def test_20220127(self):
    w = WordleSolver(verbose=False)
    self.assertEqual(w.suggest(n=4), [('arose', 27122), ('aeros', 27122), ('seria', 27095), ('riesa', 27095)])
    w.gray('arse')
    w.yellow('o',3)
    self.assertEqual(w.suggest(n=4), [('tonic', 689), ('ntico', 689), ('nicot', 689), ('conti', 689)])
    w.gray('ic')
    w.yellow('t',1)
    w.green('o',2)
    w.yellow('n',3)
    self.assertEqual(w.suggest(n=4), [('mount', 4), ('jotun', 4), ('fount', 4)])
    # mount


if __name__ == '__main__':
    unittest.main()

