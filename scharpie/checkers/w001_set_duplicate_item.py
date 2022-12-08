import ast

from scharpie.checkers import BaseChecker
from scharpie.violation import Violation

class SetDuplicateItemChecker(BaseChecker):
    '''
    W001: Check whether a duplicate item is being used in a set
    '''
    def __init__(self) -> None:
        super(SetDuplicateItemChecker, self).__init__(issue_code='W001')

    def visit_Set(self, node: ast.Set):
        seen = set()

        for element in node.elts:
            if not isinstance(element, ast.Constant):
                continue
            
            value = element.value
            if value in seen:
                violation = Violation(
                    node = element,
                    message = f"Set contains duplicate item: {value!r}"
                )
                self.violations.add(violation)
            else:
                seen.add(element.value)
