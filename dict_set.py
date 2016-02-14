#encoding: utf-8

def index_sequence(key, mask=0b111, PERTURB_SHIFT=5):
    '''
    インデックス計算の擬似コード
    '''
    perturb = hash(key)
    i = perturb & mask

    yield i
    while True:
        # 元のハッシュを利用しているのがポイント
        i = ((i << 2) + i + perturb + 1)
        perturb >>= PERTURB_SHIFT
        yield i & mask

if __name__ == '__main__':
    for i in index_sequence('abc'):
        # 辞書のインデックスを探索して空かどうか確認する:
        print i
