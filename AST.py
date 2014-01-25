
class Node(object):
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third
    def toString(self, i):
        return self.first.toString(i) + self.second.toString(i) + self.third.toString(i)

class Declarations(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def toString(self, i):
        return self.first.toString(i) + self.second.toString(i)
    def setParent(self, parent):
        self.parent = parent

class Inits(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def toString(self, i):
        return self.first.toString(i) + self.second.toString(i)
    def setParent(self, parent):
        self.parent = parent

class Inits1(object):
    def __init__(self, first):
        self.first = first
    def toString(self, i):
        return self.first.toString(i)
    def setParent(self, parent):
        self.parent = parent

class Instructions(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def toString(self, i):
        return self.first.toString(i) + self.second.toString(i)
    def setParent(self, parent):
        self.parent = parent

class Instuctions1(object):
    def __init__(self, first):
        self.first = first
    def toString(self, i):
        return self.first.toString(i)
    def setParent(self, parent):
        self.parent = parent

class Instruction(object):
    def __init__(self, first):
        self.first = first
    def toString(self, i):
        return self.first.toString(i)
    def setParent(self, parent):
        self.parent = parent

class Expression2(object):
    def __init__(self, first):
        self.first = first
    def toString(self, i):
        return self.first.toString(i)
    def setParent(self, parent):
        self.parent = parent

class ExprList(object):
    def __init__(self, first):
        self.first = first
    def toString(self, i):
        return self.first.toString(i)
    def setParent(self, parent):
        self.parent = parent

class CompoundInst(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def toString(self, i):
        return self.first.toString(i) + self.second.toString(i)
    def setParent(self, parent):
        self.parent = parent

class Condition(object):
    def __init__(self, first):
        self.first = first
    def toString(self, i):
        return self.first.toString(i)
    def setParent(self, parent):
        self.parent = parent

class ExpressionList(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def toString(self, i):
        return self.first.toString(i) + self.second.toString(i)
    def setParent(self, parent):
        self.parent = parent

class ExpressionList1(object):
    def __init__(self, first):
        self.first = first
    def toString(self, i):
        return self.first.toString(i)
    def setParent(self, parent):
        self.parent = parent

class FunDefs(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def toString(self, i):
        return self.first.toString(i) + self.second.toString(i)
    def setParent(self, parent):
        self.parent = parent

class ArgListOrEmpty(object):
    def __init__(self, first):
        self.first = first
    def toString(self, i):
        return self.first.toString(i)
    def setParent(self, parent):
        self.parent = parent

class ArgList(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def toString(self, i):
        return self.first.toString(i) + self.second.toString(i)
    def setParent(self, parent):
        self.parent = parent

class ArgList1(object):
    def __init__(self, first):
        self.first = first
    def toString(self, i):
        return self.first.toString(i)
    def setParent(self, parent):
        self.parent = parent

class Arg(object):
    def __init__(self, TYPE, ID):
        self.TYPE = TYPE
        self.ID = ID
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'ARG ' + self.ID + '\n'
    def setParent(self, parent):
        self.parent = parent

class Fundef(object):
    def __init__(self, TYPE, ID, first, second):
        self.TYPE = TYPE
        self.ID = ID
        self.first = first
        self.second = second
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        #return pal + self.TYPE + '\n' + pal + self.ID + '\n' + self.first.toString(i+1) + self.second.toString(i+1)
        return pal + 'FUNDEF' + '\n' + pal + '| ' + self.ID + '\n' + '| ' + 'RET ' + self.TYPE + '\n' + self.first.toString(i+1) + self.second.toString(i+1)
    def setParent(self, parent):
        self.parent = parent

class Expression(object):
    def __init__(self, expr1, sign, expr2):
        self.expr1 = expr1
        self.sign = sign
        self.expr2 = expr2
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.sign + '\n' +  self.expr1.toString(i+1) + self.expr2.toString(i+1)
    def setParent(self, parent):
        self.parent = parent

class MathExpression(object):
    def __init__(self, expr1, sign, expr2):
        self.expr1 = expr1
        self.sign = sign
        self.expr2 = expr2
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.sign + '\n' +  self.expr1.toString(i+1) + self.expr2.toString(i+1)
    def setParent(self, parent):
        self.parent = parent

class Expression1(object):
    def __init__(self, ID, second):
        self.ID = ID
        self.second = second
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.ID.upper() + '\n' + self.second.toString(i+1)
    def setParent(self, parent):
        self.parent = parent

class Funcall(object):
    def __init__(self, ID, second):
        self.ID = ID
        self.second = second
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'FUNCALL\n' + pal + '| ' + self.ID + '\n' + self.second.toString(i+1)
    def setParent(self, parent):
        self.parent = parent

class Repeat(object):
    def __init__(self, REPEAT, inst, UNTIL, cond):
        self.REAPEAT = REPEAT
        self.inst = inst
        self.UNTIL = UNTIL
        self.cond = cond
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.REAPEAT + '\n' + self.inst.toString(i+1) + pal + self.UNTIL + '\n' + self.cond.toString(i+1)
    def setParent(self, parent):
        self.parent = parent

class While(object):
    def __init__(self, WHILE, condition, instruction):
        self.WHILE = WHILE
        self.condition = condition
        self.instruction = instruction
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.WHILE.upper() + '\n' + self.condition.toString(i+1) + self.instruction.toString(i+1)
    def setParent(self, parent):
        self.parent = parent

class Choice(object):
    def __init__(self, IF, cond, inst, ELSE, inst2):
        self.IF = IF
        self.cond = cond
        self.inst = inst
        self.ELSE = ELSE
        self.inst2 = inst2
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.IF.upper() + '\n' + self.cond.toString(i+1) + self.inst.toString(i+1) + pal + self.ELSE.upper() + '\n' + self.inst2.toString(i+1)
    def setParent(self, parent):
        self.parent = parent

class Choice2(object):
    def __init__(self, IF, cond, instr):
        self.IF = IF
        self.cond = cond
        self.instr = instr
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.IF.upper() + '\n' + self.cond.toString(i+1) + self.instr.toString(i+1)
    def setParent(self, parent):
        self.parent = parent

class Assignment(object):
    def __init__(self, ID, expr):
        self.ID = ID
        self.expr = expr
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + '=' + '\n' + pal + '| ' + self.ID + '\n' + self.expr.toString(i+1)
    def setParent(self, parent):
        self.parent = parent

class Declaration(object):
    def __init__(self, inits):
        self.inits = inits
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'DECL' + '\n' + self.inits.toString(i+1)
    def setParent(self, parent):
        self.parent = parent

class Empty(object):
    def __init__(self):
        self.name = ""
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return self.name
    def setParent(self, parent):
        self.parent = parent

class Const(Node):
    def __init__(self, name):
        self.name = name
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.name + '\n'
    def setParent(self, parent):
        self.parent = parent


class Integer(Const):
    pass


class Float(Const):
    pass


class String(Const):
    pass


class Variable(Node):
    def __init__(self, name):
        self.name = name



class BinExpr(Node):
    def __init__(self, o1, op, o2):
        self.o1 = o1
        self.op = op
        self.o2 = o2


# ...

