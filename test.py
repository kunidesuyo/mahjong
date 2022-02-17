from xiangting.xiangting import calculate_number_of_xiangting


mytiles = []
a = [0 for i in range(9)]
b = [0 for i in range(7)]
for i in range(3):
    mytiles.append(a.copy())
mytiles.append(b.copy())


with open('hand.txt', 'r') as f:
    input_tiles = f.read()

    if len(input_tiles) != 13*2 and len(input_tiles) != 14*2:
        print("invalid input")
        exit()

    ch = {'m': 0, 'p': 1, 's': 2, 'z': 3}

    for i in range(len(input_tiles)//2):
        num = int(input_tiles[2*i]) - 1
        c = ch[input_tiles[2*i+1]]
        mytiles[c][num] += 1

    print(mytiles)
    xiangting = calculate_number_of_xiangting(mytiles)
    for key, value in xiangting.items():
        print(key, value)

