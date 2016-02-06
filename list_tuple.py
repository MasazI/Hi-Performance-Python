#encoding: utf-8

def linear_search(needle, array):
    '''
    線型探索する
    arguments:
        needle: 発見したいデータ
        array: 探索対象の配列
    '''
    for i, item in enumerate(array):
        if item == needle:
            return 1
    return -1


if __name__ == '__main__':
    print linear_search(1, [4,5,6,7,8])
    print linear_search(2, [3,4,5,2,5])
