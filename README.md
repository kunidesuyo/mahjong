# mahjong
## 向聴数計算
### 向聴数の計算式
向聴数の計算式は以下の三パターンの形があり、3つのうちの最小値を用いる。
1. 四面子一雀頭の形  
  8 - (面子数)*2 - 塔子数
2. 七対子  
  6 - (トイツ数)
3. 国士無双  
  13 - (ヤオチュウ牌の種類数) - min(ヤオチュウ牌のトイツ数, 1)

### 四面子一雀頭の形
字牌に関しては、暗刻対子の順番で処理すれば問題ない
数牌(萬子、筒子、索子)に関して、面子と塔子の選択で向聴数が変わる場合がある。

#### 特殊な状況
- 面子過多
面子と塔子は4つ以下でないといけない。  
例)  
1m2m 4m5m 5p6p7p 1s2s3s 5s6s 8s9s  
面子2塔子4で計算式だと0向聴だが実際は2向聴  
1m2m 4m5m 7m8m 1p2p 4p5p 7p8p9p  
面子1塔子5で計算式だと1向聴だが実際は3向聴  
1m2m 4m5m 7m8m 1p2p 4p5p 7p8p 1s  
面子0塔子6で計算式だと2向聴だが実際は4向聴  
1m2m 4m5m 7m8m 1p2p 4p5p 7p8p 1s2s  
面子0塔子7で計算式だと1向聴だが実際は4向聴  
塔子に対子が含まれる場合  
1m2m 4m5m 5p6p7p 1s2s3s 5s6s 8s8s  
面子2塔子4で計算式だと0向聴だが実際は1向聴  

つまり面子+塔子>4の場合、面子+塔子=4になるように塔子を減らして計算する  
また塔子に対子が含まれる場合は上の処理をしてから向聴数を1減らす  

  - 間違い
    3m5m5m7m3p5p5p7p3s5s5s7s1z2z  
    面子手3向聴だが4向聴と出力  
    数牌を個別に処理できない

- 槓子の処理

#### 疑似コード
メモ化再帰を用いて実装した。(要検証)
```
dfs(手牌) # 向聴数が最小になる面子数と塔子数のペアを返す
  # memoに計算結果が入っていたらそのまま返す
  if memo[手牌]が存在
    return memo[手牌]
  mt # 面子数と塔子数の配列
  for i in 1~9 # iは面子塔子の最小の数牌
    if 手牌にi,i+1,i+2が存在
      now_mt = dfs(手牌からi,i+1,i+2を取り除いたもの)
      now_mt.面子数++
      mt.append(now_mt)
    if 手牌にiが3枚存在
      now_mt = dfs(手牌からiを3枚取り除いたもの)
      now_mt.面子数++
      mt.append(now_mt)
    if 手牌にiが2枚存在
      now_mt = dfs(手牌からiを2枚取り除いたもの)
      now_mt.塔子数++
      mt.append(now_mt)
    if 手牌にi,i+1が存在
      now_mt = dfs(手牌からi,i+1を取り除いたもの)
      now_mt.塔子数++
      mt.append(now_mt)
    if 手牌にi,i+2が存在
      now_mt = dfs(手牌からi,i+2を取り除いたもの)
      now_mt.塔子数++
      mt.append(now_mt)
    # iを孤立牌として処理
    now_mt = dfs(手牌からiをすべて取り除いたもの)
    mt.append(now_mt)
  if mtが空 # 終了条件
    return [0, 0]
  ret_mt = min(向聴数(mt))
  memo[手牌] = ret_mt
  return ret_mt
```

#### 計算量の推定
***かなりアバウト***  
再帰なのでグラフの深さ優先探索に対応する。  
グラフの頂点数が再帰関数の呼び出し回数(メモ化再帰なので2回目以降の呼び出しはカウントしない)
考えられる分岐先は手牌14枚があるorないの2種類なので
2^14 = 16384
再帰関数内の計算処理回数 < 10 * 6 * 2
2^14 * (10 * 6 * 2) = 1966080 < 2 * 10^6
  
### 七対子と国士無双
簡単に実装可能


## タスク
- 向聴数のプログラムの正当性の検証
- webサイトにする
- 手牌効率計算の実装(向聴数が正しく動作することが確認出来たら)
