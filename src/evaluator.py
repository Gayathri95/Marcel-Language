

'''

This code can be used by Arizona State University for Grading Purposes

This codebase, takes in Abstract Syntax tree and evaluates the codebase.


'''


import nltk
import nltk.tree
from nltk import *
from nltk.tree import *


#from _future_ import *
#import random



class evaluate_prefix:
    def __init__(self):
        self.items=[]
        self.size=-1
    def isEmpty(self):
        if(self.size==-1):
            return True
        else:
            return False
    def push(self,item):
        self.items.append(item)
        self.size+=1
    def pop(self):
        if self.isEmpty():
            return 0
        else:
            self.size-=1
            return self.items.pop()
    def seek(self):
        if self.isEmpty():
            return False
        else:
            return self.items[self.size]
    def evalute(self,expr):
        elist = (expr.split(' '))
        del elist[-1]
        del elist[0]
        #print(elist)
        for i in (reversed(elist)):
            #print("yoooooooo",i)
            if i.isdigit():
                self.push(i)
            elif i == ' ':
                continue
            else:
                op1=self.pop()
                op2=self.pop()
                result=self.cal(op1,op2,i)
                self.push(result)
        return self.pop()
    def cal(self,op1,op2,i):
        if i is '*':
            return int(op1)*int(op2)
        elif i is '/':
            return int(int(op1)/int(op2))
        elif i is '+':
            return int(op1)+int(op2)
        elif i is '-':
            return int(op1)-int(op2)
        elif i is '^':
            return int(op1)^int(op2)




class Program:
    instance = None
    @staticmethod
    def getInstance():
        if Program.instance == None:
            Program()
        return Program.instance
    def __init__(self):
        if Program.instance != None:
            raise Exception("This class is a singleton!")
        else:
            Program.instance = self
            self.environment = {}
            


'''

class Block(self):
    def __init__(self, block_id,var_name,value,var_type,flag,symbol_table):
        self.block_id = block_id
        self.var_name = var_name
        self.value = value
        self.var_type =  var_type
        self.flag = flag
        symbol_table = {self.var_name : {'block_id': block_id, 'val':value, 'type':var_type, 'flag':flag}}
'''

