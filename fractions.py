## Fractions

array = [-4,3,-9,0,4,1]
def fractions(arr):
    pos, neg, zero = 0, 0, 0
    total = len(arr)
    for i in arr:
        if i > 0:
            pos += 1
        if i < 0:
            neg += 1
        if i == 0:
            zero += 1
    
    pos = format((pos/total), '.6f')
    neg = format((neg/total), '.6f')
    zero = format((zero/total), '.6f')

    print (pos)
    print (neg)
    print (zero)

print (fractions(array))

        
    
