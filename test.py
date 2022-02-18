from mahjong_tools.xiangting import calculate_number_of_xiangting
from mahjong_tools import hand_optimize as ho
import time


mytiles = []
a = [0 for i in range(9)]
b = [0 for i in range(7)]
for i in range(3):
    mytiles.append(a.copy())
mytiles.append(b.copy())

# ch = {'m': 0, 'p': 1, 's': 2, 'z': 3}
# print(ch.items())

# result = {
#     "1m": [3, [1, "s"], [2, "s"]], 
#     "2m": [2, [1, "s"], [2, "s"], [3, "s"]],
#     "3m": [2, [1, "s"], [2, "s"]] 
# }
# print(result)

# sorted_result = ho.sort_output(result)

# print(sorted_result)

# for i in range(-2, 3, 1):
#     print(i)

# exit()

#with open('hand.txt', 'r') as f:
with open('churen.txt', 'r') as f:
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
    start = time.time()
    xia = calculate_number_of_xiangting(mytiles)
    end = time.time()
    print("time ", end-start, "s")
    for key, value in xia.items():
        print(key, value)
    
    # print(mytiles)
    # start = time.time()
    # result = ho.hand_optimize(mytiles, output_sorted_data=True)
    # end = time.time()
    # print(end - start)
    # print(result)
