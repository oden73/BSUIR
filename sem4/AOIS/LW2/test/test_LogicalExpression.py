import unittest
from LogicalExpression import LogicalExpression


class TestLogicalExpression(unittest.TestCase):
    def test_calculation1(self):
        self.logical_expression = LogicalExpression('((a&b)|c)')
        self.assertEqual(self.logical_expression.evaluate(self.logical_expression.syntax_tree,
                                                          self.logical_expression.expression,
                                                          [True, False, True]), True)

    def test_calculation2(self):
        self.logical_expression = LogicalExpression('(-((a>b)~c))')
        self.assertEqual(self.logical_expression.evaluate(self.logical_expression.syntax_tree,
                                                          self.logical_expression.expression,
                                                          [True, False, False]), False)

    def test_sdnf1(self):
        self.logical_expression = LogicalExpression('((a~b)~c)')
        self.assertEqual(self.logical_expression.sdnf_generation(),
                         '((-a)∧(-b)∧c)v((-a)∧b∧(-c))v(a∧(-b)∧(-c))v(a∧b∧c)')

    def test_sdnf2(self):
        self.logical_expression = LogicalExpression('((b|(c&(-a)))>(a~c))')
        self.assertEqual(self.logical_expression.sdnf_generation(),
                         '((-a)∧(-b)∧(-c))v((-a)∧b∧(-c))v(a∧(-b)∧(-c))v(a∧(-b)∧c)v(a∧b∧c)')

    def test_sknf1(self):
        self.logical_expression = LogicalExpression('((-((a&b)>a))|(a&(b|c)))')
        self.assertEqual(self.logical_expression.sknf_generation(),
                         '(avbvc)∧(avbv(-c))∧(av(-b)vc)∧(av(-b)v(-c))∧((-a)vbvc)')

    def test_sknf2(self):
        self.logical_expression = LogicalExpression('((a>b)|(a>(b&a)))')
        self.assertEqual(self.logical_expression.sknf_generation(),
                         '((-a)vb)')

    def test_truth_table(self):
        self.logical_expression = LogicalExpression('((a>b)|(a>(b&a)))')
        self.logical_expression_table = self.logical_expression.truth_table()
        self.assertEqual(self.logical_expression_table,
                         ['I a I b I (b&a) I (a>(b&a)) I (a>b) I ((a>b)|(a>(b&a))) ',
                          'I 0 I 0 I   0   I     1     I   1   I         1         ',
                          'I 0 I 1 I   0   I     1     I   1   I         1         ',
                          'I 1 I 0 I   0   I     0     I   0   I         0         ',
                          'I 1 I 1 I   1   I     1     I   1   I         1         '])
        