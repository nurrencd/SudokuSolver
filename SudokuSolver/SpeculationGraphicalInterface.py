import graphics as g
import SudokuSolverN as ss
import tkinter as tk
def main():
    

    puzzleString1 = "0 0 0 13 10 3 1 0 0 0 0 0 0 15 16 4 0 0 0 0 0 16 12 13 0 0 0 8 0 0 3 0 1 5 0 0 0 0 0 0 0 0 0 0 13 0 0 0 0 0 0 0 0 0 0 4 0 0 15 4 0 7 0 0 0 4 0 5 7 11 0 14 0 0 0 0 0 12 0 0 0 8 0 11 0 0 15 0 0 0 0 2 0 0 0 0 9 0 0 7 6 8 0 12 0 1 0 16 0 5 0 0 0 0 10 0 0 0 0 0 4 0 0 12 15 9 0 0 13 1 0 10 0 4 0 0 0 14 0 0 0 0 9 0 0 0 5 16 9 0 0 0 0 0 0 0 4 8 10 15 0 0 9 6 12 0 14 0 0 0 0 11 0 0 1 0 7 0 0 2 0 15 0 0 1 9 0 13 0 11 5 6 1 0 0 0 14 0 0 7 0 11 0 0 10 0 0 8 0 0 8 4 16 0 11 0 0 0 5 0 0 1 0 3 0 3 0 1 0 0 0 15 0 0 14 0 0 0 13 11 12 0 13 0 0 0 8 0 6 4 0 1 5 0 0 0"
    puzzleString2 = "0 0 0 0 0 0 13 15 16 0 8 14 0 0 0 1 0 15 0 0 0 0 1 0 3 0 11 0 16 5 0 8 11 9 0 12 0 0 0 5 0 0 0 0 0 0 0 0 10 0 8 0 0 0 7 0 4 13 9 0 0 0 14 0 4 0 0 8 15 0 0 16 0 0 0 5 0 0 1 10 0 0 0 13 0 11 0 0 12 0 0 4 0 15 8 7 0 0 0 0 1 9 0 0 0 0 16 0 0 0 0 0 14 0 0 0 0 0 0 0 0 0 0 8 0 0 0 0 0 0 10 2 8 5 0 0 14 12 0 0 0 0 0 13 0 0 0 7 0 0 9 3 0 0 0 11 0 2 15 12 13 0 0 1 4 0 0 0 0 16 5 0 0 14 0 0 8 0 11 3 7 0 14 0 13 15 0 10 6 0 0 0 0 0 0 0 12 13 0 0 5 11 0 0 3 0 0 0 0 0 12 16 0 0 6 1 0 0 0 0 11 8 0 0 7 13 0 9 5 15 0 0 0 0 0 16 0 10 6 0 1 6 15 0 16 0 0 0 7 0 0 0 14 12 0 0"
    puzzleString3 = "0 0 0 9 0 0 0 8 0 10 0 0 12 4 6 13 0 3 0 0 0 10 7 0 0 0 15 0 11 0 0 0 0 16 0 12 13 0 0 0 0 7 9 0 0 5 0 0 0 10 15 0 0 11 12 0 13 16 0 4 0 0 14 0 0 0 5 6 0 0 0 12 0 0 0 0 0 16 0 0 0 0 11 14 0 0 6 0 0 0 0 0 15 0 0 0 0 1 0 0 16 0 15 2 0 8 6 0 9 0 0 0 9 0 0 0 11 0 13 0 2 4 7 0 0 0 0 0 16 0 12 0 0 14 0 0 0 0 0 0 0 0 13 0 14 0 0 0 0 0 16 15 8 0 3 0 0 0 0 0 11 0 9 13 0 0 10 0 16 0 0 0 0 0 0 12 0 0 0 10 9 0 0 7 14 0 13 15 5 0 8 0 0 0 0 0 10 0 0 0 0 0 0 5 0 8 0 0 0 0 2 0 6 0 0 0 0 15 8 14 0 7 0 10 12 14 0 0 0 7 2 11 3 0 0 0 16 0 0 15 0 9 7 0 0 0 5 16 0 0 0 0 0 0 12 0"
    puzzleString = open("25x25", mode='r').read()
    #EDIT THESE TWO LINES
#--------------------------------------------------------------------
    puzzle = ss.Puzzle(ss.sampleGrid(9))
#     puzzle = ss.Puzzle(ss.getPuzzleWithVaryingSize(puzzleString3))
#---------------------------------------------------------------------
    puzzle.solve()
    print(puzzle)
    specTree = ss.SpeculationTree(puzzle.grid, puzzle.size)
    win = g.GraphWin("Sudoku Puzzle Speculation Tree", 900, 900)

    dst = DrawableSpeculationTree(specTree)
    dst.generateTree()

    drawInteractableInterface(win, dst)
    print("Finished")

