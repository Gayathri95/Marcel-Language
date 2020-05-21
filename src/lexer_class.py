import re

#lexer class for all the operations on the code
#this class is used to tokenize the input code

class Lexer(object):
    
    def __init__(self, code):
        self.code = code
        self.list_of_tokens = []
        
    def tokenize(self):
        
        code = self.code.split()
        index_in_code = 0
        
        while index_in_code < len(code):
            
            token = code[index_in_code]
            if token in ["int","bool","str", "const", "main"]:
                token_found = self.check_parantheses(token)
                token_found_curly = self.check__curly_braces(token)
                
                if token_found == False and token_found_curly == False:
                    self.list_of_tokens.append(token)
                                
            elif re.match('[a-z]', token) or re.match('[A-Z]', token):
                
                token_found = self.check_parantheses(token)
                token_found_curly = self.check__curly_braces(token)
                
                if token_found == False and token_found_curly == False:
                    self.list_of_tokens.append(token)
                
            elif token in ["{","}", "(", ")"]:
                self.list_of_tokens.append(token)
                
            elif re.match('[0-9]', token):
                token_found = self.check_parantheses(token)
                token_found_curly = self.check__curly_braces(token)
                
                if token_found == False and token_found_curly == False:
                    self.list_of_tokens.append(token)
                
            elif token in ["+", "-", "*", "/", "?", ":", ":=", "="]:
                token_found = self.check_parantheses(token)
                token_found_curly = self.check__curly_braces(token)
                
                if token_found == False and token_found_curly == False:
                    self.list_of_tokens.append(token)
            
            elif token in ["true", "false", "not", "and", "or"]:
                token_found = self.check_parantheses(token)
                token_found_curly = self.check__curly_braces(token)
                
                if token_found == False and token_found_curly == False:
                    self.list_of_tokens.append(token)
                
            elif token in [">", "<", ">=", "<=", "!=", ";"]:
                token_found = self.check_parantheses(token)
                token_found_curly = self.check__curly_braces(token)
                
                if token_found == False and token_found_curly == False:
                    self.list_of_tokens.append(token)
                
            elif token in ["sum", "avg", "count", "length", "print"]:
                token_found = self.check_parantheses(token)
                token_found_curly = self.check__curly_braces(token)
                
                if token_found == False and token_found_curly == False:
                    self.list_of_tokens.append(token)
                
            elif token in ["if", "then", "else", "breakif", "do", "while", "breakwhile"]:
                token_found = self.check_parantheses(token)
                token_found_curly = self.check__curly_braces(token)
                
                if token_found == False and token_found_curly == False:
                    self.list_of_tokens.append(token)
            
            elif token in ["for", "range", "breakfor"]:
                token_found = self.check_parantheses(token)
                token_found_curly = self.check__curly_braces(token)
                
                if token_found == False and token_found_curly == False:
                    self.list_of_tokens.append(token)
                
            elif token[0] == '(' or token[0] == '{' or token[len(token) - 1] == ")" or token[len(token) - 1] == "}":
                token_found = self.check_parantheses(token)
                token_found_curly = self.check__curly_braces(token)
                
                if token_found == False and token_found_curly == False:
                    self.list_of_tokens.append(token)
                
            index_in_code = index_in_code + 1
            
        self.list_of_tokens.append('.')
            
        return self.list_of_tokens
        
    def get_tokens(self):
        return self.list_of_tokens
        
    def check_parantheses(self, token):
        check = False
        if "(" in token and ")" in token:
            open_index = token.find("(")
            close_index = token.find(")")
            
            self.list_of_tokens.append(token[0:open_index])
            self.list_of_tokens.append('(')
            self.list_of_tokens.append(token[open_index+1 : close_index])
            self.list_of_tokens.append(')')
            
            check = True
            
        elif "(" in token:
            open_index = token.find("(")
            
            self.list_of_tokens.append(token[0:open_index])
            self.list_of_tokens.append('(')
            self.list_of_tokens.append(token[open_index+1 : ])
            
            check = True
            
        elif ")" in token:
            close_index = token.find(")")
            
            self.list_of_tokens.append(token[0:close_index])
            self.list_of_tokens.append(')')
            if (close_index != len(token)):
                self.list_of_tokens.append(token[close_index+1 : ])
            
            check = True
        
        return check
    
    def check__curly_braces(self, token):
        check = False
        if "{" in token or "}" in token:
            open_index = token.find("{")
            close_index = token.find("}")
            
            self.list_of_tokens.append(token[0:open_index])
            self.list_of_tokens.append('{')
            self.list_of_tokens.append(token[open_index+1 : close_index])
            self.list_of_tokens.append('}')
            
            check = True
            
        return check