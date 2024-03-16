import math


class Track:
    def __init__(self, boards, timestamps, maxLength):
        self.time = 0
        self.boards = boards
        self.timestamps = timestamps
        self.maxLength = maxLength
        self.done = False
        self.index = 0

    def reset(self):
        self.time = 0
        self.done = False
        self.index = 0

    def tick(self, dt, playerR, playerC):
        self.time += dt
        good = True
        board = []
        for i in range(4):
            board.append([])
            for j in range(4):
                board[-1].append(0)

        if self.time > self.maxLength:
            self.done = True

        if self.index == len(self.timestamps) - 1:
            prog = (self.time - self.timestamps[self.index])/(self.maxLength-self.timestamps[self.index])
            for r, row in enumerate(self.boards[self.index]):
                for c, col in enumerate(row):
                    if col == 1:
                        board[r][c] = max(1-prog, 0)

        else:
            i=1
            while self.time + 2 > self.timestamps[self.index+i]:
                i += 1
                if self.index + i >= len(self.timestamps) - 1:
                    break
            for r, row in enumerate(self.boards[self.index]):
                for c, col in enumerate(row):
                    if col == 0:
                        for next in range(i):
                            if self.boards[self.index+next][r][c] == 1:
                                board[r][c] = (1-((self.timestamps[self.index+next]-self.time)/2))**6

                    else:
                        board[r][c] = 1

                    if r == playerR and c == playerC:
                        if col == 1:
                            good = False




            if self.time >= self.timestamps[self.index+1]:
                self.index += 1

        return board, good