class parseAST:
    #Pobj = None
    environment = {}

    def __init__(self):
         #Pobj = Program.getInstance()
        self.environment = {}

    def update(self,varkey,value):
        #print("Updating value")
        self.environment[varkey] = value
        #print(self.environment)

    # override method

    def update_new(self,environment,varkey,value):
        environment[varkey] = value
        return environment


    # override method

    def lookup_new(self,environment, var):
        #print(environment[var])
        return environment[var]


    

    def lookup(self,var):
        #print(self.environment[var])
        return self.environment[var]

    

    def convertsymbols(self, exprstr):
        oplist = ['add_expr', 'mul_expr','sub_expr','div_expr']
        elist = exprstr.split(' ')
        #print(elist)
        for i,j in enumerate(elist):
            #print(i, j)
            if j != ' ' and j != 'id' and j != 'num':
                if j == 'add_expr':
                    elist[i] = '+'
                elif j == 'mul_expr':
                    elist[i] = '*'
                elif j == 'div_expr':
                    elist[i] = '/'
                elif j == 'sub_expr':
                    elist[i] = '-'
            if ((not(j.isdigit())) and j != ' ' and j != 'id' and (j not in oplist) and j != 'num' and j != ''):
                elist[i] = self.lookup(j)
            #print(elist)
        exprstr = ""
        for i in elist:
            if( i != ' ' and i != 'id' and i != 'num'):
                exprstr += str(i) + ' '
        #print(exprstr)
        s=evaluate_prefix()
        value=s.evalute(exprstr)
        del(s)
        #print("@@@@@@@@@@@@2Value", value)
        return value
                
        


    def process_expression(self,expr_tree):
        val = None
        oplist = ['add_expr', 'mul_expr','sub_expr','div_expr']
        #print(expr_tree)
        for tree in expr_tree.subtrees():
            if(tree.label() == "expression_t"):
                for t in tree.subtrees():
                    if(t.label() in oplist):
                        break
                    if(t.label() != "expression_t" and ((t.label() == "id" or t.label() == "num") and t.right_sibling() is None)):
                        for l in t.subtrees():
                            if(l.label().isdigit() and (l.label() != "id" and l.label() != "num")):
                                #print("Returning")
                                return int(l.label())
                            elif( (l.label() != "id" and l.label() != "num")):
                                #print("Returning2")
                                return (self.lookup(l.label()))
            elif(tree.label() in oplist):
                #print("expr", str(t))
                newstr = str(t)
                nstr = (((newstr.replace(' ','')).replace(')','')).replace('(',' ')).replace('\n','')
                #print(nstr)
                val =  self.convertsymbols(nstr)
                #print("expr val", val)
                #val = self.evaluate_expr(newstr)
                return val
        

    def iterate_and_update(self,tree):
        #print("lol life is fun")
        val = None
        var = ""
        dtype = ""
        #print("Pretty", tree.pretty_print())
        for c in tree.subtrees():
            #print("Label", c.label())
            if( c.label() == "id"):
                #print("It is id", c.label())
                for k in c.subtrees():
                    #print(k.label())
                    if( k.label() != "id"):
                        #print("sdjshdj", k.label())
                        var = k.label()
            if(c.label() == "value_num"):
                for k in c.subtrees():
                    if( k.label() != "num" and k.label() != "value_num"):
                        val = int(k.label())
                break
            if(c.label() == "value_string"):
                for k in c.subtrees():
                    if( k.label() != "id" and k.label() != "value_string"):
                        val = str(k.label())
                break
            if(c.label() == "datatype_int"):
                #print("Type", c.label())
                dtype = "int"
            if(c.label() == "datatype_str"):
                dtype = "str"
            if(c.label() == "datatype_boolean"):
                dtype = "bool"
            if(c.label() == "expression_t"):
                #print("Expression")
                val = self.process_expression(c)
                break
        if(var != ""):
            #print("variable  value", var, val)
            self.update(var,val)
            #print("What happened")

    def process_boolean(self,tree,blist,bdict):
        #print("----------------------------------------------------------------------------------------------------------")
        op = None
        val1 = None
        val2 = None
        for c in tree.subtrees():
            #print("Helooooo", c.label())
            if c.label() in blist:
                op = bdict[c.label()]
            if (c.label() == "boolean_exp_not"):
                for t in c.subtrees():
                    if(t.label() != "boolean_exp_not"):
                        val1 = self.process_boolean(t,blist,bdict)
                        return not(val1)
            if c.label() == "expression_t" and (c.right_sibling() is not None):
                #print("------------------------------------------------------------------------")
                val1 = self.process_expression(c)
                #print("Val1",val1)
                val2 = self.process_expression(c.right_sibling())
                #print("Val2", val2)
                break

        if(op == '=='):
            return (val1 == val2)
        elif(op == 'true'):
            return True
        elif(op == 'false'):
            return False
        elif(op == '!='):
            return (val1 != val2)
        elif(op == '<'):
            return (val1 < val2)
        elif(op == '<='):
            return bool(val1 <= val2)
        elif(op == '>'):
            return (val1 > val2)
        elif(op == '>='):
            return (val1 >= val2)
        elif(op == 'or'):
            return (val1 or val2)
        elif(op == 'and'):
            return (val1 and val2)
            
                
                
                    
        

    def process_if_ternary_conditional(self,tree):
        boollist = ["boolean_exp_equal", "boolean_exp_val_true", "boolean_exp_not", "boolean_exp_not_equal", "boolean_exp_lessthan", "boolean_exp_greaterthan", "boolean_exp_greaterthan_equal","boolean_exp_lesserthan_equal","boolean_exp_or","boolean_exp_and","boolean_exp_val_false"]
        booldict = {boollist[0]: '==', boollist[1]: 'true', boollist[2]: 'not', boollist[3]: '!=', boollist[4]: '<', boollist[5]:'>', boollist[6]: '>=', boollist[7]: '<=', boollist[8]: 'or', boollist[9]: 'and', boollist[10]: 'false'}
        for child in tree.subtrees():
            boolean = None
            if(str(child.label()) in boollist):
                boolean = self.process_boolean(child, boollist, booldict)
                #boolean = False
                #print("Boolean",boolean)
                if ((child.right_sibling() is not None) and boolean == True):
                    #print("if", child.right_sibling().pretty_print())
                    self.process_command(child.right_sibling())
                    return
                elif(boolean == False):
                    #print("else", child.right_sibling().pretty_print())
                    self.process_command(child.right_sibling().right_sibling())
                    return


                    
    def process_for(self,tree):
        fenv = {}
        idcount = 0
        var1 = ""
        var2 = ""
        val = 0
        rval =0
        comm = ()
        for child in tree.subtrees():
            if(child.label() == "id" and idcount == 0):
                idcount += 1
                for c in child.subtrees():
                    if(c.label() != "id"):
                        var1 = c.label()
                        val1 = self.lookup(var1)
                        fenv = self.update_new(fenv, c.label(), val)
            elif(child.label() == "id" and idcount == 1):
                idcount += 1
                for c in child.subtrees():
                    if(c.label() != "id"):
                        var2 = c.label()
                        rval = self.lookup(c.label())
                        fenv = self.update_new(fenv, c.label(), rval)
            elif(child.label() == "num" and idcount == 1):
                idcount += 1
                for c in child.subtrees():
                    if(c.label() != "num"):
                        rval = int(c.label())

            if(idcount == 2):
                comm = child.right_sibling()
                break

        i = var1
        val = val1
        #print("value 1",val1)
        for val in range(val1,rval+1,1):
            #print("For for ")
            self.update(var1,val)
            self.process_command(comm)
            newval = self.lookup(var1)
            val = newval
            #self.update_new(fenv,var1,val)
            

    def process_while(self,tree):
        boollist = ["boolean_exp_equal", "boolean_exp_val_true", "boolean_exp_not", "boolean_exp_not_equal", "boolean_exp_lessthan", "boolean_exp_greaterthan", "boolean_exp_greaterthan_equal","boolean_exp_lesserthan_equal","boolean_exp_or","boolean_exp_and","boolean_exp_val_false"]
        booldict = {boollist[0]: '==', boollist[1]: 'true', boollist[2]: 'not', boollist[3]: '!=', boollist[4]: '<', boollist[5]:'>', boollist[6]: '>=', boollist[7]: '<=', boollist[8]: 'or', boollist[9]: 'and', boollist[10]: 'false'}

        fenv = {}
        idcount = 0
        var = ""
        val = 0
        rval =0
        comm = ()
        boolean = None
        for child in tree.subtrees():
            #boolean = 0
            if(child.label() in boollist):
                boolean = child
                #boolean = True
                #print("Boolean",boolean)
                if ((child.right_sibling() is not None)):
                    #print("if", child.right_sibling().pretty_print())
                    comm = child.right_sibling()
                break
        while(self.process_boolean(boolean,boollist,booldict)):
            #print("Again")
            self.process_command(comm)
            #print("REturn again")
        return


    def process_main(self,c):
        #print("process main")
        for child in c.subtrees():
            if(child.label() != "main"):
                while(child is not None):
                    #print("multiple declaration")
                    if child.label() == "multiple_declaration" or child.label() == "single_declaration":
                        #print("Calling multiple declaration")
                        self.process_declaration(child)
                        #print("Right sibling")
                        child = child.right_sibling()
                        #print(child.pretty_print())
                    if child.label() == "multiple_command" or child.label() == "single_command":
                        #print("multiple_command")
                        self.process_command(child)
                        child = child.right_sibling()
                    if (child is not None) and child.label() == "empty_command":
                        break
                #print("Breaking")
                return
            #if child.label() == "mutiple_command":
            #    self.process_multiple_command(child)
        #print(self.environment)

 

    def process_command(self,tree):
        flag = 0
        eflag = 0
        #print("Treeeeee")
        #print(tree.pretty_print())
        for c in tree.subtrees():
            if(c.label() != "multiple_command" and c.label() != "single_command"):
                #print(c.label())
                #print("While in command")
                #print(c.pretty_print())
                while(c is not None):
                    flag = 0
                    eflag = 0
                    #print("Whileeee", c.label())
                    if c.label() == "empty_command":
                        c = None
                        eflag = 1
                        #print("Breaking")
                        break
                    if ( (c != None) and c.label() == "comm_assign_expression"):
                        #print("Come in ")
                        var = None
                        val = None
                        flag1 = 0
                        for t in c.subtrees():
                            if(t.label() == "id"):
                                for l in t.subtrees():
                                    if(l.label() != "id"):
                                        var = l.label()
                            if(t.label() == "expression_t"):
                                #print("EXPPPPRRRRRRRRR", t.pretty_print())
                                val = self.process_expression(t)
                                self.update(var,val)
                        c = c.right_sibling()
                        if(c == None):
                            break
                        #return
                    if ( (c is not None) and c.label() == "comm_for_identifier"):
                        #print("calling for")
                        self.process_for(c)
                        c = c.right_sibling()
                        if(c == None):
                            break
                    if (( c is not None ) and c.label() == "comm_while_do"):
                        #print("Calling while")
                        self.process_while(c)
                        c = c.right_sibling()
                        if(c == None):
                            break
                    if ((c is not None) and (c.label() == "comm_if_then_else") or (c.label() == "comm_ternary")):
                        #print("calling if ")
                        self.process_if_ternary_conditional(c)
                        c = c.right_sibling()
                        if(c == None):
                            break
                    if (( c is not None) and c.label() == "comm_print_expr"):
                        for ctree in c.subtrees():
                            if ctree.label() == "str_identifier":
                                for l in ctree.subtrees():
                                    if(l.label() != "id" and l.label() != "str_identifier"):
                                           print((l.label()))
                                           flag = 1
                                           break
                            elif ctree.label() == "expression_t":
                                for l in ctree.subtrees():
                                    if(l.label() != "id" and l.label() != "expression_t"):
                                           print(self.lookup(l.label()))
                                           flag = 1
                                           break
                            elif ctree.label() == "id":
                                for l in ctree.subtrees():
                                    if(l.label() != "id"):
                                           print(self.lookup(l.label()))
                                           flag = 1
                                           break
                                
                            if(flag == 1):
                                break
                        c = c.right_sibling()
                    if ( (c is not None )and (c.label() == "multiple_command" or c.label() == "single_command")):
                        self.process_command(c)
                        c = c.right_sibling()
                        if(c == None):
                            break
                    if ( (c is not None) and c.label() == "value_num"):
                        for ctree in c.subtrees():
                            if ctree.label() == "num":
                                for l in ctree.subtrees():
                                    if(l.label() != "num"):
                                        print(l.label())
                                        break
                                        flag = 1
                            if(flag == 1):
                                break
                        c = c.right_sibling()
                        if(c == None):
                            break
                if (eflag == 1):
                    #print("Break and return")
                    break
                return                       

    

    def process_declaration(self,dtree):
        #print("Process declaration")
        count = 0
        c = ()
        for t in dtree.subtrees():
            if(t.label() != "multiple_declaration" and t.label() != "single_declaration"):
                c = t
                while(c is not None):
                    if ((c.label() == "single_declaration" and c.right_sibling() is None) or c.label() == "define_variable" or c.label() == "declare_variable") :
                        self.process_single_dec(c)
                        #print("Here at declaration")
                        if(c.right_sibling() is not None):
                            #print("There")
                            c = c.right_sibling()
                        else:
                            #print("Not there")
                            break
                    if ((c is not None) and c.label() == "multiple_declaration"):
                        #print("Process declaration")
                        self.process_declaration(c)
                        c = c.right_sibling()
                    if(c is not None and (c.label() == "multiple_command" or c.label() == "single_command")):
                        self.process_command(c)
                        c = c.right_sibling()
                    if(c is None):
                        break
                return
                
    
    def process_single_dec(self,ctree):
        for child in ctree.subtrees():
            if child.label() == "declare_variable" or child.label() == "declare_assign_number" or child.label() == "define_variable":
                #print(child.pretty_print())
                self.iterate_and_update(child)
                return

    def start_parsing(self,program):
        #print("Start parse")
        expr_tree = ParentedTree.fromstring(program)
        for mtree in expr_tree.subtrees():
            #print(mtree.label())
            if mtree.label() == "program":
                #print("program")
                for ctree in mtree.subtrees():
                    if ctree.label() == "block":
                        #print("Block")
                        self.block(ctree)

    def block(self,mtree):
        for c in mtree.subtrees():
            if c.label() == "main":
                #print("main")
                self.process_main(c)

        #print(self.environment)
                    
        
        
    '''    
    def ret_terminal(self,data):
        return data

    def dec_var(self,data):
        Pobj.symbol_table.var_name = data.varname

        '''


    def entry(self, example_expr):
       # print(example_expr)
        temp = '(' + example_expr + ')'
        example = temp.replace(', ', ")(")
        program = example
        #print(program)
        self.start_parsing(program)
        
        