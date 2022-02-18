from mahjong_tools.four_sets_one_pair import FourSetsOnePair
import time

def generate_sample():
    '''
    数牌の全パターンを生成
    '''
    # 9桁の5進数
    four_sets_one_pair = FourSetsOnePair(0)
    s = [0 for i in range(9)]

    with open('result.txt', 'w') as f:
        n_sample = 0
        max_time = 0
        min_time = 10 ** 10
        total = 0
        for num in range(5**9):
            now = num
            sample = s.copy()
            count = 0
            for i in range(9):
                sample[i] = now % 5
                count += sample[i]
                now //= 5
            if count == 14:
                n_sample += 1
                start = time.time()
                mt = four_sets_one_pair.dfs(sample)
                end = time.time()
                ctime = end - start
                total += ctime
                max_time = max(max_time, ctime)
                min_time = min(min_time, ctime)
                # ファイル書き込み
                # print(sample)
                # print(mt)
                f.write("sample: ")
                for x in sample:
                    f.write(str(x))
                    f.write(" ")
                f.write("mt: ")
                for key, value in mt.items():
                    f.write(str(value))
                    f.write(" ")
                f.write("time: ")
                f.write(str(ctime))
                f.write("s")
                f.write("\n")
        f.write("n_sample: ")
        f.write(str(n_sample))
        f.write("\n")
        f.write("total time: ")
        f.write(str(total))
        f.write("\n")
        f.write("max time: ")
        f.write(str(max_time))
        f.write("\n")
        f.write("min time: ")
        f.write(str(min_time))
        f.write("\n")
        f.write("average time: ")
        f.write(str(total / n_sample))
        f.write("\n")


def main():
    generate_sample()

if __name__ == '__main__':
    main()