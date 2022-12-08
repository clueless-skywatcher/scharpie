import sys

from scharpie import Scharpie
from scharpie.checkers import (
    SetDuplicateItemChecker,
    PdbSetTraceChecker,
    UnusedVariableChecker
)

def main():
    source_path = sys.argv[1]

    linter = Scharpie()
    linter.checks.add(SetDuplicateItemChecker())
    linter.checks.add(PdbSetTraceChecker())
    linter.checks.add(UnusedVariableChecker())
    linter.run(source_path)

if __name__ == '__main__':
    main()