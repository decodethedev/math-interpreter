from tokens import Token , TokenType

WHITESPACE = '\n\t '
DIGITS = ['0','1','2','3','4','5','6','7','8','9']



class Lexer:
    def __init__(self , text):
        self.text = iter(text)
        self.textoriginal = text
        self.advance()
    
    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None
    def generate_tokens(self):
        while self.current_char != None:
            if(self.current_char in WHITESPACE):
                self.advance()
            elif self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_number()
            #PLUS
            elif self.current_char == "+" or self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            #MINUS
            elif self.current_char == "-" or self.current_char == '−':
                self.advance()
                yield Token(TokenType.MINUS)
            #MULTIPLY
            elif self.current_char == "*" or self.current_char == "x" or self.current_char == '×':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            #DIVIDE
            elif self.current_char == "/" or self.current_char == ":":
                self.advance()
                yield Token(TokenType.DIVIDE)
            #PARENTHESES
            elif self.current_char == "(":
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ")":
                self.advance()
                yield Token(TokenType.RPAREN)
            #SQUARE BRACKETS
            elif self.current_char == "[":
                self.advance()
                yield Token(TokenType.L_SQUAREBRACKET)
            elif self.current_char == "]":
                self.advance()
                yield Token(TokenType.R_SQUAREBRACKET)
            #ANGLE BRACKETS
            elif self.current_char == ">" or self.current_char == '⟩':
                self.advance()
                yield Token(TokenType.L_ANGLEBRACKET)
            elif self.current_char == "<" or self.current_char == '⟨':
                self.advance()
                yield Token(TokenType.R_ANGLEBRACKET)
            else:
                raise Exception(f"Illigal character:{str(self.textoriginal).find(self.current_char)} '{self.current_char}' At '{(self.textoriginal)}'")
    def generate_number(self):
        decimal_point_count = 0
        number_string = self.current_char
        if(self.current_char == "."):
                decimal_point_count += 1
        self.advance()

        while self.current_char != None and (self.current_char == "." or self.current_char in DIGITS):
            if(self.current_char == "."):
                decimal_point_count += 1
                if(decimal_point_count > 1):
                    raise "Two '.' found in one float."
                    
            
            number_string += self.current_char
            self.advance()
        while True:
            if(number_string.startswith(".")):
                number_string = "0" + number_string
            elif(number_string.endswith('.')):
                number_string += "0"
            else:
                break
        
        if(decimal_point_count >= 1):
            return Token(TokenType.FLOAT, float(number_string))
        elif(decimal_point_count == 0):
            return Token(TokenType.INT, int(number_string))