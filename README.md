# SudokuSolver
Implementation of by-hand techniques, using tree-based speculation to solve all puzzles. This puzzle is

Algorithms are generalized to all n^2 * n^2 puzzle sizes, but larger puzzles are extremely slow.
Apologies for lack of user-friendliness.

To operate, run SpeculationGraphicalInterface, edit the two puzzle declaration lines if there is no file-input system in place. Comment out one, edit the other.

sampleGrid(n) displays puzzles with n = 4,5,9,10

puzzleString3 is the only large puzzle that solves quickly and displays an actual tree

When the window comes up, click on each node to show that node's progress. Different color codings depict the heuristic that placed that particular number, as shown by the legend below.

Green Nodes are on the solution-path, blue nodes are invalid, but non-contradictory puzzles, and red nodes are invalid contradictory puzzles. 

# General Solving Strategy

The algorithms implemented are divided into two categories: solving and analysis. The solving functions iterate through quick and simple
heuristics to place valid numbers. The analysis functions iterate through more computationally complex algorithms to generate better data
and refine the data structures the solving algorithms utilize. The puzzle solver begins by iterating through the fastest algorithms until
no changes have been made. Then, it begins using higher-tiered analysis functions to make progress on the puzzle. Very easy puzzles do not require these higher level analyses, but more complex puzzles do. So, ultimately, the puzzle only uses the tools it needs to solve the puzzle, leading to the most efficient solving strategy relative to current algorithm efficiency.
