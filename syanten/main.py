mytiles = []

for x in range(3):
    mytiles.append([0 for y in range(9)])
mytiles.append([0 for x in range(7)])

print(mytiles)
for i in range(4):
    print(mytiles[i])



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
    return 8 - 2*mt[0] + mt[1]

def dfs(tiles, n_mentsu, n_tatsu):
    n_mt = []
    for i in range(9):
        if tiles[i] != 0:
            # 順子
            next_tiles = tiles
            if i+2 < 9 and tiles[i+1] > 0 and tiles[i+2] > 0:
                next_tiles[i] -= 1
                next_tiles[i+1] -= 1
                next_tiles[i+2] -= 1
                n_mt.append(dfs(next_tiles, n_mentsu+1, n_tatsu))
            # 刻子
            next_tiles = tiles
            if tiles[i] >= 3:
                next_tiles[i] -= 3
                n_mt.append(dfs(next_tiles, n_mentsu+1, n_tatsu))
            # 対子
            next_tiles = tiles
            if tiles[i] >= 2:
                next_tiles[i] -= 2
                n_mt.append(dfs(next_tiles, n_mentsu, n_tatsu+1))
            # 両面(辺張)ターツ
            next_tiles = tiles
            if i+1 < 9 and tiles[i+1] > 0:
                next_tiles[i] -= 1
                next_tiles[i+1] -= 1
                n_mt.append(dfs(next_tiles, n_mentsu, n_tatsu+1))
            # 嵌張ターツ
            next_tiles = tiles
            if i+2 < 9 and tiles[i+2] > 0:
                next_tiles[i] -= 1
                next_tiles[i+2] -= 1
                n_mt.append(dfs(next_tiles, n_mentsu, n_tatsu+1))
            # 孤立
    r_mt = (0, 0)
    if n_mt is []:
        return r_mt
    max_score = 0
    for mt in n_mt:
        print(mt)
        if max_score < score(mt):
            r_mt = mt
            max_score = score(mt)

    return r_mt


test_tiles = [0 for i in range(9)]
for i in range(3):
    test_tiles[i] += 2
print("test_tiles: ", test_tiles)
print("return: ", dfs(test_tiles, 0, 0))