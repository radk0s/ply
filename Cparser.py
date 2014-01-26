#!/usr/bin/zpython

import AST
from scanner import Scanner
from TypeChecker import TypeChecker




class Cparser(object):

    palka = ''

    def __init__(self):
        self.scanner = Scanner()
        self.scanner.build()

    tokens = Scanner.tokens


    precedence = (
       ("nonassoc", 'IFX'),
       ("nonassoc", 'ELSE'),
       ("right", '='),
       ("left", 'OR'),
       ("left", 'AND'),
       ("left", '|'),
       ("left", '^'),
       ("left", '&'),
       ("nonassoc", '<', '>', 'EQ', 'NEQ', 'LE', 'GE'),
       ("left", 'SHL', 'SHR'),
       ("left", '+', '-'),
       ("left", '*', '/', '%'),
    )

    error = 0

    def p_error(self, p):
        Cparser.error = 1
        if p:
            print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, self.scanner.find_tok_column(p), p.type, p.value))
            #exit(1);
        else:
            print('At end of input')

    def p_program(self, p):
        """program : declarations fundefs instructions"""
        p[0] = AST.Program(p[1], p[2], p[3])
        #print(p[0].toString(0))
        p[1].setParent(p[0])
        p[2].setParent(p[0])
        p[3].setParent(p[0])

    def p_declarations(self, p):
        """declarations : declarations declaration"""
        p[0] = AST.Declarations(p[1], p[2])
        p[1].setParent(p[0])
        p[2].setParent(p[0])

    def p_declarations_1(self, p):
        """declarations : """
        p[0] = AST.Empty()

    def p_declaration(self, p):
        """declaration : TYPE inits ';' """
        p[0] = AST.Declaration(p[1], p[2])
        p[2].setParent(p[0])

    def p_declaration_error(self, p):
        """declaration : error ';' """
        self.p_error(p[1])


    def p_inits(self, p):
        """inits : inits ',' init"""
        p[0] = AST.Inits(p[1], p[3])
        p[1].setParent(p[0])
        p[3].setParent(p[0])

    def p_inits_1(self, p):
        """inits : init"""

        p[0] = AST.Inits(None, p[1])
        p[1].setParent(p[0])

    def p_init(self, p):
        """init : ID '=' expression """
        p[0] = AST.Init(p[1], p[3])
        p[3].setParent(p[0])

    def p_instructions(self, p):
        """instructions : instructions instruction"""
        p[0] = AST.Instructions(p[1], p[2])
        p[1].setParent(p[0])
        p[2].setParent(p[0])

    def p_instructions_1(self, p):
        """instructions : instruction"""
        p[0] = AST.Instructions(None, p[1])
        p[1].setParent(p[0])

    def p_instruction(self, p):
        """instruction : print_instr
                       | labeled_instr
                       | assignment
                       | choice_instr
                       | while_instr
                       | repeat_instr
                       | return_instr
                       | break_instr
                       | continue_instr
                       | compound_instr"""
        p[0] = AST.Instruction(p[1])
        p[1].setParent(p[0])

    def p_print_instr(self, p):
        """print_instr : PRINT expression ';'"""
        p[0] = AST.Print(p[2])
        p[2].setParent(p[0])

    def p_print_instr_1(self, p):
        """print_instr : PRINT error ';' """
        self.p_error(p[2])

    def p_labeled_instr(self, p):
        """labeled_instr : ID ':' instruction """
        p[0] = AST.Labeled(p[1], p[3])
        p[3].setParent(p[0])

    def p_assignment(self, p):
        """assignment : ID '=' expression ';' """
        p[0] = AST.Assignment(p[1], p[3])
        p[3].setParent(p[0])

    def p_choice_instr(self, p):
        """choice_instr : IF '(' condition ')' instruction  %prec IFX"""
        p[0] = AST.Choice(p[3], p[5], None)
        p[3].setParent(p[0])
        p[5].setParent(p[0])

    def p_choice_instr_1(self, p):
        """choice_instr : IF '(' condition ')' instruction ELSE instruction"""
        p[0] = AST.Choice(p[3], p[5], p[7])
        p[3].setParent(p[0])
        p[5].setParent(p[0])
        p[7].setParent(p[0])

    def p_choice_instr_error(self, p):
        """choice_instr : IF '(' error ')' instruction ELSE instruction
                        | IF '(' error ')' instruction  %prec IFX"""
        self.p_error(p[3])

    def p_while_instr(self, p):
        """while_instr : WHILE '(' condition ')' instruction"""
        p[0] = AST.While(p[3], p[5])
        p[3].setParent(p[0])
        p[5].setParent(p[0])

    def p_while_instr_error(self, p):
        """while_instr : WHILE '(' error ')' instruction """
        self.p_error(p[3])

    def p_repeat_instr(self, p):
        """repeat_instr : REPEAT instructions UNTIL condition ';' """
        p[0] = AST.Repeat(p[2], p[4])
        p[2].setParent(p[0])
        p[4].setParent(p[0])

    def p_repeat_error(self, p):
        """repeat_instr : REPEAT instructions UNTIL error ';' """
        self.p_error(p[4])

    def p_return_instr(self, p):
        """return_instr : RETURN expression ';' """
        p[0] = AST.Return(p[2])
        #p[2].setParent(p[0])

    def p_continue_instr(self, p):
        """continue_instr : CONTINUE ';' """
        p[0] = AST.Keyword(p[1])

    def p_break_instr(self, p):
        """break_instr : BREAK ';' """
        p[0] = AST.Keyword(p[1])

    def p_compound_instr(self, p):
        """compound_instr : '{' declarations instructions '}' """
        p[0] = AST.CompoundInstruction(p[2], p[3])
        p[2].setParent(p[0])
        p[3].setParent(p[0])

    def p_condition(self, p):
        """condition : expression"""
        p[0] = AST.Condition(p[1])
        p[1].setParent(p[0])

    def p_int(self, p):
        """const : INTEGER"""
        p[0] = AST.Integer(p[1])

    def p_float(self, p):
        """const : FLOAT"""
        p[0] = AST.Float(p[1])

    def p_string(self, p):
        """const : STRING"""
        p[0] = AST.String(p[1])


    def p_expression_const(self, p):
        """expression : const"""
        p[0] = p[1]

    def p_expression_id(self, p):
        """expression : ID"""
        p[0] = AST.Variable(p[1])


    def p_expression(self, p):
        """expression : expression '+' expression
                      | expression '-' expression
                      | expression '*' expression
                      | expression '/' expression
                      | expression '%' expression
                      | expression '^' expression
                      | expression '|' expression
                      | expression '&' expression
                      | expression AND expression
                      | expression OR expression
                      | expression SHL expression
                      | expression SHR expression
                      | expression EQ expression
                      | expression NEQ expression
                      | expression '>' expression
                      | expression '<' expression
                      | expression LE expression
                      | expression GE expression """
        p[0] = AST.BinExpression(p[1], p[2], p[3])
        p[1].setParent(p[0])
        p[3].setParent(p[0])

    def p_expression_1(self, p):
        """expression : ID '(' expr_list_or_empty ')'"""
        p[0] = AST.Funcall(p[1], p[3])
        p[3].setParent(p[0])


    def p_expression_2(selfself, p):
        """expression : '(' expression ')'"""
        p[0] = AST.ExpressionInParentheses(p[2])
        p[2].setParent(p[0])

    def p_expression_error(self, p):
        """expression : '(' error ')'"""
        self.p_error(p[2])

    def p_expression_error_2(self, p):
        """expression : ID '(' error ')'"""
        self.p_error(p[3])

    def p_expr_list_or_empty(self, p):
        """expr_list_or_empty : expr_list"""
        p[0] = AST.ExpressionList(p[1], None)
        p[1].setParent(p[0])

    def p_expr_list_or_empty_1(self, p):
        """expr_list_or_empty : """
        p[0] = AST.Empty()

    def p_expr_list(self, p):
        """expr_list : expr_list ',' expression"""
        p[0] = AST.ExpressionList(p[1], p[3])
        p[1].setParent(p[0])
        p[3].setParent(p[0])

    def p_expr_list_1(self, p):
        """expr_list : expression"""
        p[0] = AST.ExpressionList(None, p[1])
        p[1].setParent(p[0])

    def p_fundefs(self, p):
        """fundefs : fundef fundefs"""
        p[0] = AST.FunctionDefinitions(p[1], p[2])
        p[1].setParent(p[0])
        p[2].setParent(p[0])

    def p_fundefs_1(self, p):
        """fundefs : """
        p[0] = AST.Empty()

    def p_fundef(self, p):
        """fundef : TYPE ID '(' args_list_or_empty ')' compound_instr """
        p[0] = AST.FunctionDefinition(p[1], p[2], p[4], p[6])
        p[4].setParent(p[0])
        p[6].setParent(p[0])

    def p_args_list_or_empty(self, p):
        """args_list_or_empty : args_list"""
        p[0] = AST.ArgumentList(p[1], None)
        p[1].setParent(p[0])

    def p_arg_list_or_empty_1(self, p):
        """args_list_or_empty : """
        p[0] = AST.Empty()

    def p_args_list(self, p):
        """args_list : args_list ',' arg"""
        p[0] = AST.ArgumentList(p[1], p[3])
        p[1].setParent(p[0])
        p[3].setParent(p[0])

    def p_arg_list_1(self, p):
        """args_list : arg"""
        p[0] = AST.ArgumentList(None, p[1])
        p[1].setParent(p[0])

    def p_arg(self, p):
        """arg : TYPE ID """
        p[0] = AST.Argument(p[1], p[2])
