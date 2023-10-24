from datetime import datetime, timedelta


pattern = '%H:%M'
start, finish = [datetime.strptime(input(), pattern) for _ in '12']
while start + timedelta(minutes=45) <= finish:
    print(f"{start.strftime(pattern)} - {(start + timedelta(minutes=45)).strftime(pattern)}")
    start += timedelta(minutes=10 + 45)
