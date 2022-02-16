# mytiles = []

# for x in range(3):
#     mytiles.append([0 for y in range(9)])
# mytiles.append([0 for x in range(7)])

# print(mytiles)
# for i in range(4):
#     print(mytiles[i])



# def syanten(mytiles):
#     '''
#     シャンテン数計算式
#     (1)メンツ手の場合
#     8 - (メンツ数)*2 - ターツ数
#     (2)七対子
#     (3)国士無双
#     '''
#     r = mentsu(mytiles)
    

# def mentsu(mytiles):
#     n_mentu = 0
#     n_tatsu = 0
#     for i in range(3):
#         # 数牌
#         n_mentu, n_tatsu += dfs(mytiles[i])

def score(mt):
    return 8 - 2*mt[0] - mt[1]

memo = {}

def dfs(tiles):
    # メモ化再帰
    # 辞書型のkeyにlist型は設定できない
    # if tiles in memo:
    #    return memo[tiles]
    key_of_tiles = 0
    v = 1
    for i in range(9):
        key_of_tiles += tiles[i] * v
        v *= 10
    if key_of_tiles in memo:
        return memo[key_of_tiles]
    mts = []
    for i in range(9):
        if tiles[i] > 0:
            # 順子
            next_tiles = tiles.copy()
            if i+2 < 9 and tiles[i+1] > 0 and tiles[i+2] > 0:
                next_tiles[i] -= 1
                next_tiles[i+1] -= 1
                next_tiles[i+2] -= 1
                now_mt = dfs(next_tiles).copy()
                now_mt[0] += 1
                mts.append(now_mt)
            # 刻子
            next_tiles = tiles.copy()
            if tiles[i] >= 3:
                next_tiles[i] -= 3
                now_mt = dfs(next_tiles).copy()
                now_mt[0] += 1
                mts.append(now_mt)
            # 対子
            next_tiles = tiles.copy()
            if tiles[i] >= 2:
                next_tiles[i] -= 2
                now_mt = dfs(next_tiles).copy()
                now_mt[1] += 1
                mts.append(now_mt)
            # 両面(辺張)ターツ
            next_tiles = tiles.copy()
            if i+1 < 9 and tiles[i+1] > 0:
                next_tiles[i] -= 1
                next_tiles[i+1] -= 1
                now_mt = dfs(next_tiles).copy()
                now_mt[1] += 1
                mts.append(now_mt)
            # 嵌張ターツ
            next_tiles = tiles.copy()
            if i+2 < 9 and tiles[i+2] > 0:
                next_tiles[i] -= 1
                next_tiles[i+2] -= 1
                now_mt = dfs(next_tiles).copy()
                now_mt[1] += 1
                mts.append(now_mt)
            # 孤立
            next_tiles = tiles.copy()
            next_tiles[i] = 0
            now_mt = dfs(next_tiles).copy()
            mts.append(now_mt)

    # ret_mt = [n_mentsu, n_tatsu]
    # min_shanten = score((n_mentsu, n_tatsu))
    #print("tiles: ", tiles)
    # if mts == []:
    #     memo[key_of_tiles] = [0, 0]
    #     return memo[key_of_tiles]
    min_shanten = 8
    ret_mt = [0, 0]
    # print(tiles)
    for mt in mts:
        # print(mt)
        now_shanten = score(mt)
        if min_shanten > now_shanten:
            ret_mt = mt.copy()
            min_shanten = now_shanten

    memo[key_of_tiles] = ret_mt.copy()
    return memo[key_of_tiles]

# print("test")
# a = []
# b = 1
# c = 2
# a.append((b, c))
# print(a)




test_tiles = [0 for i in range(9)]
for i in range(3):
    test_tiles[i] += 2
test_tiles[4] += 2
#test_tiles = [2, 2, 2, 0, 0, 0, 0, 0, 0]
#test_tiles = [0, 0, 1, 0, 0, 0, 0, 0, 0]
# test_tiles = [3, 3, 3, 3, 2, 0, 0, 0, 0]
test_tiles = [4, 1, 1, 1, 1, 1, 1, 1, 3]
print("test_tiles: ", test_tiles)
print("return: ", dfs(test_tiles))
result = dfs(test_tiles).copy()
print(score(result))
