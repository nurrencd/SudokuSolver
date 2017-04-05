import time
'''
Created on Jun 12, 2016
@author: nurrencd
'''

def main():
    beginning()

def mainSolve(puzzle):
#     print("Attempting to solve this puzzle:\n")
    start = time.time()
#     puzzle.printGrid()
#     print()
    success = puzzle.solve(0)
    print(success)
#     puzzle.printHints()
#     puzzle.printBlockedHints()
#     print(puzzle.pairs)
    end = time.time()
    totalTime = (end - start) // .0001 / 10000
#     print("Took about " + str(totalTime) + " seconds.")
    return [success, totalTime]


def beginning():
    choice = int(input("Enter 0 for own puzzle, 1 for preset, and 2 for text file testing: "))
    if choice == 1:
        i = int(input("Puzzle number?"))
        puzzle = SudokuGrid(sampleGrid(i))
        mainSolve(puzzle)
    elif choice == 2:
        puzzles = textFilePuzzleParsing()
        textFileSolver(puzzles)
    else:
        puzzle = SudokuGrid(getGrid())
        mainSolve(puzzle)

def getGrid():
    sudokuGrid = []
    for k in range(9):
        row = input(("Enter row " + str(k + 1) + ": "))
        sudokuGrid.append(parseRow(row))
    return sudokuGrid

def parseRow(input):
    row = []
    input = input.lstrip()
    if (len(input) == 9):
        for k in range(9):
            if input[k] != "0":
                row.append(int(input[k]))
            else:
                row.append(None)
    else:
        return None
    return row

def textFilePuzzleParsing():
    filepath = "C:\EclipseWorkspaces\csse120\Random Stuff\src\SudokuSolver\\"
    file = ""
    choice = int(input("Enter one of [1,2]"))
    if choice == 1:
        file += "Easy.txt"
    elif choice == 2:
        file += "2365HardPuzzles.txt"
    else:
        pass
    puzzleFiles = open(filepath + file, 'r').read()
    puzzleArray = puzzleFiles.split('\n')
    puzzles = []
    for k in range(10):  # len(puzzleArray)):
        puzzle = textPuzzleParse(puzzleArray[k])
        sudokuPuzzle = SudokuGrid(puzzle)
        puzzles.append(sudokuPuzzle)
    return puzzles

def textFileSolver(puzzles):
    attempted = 0
    solved = 0
    time = 0
    shortestTime = 1
    longestTime = 0

    for k in range(len(puzzles)):
        # gets data from solve function
        # [solved bool, time taken]
        data = mainSolve(puzzles[k])
        attempted += 1
        print(data[0])
        if data[0] == True:
            solved += 1
        time += data[1]
        if data[1] < shortestTime:
            shortestTime = data[1]
        if data[1] > longestTime:
            longestTime = data[1]
        print("Puzzle " + str(k + 1) + " took " + "{0:.4f}".format(data[1]) + " ms.")

    print("Success rate: " + str(solved) + " of " + str(attempted))
    print("Total time: " + "{0:.4f}".format(time) + "ms")
    print("Shortest time taken: " + "{0:.4f}".format(shortestTime))
    print("Longest time taken: " + "{0:.4f}".format(longestTime))
    print("Average time taken: " + "{0:.4f}".format(time / attempted))

def textPuzzleParse(line):
    puzzle = []
    for k in range(9):
        row = []
        for j in range(9):
            char = line[k * 9 + j]
            if char == ".":
                row.append(None)
            else:
                row.append(int(char))
        puzzle.append(row)
    return puzzle

