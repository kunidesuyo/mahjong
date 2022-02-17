from xiangting.thirteen_orphans import ThirteenOrphans
from xiangting.four_sets_one_pair import FourSetsOnePair
from xiangting.seven_pairs import SevenPairs

def calculate_number_of_xiangting(mytiles):
    '''
    シャンテン数計算式
    (1)メンツ手の場合
    8 - (メンツ数)*2 - ターツ数
    (2)七対子
    6 - (トイツ数)
    (3)国士無双
    13 - (ヤオチュウ牌の種類数) - min(ヤオチュウ牌のトイツ数, 1)
    '''
    # mytilesの形式チェック追加予定

    xiangting = {}
    four_sets_one_pair = FourSetsOnePair(mytiles)
    xiangting["four_sets_one_pair"] = four_sets_one_pair.calculation_xiangting()
    # print(len(four_sets_one_pair.memo))
    seven_pairs = SevenPairs(mytiles)
    xiangting["seven_pairs"] = seven_pairs.calculation_xiangting()
    thirteen_orphans = ThirteenOrphans(mytiles)
    xiangting["thirteen_orphans"] = thirteen_orphans.calculation_xiangting()

    return xiangting