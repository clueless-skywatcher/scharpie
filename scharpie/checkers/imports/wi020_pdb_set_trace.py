import ast

from scharpie.checkers import BaseChecker
from scharpie.violation import Violation

class PdbSetTraceChecker(BaseChecker):
    '''
    WI020: Check whether there is a `pdb.set_trace()` line in the code.
    This line can halt the code in debugging mode.
    '''
    _SET_TRACE_CALL_FUNC = ast.Attribute(
        value = ast.Name(id = 'pdb', ctx = ast.Load()),
        attr = 'set_trace',
        ctx = ast.Load()
    )

    def __init__(self) -> None:
        super(PdbSetTraceChecker, self).__init__(issue_code = 'WI020')

    def visit_Expr(self, node: ast.Expr):
        if isinstance(node.value, ast.Call):
            call = node.value
            call_func = call.func
            
            if not hasattr(call_func, 'value'):
                return
            if not hasattr(call_func, 'ctx'):
                return

            if call_func.value.id == 'pdb' and \
                isinstance(call_func.value.ctx, ast.Load) and \
                call_func.attr == 'set_trace' and \
                isinstance(call_func.ctx, ast.Load):
                violation = Violation(
                    node = call,
                    message = 'pdb.set_trace() detected in code. Code may halt here'
                )

                self.violations.add(violation)
