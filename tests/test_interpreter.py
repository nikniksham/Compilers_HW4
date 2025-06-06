import math

import pytest
from src.interpreter import InterpreterError, run_interpreter_from_string


def interpret_code(code_string):
    return run_interpreter_from_string(code_string)


class TestInterpreterUnit:
    def test_integer_literal(self):
        assert interpret_code("print 123;") == ["123"]
        assert interpret_code("print -123;") == ["-123"]

    def test_float_literal(self):
        assert interpret_code("print 12.34;") == ["12.34"]
        assert interpret_code("print -12.34;") == ["-12.34"]

    def test_string_literal(self):
        assert interpret_code("print 'hello';") == ["hello"]
        assert interpret_code('print "world";') == ["world"]
        assert interpret_code("print 'hello \\'world\\'';") == ["hello 'world'"]
        assert interpret_code('print "hello \\"world\\"";') == ['hello "world"']
        assert interpret_code("print 'hello\\nworld';") == ["hello\nworld"]

    def test_simple_assignment_and_print(self):
        assert interpret_code("a = 10; print a;") == ["10"]
        assert interpret_code("val = -10; print val;") == ["-10"]

    def test_float_assignment_and_print(self):
        assert interpret_code("a = 10.5; print a;") == ["10.5"]
        assert interpret_code("val = -5.25; print val;") == ["-5.25"]

    def test_string_assignment_and_print(self):
        assert interpret_code("a = 'hello'; print a;") == ["hello"]
        assert interpret_code('val = "world"; print val;') == ["world"]

    def test_arithmetic_operations(self):
        assert interpret_code("print 1 + 2;") == ["3"]
        assert interpret_code("print 5 - 3;") == ["2"]
        assert interpret_code("print 4 * 6;") == ["24"]
        assert interpret_code("print 10 / 2;") == ["5"]
        assert interpret_code("print 10 / 3;") == ["3"]
        assert interpret_code("print 1 + 2 * 3;") == ["7"]
        assert interpret_code("print (1 + 2) * 3;") == ["9"]
        assert interpret_code("a = 10; b = 5; print a - b * 2 / 1;") == ["0"]

    def test_float_arithmetic_operations(self):
        assert interpret_code("print 1.5 + 2.5;") == ["4.0"]
        assert interpret_code("print 5.5 - 3.2;") == ["2.3"]
        assert interpret_code("print 4.5 * 2.0;") == ["9.0"]
        assert interpret_code("print 10.0 / 2.0;") == ["5.0"]
        assert interpret_code("print 1.5 + 2.0 * 3.0;") == ["7.5"]
        assert interpret_code("print (1.0 + 2.0) * 3.0;") == ["9.0"]

    def test_mixed_arithmetic_operations(self):
        assert interpret_code("print 1 + 2.5;") == ["3.5"]
        assert interpret_code("print 5.5 - 3;") == ["2.5"]
        assert interpret_code("print 4 * 2.5;") == ["10.0"]
        assert interpret_code("print 10 / 2.5;") == ["4.0"]

    def test_string_operations(self):
        assert interpret_code("print 'hello' + ' ' + 'world';") == ["hello world"]
        assert interpret_code("print 'abc' * 3;") == ["abcabcabc"]
        with pytest.raises(InterpreterError):
            interpret_code("print 'abc' - 'a';")
        with pytest.raises(InterpreterError):
            interpret_code("print 'abc' / 2;")

    def test_string_number_concatenation(self):
        assert interpret_code("print 'Number: ' + 42;") == ["Number: 42"]
        assert interpret_code("print 123 + ' is a number';") == ["123 is a number"]
        assert interpret_code("print 'Pi: ' + 3.14159;") == ["Pi: 3.14159"]

    def test_comparison_operations(self):
        assert interpret_code("print 1 < 2;") == ["1"]
        assert interpret_code("print 2 < 1;") == ["0"]
        assert interpret_code("print 1 > 2;") == ["0"]
        assert interpret_code("print 2 > 1;") == ["1"]
        assert interpret_code("print 1 == 1;") == ["1"]
        assert interpret_code("print 1 == 2;") == ["0"]
        assert interpret_code("print 1 != 2;") == ["1"]
        assert interpret_code("print 1 != 1;") == ["0"]
        assert interpret_code("print 1 <= 1;") == ["1"]
        assert interpret_code("print 1 <= 0;") == ["0"]
        assert interpret_code("print 1 >= 1;") == ["1"]
        assert interpret_code("print 0 >= 1;") == ["0"]

    def test_float_comparison_operations(self):
        assert interpret_code("print 1.5 < 2.5;") == ["1"]
        assert interpret_code("print 2.5 < 1.5;") == ["0"]
        assert interpret_code("print 1.5 > 2.5;") == ["0"]
        assert interpret_code("print 2.5 > 1.5;") == ["1"]
        assert interpret_code("print 1.5 == 1.5;") == ["1"]
        assert interpret_code("print 1.5 == 2.5;") == ["0"]
        assert interpret_code("print 1.5 != 2.5;") == ["1"]
        assert interpret_code("print 1.5 != 1.5;") == ["0"]
        assert interpret_code("print 1.5 <= 1.5;") == ["1"]
        assert interpret_code("print 1.5 <= 0.5;") == ["0"]
        assert interpret_code("print 1.5 >= 1.5;") == ["1"]
        assert interpret_code("print 0.5 >= 1.5;") == ["0"]

    def test_mixed_type_comparison(self):
        assert interpret_code("print 1 == 1.0;") == ["1"]
        assert interpret_code("print 1.0 == 1;") == ["1"]
        assert interpret_code("print 2 > 1.5;") == ["1"]
        assert interpret_code("print 1.5 > 2;") == ["0"]
        with pytest.raises(InterpreterError):
            interpret_code("print 'a' > 1;")
        with pytest.raises(InterpreterError):
            interpret_code("print 1 < 'a';")
        assert interpret_code("print 'abc' == 'abc';") == ["1"]
        assert interpret_code("print 'abc' != 'def';") == ["1"]
        assert interpret_code("print 'abc' < 'def';") == ["1"]
        assert interpret_code("print 'xyz' > 'abc';") == ["1"]

    def test_string_in_control_flow(self):
        code = """
        str = 'hello';
        if (str == 'hello') {
            print 'correct';
        } else {
            print 'wrong';
        }
        """
        assert interpret_code(code) == ["correct"]

    def test_float_in_control_flow(self):
        code = """
        x = 1.5;
        if (x > 1.0) {
            print 'greater';
        } else {
            print 'not greater';
        }
        """
        assert interpret_code(code) == ["greater"]

    def test_empty_string_truth_value(self):
        code = """
        s = '';
        if (s) {
            print 'non-empty';
        } else {
            print 'empty';
        }
        """
        assert interpret_code(code) == ["empty"]

    def test_zero_float_truth_value(self):
        code = """
        x = 0.0;
        if (x) {
            print 'non-zero';
        } else {
            print 'zero';
        }
        """
        assert interpret_code(code) == ["zero"]

    def test_if_statement_true(self):
        code = """
        a = 10;
        result = 0;
        if (a > 5) {
            result = 100;
        }
        print result;
        """
        assert interpret_code(code) == ["100"]

    def test_if_statement_false(self):
        code = """
        a = 3;
        result = 0;
        if (a > 5) {
            result = 100;
        }
        print result;
        """
        assert interpret_code(code) == ["0"]

    def test_if_else_statement_if_branch(self):
        code = """
        a = 10;
        result = 0;
        if (a > 5) {
            result = 100;
        } else {
            result = 200;
        }
        print result;
        """
        assert interpret_code(code) == ["100"]

    def test_if_else_statement_else_branch(self):
        code = """
        a = 3;
        result = 0;
        if (a > 5) {
            result = 100;
        } else {
            result = 200;
        }
        print result;
        """
        assert interpret_code(code) == ["200"]

    def test_while_statement(self):
        code = """
        count = 3;
        sum = 0;
        while (count > 0) {
            sum = sum + count;
            count = count - 1;
            print sum; // Print sum in each iteration
        }
        print count;
        """
        assert interpret_code(code) == ["3", "5", "6", "0"]

    def test_nested_control_flow(self):
        code = """
        x = 1;
        y = 0;
        if (x == 1) {
            while (x < 3) {
                y = y + 10;
                x = x + 1;
                print y;
            }
        } else {
            y = -1;
        }
        print y;
        print x;
        """
        assert interpret_code(code) == ["10", "20", "20", "3"]

    def test_uninitialized_variable_error(self):
        with pytest.raises(InterpreterError, match="Variable 'b' not defined."):
            interpret_code("a = 10; print b;")

    def test_division_by_zero_error(self):
        with pytest.raises(InterpreterError, match="Division by zero"):
            interpret_code("a = 10 / 0; print a;")
        with pytest.raises(InterpreterError, match="Division by zero"):
            interpret_code("a = 10.5 / 0.0; print a;")

    def test_program_with_multiple_statements(self):
        code = """
        a = 5;
        b = a + 2; // b = 7
        print b;   // Output: 7
        a = b * 2; // a = 14
        print a;   // Output: 14
        """
        assert interpret_code(code) == ["7", "14"]

    def test_parentheses_in_expressions(self):
        assert interpret_code("print (2 + 3) * 4;") == ["20"]
        assert interpret_code("print 2 + (3 * 4);") == ["14"]
        assert interpret_code("print (10 - (2 * 3)) / 2;") == ["2"]

    def test_negative_numbers_in_expressions(self):
        assert interpret_code("print -5 + 3;") == ["-2"]
        assert interpret_code("print 10 * -2;") == ["-20"]
        assert interpret_code("a = -1; print a;") == ["-1"]

    def test_comments_are_ignored(self):
        code = """
        // This is a comment
        a = 10; // Another comment
        print a; 
        // b = 20; print b; // This line is commented out
        """
        assert interpret_code(code) == ["10"]

    def test_empty_program(self):
        assert interpret_code("// only comments") == []

    def test_if_without_else(self):
        code = """
        x = 1;
        if (x == 1) {
            print 10;
        }
        print x;
        """
        assert interpret_code(code) == ["10", "1"]

        code_false = """
        x = 0;
        if (x == 1) {
            print 10;
        }
        print x;
        """
        assert interpret_code(code_false) == ["0"]

    def test_complex_boolean_expression_in_if(self):
        code = """
        a = 5;
        b = 10;
        if ((a * 2) == b && (b - a) == a) {
            print 1;
        } else {
            print 0;
        }
        """
        code_valid = """
        a = 5;
        b = 10;
        c = 0;
        if ((a*2) == b) {
            c = 1;
        }
        print c;
        """
        assert interpret_code(code_valid) == ["1"]

    def test_variable_reassignment(self):
        code = """
        x = 10;
        print x;
        x = 20;
        print x;
        x = x + 5;
        print x;
        """
        assert interpret_code(code) == ["10", "20", "25"]

    def test_factorial(self):
        for i in range(2, 10):
            code = f"""
            n = {i};

            result = 1;
            while (n > 1) {{
                result = result * n;
                n = n - 1;
            }}
            print result;"""
            assert interpret_code(code) == [str(math.prod(range(1, i + 1)))]