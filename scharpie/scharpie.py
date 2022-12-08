import ast
import os

class Scharpie:
    def __init__(self) -> None:
        self.checks = set()
        self._violations = []

    def get_violations(self, file_name):
        for checker, violation in self._violations:
            print(
                f"{file_name} > Line {violation.node.lineno} > Column {violation.node.col_offset} -> "
                f"{checker.issue_code}: {violation.message}"
            )

    def run(self, source_path):
        file_name = os.path.basename(source_path)

        with open(source_path) as source_file:
            source_code = source_file.read()
        
        tree = ast.parse(source_code)

        for checker in self.checks:
            checker.visit(tree)
            self._violations.extend([(checker, v) for v in checker.violations])
        
        self._violations = sorted(self._violations, key = lambda v: v[1].node.lineno)
        self.get_violations(file_name)
