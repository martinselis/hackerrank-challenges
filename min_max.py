def min_max(n):
    min_val = 0
    max_val = 0
    n = sorted(n, key=int)
    counter = -1
    for i in n:
        counter += 1
        if counter == 0: continue
        max_val = max_val + i
    counter = -1
    n = sorted(n, key=int, reverse=True)
    for i in n:
        counter += 1
        if counter == 0: continue
        min_val = min_val + i

    print (min_val, max_val)

array = [7,69,2,221,8974]

min_max(array)
