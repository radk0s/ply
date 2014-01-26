class Node(object):
    def accept(self, visitor, table):
        return visitor.visit(self)
    def setParent(self, parent):
        self.parent = parent

class Program(Node):
    def __init__(self, declarations, fundefs, instructions):
        self.declarations = declarations
        self.fundefs = fundefs
        self.instructions = instructions
        self.children = ( declarations, fundefs, instructions )
    def toString(self, i):
        return self.declarations.toString(i) + \
               (self.fundefs.toString(i) if("toString" in dir(self.fundefs)) else '')+ \
               self.instructions.toString(i)

class Declarations(Node):
    def __init__(self, declarations, declaration):
        self.declarations = declarations
        self.declaration = declaration
        self.children = ( declarations, declaration )
    def toString(self, i):
        return self.declarations.toString(i) + \
               self.declaration.toString(i)

class Declaration(Node):
    def __init__(self, type, inits):
        self.type = type
        self.inits = inits
        self.children = ( inits )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'DECL' + '\n' + \
               self.inits.toString(i+1) if("toString" in dir(self.inits)) else '<<ERROR HERE>>\n'

class Inits(Node):
    def __init__(self, inits, init):
        self.inits = inits
        self.init = init
        self.children = ( inits, init )
    def toString(self, i):
        return (self.inits.toString(i) if("toString" in dir(self.inits)) else '') + \
               (self.init.toString(i) if("toString" in dir(self.init)) else '')

class Init(Node):
    def __init__(self, ID, expr):
        self.ID = ID
        self.expr = expr
        self.children = ( expr )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + '=' + '\n' + pal + '| ' + self.ID + '\n' + self.expr.toString(i+1)


class Instructions(Node):
    def __init__(self, instructions, instruction):
        self.instructions = instructions
        self.instruction = instruction
        self.children = ( instructions, instruction )
    def toString(self, i):
        return (self.instructions.toString(i) if("toString" in dir(self.instructions)) else '') + \
               (self.instruction.toString(i) if("toString" in dir(self.instruction)) else '')


class Instruction(Node):
    def __init__(self, instruction):
        self.instruction = instruction
        self.children = ( instruction )
    def toString(self, i):
        return self.instruction.toString(i)

class Print(Node):
    def __init__(self, expression):
        self.expression = expression
        self.children = ( expression )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'PRINT' + '\n'\
               + self.expression.toString(i+1)

class Labeled(Node):
    def __init__(self, id, instruction):
        self.id = id
        self.instruction = instruction
        self.children = ( instruction )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.id.upper() + '\n'\
               + self.instruction.toString(i+1)

class Assignment(Node):
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression
        self.children = ( expression )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + '=' + '\n' + pal + '| ' + self.id + '\n' + self.expression.toString(i+1)

class Choice(Node):
    def __init__(self, cond, instruction, instruction2):
        self.cond = cond
        self.instruction = instruction
        self.instruction2 = instruction2
        self.children = ( cond, instruction, instruction2 )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'IF' + '\n' + \
               self.cond.toString(i+1) + \
               self.instruction.toString(i+1) + \
               pal + 'ELSE' + '\n' + \
               self.instruction2.toString(i+1)

class While(Node):
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction
        self.children = ( condition, instruction )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'WHILE' + '\n' + \
               self.condition.toString(i+1) + \
               self.instruction.toString(i+1)

class Repeat(Node):
    def __init__(self, inst, cond):
        self.inst = inst
        self.cond = cond
        self.children = ( inst, cond )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'REPEAT' + '\n' + self.inst.toString(i+1) + \
               pal + 'UNTIL' + '\n' + self.cond.toString(i+1)


class Return(Node):
    def __init__(self, expression):
        self.expression = expression
        self.children = ( expression )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'RETURN' + '\n' + \
               self.expression.toString(i+1)

class Keyword(Node):
    def __init__(self, keyword):
        self.keyword = keyword
        self.children = (  )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.keyword + '\n'

class CompoundInstruction(Node):
    def __init__(self, declarations, instructions):
        self.declarations = declarations
        self.instructions = instructions
        self.children = ( declarations, instructions )
    def toString(self, i):
        return self.declarations.toString(i) + self.instructions.toString(i)

class Condition(Node):
    def __init__(self, expression):
        self.expression = expression
        self.children = ( expression )
    def toString(self, i):
        return self.expression.toString(i)


class Integer(Node):
    def __init__(self, value):
        self.value = value
        self.children = ( )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.value + '\n'

class Float(Node):
    def __init__(self, value):
        self.value = value
        self.children = ( )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.value + '\n'

class String(Node):
    def __init__(self, value):
        self.value = value
        self.children = ( )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.value + '\n'

class Variable(Node):
    def __init__(self, name):
        self.name = name
        self.children = ( )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.name + '\n'

class BinExpression(Node):
    def __init__(self, expr1, sign, expr2):
        self.expr1 = expr1
        self.sign = sign
        self.expr2 = expr2
        self.children = ( expr1, sign, expr2 )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.sign + '\n' +  self.expr1.toString(i+1) + self.expr2.toString(i+1)

class ExpressionInParentheses(Node):
    def __init__(self, expression):
        self.expression = expression
        self.children = ( expression )
    def toString(self, i):
        return self.expression.toString(i)

class Funcall(Node):
    def __init__(self, ID, exprList):
        self.ID = ID
        self.exprList = exprList
        self.children = ( exprList )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'FUNCALL\n' + pal + \
               '| ' + self.ID + '\n' + self.exprList.toString(i+1)

class ExpressionList(Node):
    def __init__(self, expressionList, expression):
        self.expressionList = expressionList
        self.expression = expression
        self.children = ( expressionList, expression)
    def toString(self, i):
        return (self.expressionList.toString(i) if("toString" in dir(self.expressionList)) else '') + \
               (self.expression.toString(i) if("toString" in dir(self.expression)) else '')


class FunctionDefinitions(Node):
    def __init__(self, fundef, fundefs):
        self.fundef = fundef
        self.fundefs = fundefs
        self.children = ( fundef, fundefs)
    def toString(self, i):
        return self.fundef.toString(i) + self.fundefs.toString(i)

class FunctionDefinition(Node):
    def __init__(self, TYPE, ID, argList, compoundInstr):
        self.TYPE = TYPE
        self.ID = ID
        self.argList = argList
        self.compoundInstr = compoundInstr
        self.children = ( argList, compoundInstr)
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        #return pal + self.TYPE + '\n' + pal + self.ID + '\n' + self.first.toString(i+1) + self.second.toString(i+1)
        return pal + 'FUNDEF' + '\n' + \
               pal + '| ' + self.ID + '\n' + \
               '| ' + 'RET ' + self.TYPE + '\n' + \
               self.argList.toString(i+1) + \
               self.compoundInstr.toString(i+1)

class ArgumentList(Node):
    def __init__(self, argList, arg):
        self.argList = argList
        self.arg = arg
        self.children = ( argList, arg )
    def toString(self, i):
        return (self.argList.toString(i) if("toString" in dir(self.argList)) else '') + \
               (self.arg.toString(i) if("toString" in dir(self.arg)) else '')

class Argument(Node):
    def __init__(self, TYPE, ID):
        self.TYPE = TYPE
        self.ID = ID
        self.children = ( )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'ARG ' + self.ID + '\n'

class Empty(Node):
    def __init__(self):
        self.name = ""
        self.children = ( )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return self.name

