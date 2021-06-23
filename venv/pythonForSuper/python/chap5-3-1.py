from datetime import date, timedelta

start = date(2018, 6, 18)
for d in range(14):
    cur = start + timedelta(days=d)
    print(cur)