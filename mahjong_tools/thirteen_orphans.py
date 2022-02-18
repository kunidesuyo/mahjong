class ThirteenOrphans(object):

    def __init__(self, mytiles):
        self.mytiles = mytiles

    def calculation_xiangting(self):
        pair = False
        yaochu = 0
        for i in range(3):
            if self.mytiles[i][0] >= 1:
                yaochu += 1
                if self.mytiles[i][0] >= 2:
                    pair = True
            if self.mytiles[i][8] >= 1:
                yaochu += 1
                if self.mytiles[i][8] >= 2:
                    pair = True
        for i in range(7):
            if self.mytiles[3][i] >= 1:
                yaochu += 1
                if self.mytiles[3][i] >= 2:
                    pair = True

        xiangting = 13 - yaochu
        if pair is True:
            xiangting -= 1
        return xiangting