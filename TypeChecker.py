#!/usr/bin/python

import AST

class NodeVisitor(object):

    def visit(self, node, table = None):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node, table)


    def generic_visit(self, node, table):        # Called if no explicit visitor function exists for a node.
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

    scopeStack = []

    def visit_Program(self, node, table):
        symbolTable = {}
        self.visit(node.declarations, symbolTable)
        self.visit(node.fundefs, symbolTable)
        self.visit(node.instructions, symbolTable)

    def visit_Declarations(self, node, table):
        self.visit(node.declarations, table)
        self.visit(node.declaration, table)

    def visit_Declaration(self, node, table):
        print node.type
        self.visit(node.inits, table)

    def visit_Inits(self, node, table):
        if ( node.inits ):
            self.visit(node.inits, table)
        self.visit(node.init, table)

    def visit_Init(self, node, table):
        print node.ID
        self.visit(node.expr, table)

    def visit_Instructions(self, node, table):
        if ( node.instructions ):
            self.visit(node.instructions, table)
        self.visit(node.instruction, table)

    def visit_Instruction(self, node, table):
        self.visit(node.instruction, table)

    def visit_Print(self, node, table):
        self.visit(node.expression, table)

    def visit_Labeled(self, node, table):
        print node.id
        self.visit(node.instruction, table)

    def visit_Assignment(self, node, table):
        print node.id
        self.visit(node.expression, table)

    def visit_Choice(self, node, table):
        self.visit(node.cond, table)
        self.visit(node.instruction, table)
        if(node.instruction2):
            self.visit(node.instruction2, table)

    def visit_While(self, node, table):
        self.visit(node.condition, table)
        self.visit(node.instruction, table)
        pass

    def visit_Repeat(self, node, table):
        self.visit(node.cond, table)
        self.visit(node.inst, table)

    def visit_Return(self, node, table):
        self.visit(node.expression, table)

    def visit_Keyword(self, node, table):
        print node.keyword

    def visit_CompoundInstruction(self, node, table):
        #newSCOPE
        self.visit(node.declarations, table)
        self.visit(node.instructions, table)

    def visit_Condition(self, node, table):
        self.visit(node.expression, table)

    def visit_Integer(self, node, table):
        print node.value

    def visit_Float(self, node, table):
        print node.value

    def visit_String(self, node, table):
        print node.value

    def visit_Variable(self, node, table):
        print node.name

    def visit_BinExpression(self, node, table):
        print node.sign
        self.visit(node.expr1, table)
        self.visit(node.expr2, table)

    def visit_ExpressionInParentheses(self, node, table):
        self.visit(node.expression, table)

    def visit_Funcall(self, node, table):
        print node.ID
        self.visit(node.exprList, table)

    def visit_ExpressionList(self, node, table):
        if(node.expressionList):
            self.visit(node.expressionList, table)
        if(node.expression):
            self.visit(node.expression, table)

    def visit_FunctionDefinitions(self, node, table):
        self.visit(node.fundef, table)
        self.visit(node.fundefs, table)

    def visit_FunctionDefinition(self, node, table):
        print node.TYPE, node.ID
        self.visit(node.argList, table)
        self.visit(node.compoundInstr, table)

    def visit_ArgumentList(self, node, table):
        if(node.argList):
            self.visit(node.argList, table)
        if(node.arg):
            self.visit(node.arg, table)

    def visit_Argument(self, node, table):
        print node.TYPE, node.ID

    def visit_Empty(self, node, table):
        pass



