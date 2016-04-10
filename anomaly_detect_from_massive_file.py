# encoding: utf-8
from random import normalvariate, random
from itertools import count

from datetime import date, datetime
from itertools import groupby

import math

from itertools import ifilter, imap, islice


def readdata(filename):
    '''
    1行ずつ返す
    arguments:
        filename
    return:
        行のデータをint型で返す
    '''
    with open(filename) as fd:
        for line in fd:
            data = line.strip().split(',')
            yield map(int, data)


def read_fake_data(filename):
    '''
    フェイクデータを返す
    arguments:
        filename(dammy)
    return:
        フェイクデータ
    '''
    for i in count():
        sigma = random() * 10
        # 平均0、分散sigmaの正規分布に従った値をサンプルする
        yield (i, normalvariate(0, sigma))


def day_grouper(iterable):
    '''
    タイムスタンプが同じ日の連続した行をグループ化してデータを取得
    '''
    # timestampからdateを取得するlambda
    # 1 (1/1/1980)から順に日付を取得する
    key = lambda(timestamp, value) : date.fromtimestamp(timestamp)
    return groupby(iterable, key)


def rolling_window_grouper(data, window_size=3600*24):
    '''
    1日分の移動ウィンドウでデータを取得
    '''    
    window = tuple(islice(data, 0, window_size))
    while True:
        current_datetime = datetime.fromtimestamp(window[0][0])
        yield (current_datetime, window)
        window = window[1:] + (data.next(),)

def check_anomaly((day, day_data)):
    '''
    日付と日付のデータを取得して異常の場合はdateオブジェクトを返す
    aruguments:
        dayとday_dataのtuble
    return:
        異常：date
        正常：False
    '''
    n = 0
    mean = 0
    M2 = 0
    max_value = None
    for timestamp, value in day_data:
        n += 1
        delta = value - mean
        mean = mean + delta/n
        M2 += delta * (value - mean)
        max_value = max(max_value, value)
    variance = M2/(n - 1)
    standard_deviation = math.sqrt(variance)

    if max_value > mean + 1000 * standard_deviation:
        return day
    return False


def anomaly_detect():
    data = read_fake_data('fake')
    data_by_day = day_grouper(data)
    anomalous_dates = ifilter(None, imap(check_anomaly, data_by_day))
    first_anomalous_date = anomalous_dates.next()
    print("The first anomalous date is: %s" % (first_anomalous_date))

if __name__ == '__main__':
    anomaly_detect()
