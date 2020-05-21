:- table expr/3, term/3.

program(program(X)) --> block(X).

block(block(X)) --> main(X),[.].
block(block(X,Y)) --> function(X),main(Y),[.].
main(main(X,Y)) --> [main], ['{'], declaration(X), command(Y), ['}'].

function(funct(W, X, Y, Z)) --> datatype(W), funcname(X), ['('], signature(Y), [')'], funcbody(Z).
funcbody(funcbody_comm(X,Y)) --> ['{'], declaration(X), command(Y), ['}'].
%funcbody(funcbody_fn_sg(X, Y)) --> funcname(X), ['('],signature(Y), [')'],[';'].
%funcbody(funcbody_declaration(X)) --> declaration(X).
%funcbody(funcbody_funct(X)) --> function(X).

funcname(func_name(X)) --> identifier(X).
%funcname(func_name_str(X)) --> string(X).

declaration(multiple_declaration(X,Y)) --> single_declaration(X), [;], declaration(Y).
declaration(single_declaration(X)) --> single_declaration(X), [;].
single_declaration(dec_assign_number(X, Y, Z)) --> [const], datatype(X), identifier(Y), [=], val(Z).
single_declaration(declare_variable( Y, Z)) --> [str], identifier(Y), ['='], val(Z).
single_declaration(declare_variable(X, Y, Z)) --> datatype(X), identifier(Y), ['='], expression(Z).
single_declaration(define_variable(X, Y)) --> datatype(X), identifier(Y).
single_declaration(declare_variable(X,Y)) --> [int], identifier(X), ['='], [vector], oneDim(Y).
single_declaration(declare_variable(X,Y)) --> [int], identifier(X), ['='], [vector], twoDim(Y).

oneDim(oneDimensionArray) --> ['1D'].
twoDim(twoDimensionArray) --> ['2D'].

datatype(datatype_int) --> [int].
datatype(datatype_boolean) --> [bool].
datatype(datatype_str) --> [str].

signature(signature_val(X)) --> val(X).
signature(empty_sig) --> [].
signature(signature_identifier(X,Y)) --> identifier(X), signature(Y).
signature(signature_identifier(X)) --> identifier(X).

command(multiple_command(X,Y)) --> single_command(X), [;], command(Y).
command(single_command(X)) --> single_command(X), [;].
command(empty_command([])) --> [].
%single_command(comm_read(X)) --> identifier(X), ['='], [userInput()].
single_command(comm_assign_expression(X,Y)) --> identifier(X), [=], expression(Y).
single_command(comm_if_then_else(X,Y,Z)) --> [if], boolean_exp(X), [then], command(Y), [else], command(Z), [breakif].
single_command(comm_while_do(X,Y)) --> [while], boolean_exp(X), [do], command(Y), [breakwhile].
single_command(comm_print_expr(X)) --> [print], ['('], val(X), [')'].
single_command(comm_print_expr(X)) --> [print], ['('], identifier(X), [')'].


single_command(comm_program(X)) --> main(X).
single_command(comm_ternary(X, Y, Z)) --> boolean_exp(X), ['?'], val(Y), [':'], val(Z).
single_command(comm_math(X)) --> math(X).
single_command(comm_math(X, Y)) --> identifier(X), ['='], math(Y).
single_command(comm_declaration(X)) --> declaration(X).
single_command(comm_for_num(X, Y, Z)) --> 
    ['for'], ['('], identifier(X), ['range'], num(Y), [')'], ['{'], command(Z), ['}'], ['breakfor'].
single_command(comm_for_identifier(X, Y, Z)) --> 
    ['for'], ['('], identifier(X), ['range'], identifier(Y), [')'], ['{'], command(Z), ['}'], ['breakfor'].

math(math_sum(X)) --> ['sum'], ['('], identifier(X), [')'].
math(math_avg(X)) --> ['avg'], ['('], identifier(X), [')'].
math(math_count(X)) --> ['count'], ['('], identifier(X), [')'].
math(math_length(X)) --> ['length'], ['('], identifier(X), [')'].

val(value_num(X)) --> num(X).
val(value_string(X)) --> string(X).
val(value_booleanexpr(X)) --> boolean_exp(X).
%val(value_expr(X)) --> expression(X).

string(str_id_num(X, Y, Z)) --> ['"'], string(X), identifier(Y), num(Z), ['"'].
string(str_id(X, Y)) --> ['"'], string(X), identifier(Y), ['"'].
string(str_num(X, Y)) --> ['"'], string(X), num(Y), ['"'].
string(str_identifier(X)) --> ['"'], identifier(X), ['"'].
%string(str_identifier(X)) --> identifier(X).

boolean_exp(boolean_exp_not(X)) --> ['not' ], boolean_exp(X).
boolean_exp(boolean_exp_val_true(true)) --> [true].
boolean_exp(boolean_exp_val_false(false)) --> [false].
boolean_exp(boolean_exp_equal(X,Y)) --> expression(X), ['=='], expression(Y).
boolean_exp(boolean_exp_not_equal(X,Y)) --> expression(X), ['!='], expression(Y).
boolean_exp(boolean_exp_lessthan(X,Y)) --> expression(X), [<], expression(Y).
boolean_exp(boolean_exp_greaterthan(X,Y)) --> expression(X), [>], expression(Y).
boolean_exp(boolean_exp_greaterthan_equal(X,Y)) --> expression(X), [>=], expression(Y).
boolean_exp(boolean_exp_lesserthan_equal(X,Y)) --> expression(X), [<=], expression(Y).
boolean_exp(boolean_exp_or(X,Y)) --> expression(X), ['or'], expression(Y).
boolean_exp(boolean_exp_and(X,Y)) --> expression(X), ['and'], expression(Y).

expression(assign_multiple_expression(X,Y)) --> identifier(X), [=], expression(Y).
expression(expression_t(X)) --> expr(X).

expr(add_expr(X,Y)) --> expr(X), [+], term(Y).
expr(sub_expr(X,Y)) --> expr(X), [-], term(Y).
expr(X) --> term(X).

term(mul_expr(X,Y)) --> term(X), [*], term_bracket(Y).
term(div_expr(X,Y)) --> term(X), [/], term_bracket(Y).
term(X) --> term_bracket(X).

term_bracket(bracket_expr(X)) --> ['('], expression(X), [')'].
term_bracket(X) --> identifier(X).
term_bracket(X) --> num(X).

identifier(id(I)) --> [I], {atomic(I)}.


num(num(X)) --> [X], {number(X)}.

boolean_exp_value(boolean_value_true) --> [true].
boolean_exp_value(boolean_value_false) --> [false].