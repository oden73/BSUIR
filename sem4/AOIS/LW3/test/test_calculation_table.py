import unittest
from calculation_table_method.calculation_table_method import CalculationTableMethodNormalForm
from calculation_method.calculation_method import CalculationMethodNormalForm
from logical_expression.LogicalExpression import LogicalExpression


class TestCalculationMethodNormalForm(unittest.TestCase):
    def test_minimization_sdnf_1(self):
        self.logical_expression: LogicalExpression = LogicalExpression('(a>(b>c))')
        calculation_method: CalculationMethodNormalForm = (
            CalculationMethodNormalForm(self.logical_expression.sdnf_generation(), 'sdnf'))
        calculation_table_method: CalculationTableMethodNormalForm = (
            CalculationTableMethodNormalForm(calculation_method))
        calculation_table_method.final_normal_form()
        normal_form: str = calculation_table_method.normal_form()
        self.assertEqual(normal_form, '((-a)|((-b)|c))')

    def test_minimization_sdnf_2(self):
        self.logical_expression: LogicalExpression = LogicalExpression('(a&(b>(c|d)))')
        calculation_method: CalculationMethodNormalForm = (
            CalculationMethodNormalForm(self.logical_expression.sdnf_generation(), 'sdnf'))
        calculation_table_method: CalculationTableMethodNormalForm = (
            CalculationTableMethodNormalForm(calculation_method))
        calculation_table_method.final_normal_form()
        normal_form: str = calculation_table_method.normal_form()
        self.assertEqual(normal_form, '((a&(-b))|((a&d)|(a&c)))')

    def test_minimization_sknf_1(self):
        self.logical_expression: LogicalExpression = LogicalExpression('(a>(b>c))')
        calculation_method: CalculationMethodNormalForm = (
            CalculationMethodNormalForm(self.logical_expression.sknf_generation(), 'sknf'))
        calculation_table_method: CalculationTableMethodNormalForm = (
            CalculationTableMethodNormalForm(calculation_method))
        calculation_table_method.final_normal_form()
        normal_form: str = calculation_table_method.normal_form()
        self.assertEqual(normal_form, '((-a)|((-b)|c))')

    def test_minimization_sknf_2(self):
        self.logical_expression: LogicalExpression = LogicalExpression('(a&(b>(c|d)))')
        calculation_method: CalculationMethodNormalForm = (
            CalculationMethodNormalForm(self.logical_expression.sknf_generation(), 'sknf'))
        calculation_table_method: CalculationTableMethodNormalForm = (
            CalculationTableMethodNormalForm(calculation_method))
        calculation_table_method.final_normal_form()
        normal_form: str = calculation_table_method.normal_form()
        self.assertEqual(normal_form, '(a&((-b)|(c|d)))')
