class FourSetsOnePair(object):

    def __init__(self, mytiles):
        self.memo = {}
        self.mytiles = mytiles

    def xiangting_from_mt(self, mt):
        '''
        面子数と塔子数から向聴数を計算する
        '''
        return 8 - 2*mt[0] - mt[1]

    def dfs(self, tiles):
        '''
        数牌(萬子索子筒子)に対する面子とターツの数を返す関数
        '''
        # メモ化再帰
        # 辞書型のkeyにlist型は設定できない
        # if tiles in memo:
        #    return memo[tiles]
        key_of_tiles = 0
        v = 1
        for i in range(9):
            key_of_tiles += tiles[i] * v
            v *= 10
        if key_of_tiles in self.memo:
            return self.memo[key_of_tiles]
        mts = []
        for i in range(9):
            if tiles[i] > 0:
                # 順子
                next_tiles = tiles.copy()
                if i+2 < 9 and tiles[i+1] > 0 and tiles[i+2] > 0:
                    next_tiles[i] -= 1
                    next_tiles[i+1] -= 1
                    next_tiles[i+2] -= 1
                    now_mt = self.dfs(next_tiles).copy()
                    now_mt[0] += 1
                    mts.append(now_mt)
                # 刻子
                next_tiles = tiles.copy()
                if tiles[i] >= 3:
                    next_tiles[i] -= 3
                    now_mt = self.dfs(next_tiles).copy()
                    now_mt[0] += 1
                    mts.append(now_mt)
                # 対子
                next_tiles = tiles.copy()
                if tiles[i] >= 2:
                    next_tiles[i] -= 2
                    now_mt = self.dfs(next_tiles).copy()
                    now_mt[1] += 1
                    mts.append(now_mt)
                # 両面(辺張)ターツ
                next_tiles = tiles.copy()
                if i+1 < 9 and tiles[i+1] > 0:
                    next_tiles[i] -= 1
                    next_tiles[i+1] -= 1
                    now_mt = self.dfs(next_tiles).copy()
                    now_mt[1] += 1
                    mts.append(now_mt)
                # 嵌張ターツ
                next_tiles = tiles.copy()
                if i+2 < 9 and tiles[i+2] > 0:
                    next_tiles[i] -= 1
                    next_tiles[i+2] -= 1
                    now_mt = self.dfs(next_tiles).copy()
                    now_mt[1] += 1
                    mts.append(now_mt)
                # 孤立
                next_tiles = tiles.copy()
                next_tiles[i] = 0
                now_mt = self.dfs(next_tiles).copy()
                mts.append(now_mt)

        min_shanten = 8
        ret_mt = [0, 0]
        for mt in mts:
            now_shanten = self.xiangting_from_mt(mt)
            if min_shanten > now_shanten:
                ret_mt = mt.copy()
                min_shanten = now_shanten

        self.memo[key_of_tiles] = ret_mt.copy()
        return self.memo[key_of_tiles]


    def honours_mt(self):
        '''
        字牌の面子数、塔子数をリスト型で返す関数
        return [面子数, 塔子数]
        '''
        mt = [0, 0]
        tiles = self.mytiles[3]
        for tile in tiles:
            if tile >= 3:
                mt[0] += 1
            elif tile == 2:
                mt[1] += 1
        return mt


    def calculation_xiangting(self):
        mt = [0, 0]
        # 数牌
        for i in range(3):
            r_mt = self.dfs(self.mytiles[i]).copy()
            for j in range(2):
                mt[j] += r_mt[j]
        # 字牌
        r_mt = self.honours_mt().copy()
        for j in range(2):
            mt[j] += r_mt[j]

        return self.xiangting_from_mt(mt)