import unittest
from calculation_method.calculation_method import CalculationMethodNormalForm
from logical_expression.LogicalExpression import LogicalExpression


class TestCalculationMethodNormalForm(unittest.TestCase):
    def test_minimization_sdnf_1(self):
        self.logical_expression: LogicalExpression = LogicalExpression('(a>(b>c))')
        calculation_method = CalculationMethodNormalForm(self.logical_expression.sdnf_generation(), 'sdnf')
        normal_form = calculation_method.normal_form_without_one_implicate(-1)
        self.assertEqual(normal_form, '((-a)|((-b)|c))')

    def test_minimization_sdnf_2(self):
        self.logical_expression: LogicalExpression = LogicalExpression('(a&(b>(c|d)))')
        calculation_method = CalculationMethodNormalForm(self.logical_expression.sdnf_generation(), 'sdnf')
        normal_form = calculation_method.normal_form_without_one_implicate(-1)
        self.assertEqual(normal_form, '((a&(-b))|((a&d)|(a&c)))')

    def test_minimization_sknf_1(self):
        self.logical_expression: LogicalExpression = LogicalExpression('(a>(b>c))')
        calculation_method = CalculationMethodNormalForm(self.logical_expression.sknf_generation(), 'sknf')
        normal_form = calculation_method.normal_form_without_one_implicate(-1)
        self.assertEqual(normal_form, '((-a)|((-b)|c))')

    def test_minimization_sknf_2(self):
        self.logical_expression: LogicalExpression = LogicalExpression('(a&(b>(c|d)))')
        calculation_method = CalculationMethodNormalForm(self.logical_expression.sknf_generation(), 'sknf')
        normal_form = calculation_method.normal_form_without_one_implicate(-1)
        self.assertEqual(normal_form, '(a&((-b)|(c|d)))')
