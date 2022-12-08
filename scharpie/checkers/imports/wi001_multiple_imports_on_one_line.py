import ast

from scharpie.checkers.base import BaseChecker
from scharpie.violation import Violation

class MultipleImportsOnOneLineChecker(BaseChecker):
    '''
    WI001: Multiple imports on one line
    '''
    def __init__(self) -> None:
        super(MultipleImportsOnOneLineChecker, self).__init__(issue_code = 'WI001')
    
    def visit_Import(self, node: ast.Import):
        if len(node.names) > 1:
            violation = Violation(node, f"Multiple imports on one line")
            self.violations.add(violation)