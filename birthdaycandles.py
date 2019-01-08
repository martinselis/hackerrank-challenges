##birthday candles. blow out the tallest candle. return int of total candles blown

def birthdayCakeCandles(ar):
    a = max(ar)
    counter = 0
    for i in ar:
        if i == a:
            counter += 1
    return counter
            


array = [1, 3, 6, 6]

print (max(array))

birthdayCakeCandles(array)
