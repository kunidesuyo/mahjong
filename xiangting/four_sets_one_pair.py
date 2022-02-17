class FourSetsOnePair(object):

    def __init__(self, mytiles):
        self.memo = {}
        self.mytiles = mytiles

    def ts_init(self):
        return {"t012": 0, "t000": 0, "t00": 0, "t01": 0, "t02": 0}

    def xiangting_from_ts(self, ts):
        '''
        面子数と塔子数から向聴数を計算する
        '''
        m = 0
        t = 0
        pair = False
        for key, value in ts.items():
            if len(key) == 4:
                m += value
            elif len(key) == 3:
                t += value
                if key == "t00" and value > 0:
                    pair = True
        if m + t <= 4:
            return 8 - 2 * m - t
        else:
            while not (m + t == 4):
                t -= 1
            ret = 8 - 2 * m - t
            if pair is True:
                ret -= 1
            return ret

    def dfs(self, tiles):
        '''
        数牌(萬子索子筒子)に対する面子とターツの数を返す関数
        順子 t012
        刻子 t000
        対子 t00
        両面(辺張) t01
        嵌張 t02
        '''
        # メモ化再帰
        # 辞書型のkeyにlist型は設定できない
        # if tiles in memo:
        #    return memo[tiles]

        # tile_structure = {"t012": 0, "t000": 0, "t00": 0, "t01": 0, "t02": 0}
        key_of_tiles = 0
        v = 1
        for i in range(9):
            key_of_tiles += tiles[i] * v
            v *= 10
        if key_of_tiles in self.memo:
            return self.memo[key_of_tiles]
        tss = []
        for i in range(9):
            if tiles[i] > 0:
                # 順子
                next_tiles = tiles.copy()
                if i+2 < 9 and tiles[i+1] > 0 and tiles[i+2] > 0:
                    next_tiles[i] -= 1
                    next_tiles[i+1] -= 1
                    next_tiles[i+2] -= 1
                    now_ts = self.dfs(next_tiles).copy()
                    now_ts["t012"] += 1
                    tss.append(now_ts)
                # 刻子
                next_tiles = tiles.copy()
                if tiles[i] >= 3:
                    next_tiles[i] -= 3
                    now_ts = self.dfs(next_tiles).copy()
                    now_ts["t000"] += 1
                    tss.append(now_ts)
                # 対子
                next_tiles = tiles.copy()
                if tiles[i] >= 2:
                    next_tiles[i] -= 2
                    now_ts = self.dfs(next_tiles).copy()
                    now_ts["t00"] += 1
                    tss.append(now_ts)
                # 両面(辺張)ターツ
                next_tiles = tiles.copy()
                if i+1 < 9 and tiles[i+1] > 0:
                    next_tiles[i] -= 1
                    next_tiles[i+1] -= 1
                    now_ts = self.dfs(next_tiles).copy()
                    now_ts["t01"] += 1
                    tss.append(now_ts)
                # 嵌張ターツ
                next_tiles = tiles.copy()
                if i+2 < 9 and tiles[i+2] > 0:
                    next_tiles[i] -= 1
                    next_tiles[i+2] -= 1
                    now_ts = self.dfs(next_tiles).copy()
                    now_ts["t02"] += 1
                    tss.append(now_ts)
                # 孤立
                next_tiles = tiles.copy()
                next_tiles[i] = 0
                now_ts = self.dfs(next_tiles).copy()
                tss.append(now_ts)

        ret_ts = self.ts_init()
        min_shanten = 8
        for ts in tss:
            now_shanten = self.xiangting_from_ts(ts)
            if min_shanten > now_shanten:
                ret_ts = ts.copy()
                min_shanten = now_shanten
            elif min_shanten == now_shanten:
                if ret_ts["t00"] < ts["t00"]:
                    ret_ts = ts.copy()
                    min_shanten = now_shanten

        self.memo[key_of_tiles] = ret_ts.copy()
        return self.memo[key_of_tiles]


    def honours_ts(self):
        '''
        字牌の面子数、塔子数をリスト型で返す関数
        return [面子数, 塔子数]
        '''
        ts = self.ts_init()
        tiles = self.mytiles[3]
        for tile in tiles:
            if tile >= 3:
                ts["i000"] += 1
            elif tile == 2:
                ts["i00"] += 1
        return ts


    def calculation_xiangting(self):
        ts = self.ts_init()
        # 数牌
        for i in range(3):
            r_ts = self.dfs(self.mytiles[i]).copy()
            for key, value in r_ts.items():
                ts[key] += value
        # 字牌
        r_ts = self.honours_ts().copy()
        for key, value in r_ts.items():
            ts[key] += value
        print(ts)

        return self.xiangting_from_ts(ts)