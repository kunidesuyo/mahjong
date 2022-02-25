from sympy import comp
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

    thirteen_orphans_file_list =[
        '13orphans.txt',
        '13orphans0.txt',
        '13orphans0_pair.txt',
        '13orphans1.txt',
        '13orphans1_pair.txt',
        '13orphans2.txt',
        '13orphans2_pair.txt',
        '13orphans3.txt',
        '13orphans3_pair.txt',
        '13orphans4.txt',
        '13orphans4_pair.txt',
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
        with open("test_data\\four_sets_one_pair\\" + file_name, 'r') as f:
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

            # FSOP = four_sets_one_pair.FourSetsOnePair(now_hand)

            print(now_hand)
            start = time.time()
            xia = calculate_number_of_xiangting(now_hand)
            end = time.time()
            result = 20
            for key, value in xia.items():
                result = min(result, value)
            print("time ", end-start, "s")
            print("calculation result: ", result)
            print("true value: ", true_v)
            if result == true_v:
                correct_count += 1
            else:
                incorrect_data.append(file_name)

    for file_name in thirteen_orphans_file_list:
        count += 1
        now_hand = []
        for t in init_tiles:
            now_hand.append(t.copy())
        with open("test_data\\thirteen_orphans\\" + file_name, 'r') as f:
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

            # FSOP = four_sets_one_pair.FourSetsOnePair(now_hand)

            print(now_hand)
            start = time.time()
            xia = calculate_number_of_xiangting(now_hand)
            print(xia)
            result = 20
            for key, value in xia.items():
                result = min(result, value)
            end = time.time()
            print("time ", end-start, "s")
            print("calculation result: ", result)
            print("true value: ", true_v)
            if result == true_v:
                correct_count += 1
            else:
                incorrect_data.append(file_name)
    
    if count == correct_count:
        print("all ok")
    else:
        for ff in incorrect_data:
            print(ff)


win_hand = []

def encode_index(num):
    '''
    0~8 (0, 0~8)
    9~17 (1, 0~8)
    18~26 (2, 0~8)
    27~33 (3, 0~6)
    '''
    i = 0
    j = 0
    if num <= 26:
        j = num % 9
        i = num // 9
    else:
        num -= 27
        j = num % 7
        i = 3
    return [i, j]


def decode_index(ij):
    i, j = ij
    num = 0
    if i == 3:
        num = 27
        num += j
    else:
        num = 9 * i + j
    return num


def create_win_hand(now_hand, start=0, n_mentu=0):
    # 処理重い
    if n_mentu == 4:
        for i in range(9*3+7):
            x, y = encode_index(i)
            completed_hand = []
            for j in range(4):
                completed_hand.append(now_hand[j].copy())
            completed_hand[x][y] += 2
            if completed_hand[x][y] <= 4:
                win_hand.append(completed_hand)
        return

    for i in range(start, 9*3+7):
        # 順子
        next_hand = []
        for x in range(4):
            next_hand.append(now_hand[x].copy())
        x, y = encode_index(i)
        if x < 3 and y+2 < 9:
            go = True
            for dy in range(3):
                next_hand[x][y+dy] += 1
                if next_hand[x][y+dy] > 4:
                    go = False
            if go == True:
                create_win_hand(next_hand, start, n_mentu+1)
        # 刻子
        next_hand = []
        for x in range(4):
            next_hand.append(now_hand[x].copy())
        x, y = encode_index(i)
        go = True
        next_hand[x][y] += 3
        if next_hand[x][y] > 4:
            go = False
        if go == True:
            create_win_hand(next_hand, start, n_mentu+1)


def create_win_hand_same_color(now_hand, start=0, n_mentu=0):
    if n_mentu == 4:
        for i in range(9):
            completed_hand = now_hand.copy()
            completed_hand[i] += 2
            if completed_hand[i] <= 4:
                win_hand.append(completed_hand)
        return

    for i in range(start, 9):
        # 順子
        next_hand = now_hand.copy()
        go = True
        if i + 2 < 9:
            for di in range(3):
                next_hand[i+di] += 1
                if next_hand[i+di] > 4:
                    go = False
            if go == True:
                create_win_hand_same_color(next_hand.copy(), start, n_mentu+1)
        # 刻子
        next_hand = now_hand.copy()
        go = True
        next_hand[i] += 3
        if next_hand[i] > 4:
            go = False
        if go == True:
            create_win_hand_same_color(next_hand.copy(), start, n_mentu+1)


            
def init_hand():
    a = [0 for x in range(9)]
    b = [0 for x in range(7)]
    ret = []
    for i in range(3):
        ret.append(a.copy())
    ret.append(b.copy())
    return ret

    # 計算結果を出力する(ファイル名に日時を使って重複を避ける)


def output_win_hand():
    '''
    清一色のアガリ手をファイル出力する
    '''
    init = [0 for x in range(9)]
    create_win_hand_same_color(init, 0, 0)
    global win_hand
    win_hand = sorted(win_hand)
    c = 0
    while c+1 < len(win_hand):
        if win_hand[c] == win_hand[c+1]:
            del win_hand[c+1]
        else:
            c += 1

    ch = {'0': 'm', '1': 'p', '2': 's', '3': 'z'}

    with open("test_data\\win_hand.txt", 'w') as f:
        count = 0
        for hand in win_hand:
            output_hand = []
            output_hand.append(hand.copy())
            a = [0 for _ in range(9)]
            b = [0 for _ in range(7)]
            output_hand.append(a.copy())
            output_hand.append(a.copy())
            output_hand.append(b.copy())
            # ファイルに書き込み
            for i in range(4):
                for j in range(len(output_hand[i])):
                    num = output_hand[i][j]
                    if num > 0:
                        for _ in range(num):
                            f.write(str(j+1))
                            f.write(str(ch[str(i)]))
            f.write(" ")
            f.write(str(-1))
            f.write("\n")
            count += 1


def convert_mytiles(input_tiles):
    ret = init_hand()
    if len(input_tiles) != 13*2 and len(input_tiles) != 14*2:
        print("invalid input")
        exit()

    ch = {'m': 0, 'p': 1, 's': 2, 'z': 3}

    for i in range(len(input_tiles)//2):
        num = int(input_tiles[2*i]) - 1
        c = ch[input_tiles[2*i+1]]
        ret[c][num] += 1

    return ret


def testing_win_hand():

    incorrect_data = []
    total_time = 0
    max_time = 0
    min_time = 1000000
    n_data = 0
    n_incorrect = 0

    with open("test_data\\win_hand.txt", 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            input_tiles, true_v = line.split()
            true_v = int(true_v)
            now_hand = convert_mytiles(input_tiles)
            n_data += 1

            start = time.time()
            xia = calculate_number_of_xiangting(now_hand)
            end = time.time()
            t = end - start
            total_time += t
            max_time = max(max_time, t)
            min_time = min(min_time, t)
            result = 20
            for key, value in xia.items():
                result = min(result, value)
            if result != true_v:
                n_incorrect += 1
                incorrect_data.append(input_tiles)       

            # if n_data == 100:
            #     break

            if n_data % 100 == 0:
                print(n_data)

    
    print("n_data: ", n_data)
    print("total time: ", total_time, "s")
    print("average time: ", total_time / n_data, "s")
    print("max time: ", max_time, "s")
    print("min time: ", min_time, "s")
    print("incorrect data: ", n_incorrect)
    for x in incorrect_data:
        print(x)



def main():
    testing_win_hand()

if __name__ == '__main__':
    main()
