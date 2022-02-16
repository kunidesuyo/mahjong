class SevenPairs(object):

    def __init__(self, mytiles):
        self.mytiles = mytiles

    def calculation_xiangting(self):
        number_of_pairs = 0
        for tiles in self.mytiles:
            for tile in tiles:
                if tile >= 2:
                    number_of_pairs += 1
        
        return 6 - number_of_pairs