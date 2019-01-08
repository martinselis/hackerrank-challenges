# compare the score
## https://www.hackerrank.com/challenges/compare-the-triplets/problem?h_r=next-challenge&h_v=zen

a = [1, 3, 5]
b = [0, 3, 9]
def compareTriplets(a, b):
    a_score, b_score = 0, 0
    for i in range(0,3):
        print (a_score, b_score)
        if a[i] > b[i]:
            a_score += 1
        if a[i] == b[i]:
            continue
        if a[i] < b[i]:
            b_score += 1
    return [a_score, b_score]

print (compareTriplets(a, b))
