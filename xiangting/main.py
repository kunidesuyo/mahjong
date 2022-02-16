# mytiles = []

# for x in range(3):
#     mytiles.append([0 for y in range(9)])
# mytiles.append([0 for x in range(7)])

# print(mytiles)
# for i in range(4):
#     print(mytiles[i])




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
