import ast

from scharpie.checkers.base import BaseChecker
from scharpie.violation import Violation

class UnusedVariableInScopeChecker(BaseChecker):
    def __init__(self) -> None:
        super(UnusedVariableInScopeChecker, self).__init__(issue_code = None)
        self.unused_vars = {}
        self.vars = {}

    def visit_Name(self, node: ast.Name):
        node_name = node.id

        if isinstance(node.ctx, ast.Store):
            if node_name not in self.vars:
                self.vars[node_name] = node
            if node_name not in self.unused_vars:
                self.unused_vars[node_name] = True
        else:
            self.unused_vars[node_name] = False

class UnusedVariableChecker(BaseChecker):
    def __init__(self) -> None:
        super(UnusedVariableChecker, self).__init__(issue_code='W002')

    def check_for_unused_vars(self, node: ast.AST):
        visitor = UnusedVariableInScopeChecker()
        visitor.visit(node)

        for name, unused in visitor.unused_vars.items():
            if unused:
                node = visitor.vars[name]
                v = Violation(node, f"Unused variable: {name}")
                self.violations.add(v)

    def visit_Module(self, node: ast.Module):
        self.check_for_unused_vars(node)
        super().generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef):
        self.check_for_unused_vars(node)
        super().generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.check_for_unused_vars(node)
        super().generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self.check_for_unused_vars(node)
        super().generic_visit(node)