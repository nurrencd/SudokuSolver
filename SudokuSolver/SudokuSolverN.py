'''
Created on Jul 17, 2017
@author: nurrencd
'''
import random
import math
import graphics as g
import time
from copy import deepcopy
from cmath import sqrt

def main():

    choice = int(input("Enter 0 copypasta code puzzle\n      1 for preset\n   or 2 for a different sized input: "))
    if choice == 0:
        newString = input("enter puzzle string:\n")
        createReturnCode(newString)
    elif choice == 1:
        i = int(input("Puzzle number?"))
        puzzle = Puzzle(sampleGrid(i), 3)
        print(puzzle)
        startTime = time.clock()
#         puzzle.solve()
        puzzle.nakedPairInBox()
#         endTime = time.clock ()
        print(puzzle)
        tree = SpeculationTree(puzzle.grid, puzzle.size)
        endTime = time.clock ()
        print(str((endTime - startTime) // .0000001 / 10000000) + " seconds")
        print(puzzle.colorGrid)
    elif choice == 2:
        puzzleSize = int(input("Enter puzzle size 3 for 9x9, 4 for 16x16, etc"))
        puzzleString = input("Enter puzzle string:\n")
        puzzleGrid = getPuzzleWithVaryingSize(puzzleString, puzzleSize)
        puzzle = Puzzle(puzzleGrid, puzzleSize)
        print(puzzle)
        puzzle.solve()
        print(puzzle)
        tree = SpeculationTree(puzzle.grid, puzzle.size)



def getPuzzleWithVaryingSize(puzzle):
    grid = []
    numbers = puzzle.split(" ")
    size2 = int(math.sqrt(len(numbers)))  # size^2
    for k in range(size2):
        row = []
        for j in range(size2):
            curChar = numbers[k * size2 + j]
            if curChar == "0":
                row.append(None)
            else:
                row.append(int(curChar))
        grid.append(row)

    return grid

def createReturnCode(inputString):
    """
    .94...13..............76..2.8..1.....32.........2...6.....5.4.......8..7..63.4..8
    """
    outputString = "return ["
    for k in range(9):
        outputString += "["
        for j in range(9):
            currentChar = inputString[k * 9 + j]
            if currentChar == ".":
                outputString += "None"
            else:
                outputString += currentChar
            if j != 8:
                outputString += ", "
        outputString += "]"
        if k != 8:
            outputString += ",\n\t\t\t\t"
    outputString += "]"
    print(outputString)

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
        return [[None, 5, None, 1, 3, 4, 6, None, None],
            [None, None, None, 6, 5, 2, 1, 3, 8],
            [None, 3, None, 8, 7, 9, None, 4, None],
            [2, 1, 5, None, None, 3, None, None, 6],
            [None, 8, None, 2, 6, 1, 3, 5, None],
            [3, 6, None, None, 8, 5, 9, 2, 1],
            [None, 4, None, None, 2, 7, None, 1, 3],
            [None, 7, 3, None, None, 6, None, None, None],
            [None, 2, None, 3, None, 8, 7, 6, None]]

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
    elif num == 7:
        return [[None, 9, 4, None, None, None, 1, 3, None],
                [None, None, None, None, None, None, None, None, None],
                [None, None, None, None, 7, 6, None, None, 2],
                [None, 8, None, None, 1, None, None, None, None],
                [None, 3, 2, None, None, None, None, None, None],
                [None, None, None, 2, None, None, None, 6, None],
                [None, None, None, None, 5, None, 4, None, None],
                [None, None, None, None, None, 8, None, None, 7],
                [None, None, 6, 3, None, 4, None, None, 8]]
    elif num == 8:
        return [[None, None, None, None, None, None, None, None, None],
                [None, None, None, 9, 4, 2, None, 8, None],
                [1, 6, None, None, None, None, None, 2, 9],
                [None, None, None, None, None, None, None, None, 8],
                [9, None, 6, None, None, None, None, None, 1],
                [4, None, None, 2, 5, None, None, None, None],
                [None, None, 4, None, None, None, None, None, None],
                [None, 2, None, None, None, 8, None, 9, None],
                [None, 5, None, None, None, None, 7, None, None]]
    elif num == 9:
        return [[8, None, None, None, None, None, None, None, None],
        [None, None, 3, 6, None, None, None, None, None],
        [None, 7, None, None, 9, None, 2, None, None],
        [None, 5, None, None, None, 7, None, None, None],
        [None, None, None, None, 4, 5, 7, None, None],
        [None, None, None, 1, None, None, None, 3, None],
        [None, None, 1, None, None, None, None, 6, 8],
        [None, None, 8, 5, None, None, None, 1, None],
        [None, 9, None, None, None, None, 4, None, None]]
    elif num == 10:
        return [[None, None, None, 8, None, 1, None, None, None],
                [None, None, None, None, None, None, 4, 3, None],
                [5, None, None, None, None, None, None, None, None],
                [None, None, None, None, 7, None, 8, None, None],
                [None, None, None, None, None, None, 1, None, None],
                [None, 2, None, None, 3, None, None, None, None],
                [6, None, None, None, None, None, None, 7, 5],
                [None, None, 3, 4, None, None, None, None, None],
                [None, None, None, 2, None, None, 6, None, None]]


class Puzzle(object):
    # TODO: Finish this class, rework other algorithms
    # remember dual-box joint hint linearity, missing from last attempt
    # try X wing, but not sword fish

    # boxes in form:
    # 0 1 2
    # 3 4 5
    # 6 7 8
    charArray = ["*", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
    def __init__(self, grid, speculation=False):
        self.size = int(math.sqrt(len(grid)))
        self.grid = grid
        self.blankSpotsLeft = 0

        self.rows = self.createRows()
        self.columns = self.createColumns()
        self.boxes = self.createBoxes()

        self.hints = self.createHintArray()
        self.listHints = self.createListHintArray()
        self.blockedHints = self.createHintArray()

        self.initilizeBoxes()
        self.initialHintUpdate()

        self.speculation = speculation
        self.colorGrid = self.createColorGrid()



    def __repr__(self, *args, **kwargs):
        puzzleString = ""
        for row in range(self.size * self.size):
            for col in range(self.size * self.size):
                char = self.grid[row][col]
                if char != None:
#                     print(char, end=" ")
                    puzzleString += self.charArray[int(char)]
                else:
                    puzzleString += "*"
                puzzleString += " "
                if col % self.size == self.size - 1 and col < self.size * self.size - 1:
                    puzzleString += " | "
            puzzleString += "\n"
            if row % self.size == self.size - 1 and row < self.size * self.size - 1:
                puzzleString += "- "*(self.size * self.size + self.size) + "\n"

        return puzzleString

    def deallocate(self):
        """
        deletes every attirube not necessary for drawing
        """
        del self.blankSpotsLeft

        del self.rows
        del self.columns
        del self.boxes

        del self.hints
        del self.listHints
        del self.blockedHints
        
        del self.speculation

    # -----------------------------------------------------------
    # -----------------------INIT FUNCTIONS----------------------
    # -----------------------------------------------------------
    def createColorGrid(self):
        arr = []
        for k in range(self.size * self.size):
            rowArr = []
            for k in range(self.size * self.size):
                rowArr.append(g.Color(15 / 16.0, 15 / 16.0, 15 / 16.0, weight=.0001))
#                 rowArr.append(None)
            arr.append(rowArr)
        return arr

    def createRows(self):
        newRows = []
        for j in range(self.size * self.size):
            newRows.append(None)
        for k in range(self.size * self.size):
            newRows[k] = Row(self.grid[k], self.size)
        return newRows

    def createColumns(self):
        newColumns = []
        for k in range(self.size * self.size):
            newColumns.append(None)
        for col in range(self.size * self.size):
            newColumn = []
            for row in range(self.size * self.size):
                newColumn.append(self.grid[row][col])
            newColumns[col] = Row(newColumn, self.size)
        return newColumns

    def createHintArray(self):
        finalArray = []
        for k in range(self.size * self.size):
            rowArray = []
            for j in range(self.size * self.size):
                colArray = [None]
                for i in range(self.size * self.size):
                    colArray.append(False)
                rowArray.append(colArray)
            finalArray.append(rowArray)
        return finalArray

    def createListHintArray(self):
        finalArray = []
        for k in range(self.size * self.size):
            rowArray = []
            for j in range(self.size * self.size):
                rowArray.append([]);
            finalArray.append(rowArray)
        return finalArray

    def createBoxes(self):
        # initialize array of boxes
        boxArray = []
        for k in range(self.size * self.size):
            boxArray.append(Box(self.size))
        return boxArray

    def initilizeBoxes(self):
        for row in range(self.size * self.size):
            for col in range(self.size * self.size):
                num = self.grid[row][col]
                if num != None:
                    self.boxes[row // self.size * self.size + col // self.size].contains[num] = True


    def initialHintUpdate(self):
        self.blankSpotsLeft = 0
        for row in range(self.size * self.size):
            for col in range(self.size * self.size):
                box = row // self.size * self.size + col // self.size
                # for each empty spot in each row..
                if self.grid[row][col] == None:
                    self.blankSpotsLeft += 1
                    # for each potential candidate...
                    self.listHints[row][col] = []
                    self.hints[row][col] = [None]
                    for k in range(self.size * self.size):
                        self.hints[row][col].append(False)
                    for num in range(1, self.size * self.size + 1):
                        if not self.rows[row].contains[num] and not self.columns[col].contains[num]:
#                             print(str(row) + " " + str(col) + str(num))
#                             print(self.boxes[box])
#                             print(self.hints[row][col])
                            if not self.boxes[box].contains[num]:
                                # if not self.blockedHints[row][col][num] and ...
                                self.hints[row][col][num] = True
                                self.listHints[row][col].append(num)
    # -----------------------------------------------------------
    # ----------------------FULL SOLVE FUNCTION------------------
    # -----------------------------------------------------------
    def solve(self):
        return self.stageSolve(0)

    def stageSolve(self, stage):
        maxStage = 3  # self-input for now
        if stage > maxStage:
#             print("Puzzle is impossible to solve with current algorithms")
            return False
        i = 0
        if stage >= 4:
            pass
#             while (self.analyzeHiddenRows() != 0):
#                 i += 1
        if stage >= 3:
            # analyzing functoins don't place, so modifications will loop forever
            i += self.nakedPairInBox()
            i += self.nakedPairInRow()
            i += self.hiddenPairInBox()
        if stage >= 2:
            while (self.soleRowColCandidate() != 0):
                i += 1
        if stage >= 1:
            while (self.soleSpotCandidate() != 0):
                i += 1
#             pass
        if stage >= 0:
            while (self.soleBoxCandidate() != 0):
                i += 1
#             pass

        # finish cycling through algorithms...
        if i == 0:
            if self.blankSpotsLeft > 0:
                return self.stageSolve(stage + 1)
            else:
                print ("You solved the puzzle")
                self.deallocate()
                return True
        else:
            return self.stageSolve(stage)




    # -----------------------------------------------------------
    # ----------------------PLACE FUNCTIONS----------------------
    # -----------------------------------------------------------
    def placeNumber(self, number, r, c, color):
        self.grid[r][c] = number
        self.rows[r].contains[number] = True
        self.columns[c].contains[number] = True
        box = r // self.size * self.size + c // self.size
        self.boxes[box].contains[number] = True
        # subtract blankSpots counter
        self.boxes[box].blankSpots -= 1
        self.rows[r].blankSpots -= 1
        self.columns[c].blankSpots -= 1
        # update color
        self.placeColor(r, c, color)
        # update box, rows
#         self.updateHints(r, c)
        self.initialHintUpdate()
#         print("placing " + str(number) + " at [" + str(r) + "][" + str(c) + "]")

    def placeColor(self, r, c, color):
        self.colorGrid[r][c].addColor(color)

    def updateHints(self, r, c):
        # generalize for all sizes...
        # TODO Figure out what's wrong here and fix it
        # update placement's column
        for row in range(9):
            if self.grid[row][c] == None:
                self.listHints[row][c] = []
                self.hints[row][c] = [None, False, False, False, False, False, False, False, False, False]
                for num in range(1, 10):
                    if not self.rows[row].contains[num] and not self.columns[c].contains[num]:
                        if not self.boxes[r // 3 * 3 + c // 3].contains[num] and not self.blockedHints[row][c][num]:
                            self.hints[row][c][num] = True
                            self.listHints[row][c].append(num)
        # update placement's row
        for col in range(9):
            if self.grid[r][col] == None:
                self.listHints[r][col] = []
                self.hints[r][col] = [None, False, False, False, False, False, False, False, False, False]
                for num in range(1, 10):
                    if not self.rows[r].contains[num] and not self.columns[col].contains[num]:
                        if not self.boxes[r // 3 * 3 + c // 3].contains[num] and not self.blockedHints[r][col][num]:
                            self.hints[r][col][num] = True
                            self.listHints[r][col].append(num)
        # update placement's box
        newR = r // 3 * 3
        newC = c // 3 * 3
        for k in range(9):
            finalR = newR + k // 3
            finalC = newC + k % 3
            if self.grid[finalR][finalC] == None:
                self.listHints[finalR][finalC] = []
                self.hints[finalR][finalC] = [None, False, False, False, False, False, False, False, False, False]
                if not self.rows[r].contains[num] and not self.columns[c].contains[num]:
                        if not self.blockedHints[row][c][num]:
                            self.hints[row][c][num] = True
                            self.listHints[row][c].append(num)


    # -----------------------------------------------------------
    # ----------------------SOLVE FUNCTIONS----------------------
    # -----------------------------------------------------------
    def soleSpotCandidate(self):
        changed = 0
        color = g.Color(.25, .25, 1)
        for row in range(self.size * self.size):
            for col in range(self.size * self.size):
                if self.grid[row][col] == None:
                    # check to see if theres one candidate
                    if len(self.listHints[row][col]) == 1:
                        self.placeNumber(self.listHints[row][col][0], row, col, color)
                        changed += 1
        return changed

    def soleBoxCandidate(self):
        changed = 0
        color = g.Color(1, .25, .25)
        # if a number can only go in one spot in a box, place it
        for box in range(self.size * self.size):
            for num in range(1, self.size * self.size + 1):
                # don't bother checking if the box already contains it
                if not self.boxes[box].contains[num]:
                    # k is coordinate number
                    count = 0
                    lastCoordinate = 0
                    for k in range(self.size * self.size):
                        # every 3 boxes is another 3 rows, every 3 k is a single row
                        r = box // self.size * self.size + k // self.size
                        c = box % self.size * self.size + k % self.size
                        if self.grid[r][c] == None:
                            if self.hints[r][c][num]:
                                count += 1
                                lastCoordinate = k
                    if count == 1:
                        self.placeNumber(num, box // self.size * self.size + lastCoordinate // self.size, box % self.size * self.size + lastCoordinate % self.size, color)
                        changed += 1
        return changed

    def soleRowColCandidate(self):
        changed = 0
        color = g.Color(.25, 1, .25)  # greenish
        for row in range(self.size * self.size):
            for num in range(1, self.size * self.size + 1):
                if not self.rows[row].contains[num]:
                    # count number of candidate spots
                    count = 0
                    lastCoordinate = 0
                    for col in range(self.size * self.size):
                        if self.hints[row][col][num] and self.grid[row][col] == None:
                            count += 1
                            lastCoordinate = col
                    if count == 1:
                        self.placeNumber(num, row, lastCoordinate, color=color)
                        changed += 1

        for col in range(self.size * self.size):
            for num in range(1, self.size * self.size + 1):
                if not self.columns[col].contains[num]and self.grid[row][col] == None:
                    # start count
                    count = 0
                    lastCoordinate = 0
                    for row in range(self.size * self.size):
                        if self.hints[row][col][num]:
                            count += 1
                            lastCoordinate = row
                    if count == 1:
                        self.placeNumber(num, lastCoordinate, col, color=color)
                        changed += 1

        return changed

    # -----------------------------------------------------------
    # ---------------------ANALYZE FUNCTIONS---------------------
    # -----------------------------------------------------------

    # include blocking functions?
    def blockNumber(self, num, r, c, color=None):
        if not self.boxes[r // self.size * self.size + c // self.size].contains[num]:
            if self.grid[r][c] == None:
                if not self.blockedHints[r][c][num]:
                    self.blockedHints[r][c][num] = True
#                     print("Blocking " + str(num) + " at [" + str(r) + "][" + str(c) + "]")
                    if color != None:
                        self.placeColor(r, c, color)
#                         print("placin.g color from blocking!")
                    return True
        return False

    def blockRow(self, num, r, c, type):
        changed = False
        if type == 0:  # is a row, based on type from analyzeHiddenRows loop
            for col in range(9):
                if col // 3 != c // 3:
                    if self.blockNumber(num, r, col):
                        changed = True
        elif type == 1:
            for row in range(9):
                if row // 3 != r // 3:
                    if self.blockNumber(num, row, c):
                        changed = True
        return changed
    def blockClusterBox(self, box, spots, nums, color=None):
        changed = False
        baseR = box // self.size * self.size
        baseC = box % self.size * self.size
        for spot in range(self.size * self.size):
            if spot in spots:  # it's where the pair was isolated
#                 self.placeColor(baseR + spot // self.size, baseC + spot % self.size, color)
                for newNum in range(1, self.size * self.size + 1):
                    if newNum in nums:
                        continue
                    if self.blockNumber(newNum, baseR + spot // self.size, baseC + spot % self.size, color=color):
                        changed = True
            else:  # block the pair from other spots
                for num in nums:
                    if self.blockNumber(num, baseR + spot // self.size, baseC + spot % self.size, color=color):
                        changed = True
        return changed

    def blockClusterRow(self, row, spots, nums, color=None):
        changed = False
        for spot in range(self.size * self.size):
            if spot in spots:
                # where the pair was found
                for newNum in range(self.size * self.size):
                    if not newNum in nums:
                        if self.blockNumber(newNum, row, spot, color=color):
                            changed = True
            else:
                # where everything else is
                for num in nums:
                    if self.blockNumber(num, row, spot, color=color):
                        changed = True
        return changed
                

    def blockClusterCol(self, col, spots, nums, color=None):
        changed = False
        for spot in range(self.size * self.size):
            if spot in spots:
                # where the pair was found
                for newNum in range(self.size * self.size):
                    if not newNum in nums:
                        if self.blockNumber(newNum, spot, col, color=color):
                            changed = True
            else:
                # where everything else is
                for num in nums:
                    if self.blockNumber(num, spot, col, color=color):
                        changed = True
        return changed
    
    # -----------------------------------------------------------
    # ---------------------SUBSET FUNCTIONS---------------------
    # -----------------------------------------------------------

    def nakedPairInBox(self):
        """
        This algorithm naively* detects isolated pairs within a single box.
        
        *It is naive because it is intuitively easy, but is a different class
        of isolated-pair from hidden pairs. Therefore it must be attempted.
        """
        changed = 0
        blockingColor = g.Color(1, .75, .8, weight=.2)
        s = self.size
        for box in range(s * s):
            if self.boxes[box].blankSpots == 2:
                # no point in doing this if there are only two left...
                continue
            # else there are more, do it
            baseR = box // s * s
            baseC = box % s * s
            for k in range(s * s):
                hintsK = self.listHints[baseR + k // s][baseC + k % s]
                if len(hintsK) != 2:
                    # this is no pair
                    continue
                for j in range(s * s):
                    if k == j:
                        continue
                    hintsJ = self.listHints[baseR + j // s][baseC + j % s]
                    if len(hintsJ) != 2:
                        continue
                    # else they are the same length
                    if self.compareArrays(hintsJ, hintsK):
                        # they match, begin blocking algorithms
                        if self.blockClusterBox(box, [k, j], hintsJ, color=blockingColor):
                            changed += 1
                            self.placeColor(baseR + k // s, baseC + k % s, blockingColor)
                            self.placeColor(baseR + j // s, baseC + j % s, blockingColor)
#                           print("Found a naked pair in box " + str(box),end=" ")
#                             print(hintsK)
                        if k // s == j // s:
                            # they form a locked pair
                            pass
                            
                    
        return changed
    
    def nakedPairInRow(self):
        """
        This algorithm naively* detects isolated pairs within a single row.
        
        *It is naive because it is intuitively easy, but is a different class
        of isolated-pair from hidden pairs. Therefore it must be attempted.
        """
        # find naked pairs in all rows
        blockingColor = g.Color(.75, 1, .8, weight=.2);
        changed = 0
        s = self.size
        for row in range(s * s):
            if self.rows[row].blankSpots == 2:  # no point in doing this...
                continue
            for k in range(s * s):
                hintsK = self.listHints[row][k]
                if len(hintsK) != 2:
                    continue  # not a pair
                for j in range(s * s):
                    if k == j:
                        continue
                    hintsJ = self.listHints[row][j]
                    if len(hintsJ) != 2:  # not a paid
                        continue
                    if self.compareArrays(hintsK, hintsJ):
                        # They match!
                        if self.blockClusterRow(row, [k, j], hintsK, color=blockingColor):
                            changed += 1
                            self.placeColor(row, k, blockingColor)
                            self.placeColor(row, j, blockingColor)
                        # locked pair analysis
        
        # find naked pairs in all columns
        for col in range(s * s):
            if self.columns[col].blankSpots == 2:
                continue
            for k in range(s * s):
                hintsK = self.listHints[k][col]
                if len(hintsK) != 2:
                    continue  # not a pair
                for j in range(s * s):
                    if k == j:
                        continue
                    hintsJ = self.listHints[j][col]
                    if len(hintsJ) != 2:  # not a paid
                        continue
                    if self.compareArrays(hintsK, hintsJ):
                        # They match!
                        if self.blockClusterCol(col, [k, j], hintsK, color=blockingColor):
                            changed += 1
                            self.placeColor(k, col, blockingColor)
                            self.placeColor(j, col, blockingColor)
                        # locked pair analysis
        return changed
    
    def hiddenPairInBox(self):
        """
        This algorithm detects hidden pairs within a single box. More in-depth than naked pairs.
        
        steps: (per box)
        setup local data structure for pair isolations
        populate structure with box information
        analyze data
        block numbers
        """
        changedColor = g.Color(.85, .6, .03, weight=.2)  # honey
        s = self.size
        changed = 0
        for box in range(s * s):
            if self.boxes[box].blankSpots == 2:
                continue
            localHintArray = [None]
            baseR = box // s * s
            baseC = box % s * s
            # set up local structure
            for k in range(s * s):
                localHintArray.append([])
            # populate local structure
            for spot in range(s * s):
                spotHints = self.listHints[baseR + spot // s][baseC + spot % s]
                for num in spotHints:
                    localHintArray[num].append(spot)
            # analyze local structure
            for a in range(1, s * s):
                if len(localHintArray[a]) != 2:
                    continue
                for b in range(a + 1, s * s + 1):
                    if len(localHintArray[b]) != 2:
                        continue
                    # arrays are same length, check for pair
                    if self.compareArrays(localHintArray[a], localHintArray[b]):
                        if self.blockClusterBox(box, localHintArray[a], [a, b], changedColor):
                            k = localHintArray[a][0]
                            j = localHintArray[a][1]
                            self.placeColor(baseR + k// s, baseC + k % s, changedColor)
                            self.placeColor(baseR + j // s, baseC + j % s, changedColor)
#                             print("Found a hidden pair in box " + str(box),end=" ")
#                             print([a,b])
                            changed += 1
                        
        return changed
            
    def compareArrays(self, array1, array2):
        for k in range(len(array1)):
            if array1[k] != array2[k]:
                return False
        return True
    # -----------------------------------------------------------
    # ------------------SPECULATIVE FUNCTIONS--------------------
    # -----------------------------------------------------------
    def contradictionExists(self):
        for r in range(self.size * self.size):
            for c in range(self.size * self.size):
                if self.grid[r][c] == None and len(self.listHints[r][c]) == 0:
#                     self.deallocate()
                    return True
        return False

    # -----------------------------------------------------------
    # ----------------------PRINT FUNCTIONS----------------------
    # -----------------------------------------------------------

    def printHints(self):
        for row in self.listHints:
            print(row)

    def printBoxes(self):
        for box in self.boxes:
            print(box.contains)

class Row(object):
    def __init__(self, list, size):
        self.numbers = list
        self.blankSpots = size * size
        self.contains = [None]
        for k in range(size * size):
            self.contains.append(False)
        self.setContainsArray()

    def setContainsArray(self):
        # TODO: rework so only one array iteration
        for num in self.numbers:
            if num != None:
                self.blankSpots -= 1
                self.contains[num] = True

class Box(object):
    """
    This class exists simply to produce the same ...[num].contains[num]
    as the Row class, and pair / trio isolated variables
    """
    def __init__(self, size):
        self.blankSpots = size * size
        self.contains = [None]
        self.isPaired = [None]
        for k in range(size * size):
            self.isPaired.append(False)
            self.contains.append(False)

class SpeculationTree(object):
    # TODO: finish the class
    def __init__(self, grid, size):
        self.startingGrid = deepcopy(grid)
        self.root = Node(grid, size)
        # automatically branches and solve
        self.depth = self.root.depth

    def displayFinalPuzzle(self, puzzle):
        print(puzzle.grid)
        

class Node(object):
    def __init__(self, grid, size, parent=None, row=None, col=None, val=None, depth=0):
        self.startPuzzle = deepcopy(grid)
        self.puzzle = Puzzle(deepcopy(grid), size)

        self.parent = parent
        self.children = []

        self.row = row
        self.col = col
        self.val = val

        self.depth = depth

        self.valid = True
        self.correct = False

        self.timeTaken = None

        self.solveAndBranch()
        
    def getTotalTime(self):
        if len(self.children) == 0:
#             print("adding " + str(self.timeTaken))
            return self.timeTaken
        totalTime = self.timeTaken
        if totalTime == None:
            totalTime = 0;
        for child in self.children:
            totalTime += child.getTotalTime()
        return totalTime
        
    def getCorrectTime(self):
        if len(self.children) == 0:
            return self.timeTaken;
        for child in self.children:
            if child.correct:
                return child.timeTaken + child.getCorrectTime()
        

    def solveAndBranch(self):
        if self.val != None:
#             print("Starting node of depth " + str(self.depth) + "  by placing " + str(self.val) + " at [" + str(self.row) + "][" + str(self.col) + "]",end=" ")
#             print("With " + str(self.puzzle.blankSpotsLeft) + " spots left")
            self.puzzle.placeNumber(self.val, self.row, self.col, g.Color(.5, .5, .5))

            startTime = time.clock()
            solveStatus = self.puzzle.solve()
            endTime = time.clock()
            self.timeTaken = endTime - startTime

            if solveStatus:
                print("SOLVED THIS PUZZLE")
                print(self.puzzle)
                self.returnToTree(True)
                return
            elif self.puzzle.contradictionExists():
                self.valid = False
                
        bestR = 0
        bestC = 0
        minGuesses = self.puzzle.size * self.puzzle.size
        for r in range(self.puzzle.size * self.puzzle.size):
            for c in range(self.puzzle.size * self.puzzle.size):
                if self.puzzle.grid[r][c] == None:
                    if len(self.puzzle.listHints[r][c]) < minGuesses and len(self.puzzle.listHints[r][c]) > 0:
                        bestR = r
                        bestC = c
                        minGuesses = len(self.puzzle.listHints[r][c])
        for num in self.puzzle.listHints[bestR][bestC]:
            if not self.correct and self.valid:  # fixed contradictory nodes making children
                self.children.append(Node(self.puzzle.grid, self.puzzle.size, parent=self, row=bestR, col=bestC, val=num, depth=self.depth + 1))
            if not self.correct:
                self.returnToTree(False)
        return

    def returnToTree(self, value):
        self.correct = value
        if self.parent != None:
            self.parent.returnToTree(value)

if __name__ == '__main__':
    main()
