def simple_sequence():
    cnt = 1
    while True:
        for _ in range(1, cnt + 1):
            yield cnt
        cnt += 1
