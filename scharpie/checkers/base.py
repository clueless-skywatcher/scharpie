import ast

class BaseChecker(ast.NodeVisitor):
    def __init__(self, issue_code) -> None:
        self.issue_code = issue_code
        self.violations = set()