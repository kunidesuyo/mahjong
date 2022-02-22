from mahjong_tools import four_sets_one_pair
from mahjong_tools.xiangting import calculate_number_of_xiangting
import time

def minimum_test():
    init_tiles = []
    a = [0 for i in range(9)]
    b = [0 for i in range(7)]
    for i in range(3):
        init_tiles.append(a.copy())
    init_tiles.append(b.copy())
    file_list = [
        # 塔子オーバー
        '0m5t.txt',
        '0m5t_pair.txt',
        '0m6t.txt',
        '0m6t_pair.txt',
        '0m7t.txt',
        '0m7t_pair.txt',
        '1m4t.txt',
        '1m4t_pair.txt',
        '1m5t.txt',
        '1m5t_pair.txt',
        '2m3t.txt',
        '2m3t_pair.txt',
        '2m4t.txt',
        '2m4t_pair.txt',
        '3m2t.txt',
        '3m2t_pair.txt',
        # 七対子
        # 国士無双
    ]
    # 1m1m1m1m2m3m4m5m6m7m8m9m9m9m -1
    # file_list = ['churen.txt']
    # for file_name in file_list:
    #     open("test_data\\" + file_name, 'w')
    # exit()

    count = 0
    correct_count = 0
    incorrect_data = []
    for file_name in file_list:
        count += 1
        now_hand = []
        for t in init_tiles:
            now_hand.append(t.copy())
        with open("test_data\\" + file_name, 'r') as f:
            input_data = f.read()
            input_tiles, true_v = input_data.split()
            true_v = int(true_v)
            #print(input_tiles, true_v)
            #exit()

            if len(input_tiles) != 13*2 and len(input_tiles) != 14*2:
                print("invalid input")
                exit()

            ch = {'m': 0, 'p': 1, 's': 2, 'z': 3}

            for i in range(len(input_tiles)//2):
                num = int(input_tiles[2*i]) - 1
                c = ch[input_tiles[2*i+1]]
                now_hand[c][num] += 1

            FSOP = four_sets_one_pair.FourSetsOnePair(now_hand)

            print(now_hand)
            start = time.time()
            xia = FSOP.calculation_xiangting()
            end = time.time()
            print("time ", end-start, "s")
            print("calculation result: ", xia)
            print("true value: ", true_v)
            if xia == true_v:
                correct_count += 1
            else:
                incorrect_data.append(file_name)
    
    if count == correct_count:
        print("all ok")
    else:
        for ff in incorrect_data:
            print(ff)
            
    # テンパイの手牌を生成

    # 計算結果を出力する(ファイル名に日時を使って重複を避ける)

def main():
    minimum_test()

if __name__ == '__main__':
    main()
