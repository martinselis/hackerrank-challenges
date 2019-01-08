# // For example, given the input of S = "abppplee" and
# D = {"able", "ale", "apple", "bale", "kangaroo"}
# the correct output would be "apple"

D = {"able", "ale", "apple", "bale", "kangaroo"}

checkAgainst = "abpplee"
wordList = []
def subStringChecker(some_list):
    
    for word in some_list:
        counter = 0
        startPosition = 0
        furthestWord = ''
        for let in word:
            for num, verify in enumerate(checkAgainst):
                if num >= startPosition:
                    if let == verify and counter < len(word):
                        counter += 1
                        startPosition = num
                        furthestWord = furthestWord + let
                        print(word, let, str(num) + ":" + verify)
                        next(checkAgainst, None)
                        next(word, none)
                    
        addition = {word: furthestWord}
        wordList.append(addition)

subStringChecker(D)
print (wordList)
            
