
class Node(object):

    def __str__(self):
        return self.printTree()


class Const(Node):
    def __init__(self, name):
        self.name = name
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.name + '\n'


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

class One(object):
    def __init__(self, first):
        self.first = first
    def toString(self, i):
        return self.first.toString(i)

class Two(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def toString(self, i):
        return self.first.toString(i) + self.second.toString(i)

class Three(object):
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third
    def toString(self, i):
        return self.first.toString(i) + self.second.toString(i) + self.third.toString(i)

class Arg(object):
    def __init__(self, TYPE, ID):
        self.TYPE = TYPE
        self.ID = ID
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'ARG ' + self.ID + '\n'

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

class Expression1(object):
    def __init__(self, ID, second):
        self.ID = ID
        self.second = second
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + self.ID.upper() + '\n' + self.second.toString(i+1)

class Funcall(object):
    def __init__(self, ID, second):
        self.ID = ID
        self.second = second
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'FUNCALL\n' + pal + '| ' + self.ID + '\n' + self.second.toString(i+1)

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

class Assignment(object):
    def __init__(self, ID, expr):
        self.ID = ID
        self.expr = expr
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + '=' + '\n' + pal + '| ' + self.ID + '\n' + self.expr.toString(i+1)

class Declaration(object):
    def __init__(self, inits):
        self.inits = inits
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return pal + 'DECL' + '\n' + self.inits.toString(i+1) if("toString" in dir(self.inits)) else '<<ERROR HERE>>\n'

class Empty(object):
    def __init__(self):
        self.name = ""
    def toString(self, i):
        pal = ""
        for x in range(0, i):
            pal += '| '
        return self.name