def trioIsolationSolve(puzzle):
    changed = False
    for num in range(1, 10, 1):
        for k in range(9):
            if puzzle.boxHas(k, num) == False:
                if puzzle.getBoxHintCount(k, num) == 3:
                    for num2 in range(num + 1, 10, 1):
                        if puzzle.getBoxHintCount(k, num2) == 3 and puzzle.boxHas(k, num2) == False:
                            for num3 in range(num2 + 1, 10, 1):
                                if puzzle.getBoxHintCount(k, num3) == 3 and puzzle.boxHas(k, num3) == False:
                                    print("Got here with " + str(num) + " " + str(num2) + " " + str(num3))
                                    list1 = puzzle.getHintLocation(k, num)
                                    list2 = puzzle.getHintLocation(k, num2)
                                    list3 = puzzle.getHintLocation(k, num3)
                                    if puzzle.compareHintLocations(list1, list2) and puzzle.compareHintLocations(list2, list3):
                                        if not puzzle.checkTrio([num, num2, num3], k):
                                            puzzle.blockHint(k, [num, num2, num3], list1)
                                            changed = True
                                            print("trio isolated")
                                            puzzle.update()
    return changed


def specificRowColSolve(puzzle):
    # TODO: rewrite this piece of crap
    changed = 0
    # generate location array per each row
    for row in range(9):
#         print("ITERATION " + str(row))
        locArray = []
        for num in range(1, 10, 1):
            spots = []
            if not puzzle.rowHas(row, num):
                for loc in range(9):
                    if puzzle.grid[row][loc] == None:
                        spots.append(loc)
#             print(num, end=": ")
#             print(spots, end=", ")

            locArray.append(spots)
            # reduces the list to possible locations
            # k is row number

#             print(locArray[num - 1])
            if puzzle.rowHas(row, num) == False:
#                 puzzle.printGrid()
#                 numsToRemove = []
#                 for spot in locArray[num - 1]:
#                     if puzzle.colHas(spot, num) or puzzle.boxHas((row // 3) * 3 + spot // 3, num):
#                         print("appending! " + str(spot) + " to " + str(num) + "'s list")
#                         numsToRemove.append(spot)
#                 print(locArray[num - 1])
#                 print(numsToRemove)
#                 for num2 in numsToRemove:
#                     if numsToRemove.count(num2) > 1:
#                         for k in range(numsToRemove.count(num2) - 1):
#                             numsToRemove.remove(num2)
#                 for num3 in numsToRemove:
#                     locArray[num - 1].remove(num3)
#                 print(locArray[num - 1])
                if len(locArray[num - 1]) == 1:
#                     print("\n\n\n")
#                     print("ROW SOLVER ACTUALLY DID SOMETHING")
#                     print("\n\n\n")
#                     puzzle.grid[row][locArray[num - 1][0]] == num
                    puzzle.placeNumber(row, locArray[num - 1][0], num)
#                     puzzle.update()
#                     print()
#                     puzzle.printGrid()
                    changed += 1
