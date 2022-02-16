from xiangting.xiangting import calculate_number_of_xiangting


mytiles = []
a = []
b = []
for i in range(9):
    a.append(0)
for i in range(7):
    b.append(0)
for i in range(3):
    mytiles.append(a.copy())
mytiles.append(b.copy())


tiles = input()

if len(tiles) != 13*2 and len(tiles) != 14*2:
    print("invalid input")
    exit()

ch = {'m': 0, 'p': 1, 's': 2, 'z': 3}

for i in range(len(tiles)//2):
    num = int(tiles[2*i]) - 1
    c = ch[tiles[2*i+1]]
    mytiles[c][num] += 1

print(mytiles)
xiangting = calculate_number_of_xiangting(mytiles)
for key, value in xiangting.items():
    print(key, value)



t = 1
for _ in range(14):
    t *= 2
t *= 10*6*2
print(t)
