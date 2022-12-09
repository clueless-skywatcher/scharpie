import ast

from scharpie.checkers import BaseChecker
from scharpie.violation import Violation

class UnreachableCodeChecker(BaseChecker):
    '''
    WC001: Unreachable code (Code after a 'return' or 'raise')
    '''
    def __init__(self):
        super(UnreachableCodeChecker, self).__init__(issue_code='WC001')

    def check_for_code_after_raise_return(self, node: ast.AST):
        mark_end = False
        for elem in node.body:
            if isinstance(elem, (ast.Raise, ast.Return)):
                mark_end = True
                continue
            if mark_end:
                violation = Violation(elem, "Unreachable code")
                self.violations.add(violation)
    
    def visit_Module(self, node: ast.Module):
        self.check_for_code_after_raise_return(node)
        super().generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.check_for_code_after_raise_return(node)
        super().generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef):
        self.check_for_code_after_raise_return(node)
        super().generic_visit(node)

    def visit_For(self, node: ast.For):
        self.check_for_code_after_raise_return(node)
        super().generic_visit(node)

    def visit_If(self, node: ast.If):
        self.check_for_code_after_raise_return(node)
        super().generic_visit(node)

    def visit_While(self, node: ast.While):
        self.check_for_code_after_raise_return(node)
        super().generic_visit(node)
