class ThirteenOrphans(object):

    def __init__(self, mytiles):
        self.mytiles = mytiles

    def calculation_xiangting(self):
        print(self.mytiles)
        pair = False
        yaochu = 0
        for i in range(4):
            if i == 3:
                for j in range(7):
                    if self.mytiles[i][j] >= 1:
                        yaochu += 1
                        if self.mytiles[i][j] >= 2:
                            pair = True
            else:
                for j in [0, 8]:
                    if self.mytiles[i][j] >= 1:
                        yaochu += 1
                        if self.mytiles[i][j] >= 2:
                            pair = True
        xiangting = 13 - yaochu
        if pair is True:
            xiangting -= 1
        return xiangting