##### datetime库常用方法
``` python
import datetime
datetime.datetime(year,month,day,hour=0,minute=0,second=0,microsecond=0)
datetime.date(year,month,day)
datetime.time(hour=0,minute=0,second=0,microsecond=0)
datetime.timedelta(days=0,seconds=0,minutes=0,hours=0,weeks=0) # 将时间转换为可加减的变量
date.weekday() # 0表示周一 6表示周日
date.isoweekday() # 1表示周一 7表示周日
```

###### tips
1. 1s = 1000ms  1s = 1000000us
> 毫秒：millisecond  微秒：microsecond

