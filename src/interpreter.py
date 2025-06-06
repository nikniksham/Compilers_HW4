from antlr4 import *
from .LangLexer import LangLexer
from .LangParser import LangParser
from .LangVisitor import LangVisitor


class InterpreterError(Exception):
    pass


class Interpreter(LangVisitor):
    def __init__(self):
        self.variables = {}
        self.output = []

    def visitProgram(self, ctx: LangParser.ProgramContext):
        for stmt_ctx in ctx.statement():
            self.visit(stmt_ctx)
        return self.output

    def visitAssignment_statement(self, ctx: LangParser.Assignment_statementContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value
        return value

    def visitIf_statement(self, ctx: LangParser.If_statementContext):
        condition = self.visit(ctx.expression())
        # Any non-zero number, non-empty string is considered True
        if condition != 0 and condition != 0.0 and condition != "":
            self.visit(ctx.program(0))
        elif ctx.ELSE():
            self.visit(ctx.program(1))
        return None

    def visitWhile_statement(self, ctx: LangParser.While_statementContext):
        while (
            self.visit(ctx.expression()) != 0
            and self.visit(ctx.expression()) != 0.0
            and self.visit(ctx.expression()) != ""
        ):
            self.visit(ctx.program())
        return None

    def visitPrint_statement(self, ctx: LangParser.Print_statementContext):
        value = self.visit(ctx.expression())
        self.output.append(str(value))
        return value

    def _get_numeric_type(self, left, right):
        """Determine the type for numeric operations"""
        # If either is float, result should be float
        if isinstance(left, float) or isinstance(right, float):
            # Convert to float if they're numeric
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return float(left), float(right), "float"
        # If both are int, result is int
        if isinstance(left, int) and isinstance(right, int):
            return left, right, "int"
        # Mixed numeric-string operations
        if isinstance(left, (int, float)) and isinstance(right, str):
            return left, right, "mixed"
        if isinstance(left, str) and isinstance(right, (int, float)):
            return left, right, "mixed"
        # Both are strings
        if isinstance(left, str) and isinstance(right, str):
            return left, right, "string"
        # Default
        return left, right, "unknown"

    def visitMulDivExpr(self, ctx: LangParser.MulDivExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()

        left, right, type_result = self._get_numeric_type(left, right)

        if op == "*":
            if type_result == "int" or type_result == "float":
                return left * right
            elif type_result == "mixed":
                # String multiplication with number
                if isinstance(left, str) and isinstance(right, (int, float)):
                    return left * int(right)
                elif isinstance(left, (int, float)) and isinstance(right, str):
                    return right * int(left)
            else:
                raise InterpreterError(f"Cannot multiply '{left}' and '{right}'")
        elif op == "/":
            if type_result != "int" and type_result != "float":
                raise InterpreterError(
                    f"Cannot divide non-numeric types: '{left}' / '{right}'"
                )
            if right == 0 or right == 0.0:
                raise InterpreterError("Division by zero")
            if type_result == "int":
                return int(left / right)
            else:
                return left / right

        raise InterpreterError(f"Unknown operator: {op}")

    def visitAddSubExpr(self, ctx: LangParser.AddSubExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()

        left, right, type_result = self._get_numeric_type(left, right)

        if op == "+":
            if type_result == "int" or type_result == "float":
                return left + right
            elif type_result == "string":
                return left + right
            elif type_result == "mixed":
                # Convert number to string for concatenation
                if isinstance(left, str):
                    return left + str(right)
                else:
                    return str(left) + right
        elif op == "-":
            if type_result != "int" and type_result != "float":
                raise InterpreterError(
                    f"Cannot subtract non-numeric types: '{left}' - '{right}'"
                )
            return left - right

        raise InterpreterError(f"Unknown operator: {op}")

    def visitCompExpr(self, ctx: LangParser.CompExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()

        # For comparison, we only convert between int and float, not strings
        if isinstance(left, int) and isinstance(right, float):
            left = float(left)
        elif isinstance(left, float) and isinstance(right, int):
            right = float(right)

        if op == "==":
            return 1 if left == right else 0
        elif op == "!=":
            return 1 if left != right else 0
        elif op == ">":
            if (isinstance(left, str) and not isinstance(right, str)) or (
                not isinstance(left, str) and isinstance(right, str)
            ):
                raise InterpreterError(
                    f"Cannot compare string with non-string: '{left}' > '{right}'"
                )
            return 1 if left > right else 0
        elif op == "<":
            if (isinstance(left, str) and not isinstance(right, str)) or (
                not isinstance(left, str) and isinstance(right, str)
            ):
                raise InterpreterError(
                    f"Cannot compare string with non-string: '{left}' < '{right}'"
                )
            return 1 if left < right else 0
        elif op == ">=":
            if (isinstance(left, str) and not isinstance(right, str)) or (
                not isinstance(left, str) and isinstance(right, str)
            ):
                raise InterpreterError(
                    f"Cannot compare string with non-string: '{left}' >= '{right}'"
                )
            return 1 if left >= right else 0
        elif op == "<=":
            if (isinstance(left, str) and not isinstance(right, str)) or (
                not isinstance(left, str) and isinstance(right, str)
            ):
                raise InterpreterError(
                    f"Cannot compare string with non-string: '{left}' <= '{right}'"
                )
            return 1 if left <= right else 0
        raise InterpreterError(f"Unknown comparison operator: {op}")

    def visitAtomExpr(self, ctx: LangParser.AtomExprContext):
        return self.visit(ctx.atom())

    def visitAtom(self, ctx: LangParser.AtomContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.STRING():
            # Remove quotes from string literals
            text = ctx.STRING().getText()
            # Remove surrounding quotes
            if text.startswith("'") and text.endswith("'"):
                text = text[1:-1]
            elif text.startswith('"') and text.endswith('"'):
                text = text[1:-1]
            # Handle escape sequences
            text = (
                text.replace("\\'", "'")
                .replace('\\"', '"')
                .replace("\\n", "\n")
                .replace("\\t", "\t")
            )
            return text
        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                raise InterpreterError(f"Variable '{var_name}' not defined.")
        elif ctx.LPAREN():
            return self.visit(ctx.expression())
        raise InterpreterError("Unknown atom type")


def run_interpreter(input_stream):
    lexer = LangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LangParser(stream)
    tree = parser.program()

    interpreter = Interpreter()
    return interpreter.visit(tree)


def run_interpreter_from_string(code_string):
    input_stream = InputStream(code_string)
    return run_interpreter(input_stream)


def run_interpreter_from_file(file_path):
    input_stream = FileStream(file_path)
    return run_interpreter(input_stream)