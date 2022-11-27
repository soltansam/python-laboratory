from datetime import datetime
import time


dt = datetime(2018, 9, 20)
print(dt)
dt = datetime.now()
print(dt)
dt = datetime.strptime("2015/09/15", "%Y/%m/%d")
print(dt)
dt = datetime.now().strftime("%Y/%d") 
print(dt)
dt = datetime.fromtimestamp(time.time())
print(f"{dt.year}/{dt.month}")
