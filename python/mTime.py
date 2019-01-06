#coding=utf-8

import time
import when
from pytime import pytime

# 时间处理函数
class mTime:
    def furter(self, years=0, months=0, weeks=0, days=0,
               hours=0, minutes=0, seconds=0, milliseconds=0, microseconds=0,
               utc=False, now_date=None):
        if now_date:
            t = pytime.after(now_date, "days=" + str(days))
            pass
        else:
            t = when.future(years=years, months=months, weeks=weeks, days=days,
                            hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds,
                            microseconds=microseconds,
                            utc=utc)
        return t

    pass

# mt = mTime()
# t1 = mt.furter(days=1).strftime("%Y-%m-%d %H:%M:%S")
# t2 = mt.furter(hours=1).strftime("%Y-%m-%d %H:%M:%S")
# t3 = mt.furter(days=1, now_date="2018-11-01").strftime("%Y-%m-%d %H:%M:%S")
#
# print(t1)
# print(t2)
# print(t3)