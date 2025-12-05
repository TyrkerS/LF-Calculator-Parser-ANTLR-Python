#!/usr/bin/python3
import sys
from antlr4 import *
from dist.CalculatorLexer import CalculatorLexer
from dist.CalculatorParser import CalculatorParser
from dist.CalculatorVisitor import CalculatorVisitor

class VariableNotFound(Exception):
    pass

class CalcVisitor(CalculatorVisitor):
    def __init__(self):
        self.variables= {}

    def visitStartCont(self, ctx:CalculatorParser.StartContContext):
        if ctx.variable_assignments():
            self.visit(ctx.variable_assignments())
        return self.visit(ctx.expr())
    
    def visitBracesAssig(self, ctx:CalculatorParser.BracesAssigContext):
        return self.visit(ctx.assignments())
    
    def visitMultipleAssig(self, ctx:CalculatorParser.MultipleAssigContext):
        for assignment in ctx.assignment():
            self.visit(assignment)
        return None
    
    def visitAssig(self, ctx:CalculatorParser.AssigContext):
        var_name = ctx.VAR().getText()
        value = self.visit(ctx.expr())
        self.variables[var_name] = value
        return value
    
    def visitAtomExpr(self, ctx:CalculatorParser.AtomExprContext):
        return int(ctx.getText())
    
    def visitVarExpr(self, ctx:CalculatorParser.VarExprContext):
        var_name = ctx.VAR().getText()
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            raise VariableNotFound(f"No se ha encontrado la variable {var_name}")

    def visitParenExpr(self, ctx:CalculatorParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitOpExpr(self, ctx:CalculatorParser.OpExprContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text
        if op == '+':
            print(f"He entrado a sumar y devuelvo: {l+r}")
            return l + r
        elif op == '-':
            print(f"He entrado a restar y devuelvo: {l-r}")
            return l - r
        elif op == '*':
            print(f"He entrado a multiplicar y devuelvo: {l*r}")
            return l * r
        elif op == '/':
            print(f"He entrado a dividir y devuelvo: {l/r}")
            if r == 0:
                print('divide by zero!')
                return 0
            return l / r



def calc(line) -> float:
    try: 
        input_stream = InputStream(line)

        # lexing 
        lexer = CalculatorLexer(input_stream)
        stream = CommonTokenStream(lexer)

        # parsing 
        parser = CalculatorParser(stream)
        tree = parser.start()

        # use customized visitor to traverse AST
        visitor = CalcVisitor()
        return visitor.visitStartCont(tree)
    except VariableNotFound as v:
        print(f"Error: {v}. String no acceptado")
    except Exception as e:
        print("String no acceptado")



if __name__ == '__main__':
    while True:
        print(">>> ", end='')
        line = input()
        print(calc(line))
