from mahjong_tools.xiangting import calculate_number_of_xiangting
import time

def minimum_xiangting(mytiles):
    xia = calculate_number_of_xiangting(mytiles)
    # 書く形式の向聴数に関して辞書型で変えてくるので最小値を返す
    ret = 20
    for key, value in xia.items():
        if ret > value:
            ret = value
    return ret

def init_pikey_dictionary():
    dic = []
    dic.append("m")
    dic.append("p")
    dic.append("s")
    dic.append("z")
    return dic.copy()


def pikey_from_index(i, j):
    # errorチェック
    dic = init_pikey_dictionary()
    ret = []
    ret.append(j+1)
    ret.append(dic[i])
    return ret.copy()

    
def sort_output(x):
    output = x
    temp = sorted(output.items(), reverse=True, key = lambda x : len(x[1]))
    output.clear()
    output.update(temp)
    temp = sorted(output.items(), key = lambda x : x[1][0])
    output.clear()
    output.update(temp)
    return output.copy()


def is_necessary_tile(i, j, now_hand):
    '''
    i,j牌が明らかに有効牌じゃない場合はFalseを返す
    数牌の場合はi,j牌の前後2以内に牌が存在しなかったら有効牌じゃない
    ただしヤオチュウ牌は国士の向聴数が増えるので例外
    '''
    # もう少し削れるがとりあえず簡単な処理にとどめておく
    if i == 3 or j == 0 or j == 8:
        return True
    else:
        is_necessary = False
        for dj in range(-2, 3, 1):
            now_j = j + dj
            if 0 <= now_j and now_j < 9:
                if now_hand[i][now_j] > 0:
                    is_necessary = True
            else:
                continue
        return is_necessary
    

def hand_optimize(mytiles, output_sorted_data=False):
    '''
    input: 手牌のデータ(14牌)
    output: {"切る牌": [シャンテン数, [有効牌]], ...}
    output_sorted_data=Trueならソートされたデータを出力する
    ソート規則: 向聴数が低いほうが前、有効牌が多いほうが前
    '''
    output = {}
    max_time = 0
    max_time_tiles = []
    count = 0
    for i in range(len(mytiles)):
        for j in range(len(mytiles[i])):
            # print("i j: ", i, j)
            ret_key = []
            ret_value = []
            if mytiles[i][j] > 0:
                ret_key = pikey_from_index(i, j)
                # mytiles[i][j]を切ったときの向聴数を計算
                now_hand = []
                for n in mytiles:
                    now_hand.append(n.copy())
                now_hand[i][j] -= 1
                xia = minimum_xiangting(now_hand)
                ret_value.append(xia)
                # 有効牌(ツモったときに向聴数が増える牌)を全探索で求める
                for ii in range(4):
                    num = 9
                    if ii == 3:
                        num = 7
                    for jj in range(num):
                        # print("ii jj: ", ii, jj)
                        next_hand = []
                        for n in now_hand:
                            next_hand.append(n.copy())
                        # 明らかに有効牌ではなかったら計算しない
                        if is_necessary_tile(ii, jj, next_hand) == False:
                            continue
                        next_hand[ii][jj] += 1
                        if next_hand[ii][jj] > 4:
                            continue
                        start = time.time()
                        count += 1
                        now_xia = minimum_xiangting(next_hand)
                        end = time.time()
                        t = end - start
                        # print(t)
                        if t > max_time:
                            max_time = t
                            max_time_tiles = []
                            for n in next_hand:
                                max_time_tiles.append(n.copy())
                        # print(end - start)
                        if xia > now_xia:
                            ret_value.append(pikey_from_index(ii, jj))
            if ret_key == [] and ret_value == []:
                continue
            ret_key_str = str(ret_key[0]) + str(ret_key[1])
            output[ret_key_str] = ret_value
    if output_sorted_data == True:
        output = sort_output(output)
    print("count: ", count)
    print("max_time: ", max_time)
    print("max_time_tiles", max_time_tiles)
    return output.copy()

