from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter
from configs import *
while True:
    try:
        text = input("[ 'q' to quit ] MATH > ")
        if(text == 'q'): break
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        if(LEXER_DEBUG):
            print(list(tokens))
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree: continue
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        print(value)
    except Exception as e:
        print(e)