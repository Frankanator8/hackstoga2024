class Track:
    def __init__(self, boards, timestamps, maxLength):
        self.time = 0
        self.boards = boards
        self.timestamps = timestamps
        self.maxLength = maxLength
        self.score = 0
        self.done = False
        self.index = 0

    def reset(self):
        self.time = 0
        self.score = 0
        self.done = False
        self.index = 0

    def tick(self, dt):
        self.time += dt
        board = []
        for i in range(4):
            board.append([])
            for j in range(4):
                board[-1].append(0)
        if self.index == len(self.timestamps) - 1:
            pass

        else:
            if self.time >= self.timestamps[self.index+1]
                self.index += 1

            prog = (self.time - self.timestamps[self.index])/(self.timestamps[self.index+1]-self.timestamps[self.index])
            for r, row in enumerate(self.boards[self.index]):
                for c, col in enumerate(row):
                    if col == 0:
                        pass

                    else:



