# SudokuSolver
Implementation of by-hand techniques, using tree-based speculation to solve all puzzles.

Algorithms are generalized to all n^2 * n^2 puzzle sizes, but larger puzzles are extremely slow.
Apologies for lack of user-friendliness.
To operate, run SpeculationGraphicalInterface, edit the two puzzle declaration lines if there is no file-input system in place. Comment out one, edit the other.

sampleGrid(n) displays puzzles with n = 4,5,9,10
puzzleString3 is the only large puzzle that solves quickly and displays an actual tree
