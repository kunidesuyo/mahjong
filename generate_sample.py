from xiangting.four_sets_one_pair import FourSetsOnePair


def generate_sample():
    '''
    数牌の全パターンを生成
    '''
    # 9桁の5進数
    four_sets_one_pair = FourSetsOnePair(0)
    s = [0 for i in range(9)]

    with open('result.txt', 'w') as f:
        for num in range(5**9):
            now = num
            sample = s.copy()
            count = 0
            for i in range(9):
                sample[i] = now % 5
                count += sample[i]
                now //= 5
            if count <= 14:
                mt = four_sets_one_pair.dfs(sample)
                # ファイル書き込み
                # print(sample)
                # print(mt)
                f.write("sample: ")
                for x in sample:
                    f.write(str(x))
                    f.write(" ")
                f.write("mt: ")
                for x in mt:
                    f.write(str(x))
                    f.write(" ")
                f.write("\n")


def main():
    generate_sample()

if __name__ == '__main__':
    main()