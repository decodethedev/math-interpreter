from nodes import *
from values import *

class Interpreter:
    def __init__(self):
        pass

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)
        
    def visit_IntNode(self, node):
        return IntValue(node.value)
    def visit_FloatNode(self, node):
        return FloatValue(node.value)

    def visit_AddNode(self, node):
        if(type(node.node_a) == float):
            return FloatValue(self.visit(node.node_a).value + self.visit(node.node_b).value)
        else:
            return IntValue(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubtractNode(self, node):

        if(type(node.node_a) == float):
            return FloatValue(self.visit(node.node_a).value -  self.visit(node.node_b).value)
        else:
            return IntValue(self.visit(node.node_a).value -  self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):

        if(type(node.node_a) == float):
            return FloatValue(self.visit(node.node_a).value *  self.visit(node.node_b).value)
        else:
            return IntValue(self.visit(node.node_a).value *  self.visit(node.node_b).value)
    def visit_DivideNode(self, node):
        try:
            if(type(node.node_a) == float):
                return FloatValue(self.visit(node.node_a).value / self.visit(node.node_b).value)
            else:
                return IntValue(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error")