#                 print()
    # generate location array per each column
    for k in range(9):
        locArray = []
        for num in range(1, 10, 1):
            spots = []
            for loc in range(9):
                if puzzle.grid[loc][k] == None:
                    spots.append(loc)
            locArray.append(spots)
        # reduces the list to possible locations
        # k is column number
            if puzzle.colHas(k, num) == False:
                numsToRemove = []
                for spot in locArray[num - 1]:
                    if puzzle.rowHas(spot, num) or puzzle.boxHas((k // 3) * 3 + spot // 3, num):
                        numsToRemove.append(spot)
                    if puzzle.boxHas((k // 3) * 3 + spot // 3, num):
                        if numsToRemove.count(num) == 0:
                            numsToRemove.append(spot)
                for num2 in numsToRemove:
                    if numsToRemove.count(num2) > 1:
                        for k in range(numsToRemove.count(num2) - 1):
                            numsToRemove.remove(num2)
                for newNum in numsToRemove:

                    locArray[num - 1].remove(newNum)
                if len(locArray[num - 1]) == 1:
#                     print(locArray[num - 1][0])
#                     print(str(k))
#                     print("HIT A SUCCESSFUL VALUE:" + str(num))
#                     puzzle.grid[k][locArray[num - 1][0]] == num
                    puzzle.placeNumber(k, locArray[num - 1][0], num)
#                     puzzle.update()
#                     puzzle.printGrid()
                    changed += 1
    return changed


def printGrid(puzzleArray):
    for k in range(9):
        string = ""
        for j in range(9):
            if puzzleArray[k][j] != None:
                string += str(puzzleArray[k][j])
            else:
                string += "*"
            if j == 2 or j == 5:
                string += " | "
            else:
                string += " "
        print(string)
        if k == 2 or k == 5:
            print("- - - | - - - | - - -")


def sampleGrid(num):
    if num == 0:
        return [[9, 5, None, None, 4, 8, None, None, 2],
                [None, None, 1, None, 3, 5, 4, None, None],
                [None, None, None, 2, None, None, None, None, None],
                [2, 3, None, None, None, 7, 6, 5, None],
                [7, None, None, 5, 1, 2, None, None, 8],
                [None, 4, 5, 6, None, None, None, 7, 9],
                [None, None, None, None, None, 6, None, None, None],
                [None, None, 6, 1, 5, None, 7, None, None],
                [3, None, None, 8, 7, None, None, 1, 6]]
    elif num == 1:
        return [[1, None, 8, None, 6, None, 7, 4, None],
                [None, 9, 5, None, 4, None, None, None, 8],
                [None, None, 7, None, None, None, 9, None, None],
                [5, 7, 6, None, None, 3, None, None, None],
                [None, None, None, None, 5, None, None, None, None],
                [None, None, None, 9, None, None, 4, 6, 5],
                [None, None, 4, None, None, None, 6, None, None],
                [7, None, None, None, 1, None, 3, 2, None],
                [None, 6, 2, None, 9, None, 5, None, 7]
                ]
    elif num == 2:
        return [[None, 7, None, 8, None, 2, None, None, None],
                [None, None, None, None, None, None, None, None, 7],
                [1, 4, 8, 3, 5, None, None, None, None],
                [None, None, 5, None, None, 8, 3, None, None],
                [None, 6, None, None, None, None, None, None, 9],
                [3, None, None, None, None, None, 7, None, None],
                [5, None, None, None, None, None, 1, 7, None],
                [None, None, 4, None, 9, None, None, None, None, None],
                [None, None, 7, 4, None, None, None, None, 2]
                 ]

    elif num == 3:
        return [[None, None, None, None, None, None, None, None, 2],
                [None, None, None, None, None, None, 2, None, 2],
                [None, None, None, None, None, None, 2, 2, 2],
                [None, None, None, None, None, None, 2, 2, 2],
                [None, None, None, None, None, None, 2, 2, 1],
                [None, None, None, None, None, None, 2, 2, 2],
                [None, None, None, None, None, 1, None, None, 2],
                [None, None, None, None, None, None, 2, None, 2],
                [None, None, None, None, None, None, 2, None, None]
                ]
    elif num == 4:
        return [[1, None, None, None, 8, None, None, None, 9],
                [None, 4, None, 2, None, 3, None, 1, None],
                [None, None, 2, None, None, None, 3, None, None],
                [None, 9, None, 6, None, 7, None, 3, None],
                [7, None, None, None, None, None, None, None, 6],
                [None, 5, None, 3, None, 4, None, 7, None],
                [None, None, 5, None, None, None, 7, None, None],
                [None, 2, None, 9, None, 1, None, 4, None],
                [3, None, None, None, 6, None, None, None, 2]]
    elif num == 5:
        return [[3, None, None, None, None, 1, None, None, None],
                [None, None, 4, 9, 7, None, None, None, None],
                [None, None, 6, None, None, None, None, 4, 7],
                [4, None, None, 1, None, 8, None, None, 3],
                [None, None, None, None, 2, None, None, None, None],
                [1, None, None, 7, None, 3, None, None, 6],
                [2, 3, None, None, None, None, 9, None, None],
                [None, None, None, None, 3, 2, 8, None, None],
                [6, None, None, None, None, None, None, None, 5]]
    elif num == 6:
        return [[1, 2, 3, None, None, 9, 7, 8, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, 5, 4, None, None, None, 6],
                [None, None, None, 4, None, None, None, None, 5],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None]
                ]

class SudokuGrid(object):

    def __init__(self, grid):
        self.grid = grid
        self.boxes = self.getBoxes()
        self.blockedHints = self.createBlockedHints()
        self.hints = self.getHints()
        self.pairs = []
        self.trios = []
#         self.boxHints = self.getBoxHints()
    # -----------------------------------------------------------
    # ----------------------SOLVE FUNCTIONS----------------------
    # -----------------------------------------------------------
    # TODO: solve
    def solve(self, stage):
        maxStage = 4
        i = 0
#         print("Initializing Stage " + str(stage) + "...\n")

        if stage >= 4:
            specificRowColSolve(self)
#             self.specificRowColSolve()
        if stage >= 3:
            while (self.twinIsolationSolve() != False):
                i += 1
        if stage >= 2:
            pass
            hiddenRows = self.hiddenRowColSolve()
            if hiddenRows:
                i += 1
        if stage >= 1:
            while (self.hintSolve() != 0):
                i += 1
        if stage >= 0:

            while (self.hintSolveTwo() != 0):
                i += 1
    #     triplets = self.trioIsolationSolve()
    #     print(triplets)
#         print(str(i) + " effective iterations...\n")
#         self.printGrid()
        if i == 0:
            if self.isComplete():
                print("Puzzle Solved!")
#                 self.printGrid()

                return True
            elif stage > maxStage:
                print("Puzzle is impossible with current algorithms.")
#                 print("Current progress:\n")
#                 self.printGrid()
                return False
            else:
                self.solve(stage + 1)
        else:
            self.solve(stage)


    def hintSolve(self):
        count = 0
        for k in range(9):
            for j in range(9):
                if self.hints[k][j] != None and len(self.hints[k][j]) == 1:
                    if self.grid[k][j] == None:
                        self.placeNumber(k, j, self.hints[k][j][0])
        #                 puzzle.grid[k][j] = puzzle.hints[k][j][0]
        #                 puzzle.update()
                        count += 1
    #                     print(puzzle.hints[k][j])
    #                     printGrid(puzzle.grid)
    #                     print()
        return count

    def hintSolveTwo(self):
        # checks for one occurrence of a number rather than one hint
        count = 0
        for k in range(9):
            for num in range(1, 10, 1):
                if not self.boxHas(k, num):
                    list1 = self.getHintLocation(k, num)
                    if len(list1) == 1:
                        if self.grid[(k // 3) * 3 + list1[0] // 3][(k % 3) * 3 + list1[0] % 3] == None:
                            self.placeNumber((k // 3) * 3 + list1[0] // 3, (k % 3) * 3 + list1[0] % 3, num)
    #                         puzzle.grid[(k // 3) * 3 + list1[0] // 3][(k % 3) * 3 + list1[0] % 3] = num
                            count += 1
    #                         puzzle.update()
    #                         printGrid(puzzle.grid)
    #                         print()
        return count

    def hiddenRowColSolve(self):
        detection = False
        for k in range(9):
            for num in range(1, 10, 1):
                if not self.boxHas(k, num):
                    hL = self.hintLinearity(k, num)
                    if hL != -1:
#                         self.printHints()
                        if hL == 0:
                            for j in range(k // 3 * 3, k // 3 * 3 + 3):
                                if not self.boxHas(j, num) and j != k:
                                    if(self.blockHintLines(k, num, 0, ((k // 3) * 3 + self.getHintLocation(k, num)[0] // 3))):
                                        detection = True
                        elif hL == 1:
                            for h in range(k % 3 * 3, 7 + k % 3, 3):
                                if not self.boxHas(h, num) and h != k:
                                    if (self.blockHintLines(k, num, 1, ((k % 3) * 3 + self.getHintLocation(k, num)[0] % 3))):
                                        detection = True
                        self.update()
        return detection

    def twinIsolationSolve(self):
        changed = False
        for num in range(1, 10, 1):
            for k in range(9):
                if self.boxHas(k, num) == False:
                    if self.getBoxHintCount(k, num) == 2:
                        for num2 in range(num, 10, 1):
                            if num != num2:
                                if self.getBoxHintCount(k, num2) == 2 and self.boxHas(k, num2) == False:
    #                                 print("Got here with " + str(num) + " and " + str(num2))
                                    list1 = self.getHintLocation(k, num)
                                    list2 = self.getHintLocation(k, num2)
                                    if self.compareHintLocations(list1, list2):
                                        if not self.checkPair([[num, num2], k]):
#                                             print("making new pair with " + str(num) + " " + str(num2) + " in box " + str(k))
                                            self.blockHint(k, [num, num2], list1)
                                            changed = True
    #                                         print("pair isolated")
                                            self.addPair([num, num2], k)
#                                             self.printHints()
                                            self.update()

        return changed

    def specificRowColSolve(self):
        # TODO: Finish this

        for row in range(9):
            for num in range(1, 10, 1):
                spots = []
                if not self.rowHas(row, num):
                    for col in range(9):
                        if self.grid[row][col] == None and not self.colHas(col, num) and not self.boxHas((row // 3) * 3 + col // 3, num):
                            spots.append(col)
                    if len(spots) == 1:
                        self.placeNumber(row, spots[0], num)
        for col in range(9):
            for num in range(1, 10, 1):
                spots = []
                if not self.colHas(col, num):
                    for row in range(9):
                        if self.grid[row][col] == None and not self.colHas(col, num) and not self.boxHas((row // 3) * 3 + col // 3, num):
                            spots.append(col)
                    if len(spots) == 1:
                        self.placeNumber(row, spots[0], num)


    # -----------------------------------------------------------
    # ----------------------SETUP FUNCTIONS----------------------
    # -----------------------------------------------------------

    def getBoxes(self):
        boxes = []
        for a in range(3):
            for b in range(3):
                box = []
                for k in range(3):
                    boxRow = []
                    for j in range(3):
                        boxRow.append(self.grid[a * 3 + k][b * 3 + j])
                    box.append(boxRow)
                boxes.append(box)
        return boxes

    def getHints(self):
        hints = []
        for k in range(9):
            rowHints = []
            for j in range(9):
                sqHints = self.hintsAt(k, j)
                rowHints.append(sqHints)
            hints.append(rowHints)
        return hints

    def createBlockedHints(self):
        hints = []
        for k in range(9):
            rowHints = []
            for k in range(9):
                placeHints = []
                rowHints.append(placeHints)
            hints.append(rowHints)
        return hints

    def hintsAt(self, r, c):
        if self.grid[r][c] != None:
            return None
        hints = []
        for num in range(1, 10, 1):
            if not self.boxHas((r // 3) * 3 + (c) // 3, num) and not self.rowHas(r, num) and not self.colHas(c, num):
                if self.blockedHints[r][c].count(num) == 0:
                    hints.append(num)
        return hints


    def getHintLocation(self, boxNum, target):
        locations = []
        for r in range(3):
            for c in range(3):
                if self.hints[(boxNum // 3) * 3 + r][boxNum % 3 * 3 + c] != None:
                    for num in self.hints[(boxNum // 3) * 3 + r][boxNum % 3 * 3 + c]:
                        if target == num:
                            locations.append(r * 3 + c)

        return locations

    def hintLinearity(self, boxNum, target):
        # setup
        locs = self.getHintLocation(boxNum, target)
        if len(locs) == 0:
            return -1
        div = locs[0] // 3
        rem = locs[0] % 3
        divBool = None
        remBool = None

        # checks
        for num in locs:
            if num // 3 != div:
                divBool = False
        if divBool == None:
            divBool = True

        for num in locs:
            if num % 3 != rem:
                remBool = False
        if remBool == None:
            remBool = True

        # returns
        if remBool:
#             print("found " + str(target) + " in box " + str(boxNum) + " in a column")
            return 1
        if divBool:
#             print("found " + str(target) + " in box " + str(boxNum) + " in a row")
            return 0
        return -1



    def getBoxHints(self):
        boxes = []
        for a in range(3):
            for b in range(3):
                box = []
                for k in range(3):
                    row = []
                    for j in range(3):
                        sqHints = self.hintsAt(a * 3 + k, b * 3 + j)
                        row.append(sqHints)
                    box.append(row)
                boxes.append(box)
        return boxes

    def getBoxHintCount(self, boxNum, num):
        a = boxNum // 3
        b = boxNum % 3
        count = 0
        for k in range(3):
            for j in range(3):
                if self.hintsAt(a * 3 + k, b * 3 + j) != None:
                    for number in self.hintsAt(a * 3 + k, b * 3 + j):
                        if num == number:
                            count += 1
#         print("Number " + str(num) + " found " + str(count) + " times in box " + str(boxNum))
        return count
    def blockHint(self, boxNum, numList, locations):
        for k in range(1, 10, 1):
            if numList.count(k) == 0:
                for loc in locations:
#                     if self.blockedHints[(boxNum // 3) * 3 + loc // 3][(boxNum % 3) * 3 + loc % 3].count(k) != 0:
                    self.blockedHints[(boxNum // 3) * 3 + loc // 3][(boxNum % 3) * 3 + loc % 3].append(k)
#                     print("blocking " + str(k) + " at spot [" + str((boxNum // 3) * 3 + loc // 3) + "][" + str((boxNum % 3) * 3 + loc % 3) + "]")


    def blockHintLines(self, boxNum, target, rcID, rc):

        changed = False
        localSpots = []
        if rcID == 0:
            for k in range(9):
                if k // 3 != boxNum % 3:
                    localSpots.append(k)
        elif rcID == 1:
            for k in range(9):
                if k // 3 != boxNum // 3:
                    localSpots.append(k)
        # row hints
#         print("number " + str(target) + " exists in spots: ", end="")
#         print(localSpots)
        if rcID == 0:
            for num in localSpots:
                if self.blockedHints[rc][num].count(target) == 0 and self.grid[rc][num] == None:
                    if not self.boxHas(rc // 3 * 3 + num // 3, target) and not self.rowHas(rc, target) and not self.colHas(num, target):
                        self.blockedHints[rc][num].append(target)
#                         print("blocking " + str(target) + " at spot [" + str(rc) + "][" + str(num) + "]")
                        changed = True
        # col hints
        elif rcID == 1:
            for num in localSpots:
                if self.blockedHints[num][rc].count(target) == 0 and self.grid[num][rc] == None:
                    if not self.boxHas(num // 3 * 3 + rc // 3, target) and not self.rowHas(num, target) and not self.colHas(rc, target):
                        self.blockedHints[num][rc].append(target)
#                         print("blocking " + str(target) + " at spot [" + str(num) + "][" + str(rc) + "]")
                        changed = True
#         self.printHints()
#         self.printGrid()
#         print(str(changed) + " is the HRC value")
        return changed

    def placeNumber(self, row, column, num):
#         print("placing " + str(num) + " at [" + str(row) + "][" + str(column) + "]")
        self.grid[row][column] = num
#         self.printGrid()
#         self.updateHints(row, column)
        self.update()

    def update(self):
#         self.rows = self.getRows()
#         self.columns = self.getColumns()
        self.boxes = self.getBoxes()
        self.hints = self.getHints()

    def updateHints(self, r, c):
        for k in range(9):
            if k // 3 != c // 3:
                if self.grid[r][k] == None:
                    self.hints[r][k] = []
                    for num in range(1, 10, 1):
                        if not self.boxHas((r // 3) * 3 + (k) // 3, num) and not self.rowHas(r, num) and not self.colHas(k, num):
                            if self.blockedHints[r][k].count(num) == 0:
                                self.hints[r][k].append(num)

            if k // 3 != r // 3:
                if self.grid[k][c] == None:
                    self.hints[k][c] = []
                    for num in range(1, 10, 1):
                        if not self.boxHas((k // 3) * 3 + (c) // 3, num) and not self.rowHas(k, num) and not self.colHas(c, num):
                            if self.blockedHints[k][c].count(num) == 0:
                                self.hints[k][c].append(num)
        for a in range(r // 3 * 3, r // 3 * 3 + 3, 1):
            for b in range(c // 3 * 3, c // 3 * 3 + 3, 1):
                if self.grid[a][b] == None:
                    self.hints[a][b] = []
                    for num in range(1, 10, 1):
                        if not self.boxHas((a // 3) * 3 + (b) // 3, num) and not self.rowHas(a, num) and not self.colHas(b, num):
                                if self.blockedHints[k][c].count(num) == 0:
                                    self.hints[a][b].append(num)
    # -----------------------------------------------------------
    # ----------------------CHECK FUNCTIONS----------------------
    # -----------------------------------------------------------

    def isComplete(self):
        for k in range(9):
            for j in range(9):
                if self.grid[k][j] == None:
                    return False
        return True

    def compareHintLocations(self, list1, list2):
        for num in list1:
            if list2.count(num) < 1:
                return False
        return True

    def boxHas(self, boxNum, num):
        for row in self.boxes[boxNum]:
            for target in row:
                if target == num:
                    return True

        return False

#     def rowColHas(self, rowCol, num):
#         for target in rowCol:
#             if target == num:
#                 return True
#         return False

    def rowHas(self, rowNum, target):
        for k in range(9):
            if self.grid[rowNum][k] == target:
                return True
        return False

    def colHas(self, colNum, target):
        for k in range(9):
            if self.grid[k][colNum] == target:
                return True
        return False
    # -----------------------------------------------------------
    # --------------------GROUPING FUNCTIONS---------------------
    # -----------------------------------------------------------

    def addPair(self, pair, box):
#         print("pair added")
        self.pairs.append([pair, box])

    def checkPair(self, pairInfo):
        for target in self.pairs:
            if target[1] == pairInfo[1]:
                for num in target[0]:
                    if pairInfo[0].count(num) == 1:
#                         print("duplicate pair detected")
                        return True
#         print("unique pair detected")
        return False

    def addTrio(self, trio, box):
#         print("trio added")
        self.trios.append([trio, box])

    def checkTrio(self, trioInfo):
        for target in self.trios:
            if target[1] == trioInfo[1]:
                for num in target[0]:
                    if trioInfo[0].count(num) == 1:
#                         print("duplicate trio detected")
                        return True
#         print("unique trio detected")
        return False

    # -----------------------------------------------------------
    # ----------------------PRINT FUNCTIONS----------------------
    # -----------------------------------------------------------
    def printBox(self, box):
        for row in box:
            s = ""
            for num in row:
                s += str(num) + " "
            print(s)
        print()

    def printRowCol(self, rowCol):
        s = ""
        for num in rowCol:
            s += str(num) + " "
        print(s)

    def printHints(self):
        for row in self.hints:
            print(row)
        print()

    def printBlockedHints(self):
        for row in self.blockedHints:
            print(row)
        print()

    def printGrid(self):
        for k in range(9):
            string = ""
            for j in range(9):
                if self.grid[k][j] != None:
                    string += str(self.grid[k][j])
                else:
                    string += "*"
                if j == 2 or j == 5:
                    string += " | "
                else:
                    string += " "
            print(string)
            if k == 2 or k == 5:
                print("- - - | - - - | - - -")





if __name__ == '__main__':
    main()
