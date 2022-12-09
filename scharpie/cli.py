import sys
from typing import Sequence

from scharpie import Scharpie
from scharpie.checkers.code_styling import (
    UnreachableCodeChecker
)
from scharpie.checkers.imports import (
    MultipleImportsOnOneLineChecker,
    PdbSetTraceChecker
)
from scharpie.checkers.variables import (
    SetDuplicateItemChecker, 
    UnusedVariableChecker
)

def cli(argv: Sequence[str] = sys.argv):
    source_paths = argv[1:]

    for path in source_paths:
        linter = Scharpie()

        linter.add_checker(SetDuplicateItemChecker()) 
        linter.add_checker(UnusedVariableChecker())
        linter.add_checker(PdbSetTraceChecker())
        linter.add_checker(MultipleImportsOnOneLineChecker())
        linter.add_checker(UnreachableCodeChecker())

        linter.run(path)
    