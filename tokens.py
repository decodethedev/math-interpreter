from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    #TYPES
    INT  = 0
    FLOAT  = 1
    #OPERATORS
    PLUS    = 2
    MINUS   = 3
    DIVIDE  = 4
    MULTIPLY  = 5
    #PARENTHESES
    LPAREN  = 6
    RPAREN  = 7
    #SQUARE BRACKETS
    L_SQUAREBRACKET  = 8
    R_SQUAREBRACKET  = 9
    #ANGLE BRACKETS
    L_ANGLEBRACKET  = 12
    R_ANGLEBRACKET  = 13

@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")