# encoding: utf-8

import pstats

p = pstats.Stats('profile.stats')
p.sort_stats('cumulative')
p.print_stats()

# 関数の呼び出し回数
p.print_callers()

# 関数の呼び出し関数
p.print_callees()
