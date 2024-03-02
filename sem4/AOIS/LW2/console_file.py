from LogicalExpression import LogicalExpression

expression = input('Введите логическое выражение(для операторов используются символы "-", "&", "|", ">", "~"):\n')
logical_expression = LogicalExpression(expression)

print('Таблица истинности:')
truth_table = logical_expression.truth_table()
for i in truth_table:
    print(i)

print('СДНФ:')
print(logical_expression.sdnf_generation())

print('СКНФ:')
print(logical_expression.sknf_generation())

print('Числовые формы:')
logical_expression.print_numeric_forms()

print('Индексная форма:')
logical_expression.print_index_form()
