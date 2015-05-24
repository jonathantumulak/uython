from pyparsing import Word, Group, ZeroOrMore, OneOrMore, Literal, alphanums, alphas, printables

class MyHL(object):
    def __init__(self):
        identifier = Word(alphas + alphanums)
        identifier_list = identifier + ZeroOrMore(Word(',') + identifier)
        self.number_exp = Group(Word(alphanums) + OneOrMore(Word("+-/*%", exact=1) + Word(alphanums)))
        expression = self.number_exp | Group(Literal('"') + Word(printables, excludeChars='"') + Literal('"')) | identifier
        datatype = Literal('number') | Literal('word')
        self.print_statement = "print" + identifier + ";"
        self.read_statement = "read" + identifier + ";"
        self.assignment_statement = identifier + "=" + expression + ";"
        self.variable_declaration = identifier_list + "use as" + datatype + ";"
        self.variable_stack = {}

        # with open('input.uy', 'r') as inputFile:
        #     code = [i.strip() for i in inputFile.readlines()]

        # self.run(code)

    def run(self, code, parent=None):

        code = self.clean_code(code)

        if code[0] != "begin vars":
            print "Code should begin with 'begin vars' statement."
            err_line = -1
        elif code[-1] != "end vars" and code[-1] != "end statements":
            print "Code should end with 'end vars' or 'end statements' statement."
            err_line = -1
        else:
            end_vars = False
            begin_stmt = False
            for i in code[1:-1]:
                if not i.startswith('//'):
                    if i == "end vars":
                        end_vars = True
                    elif i == "begin statements":
                        if end_vars:
                            var_type = "program"
                            begin_stmt = True
                        else:
                            print "Formal declaration of variables must end with 'end vars' statement."
                            err_line = -1
                            break
                    elif end_vars and not begin_stmt:
                        print "Program statements should begin with 'begin statements' statement."
                        err_line = -1
                        break
                    else:
                        success, err_code = self.check_and_execute(i, begin_stmt, parent)
                        if not success:
                            if err_code == 1:
                                print "Syntax Error at line ", code.index(i) + 1
                                err_line = code.index(i)
                            elif err_code == 2:
                                print "Undeclared variable at line ", code.index(i) + 1
                                err_line = code.index(i)
                            elif err_code == 3:
                                print "Type mismatch error at line ", code.index(i) + 1
                                err_line = code.index(i)
                            elif err_code == 4:
                                print "Execution halted at line ", code.index(i) + 1
                                err_line = code.index(i)
                            break

        if err_line >= 0:
            print err_line
            parent.setLineFormat(err_line)

    def check_and_execute(self, statement, begin_stmt, parent=None):
        if not begin_stmt:
            try:
                variables = self.variable_declaration.parseString(statement, parseAll=True)[0::2]
                for v in variables[:-1]:
                    self.variable_stack[v] = [None, variables[-1]]
            except:
                return False, 1
        else:
            if statement.startswith('print'):
                try:
                    identifier = self.print_statement.parseString(statement, parseAll=True)[1]
                    if identifier in self.variable_stack:
                        print self.variable_stack[identifier][0]
                    else:
                        return False, 2
                except:
                    return False, 1
            elif statement.startswith('read'):
                try:
                    identifier = self.read_statement.parseString(statement, parseAll=True)[1]
                    if identifier in self.variable_stack:
                        if self.variable_stack[identifier][1] == 'number':
                            val, ok = parent.getInt(identifier)
                        else:
                            val, ok = parent.getString(identifier)

                        # if not parent:
                        #     self.variable_stack[identifier][0] = raw_input("enter value for variable %s:" % identifier )
                        # else:
                        
                        if ok:
                            self.variable_stack[identifier][0] = val
                        else:
                            return False, 4
                    else:
                        return False, 2
                except:
                    return False, 1 
            else:
                try:
                    ass_stmt = self.assignment_statement.parseString(statement, parseAll=True)
                    try: 
                        self.number_exp.parseString("".join(ass_stmt[-2]), parseAll=True)
                        for i,v in enumerate(ass_stmt[-2]):
                            if not v in ['+', '-', '/' , '*', '%']:
                                try:
                                    int(v)
                                except:
                                    if v in self.variable_stack:
                                        ass_stmt[-2][i] = str(self.variable_stack[v][0])
                                    else:
                                        return False, 2
                        expression = self.arithmetic_ops("".join(ass_stmt[-2]))
                    except:
                        expression = ass_stmt[-2]
                    finally:
                        if not ass_stmt[0] in self.variable_stack:
                            return False, 2

                        if self.variable_stack[ass_stmt[0]][1] == 'number':
                            try:
                                self.variable_stack[ass_stmt[0]][0] = int(expression)
                            except:
                                return False, 3
                        else:
                            if expression[0] == '"' and expression[-1] == '"':
                                self.variable_stack[ass_stmt[0]][0] = expression[1]
                            else:
                                return False, 3

                except:
                    return False, 1 

        return True, 0


    def arithmetic_ops(self, statement):
        return eval(statement)

    def clean_code(self, code):
        ccode = []
        for c in code:
            if not c.startswith('//') and c != '':
                ccode.append(c.split('//')[0].strip())
            else:
                ccode.append(c)

        return ccode


# test = MyHL()
