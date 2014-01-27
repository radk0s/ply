class Node(object):
    def accept(self, visitor, table = None):
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
    def __init__(self, id, expression):
        self.id = id
        self.expression = expression
        self.children = ( expression )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + '=' + '\n' + pal + '| ' + self.id + '\n' + self.expression.toString(i+1)


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
    def __init__(self, condition, instruction1, instruction2):
        self.condition = condition
        self.instruction1 = instruction1
        self.instruction2 = instruction2
        self.children = ( condition, instruction1, instruction2 )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'IF' + '\n' + \
               self.condition.toString(i+1) + \
               self.instruction1.toString(i+1) + \
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
    def __init__(self, instruction, condition):
        self.instruction = instruction
        self.condition = condition
        self.children = ( instruction, condition )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'REPEAT' + '\n' + self.instruction.toString(i+1) + \
               pal + 'UNTIL' + '\n' + self.condition.toString(i+1)


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
    def __init__(self, expression1, operator, expression2):
        self.expression1 = expression1
        self.operator = operator
        self.expression2 = expression2
        self.children = ( expression1, operator, expression2 )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.operator + '\n' +  self.expression1.toString(i+1) + self.expression2.toString(i+1)

class ExpressionInParentheses(Node):
    def __init__(self, expression):
        self.expression = expression
        self.children = ( expression )
    def toString(self, i):
        return self.expression.toString(i)

class Funcall(Node):
    def __init__(self, id, expressionList):
        self.id = id
        self.expressionList = expressionList
        self.children = ( expressionList )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'FUNCALL\n' + pal + \
               '| ' + self.id + '\n' + self.expressionList.toString(i+1)

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
    def __init__(self, type, id, argList, compoundInstruction):
        self.type = type
        self.id = id
        self.argList = argList
        self.compoundInstruction = compoundInstruction
        self.children = ( argList, compoundInstruction)
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        #return pal + self.TYPE + '\n' + pal + self.ID + '\n' + self.first.toString(i+1) + self.second.toString(i+1)
        return pal + 'FUNDEF' + '\n' + \
               pal + '| ' + self.id + '\n' + \
               '| ' + 'RET ' + self.type + '\n' + \
               self.argList.toString(i+1) + \
               self.compoundInstruction.toString(i+1)

class ArgumentList(Node):
    def __init__(self, argList, arg):
        self.argList = argList
        self.arg = arg
        self.children = ( argList, arg )
    def toString(self, i):
        return (self.argList.toString(i) if("toString" in dir(self.argList)) else '') + \
               (self.arg.toString(i) if("toString" in dir(self.arg)) else '')

class Argument(Node):
    def __init__(self, type, id):
        self.type = type
        self.id = id
        self.children = ( )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'ARG ' + self.id + '\n'

class Empty(Node):
    def __init__(self):
        self.name = ""
        self.children = ( )
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return self.name

