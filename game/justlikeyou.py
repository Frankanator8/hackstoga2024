from game.track import Track


boards = [
    [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],

    [[0, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0]],

    [[1, 1, 1, 1],
     [1, 0, 0, 0],
     [1, 0, 0, 0],
     [1, 0, 0, 0]],

    [[0, 0, 0, 0],
     [0, 1, 1, 0],
     [0, 1, 1, 0],
     [0, 0, 0, 0]],


]

def readBlocks(filename):
    curRow = []
    curBlock = []
    blocks = []
    with open(filename, 'r') as file:
        lineNum = 0
        # Read the entire contents of the file
        for line in file:
            lineNum += 1
        # Process each line as needed
            content = line.strip()
            if lineNum % 5 == 1: // empty
            blocks.append(curBlock)
            curBlock = []
            curRow = []
            else:
                curRow = line.split(" ")

blocks = readBlocks("justlikeyouBlocks.txt")

times = [0, 0.5, 1, 1.5]
justlikeyou = Track(boards, times, 2)
