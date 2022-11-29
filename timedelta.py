from datetime import datetime, timedelta

dt1 = datetime(2023, 9 , 1)
dt2 = (datetime.now())
print(dt1)
print(dt2)

duration = (dt1 - dt2)
print(duration.total_seconds())
