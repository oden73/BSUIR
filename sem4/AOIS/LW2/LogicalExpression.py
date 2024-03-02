from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree


class LogicalExpression:
    def __init__(self, expression):
        self.__syntax_tree = self.form_syntax_tree(expression)
        self.__expression = expression

    @staticmethod
    def form_syntax_tree(expression):
        parent_stack = Stack()
        syntax_tree = BinaryTree([])
        parent_stack.push(syntax_tree)
        current_subtree = syntax_tree
        for i in range(0, len(expression)):
            if expression[i] == '(':
                current_subtree.insertLeft([])
                current_subtree.setRootVal([i])
                parent_stack.push(current_subtree)
                current_subtree = current_subtree.getLeftChild()
            elif expression[i] == '-':
                parent = parent_stack.pop()
                parent_list = parent.getRootVal()
                parent_list.insert(0, '-')
                parent.setRootVal(parent_list)
                parent_stack.push(parent)
            elif expression[i] not in ['&', '|', '>', '~', ')']:
                current_subtree.setRootVal([expression[i]])
                parent = parent_stack.pop()
                current_subtree = parent
            elif expression[i] in ['&', '|', '>', '~']:
                current_subtree_list = current_subtree.getRootVal()
                current_subtree_list.insert(0, expression[i])
                current_subtree.setRootVal(current_subtree_list)
                current_subtree.insertRight([])
                parent_stack.push(current_subtree)
                current_subtree = current_subtree.getRightChild()
            elif expression[i] == ')':
                current_subtree_list = current_subtree.getRootVal()
                current_subtree_list.append(i)
                current_subtree.setRootVal(current_subtree_list)
                current_subtree = parent_stack.pop()
            else:
                raise ValueError
        return syntax_tree

    def evaluate(self, syntax_subtree, expression, values_list):
        operations = {'&': self.conjunction, '-': self.negation, '|': self.disjunction, '>': self.implication,
                      '~': self.equivalence}
        left_child, right_child = syntax_subtree.getLeftChild(), syntax_subtree.getRightChild()
        if left_child and right_child:
            operation = operations[syntax_subtree.getRootVal()[0]]
            return operation(self.evaluate(left_child, expression, values_list),
                             self.evaluate(right_child, expression, values_list))
        elif left_child and not right_child:
            return self.negation(self.evaluate(left_child, expression, values_list))
        else:
            return values_list[ord(syntax_subtree.getRootVal()[0]) - ord('a')]

    def truth_table(self):
        truth_table_print_list = []
        subtrees = []
        tree = self.__syntax_tree
        get_subtrees(tree, subtrees, self.expression)
        subtrees.reverse()
        operands = []
        bits = self.operands_and_their_amount(self.expression, operands)
        number = [False for i in range(0, bits)]
        print_string = ''
        for i in operands:
            print_string += 'I ' + i + ' '
        for i in subtrees:
            print_string += 'I ' + i.expression + ' '
        # print(print_string)
        truth_table_print_list.append(print_string)
        print_string = ''
        for i in range(0, pow(2, bits)):
            for j in number:
                print_string += 'I ' + str(int(j)) + ' '
            for j in subtrees:
                print_string += 'I '
                for k in range(len(j.expression) // 2 - int(len(j.expression) % 2 == 0)):
                    print_string += ' '
                print_string += str(int(self.evaluate(j.syntax_tree, j.expression, number))) + ' '
                for k in range(len(j.expression) // 2):
                    print_string += ' '
            # print(print_string)
            truth_table_print_list.append(print_string)
            print_string = ''
            self.increment(number)
        return truth_table_print_list

    def final_values(self):
        bits = self.operands_and_their_amount(self.expression, [])
        number = [False for i in range(bits)]
        values = []
        for i in range(pow(2, bits)):
            values.append(int(self.evaluate(self.syntax_tree, self.expression, number)))
            self.increment(number)
        return values

    def sdnf_generation(self):
        bits = self.operands_and_their_amount(self.expression, [])
        sdnf = ''
        final_values = self.final_values()
        for i in range(len(final_values)):
            if final_values[i] == 1:
                if sdnf != '':
                    sdnf += 'v'
                sdnf += '('
                values = binary(i)
                for j in range(0, bits - len(values)):
                    values.insert(0, False)
                for j in range(bits):
                    if not values[j]:
                        sdnf += '(-' + chr(ord('a') + j) + ')∧'
                    else:
                        sdnf += chr(ord('a') + j) + '∧'
                sdnf = sdnf[:len(sdnf) - 1]
                sdnf += ')'
        return sdnf

    def sknf_generation(self):
        bits = self.operands_and_their_amount(self.expression, [])
        sknf = ''
        final_values = self.final_values()
        for i in range(len(final_values)):
            if final_values[i] == 0:
                if sknf != '':
                    sknf += '∧'
                sknf += '('
                values = binary(i)
                for j in range(0, bits - len(values)):
                    values.insert(0, False)
                for j in range(bits):
                    if values[j]:
                        sknf += '(-' + chr(ord('a') + j) + ')v'
                    else:
                        sknf += chr(ord('a') + j) + 'v'
                sknf = sknf[:len(sknf) - 1]
                sknf += ')'
        return sknf

    def print_numeric_forms(self):
        final_values = self.final_values()
        sdnf, sknf = [], []
        for i in range(len(final_values)):
            if final_values[i] == 0:
                sknf.append(i)
            else:
                sdnf.append(i)
        print_string = '(' + str(sdnf[0])
        for i in range(1, len(sdnf)):
            print_string += ', ' + str(sdnf[i])
        print(print_string + ') v')
        print_string = '(' + str(sknf[0])
        for i in range(1, len(sknf)):
            print_string += ', ' + str(sknf[i])
        print(print_string + ') ∧')

    def print_index_form(self):
        final_values = self.final_values()
        index_form = decimial_view(final_values)
        print_string = str(index_form) + ' - '
        for i in final_values:
            print_string += str(i)
        print(print_string)

    @staticmethod
    def increment(binary_number):
        position = len(binary_number) - 1
        while binary_number[position]:
            binary_number[position] = False
            position -= 1
        binary_number[position] = True
        return binary_number

    @staticmethod
    def operands_and_their_amount(expression, operands):
        count = 0
        for i in expression:
            if 'a' <= i <= 'z' and i not in operands:
                count += 1
                operands.append(i)
        return count

    @staticmethod
    def conjunction(first_expression, second_expression):
        return first_expression and second_expression

    @staticmethod
    def disjunction(first_expression, second_expression):
        return first_expression or second_expression

    @staticmethod
    def implication(first_expression, second_expression):
        return (not first_expression) or second_expression

    @staticmethod
    def equivalence(first_expression, second_expression):
        return first_expression == second_expression

    @staticmethod
    def negation(first_expression):
        return not first_expression

    @property
    def syntax_tree(self):
        return self.__syntax_tree

    @syntax_tree.setter
    def syntax_tree(self, new_syntax_tree):
        self.__syntax_tree = new_syntax_tree

    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, new_expression):
        self.__expression = new_expression


def get_subtrees(current_subtree, trees_list, expression):
    if len(current_subtree.getRootVal()) > 1:
        trees_list.append(LogicalExpression(
            expression[current_subtree.getRootVal()[1]:current_subtree.getRootVal()[2] + 1]))
    if current_subtree.getLeftChild():
        get_subtrees(current_subtree.getLeftChild(), trees_list, expression)
    if current_subtree.getRightChild():
        get_subtrees(current_subtree.getRightChild(), trees_list, expression)


def binary(value):
    binary_number = []
    while value > 0:
        binary_number.insert(0, bool(value % 2))
        value //= 2
    return binary_number


def decimial_view(binary_list):
    value = 0
    for i in range(len(binary_list)):
        value += binary_list[i] * pow(2, len(binary_list) - 1 - i)
    return value
