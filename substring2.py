
D = {"able", "ale", "apple", "bale", "kangaroo"}

heckAgainst = "abpplee"
wordList = []
furthestWord = ''

class wordCheck:
    def __init__(self, name):
        self.name = name
        self.startPosition = 0
        self.furthestWord = ''

def subStringChecker(some_list):
    
    for word in some_list:
        for let in word:
            checker(let, word)
            
def checker(letter, word):
     for num, verify in enumerate("abpplee"):
        if num >= wordDict[word].startPosition:
            if letter == verify:
                wordDict[word].startPosition = num + 1
                wordDict[word].furthestWord = wordDict[word].furthestWord + letter
                return

wordDict = {}                 
for item in D:
    wordDict[item] = wordCheck(item)

subStringChecker(D)
result = ''
for k in wordDict:
    if len(wordDict[k].furthestWord) > len(result):
        result = wordDict[k].furthestWord

print (result)
