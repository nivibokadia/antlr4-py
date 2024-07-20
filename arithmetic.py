import sys
sys.path.append(r"C:\Users\Nivi Bokadia\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\antlr4")
from antlr4 import *
from antlr4.tree.Tree import TerminalNode
from arithmeticLexer import arithmeticLexer
from arithmeticListener import arithmeticListener
from arithmeticParser import arithmeticParser

def handleExpression(expr):
    adding = True
    value = 0
    for child in expr.getChildren():
        if isinstance(child, TerminalNode):
            adding = child.getText() == "+"
        else:
            multValue = handleMultiply(child)
            if adding:
                value += multValue
            else:
                value -= multValue

    print(f"Parsed expression {expr.getText()} has value {value}")

def handleMultiply(expr):
    multiplying = True
    value = 1
    for child in expr.getChildren():
        if isinstance(child, TerminalNode):
            multiplying = child.getText() == "*"
        else:
            if multiplying:
                value *= int(child.getText())
            else:
                value //= int(child.getText())

    return value

def main():
    try:
        user_input = input("Enter an arithmetic expression: ")
        lexer = arithmeticLexer(InputStream(user_input))
        stream = CommonTokenStream(lexer)
        parser = arithmeticParser(stream)
        tree = parser.expression()
        handleExpression(tree)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()