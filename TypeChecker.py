#!/usr/bin/python

import AST
from Symboltable import *

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

    def __init__(self):
        self.ttype = {}
        self.ttype['+'] = {}
        self.ttype['-'] = {}
        self.ttype['*'] = {}
        self.ttype['/'] = {}
        self.ttype['%'] = {}
        self.ttype['^'] = {}
        self.ttype['|'] = {}
        self.ttype['&'] = {}
        self.ttype['AND'] = {}
        self.ttype['OR'] = {}
        self.ttype['SHL'] = {}
        self.ttype['SHR'] = {}
        self.ttype['EQ'] = {}
        self.ttype['NEQ'] = {}
        self.ttype['>'] = {}
        self.ttype['<'] = {}
        self.ttype['LE'] = {}
        self.ttype['GE'] = {}

    def visit_Program(self, node, table):
        symbolTable = SymbolTable(None, 'global')
        self.visit(node.declarations, symbolTable)
        self.visit(node.fundefs, symbolTable)
        self.visit(node.instructions, symbolTable)

    def visit_Declarations(self, node, table):
        self.visit(node.declarations, table)
        self.visit(node.declaration, table)

    def visit_Declaration(self, node, table):
        inits = []
        tmp = node.inits
        inits.append(tmp.init)
        while(tmp.inits):
            tmp = tmp.inits
            inits.append(tmp.init)
        inits.reverse()
        for init in inits:
            if(not table.put(VariableSymbol(init.id,node.type))):
                print 'error variable alreday declared: '+ init.id

    def visit_Inits(self, node, table):
        if ( node.inits ):
            self.visit(node.inits, table)
        self.visit(node.init, table)

    def visit_Init(self, node, table):
        #print node.ID
        self.visit(node.expression, table)

    def visit_Instructions(self, node, table):
        if ( node.instructions ):
            self.visit(node.instructions, table)
        self.visit(node.instruction, table)

    def visit_Instruction(self, node, table):
        self.visit(node.instruction, table)

    def visit_Print(self, node, table):
        self.visit(node.expression, table)

    def visit_Labeled(self, node, table):
        #print node.id
        self.visit(node.instruction, table)

    def visit_Assignment(self, node, table):
        #print node.id
        leftType = None
        leftSymbol = table.get(node.id)
        if leftSymbol:
            leftType = leftSymbol.type
        rightType = self.visit(node.expression, table)

        if leftType == None:
            print 'Undeclared Variable'
        elif rightType == 'undefined':
            return
        elif not (leftType == rightType or (leftType == 'float' and rightType == 'int')):
            print 'Incompatibile type of operands'

    def visit_Choice(self, node, table):
        self.visit(node.condition, table)
        self.visit(node.instruction1, SymbolTable(table, 'choice_instr1'))
        if(node.instruction2):
            self.visit(node.instruction2, SymbolTable(table, 'choice_instr2'))

    def visit_While(self, node, table):
        self.visit(node.condition, table)
        self.visit(node.instruction, SymbolTable(table, 'while'))
        pass

    def visit_Repeat(self, node, table):
        self.visit(node.condition, table)
        self.visit(node.instruction, SymbolTable(table, 'repeat'))

    def visit_Return(self, node, table):
        if isinstance(table.name, FunctionSymbol):
            rettype = self.visit(node.expression, table)
            if rettype != 'undefined':
                expected_rettype = table.name.type
                if rettype != expected_rettype:
                    print 'Wrong return expression type, expected '
                #print rettype+ ' '+expected_rettype
        else: # global scope
            print 'Return statement used outside a function'

    def visit_Keyword(self, node, table):
        #print node.keyword
        pass

    def visit_CompoundInstruction(self, node, table):
        #newSCOPe
        nextTable = None
        if isinstance(table.name, FunctionSymbol):
            nextTable = table
        else:
            nextTable = SymbolTable(table,'blockInstr')

        self.visit(node.declarations, nextTable)
        self.visit(node.instructions, nextTable)

    def visit_Condition(self, node, table):
        self.visit(node.expression, table)

    def visit_Integer(self, node, table):
        return 'int'

    def visit_Float(self, node, table):
        return 'float'

    def visit_String(self, node, table):
        return 'string'

    def visit_Variable(self, node, table):
        symbol = table.get(node.name)
        if isinstance(symbol, VariableSymbol):
            #print 'DEBUG: Captured variable symbol ' + symbol.name + ' of type ' + symbol.type
            return symbol.type
        elif isinstance(symbol, FunctionSymbol):
            #print 'error - is a function (expected a variable) '+node.name
            return 'undefined'
        else:
            #print 'error - is not defined '+node.name
            return 'undefined'

    def visit_BinExpression(self, node, table):
        #print node.operator
        type1 =self.visit(node.expression1, table)
        type2 = self.visit(node.expression2, table)

        if type1 == 'undefined' or type2 == 'undefined':
            return 'undefined'

        operator = node.operator

        result_type = 'undefined'
        if result_type == 'undefined':
            #print operator+' operand are not allowed'
            return 'undefined'

        return result_type

    def visit_ExpressionInParentheses(self, node, table):
        self.visit(node.expression, table)

    def visit_Funcall(self, node, table):
        #print node.id
        symbol = table.get(node.id)
        if isinstance(symbol, FunctionSymbol):

            expressions = []
            tmp = node.expressionList
            if not isinstance(tmp, AST.Empty):
                if(tmp.expression):
                    expressions.append(tmp.expression)
                while(tmp.expressionList):
                    tmp = tmp.expressionList
                    if(not isinstance(tmp, AST.Empty)):
                        expressions.append(tmp.expression)
            expressions.reverse()
            expressionsTypes = [self.visit(expression, table) for expression in expressions]
            print expressionsTypes
            expectedExpressionsTypes = [arg.type for arg in symbol.arguments]
            print expectedExpressionsTypes

            if 'undefined' in expressionsTypes:
                return 'undefined'

            if len(expressionsTypes) != len(expectedExpressionsTypes):
                print 'Wrong number of parameters'

            for exprType, expectedType, i in zip(expressionsTypes, expectedExpressionsTypes, range(1, len(expressionsTypes) + 1)):
                if exprType != expectedType and not (exprType == 'int' and expectedType == 'float'):
                    print 'Wrong parameter type'
                    return 'undefined'
            return symbol.type
        elif isinstance(symbol, FunctionSymbol):
            print 'This is not a function'
            return 'undefined'
        else:
            print 'Function undefined'
            return 'undefined'

    def visit_ExpressionList(self, node, table):
        if(node.expressionList):
            self.visit(node.expressionList, table)
        if(node.expression):
            self.visit(node.expression, table)

    def visit_FunctionDefinitions(self, node, table):
        self.visit(node.fundef, table)
        self.visit(node.fundefs, table)

    def visit_FunctionDefinition(self, node, table):
        arguments = []
        tmp = node.argList
        if not isinstance(tmp, AST.Empty):
            if(tmp.arg):
                arguments.append(tmp.arg)
            while(tmp.argList):
                tmp = tmp.argList
                if(not isinstance(tmp, AST.Empty)):
                    arguments.append(tmp.arg)
        arguments.reverse()
        funcSymbol = FunctionSymbol(node.id, node.type, arguments)
        if not table.put(funcSymbol):
            print 'error already defined'

        functionTable = SymbolTable(table, funcSymbol)

        for arg in arguments:
            if not functionTable.put(VariableSymbol(arg.id, arg.type)):
                print 'Parameter ' + arg.id + ' already declared'

        self.visit(node.compoundInstruction, functionTable)

    def visit_ArgumentList(self, node, table):
        if(node.argList):
            self.visit(node.argList, table)
        if(node.arg):
            self.visit(node.arg, table)

    def visit_Argument(self, node, table):
        #print node.type, node.id
        pass
    def visit_Empty(self, node, table):
        pass



