# Generated from Lang.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete generic visitor for a parse tree produced by LangParser.


class LangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LangParser#program.
    def visitProgram(self, ctx: LangParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LangParser#statement.
    def visitStatement(self, ctx: LangParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LangParser#assignment_statement.
    def visitAssignment_statement(self, ctx: LangParser.Assignment_statementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LangParser#if_statement.
    def visitIf_statement(self, ctx: LangParser.If_statementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LangParser#while_statement.
    def visitWhile_statement(self, ctx: LangParser.While_statementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LangParser#print_statement.
    def visitPrint_statement(self, ctx: LangParser.Print_statementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LangParser#MulDivExpr.
    def visitMulDivExpr(self, ctx: LangParser.MulDivExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LangParser#CompExpr.
    def visitCompExpr(self, ctx: LangParser.CompExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LangParser#AtomExpr.
    def visitAtomExpr(self, ctx: LangParser.AtomExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LangParser#AddSubExpr.
    def visitAddSubExpr(self, ctx: LangParser.AddSubExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by LangParser#atom.
    def visitAtom(self, ctx: LangParser.AtomContext):
        return self.visitChildren(ctx)


del LangParser