def createPuzzles(win, node):
    size = node.specNode.puzzle.size
    if node.specNode.timeTaken != None:
        win.create_text(win.getWidth() / 2.0, win.getHeight() * .2 , text=str(node.specNode.timeTaken // .000001 / 1000000)[0:8] + "\nseconds")
        win.create_line(win.getWidth() * .45, win.getHeight() * .12, win.getWidth() * .55, win.getHeight() * .12)
        win.create_line(win.getWidth() * .52, win.getHeight() * .10, win.getWidth() * .55, win.getHeight() * .12)
        win.create_line(win.getWidth() * .52, win.getHeight() * .14, win.getWidth() * .55, win.getHeight() * .12)

    startPuzzleXLimit = win.getWidth() * .4
    endPuzzleXStart = win.getWidth() * .6
    boxWidth = startPuzzleXLimit / size / size
    numberOffset = boxWidth / 2.0
    # draw the starting puzzle
    x = 0
    y = 0
    for k in range(size * size):
        for j in range(size * size):
            win.create_rectangle(x, y, x + boxWidth, y + boxWidth)
            x += boxWidth
        x = 0
        y += boxWidth
    # draw lines
    x = boxWidth * size
    y = 0
    for k in range(size - 1):
        win.create_line(x, y, x, y + boxWidth*size*size,width=3)
        x+= boxWidth * size
    y = boxWidth * size
    x = 0
    for j in range(size-1):
        win.create_line(x,y,x+boxWidth * size *size,y, width=3)
        y += boxWidth * size
    # put in the numbers
    x = numberOffset
    y = numberOffset
    for r in range(size * size):
        for c in range(size * size):
            num = node.specNode.startPuzzle[r][c]
            if num != None:
                win.create_text(x, y, text=str(num))
            x += boxWidth
        x = numberOffset
        y += boxWidth

    # draw the ending puzzle
    x = endPuzzleXStart
    y = 0
    for i in range(size * size):
        for h in range(size * size):
            fillString = None
            if node.specNode.puzzle.colorGrid[i][h] != None:
                fillString = node.specNode.puzzle.colorGrid[i][h].__repr__()
#             print(fillString)
            if node.specNode.puzzle.grid[i][h] == None:
                fillString = '#dddddd'
            win.create_rectangle(x, y, x + boxWidth, y + boxWidth, fill=fillString)
            x += boxWidth
        x = endPuzzleXStart
        y += boxWidth
    #draw lines
    x = endPuzzleXStart + boxWidth * size
    y = 0
    for k in range(size - 1):
        win.create_line(x, y, x, y + boxWidth*size*size,width=3)
        x+= boxWidth * size
    y = boxWidth * size
    x = endPuzzleXStart
    for j in range(size-1):
        win.create_line(x,y,x+boxWidth * size *size,y, width=3)
        y += boxWidth * size

    # put in the numbers
    x = numberOffset + endPuzzleXStart
    y = numberOffset
    for r in range(size * size):
        for c in range(size * size):
            num = node.specNode.puzzle.grid[r][c]
            if num != None:
                win.create_text(x, y, text=str(num))
            x += boxWidth
        x = numberOffset + endPuzzleXStart
        y += boxWidth



def createLegend(window, node):
    x1 = .94
    xOffset = .02
    y1 = .44
    yOffset = .02
    width = .04
    # Initial Speculation
    window.create_rectangle(window.getWidth() * x1, window.getHeight() * y1, window.getWidth() * (x1 + width), window.getHeight() * (y1 + width), fill=repr(g.Color(.5, .5, .5)))
    window.create_text(window.getWidth() * (x1 - xOffset), window.getHeight() * (y1 + width / 2), anchor=tk.E, text="Initial Speculation")
    y1 += width + yOffset
    # Specific Row Solver
    window.create_rectangle(window.getWidth() * x1, window.getHeight() * y1, window.getWidth() * (x1 + width), window.getHeight() * (y1 + width), fill=repr(g.Color(.25, 1, .25)))
    window.create_text(window.getWidth() * (x1 - xOffset), window.getHeight() * (y1 + width / 2), anchor=tk.E, text="Specific Row Solver")
    y1 += width + yOffset
    # Sole Box Candidate
    window.create_rectangle(window.getWidth() * x1, window.getHeight() * y1, window.getWidth() * (x1 + width), window.getHeight() * (y1 + width), fill=repr(g.Color(1, .25, .25)))
    window.create_text(window.getWidth() * (x1 - xOffset), window.getHeight() * (y1 + width / 2), anchor=tk.E, text="Sole Box Candidate")
    y1 += width + yOffset
    # Sole Spot Candidate
    window.create_rectangle(window.getWidth() * x1, window.getHeight() * y1, window.getWidth() * (x1 + width), window.getHeight() * (y1 + width), fill=repr(g.Color(.25, .25, 1)))
    window.create_text(window.getWidth() * (x1 - xOffset), window.getHeight() * (y1 + width / 2), anchor=tk.E, text="Sole Spot Candidate")


def drawInteractableInterface(win, tree):
    tree.drawTree(win)
    win.create_text(50,50, text=str(tree.specTree.root.getTotalTime()//.0000001*.0000001)[0:8] + " seconds for total tree",anchor=tk.W)
    win.create_text(50,70,text=str(tree.specTree.root.getCorrectTime()//.0000001 * .0000001)[0:8] + " seconds for correct path", anchor=tk.W)

    while True:
        point = win.getMouse()
        for node in tree.nodes:
            if node.inbounds(point.getX(), point.getY()):
                nodeWin = g.GraphWin("Detailed Node Report", 900, 900)
                createPuzzles(nodeWin, node)
                createLegend(nodeWin, node)
                pass



class DrawableSpeculationTree(object):

    def __init__(self, specTree):
        self.specTree = specTree
        self.rootNode = DrawableNode(specTree.root)
        self.nodes = []
        self.nodeRadius = 0
        self.depth = specTree.depth
        self.getDepth()

    def getDepth(self):
        for node in self.nodes:
            if node.depth > self.depth:
                self.depth = node.depth

    def drawTree(self, window):
        height = window.getHeight()
        width = window.getWidth()

        heightGap = height / (self.depth + 2)
        widthGapArray = [width / 2]
        depthArray = [0]


        for k in range(self.depth):
            depthArray.append(0)
        for node in self.nodes:
            depthArray[node.depth] += 1
        for k in range(len(depthArray) - 1):
            widthGapArray.append(width / (depthArray[k + 1] + 1))
        self.nodeRadius = min(heightGap / 2.5, window.getWidth() / (max(depthArray[:]) * 2.5))

#         print(depthArray)
#         print(widthGapArray)

        # setup coordinates
        currentDepth = 0
        currentOffset = 1
        for node in self.nodes:
            # moved on to new layer
            if node.depth != currentDepth:
                currentDepth += 1
                currentOffset = 1
            x = widthGapArray[node.depth] * currentOffset
            y = heightGap * (currentDepth + 1)
            nr = self.nodeRadius
#             print(str(x) + " " + str(y))
            node.setCoordinates(x - nr, y - nr, x + nr, y + nr)
            currentOffset += 1

        for node in self.nodes:
            if node.parent != None:
                x1 = (node.parent.x1 + node.parent.x2) / 2
                y1 = (node.parent.y1 + node.parent.y2) / 2
                x2 = (node.x1 + node.x2) / 2
                y2 = (node.y1 + node.y2) / 2
                window.create_line(x1, y1, x2, y2, width=1)
        for node in self.nodes:
            node.drawNode(window)



    def generateTree(self):
        #fix the two DrawableNode constructor usage...
        self.nodes.append(self.rootNode)
        index = 0
        while (index < len(self.nodes)):
            if len(self.nodes[index].children) > 0:
                for child in self.nodes[index].children:
                    newNode = DrawableNode(child.specNode)
                    newNode.setDepth(self.nodes[index].depth + 1)
                    newNode.parent = self.nodes[index]
                    self.nodes.append(newNode)
            index += 1

        self.getDepth()
#         for node in self.nodes:
#             print(node.depth)





class DrawableNode(object):
    def __init__(self, node, parent=None):
#         print(node)
        self.specNode = node
        self.depth = node.depth
        self.children = [DrawableNode(x, parent=self) for x in node.children]
        self.parent = None

        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0




    def setCoordinates(self, newX1, newY1, newX2, newY2):
        self.x1 = newX1
        self.y1 = newY1
        self.x2 = newX2
        self.y2 = newY2

    def setDepth(self, newDepth):
        self.depth = newDepth

    def inbounds(self, x, y):
        if self.x1 < x and x < self.x2 and self.y1 < y and y < self.y2:
            return True
        return False

    def drawNode(self, window):
        newfill = ''
        if self.specNode.correct:
            newfill = '#00ff00'
        elif not self.specNode.valid:
            newfill = '#ff0000'
        else:
            newfill = '#4488ff'
        window.create_oval(self.x1, self.y1, self.x2, self.y2, fill=newfill)

if __name__ == '__main__':
    main()
