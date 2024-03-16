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
            if lineNum % 5 == 1: # empty
                blocks.append(curBlock)
                curBlock = []
                curRow = []
            else:
                curRow = line.split(" ")
                curBlock.append(curRow)
    return blocks

blocks = readBlocks("../assets/justlikeyouBlocks.txt")

times = [0, 0.5, 1, 1.5]
times = [0, 2, 3.8, 5.5, 7, 9, 10.5, 12.2, 14, 15.8, 17.3, 19, 20.9, 22.5, 24, 27.7, 29.5, 31, 33, 34.8, 36.5, 38, 39.8, 41.6, 43, 44.8, 46.7, 48.6, 50, 51.8, 55, 56, 57, 57.8, 58.8, 59.5, 60, 61, 62, 62.8, 63.7, 64.5, 65.5, 66.2, 67, 68, 69, 69.8, 70.8, 71.7, 73, 74, 75, 75.8, 76.8, 77.5, 78.3, 79, 82.7, 84, 86, 87.7, 89.5, 91, 92.5]

justlikeyou = Track(boards, times, 90, [31])
