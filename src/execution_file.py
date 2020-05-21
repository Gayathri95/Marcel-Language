# this file will be the medium which connects all the 3 components lexer, parser and evaluator
# it will take code as input and pass it to lexer which will return stream of tokens
# then it will call the prolog DCG parser and input the list of tokens to obtain AST
# AST will then be passed to python evaluator script to display the output to user.

from pyswip import Prolog
#import main
import lexer_class
import evaluator
import os

prolog = Prolog()

#for user to input the file name
file_name = input("Enter file name :")
with open(file_name, "r") as f:
    code = f.read()
   
#splitting code into tokens 
lexer  = lexer_class.Lexer(code)

tokens = lexer.tokenize()
prolog.consult("parser_final.pl")
        
        
token_string = ""
for i in tokens:
    if i == "main":
        token_string += i
    elif i == "(" or i == ")" or i == "{" or i == "}" or i == ">" or i == "<" or i ==">=" or i =="<=" or i =="!=" or i =="==" or i == "range":
        token_string = token_string + "," + "'" + i + "'"
    elif i == "marcel":
        token_string = token_string + "," + '"' + "," + 'marcel' + "," + '"'
    else:
        token_string = token_string + "," + i
        
token_string = "[" + token_string + "]"

token_string.replace(",,", ",")

#print(token_string)


for solution in prolog.query("program(P, %s, [])." % (token_string)):
    result = solution["P"]


# for solution in prolog.query("program(P, [main,'{',int,fact,=,1,;,int,i,=,5,;,int,n,=,1,;,for,'(',n,range,i,')','{',fact,=,fact,*,n,;,'}',breakfor,;,print,'(',fact,')',;,'}',.], [])."):
#     result = solution["P"]
    
    
# # program(P,[main,'{',int,fact,=,1,;,int,i,=,5,;,int,n,=,1,;,for,'(',n,range,i,')','{',fact,=,fact,*,n,;,'}',breakfor,;,print,'(',fact,')',;,'}',.], []).

# print(result)

# result = "program(block(main(multiple_declaration(declare_variable(datatype_int, id(fact), expression_t(id(1))), multiple_declaration(declare_variable(datatype_int, id(i), expression_t(id(5))), single_declaration(declare_variable(datatype_int, id(n), expression_t(id(1)))))), multiple_command(comm_for_identifier(id(n), id(i), multiple_command(comm_assign_expression(id(fact), expression_t(mul_expr(id(fact), id(n)))), empty_command([]))), multiple_command(comm_print_expr(id(fact)), empty_command([]))))))"

evaluator_obj = evaluator.parseAST()
evaluator_obj.entry(result)