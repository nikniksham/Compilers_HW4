# Generated from Lang.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser


# This class defines a complete listener for a parse tree produced by LangParser.
class LangListener(ParseTreeListener):

    # Enter a parse tree produced by LangParser#program.
    def enterProgram(self, ctx: LangParser.ProgramContext):
        pass

    # Exit a parse tree produced by LangParser#program.
    def exitProgram(self, ctx: LangParser.ProgramContext):
        pass

    # Enter a parse tree produced by LangParser#statement.
    def enterStatement(self, ctx: LangParser.StatementContext):
        pass

    # Exit a parse tree produced by LangParser#statement.
    def exitStatement(self, ctx: LangParser.StatementContext):
        pass

    # Enter a parse tree produced by LangParser#assignment_statement.
    def enterAssignment_statement(self, ctx: LangParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by LangParser#assignment_statement.
    def exitAssignment_statement(self, ctx: LangParser.Assignment_statementContext):
        pass

    # Enter a parse tree produced by LangParser#if_statement.
    def enterIf_statement(self, ctx: LangParser.If_statementContext):
        pass

    # Exit a parse tree produced by LangParser#if_statement.
    def exitIf_statement(self, ctx: LangParser.If_statementContext):
        pass

    # Enter a parse tree produced by LangParser#while_statement.
    def enterWhile_statement(self, ctx: LangParser.While_statementContext):
        pass

    # Exit a parse tree produced by LangParser#while_statement.
    def exitWhile_statement(self, ctx: LangParser.While_statementContext):
        pass

    # Enter a parse tree produced by LangParser#print_statement.
    def enterPrint_statement(self, ctx: LangParser.Print_statementContext):
        pass

    # Exit a parse tree produced by LangParser#print_statement.
    def exitPrint_statement(self, ctx: LangParser.Print_statementContext):
        pass

    # Enter a parse tree produced by LangParser#MulDivExpr.
    def enterMulDivExpr(self, ctx: LangParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by LangParser#MulDivExpr.
    def exitMulDivExpr(self, ctx: LangParser.MulDivExprContext):
        pass

    # Enter a parse tree produced by LangParser#CompExpr.
    def enterCompExpr(self, ctx: LangParser.CompExprContext):
        pass

    # Exit a parse tree produced by LangParser#CompExpr.
    def exitCompExpr(self, ctx: LangParser.CompExprContext):
        pass

    # Enter a parse tree produced by LangParser#AtomExpr.
    def enterAtomExpr(self, ctx: LangParser.AtomExprContext):
        pass

    # Exit a parse tree produced by LangParser#AtomExpr.
    def exitAtomExpr(self, ctx: LangParser.AtomExprContext):
        pass

    # Enter a parse tree produced by LangParser#AddSubExpr.
    def enterAddSubExpr(self, ctx: LangParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by LangParser#AddSubExpr.
    def exitAddSubExpr(self, ctx: LangParser.AddSubExprContext):
        pass

    # Enter a parse tree produced by LangParser#atom.
    def enterAtom(self, ctx: LangParser.AtomContext):
        pass

    # Exit a parse tree produced by LangParser#atom.
    def exitAtom(self, ctx: LangParser.AtomContext):
        pass


del LangParser