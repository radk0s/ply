#!/usr/bin/python

import AST

class NodeVisitor(object):

    def visit(self, node, table):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node, table)


    def generic_visit(self, node):        # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)


class TypeChecker(NodeVisitor):

    stack = []

    def visit_Program(self, node, table):
        symbolTable = {}
        print(symbolTable)
        self.visit(node.declarations, symbolTable)
        self.visit(node.fundefs, symbolTable)
        self.visit(node.instructions, symbolTable)

    def visit_Declarations(self, node, table):
        self.visit(node.declarations, table)
        self.visit(node.declaration, table)

    def visit_Declaration(self, node, table):
        print(table)
        type = node.type
        self.stack.append(type)
        self.visit(node.inits, table)

    def visit_Inits(self, node, table):
        if ( node.inits != None):
            self.visit(node.inits, table)
        self.visit(node.init, table)

    def visit_Init(self, node, table):
        self.visit(node.expr, table)

    def visit_Instructions(self, node, table):
        print("9QQ")

    def visit_Instruction(self, node, table):
        print("8QQ")

    def visit_Print(self, node, table):
        print("9QQ")

    def visit_Labeled(self, node, table):
        print("8QQ")

    def visit_Assigment(self, node, table):
        print("8QQ")

    def visit_Choice(self, node, table):
        print("9QQ")

    def visit_While(self, node, table):
        print("8QQ")

    def visit_Repeat(self, node, table):
        print("9QQ")

    def visit_Return(self, node, table):
        print("8QQ")

    def visit_Keyword(self, node, table):
        print("9QQ")

    def visit_CompoundInstruction(self, node, table):
        print("8QQ")

    def visit_Condition(self, node, table):
        print("8QQ")

    def visit_Integer(self, node, table):
        tmp = node.parent
        while(not "type" in dir(tmp)):
            tmp = tmp.parent
        print(node.parent.ID, tmp.type, node.value)

    def visit_Float(self, node, table):
        tmp = node.parent
        while(not "type" in dir(tmp)):
            tmp = tmp.parent
        print(node.parent.ID, tmp.type, node.value)

    def visit_String(self, node, table):
        tmp = node.parent
        while(not "type" in dir(tmp)):
            tmp = tmp.parent
        print(node.parent.ID, tmp.type, node.value)

    def visit_Variable(self, node, table):
        print("8QQ")

    def visit_BinExpression(self, node, table):
        print("9QQ")

    def visit_ExpressionInParentheses(self, node, table):
        print("8QQ")

    def visit_Funcall(self, node, table):
        print("8QQ")

    def visit_ExpressionList(self, node, table):
        print("8QQ")

    def visit_FunctionDefinitions(self, node, table):
        print("8QQ")

    def visit_FunctionDefinition(self, node, table):
        print("9QQ")

    def visit_ArgumentList(self, node, table):
        print("8QQ")

    def visit_Argument(self, node, table):
        print("9QQ")

    def visit_Empty(self, node, table):
        print("8QQ")



