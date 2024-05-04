import unittest
from logical_expression.LogicalExpression import LogicalExpression
from karnaugh_method.karnaugh_for_2_args import Karnaugh
from karnaugh_method.karnaugh_for_2_args import KarnaughFor2Arguments
from karnaugh_method.karnaugh_for_3_args import KarnaughFor3Arguments
from karnaugh_method.karnaugh_for_4_args import KarnaughFor4Arguments
from karnaugh_method.karnaugh_for_5_args import KarnaughFor5Arguments


class TestKarnaughMethod(unittest.TestCase):
    def test_2_args_sdnf(self):
        self.logical_expression: LogicalExpression = LogicalExpression('(a>b)')
        karnaugh_method: KarnaughFor2Arguments = KarnaughFor2Arguments(self.logical_expression, 'sdnf')
        normal_form: str = karnaugh_method.final_normal_form()
        self.assertEqual(normal_form, '((-a)|(b))')

    def test_2_args_sknf(self):
        self.logical_expression: LogicalExpression = LogicalExpression('(a>b)')
        karnaugh_method: KarnaughFor2Arguments = KarnaughFor2Arguments(self.logical_expression, 'sknf')
        normal_form: str = karnaugh_method.final_normal_form()
        self.assertEqual(normal_form, '((-a)|b)')

    def test_3_args_sdnf(self):
        self.logical_expression: LogicalExpression = LogicalExpression('(a&(b>c))')
        karnaugh_method: KarnaughFor3Arguments = KarnaughFor3Arguments(self.logical_expression, 'sdnf')
        normal_form: str = karnaugh_method.final_normal_form()
        self.assertEqual(normal_form, '((a&(-b))|(a&c))')

    def test_3_args_sknf(self):
        self.logical_expression: LogicalExpression = LogicalExpression('(a&(b>c))')
        karnaugh_method: KarnaughFor3Arguments = KarnaughFor3Arguments(self.logical_expression, 'sknf')
        normal_form: str = karnaugh_method.final_normal_form()
        self.assertEqual(normal_form, '((a)&((-b)|c))')

    def test_4_args_sdnf(self):
        self.logical_expression: LogicalExpression = LogicalExpression('((a&b)|(c~d))')
        karnaugh_method: KarnaughFor4Arguments = KarnaughFor4Arguments(self.logical_expression, 'sdnf')
        normal_form: str = karnaugh_method.final_normal_form()
        self.assertEqual(normal_form, '(((-c)&(-d))|(c&d)|(a&b))')

    def test_4_args_sknf(self):
        self.logical_expression: LogicalExpression = LogicalExpression('((a&b)|(c~d))')
        karnaugh_method: KarnaughFor4Arguments = KarnaughFor4Arguments(self.logical_expression, 'sknf')
        normal_form: str = karnaugh_method.final_normal_form()
        self.assertEqual(normal_form, '((a|c|(-d))&(a|(-c)|d)&(b|c|(-d))&(b|(-c)|d))')

    def test_5_args_sdnf(self):
        self.logical_expression: LogicalExpression = LogicalExpression('((a>b)&(c~(d|e)))')
        karnaugh_method: KarnaughFor5Arguments = KarnaughFor5Arguments(self.logical_expression, 'sdnf')
        normal_form: str = karnaugh_method.final_normal_form()
        self.assertEqual(normal_form, '(((-a)&(-c)&(-d)&(-e))|((-a)&c&d)|((-a)&c&e)|(b&(-c)&(-d)&(-e))|(b&c&d)|(b&c&e))')

    def test_5_args_sknf(self):
        self.logical_expression: LogicalExpression = LogicalExpression('((a>b)&(c~(d|e)))')
        karnaugh_method: KarnaughFor5Arguments = KarnaughFor5Arguments(self.logical_expression, 'sknf')
        normal_form: str = karnaugh_method.final_normal_form()
        self.assertEqual(normal_form, '((c|(-e))&(c|(-d))&((-c)|d|e)&((-a)|b))')
